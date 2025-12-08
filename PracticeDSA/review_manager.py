#!/usr/bin/env python3
import json
import os
import sys
import subprocess
import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Try importing rich for a better UI, otherwise fallback (or exit)
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich import print as rprint
    from rich.markdown import Markdown
    from rich.prompt import Prompt, IntPrompt
except ImportError:
    print("This tool requires 'rich'. Please run: pip install rich")
    sys.exit(1)

CONSOLE = Console()
PROGRESS_FILE = "review_progress.json"
IGNORE_DIRS = {".git", "__pycache__", ".venv", "venv", "env", ".idea", ".vscode"}
IGNORE_FILES = {"review_manager.py", "main.py", "__init__.py"}

class ReviewManager:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.progress_file = self.root_dir / PROGRESS_FILE
        self.data = self.load_data()

    def load_data(self) -> Dict:
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                CONSOLE.print("[bold red]Error reading progress file. Starting fresh.[/bold red]")
                return {}
        return {}

    def save_data(self):
        with open(self.progress_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def find_problems(self) -> List[Path]:
        problems = []
        for root, dirs, files in os.walk(self.root_dir):
            # Modify dirs in-place to skip ignored
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            for file in files:
                if file.endswith(".py") and file not in IGNORE_FILES:
                    full_path = Path(root) / file
                    problems.append(full_path)
        return problems

    def get_progress(self, rel_path: str) -> Dict:
        return self.data.get(rel_path, {
            "reviews": 0,
            "last_review": None,
            "next_review": None,
            "interval": 0,  # Days
            "ease_factor": 2.5
        })

    def update_progress(self, rel_path: str, quality: int):
        # SM-2 Algorithm Implementation
        # Quality: 0-5 (we'll map user input 1-3 to typical SM-2 ranges or simplify)
        # Let's use a simplified 1(Hard/Fail), 2(Good), 3(Easy) map to SM-2's 0-5
        # Map: 1 -> 1 (Fail/Hard), 2 -> 3 (Pass), 3 -> 5 (Easy)
        
        q_map = {1: 1, 2: 3, 3: 5}
        q = q_map.get(quality, 3)

        item = self.get_progress(rel_path)
        
        # If quality is low (fail), reset
        if q < 3:
            item["interval"] = 1
            item["reviews"] = 0
        else:
            if item["reviews"] == 0:
                item["interval"] = 1
            elif item["reviews"] == 1:
                item["interval"] = 6
            else:
                item["interval"] = int(item["interval"] * item["ease_factor"])
            
            item["reviews"] += 1
            
        # Update Ease Factor
        # EF' = EF + (0.1 - (5-q) * (0.08 + (5-q)*0.02))
        item["ease_factor"] = item["ease_factor"] + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
        if item["ease_factor"] < 1.3:
            item["ease_factor"] = 1.3

        now = datetime.date.today()
        item["last_review"] = str(now)
        item["next_review"] = str(now + datetime.timedelta(days=item["interval"]))
        
        self.data[rel_path] = item
        self.save_data()

    def get_due_items(self) -> List[Path]:
        all_files = self.find_problems()
        due = []
        now = str(datetime.date.today())
        
        for p in all_files:
            rel_path = str(p.relative_to(self.root_dir))
            item = self.get_progress(rel_path)
            
            if not item["next_review"] or item["next_review"] <= now:
                due.append(p)
                
        return due

    def run_file(self, path: Path):
        CONSOLE.print(f"[bold blue]Running {path.name}...[/bold blue]")
        try:
            result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, timeout=5)
            if result.stdout:
                CONSOLE.print(Panel(result.stdout, title="Output", border_style="green"))
            if result.stderr:
                CONSOLE.print(Panel(result.stderr, title="Errors", border_style="red"))
        except Exception as e:
            CONSOLE.print(f"[bold red]Error running file: {e}[/bold red]")

    def parse_solution(self, path: Path) -> Dict[str, str]:
        """
        Parses the python file to separate the top-level docstring (Concept)
        from the actual code (Solution).
        """
        try:
            with open(path, 'r') as f:
                content = f.read()
            
            import ast
            try:
                module = ast.parse(content)
                if module.body and isinstance(module.body[0], ast.Expr) and isinstance(module.body[0].value, ast.Constant) and isinstance(module.body[0].value.value, str):
                    docstring = module.body[0].value.value
                    # The code is everything else? Or just read the file again?
                    # Simpler approach: AST gives us the docstring range.
                    # But for now, let's just rely on the ast.get_docstring equivalent or manual split
                    # Actually, ast.get_docstring is best.
                    docstring = ast.get_docstring(module)
                    if docstring:
                         return {"concept": docstring, "code": content}
            except Exception:
                pass # Parse error or no docstring
            
            return {"concept": "No concept/docstring found for this problem.", "code": content}
        except Exception as e:
            return {"concept": f"Error reading file: {e}", "code": ""}

    def show_concept(self, path: Path):
        data = self.parse_solution(path)
        CONSOLE.print(Panel(data["concept"], title=f"Concept: {path.name}", border_style="yellow"))

    def show_solution(self, path: Path):
        data = self.parse_solution(path)
        # We show the full content as solution usually, or we could strip the docstring.
        # For now, showing full content is safer to ensure context is seen.
        CONSOLE.print(Panel(data["code"], title=f"Solution: {path.name}", border_style="blue"))

    def start_session(self):
        due_items = self.get_due_items()
        
        if not due_items:
            CONSOLE.print(Panel("🎉 All caught up! No problems due for review today.", style="bold green"))
            return

        CONSOLE.print(f"[bold]Found {len(due_items)} problems due for review.[/bold]\n")
        
        for idx, path in enumerate(due_items, 1):
            CONSOLE.clear()
            rel_path = str(path.relative_to(self.root_dir))
            
            CONSOLE.print(f"[{idx}/{len(due_items)}] Reviewing: [bold cyan]{rel_path}[/bold cyan]")
            CONSOLE.print(f"Parent Folder: [yellow]{path.parent.name}[/yellow]")
            CONSOLE.print("-" * 50)
            
            while True:
                action = Prompt.ask(
                    "Action",
                    choices=["c", "s", "r", "n", "q"],
                    default="c",
                    show_choices=False
                )
                rprint("[dim]([bold]c[/bold]oncept, [bold]s[/bold]how code, [bold]r[/bold]un, [bold]n[/bold]ext/rate, [bold]q[/bold]uit)[/dim]")

                if action == "q":
                    CONSOLE.print("Goodbye!")
                    sys.exit(0)
                elif action == "c":
                    self.show_concept(path)
                elif action == "s":
                    self.show_solution(path)
                elif action == "r":
                    self.run_file(path)
                elif action == "n":
                    rating = IntPrompt.ask(
                        "How was it? (1: Hard/Fail, 2: Good, 3: Easy)" ,
                        choices=["1", "2", "3"]
                    )
                    self.update_progress(rel_path, rating)
                    break

def main():
    manager = ReviewManager(os.path.dirname(os.path.abspath(__file__)))
    
    if len(sys.argv) > 1 and sys.argv[1] == "stats":
        # Simple stats
        total = len(manager.find_problems())
        reviewed = len(manager.data)
        CONSOLE.print(Panel(f"Total Problems: {total}\nTracked: {reviewed}", title="Stats"))
    else:
        manager.start_session()

if __name__ == "__main__":
    main()
