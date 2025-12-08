import os
import json
import argparse
from datetime import datetime, timedelta

# --- CONFIGURATION ---
HISTORY_FILE = '.review_history.json'
ROOT_DIR = '.'

# Spaced Repetition Intervals (in days)
# Level 0 (New) -> 1 day -> 3 days -> 7 days -> 14 days -> 28 days
INTERVALS = [1, 3, 7, 14, 28, 60]

def load_data():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return {"reviews": {}}

def save_data(data):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_due_problems(data):
    due = []
    # 1. Scan for all Python files
    all_files = []
    for root, _, files in os.walk(ROOT_DIR):
        if '__pycache__' in root or '.venv' in root: continue
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                rel_path = os.path.relpath(os.path.join(root, file), os.getcwd())
                all_files.append(rel_path)

    # 2. Check which are due
    today = datetime.now().date()
    
    for file_path in all_files:
        if file_path not in data["reviews"]:
            # New problem!
            due.append((file_path, 0, "New Problem"))
        else:
            review_info = data["reviews"][file_path]
            next_date = datetime.strptime(review_info["next_review"], "%Y-%m-%d").date()
            if today >= next_date:
                days_overdue = (today - next_date).days
                due.append((file_path, review_info["level"], f"Due ({days_overdue} days ago)"))
    
    # Sort by level (newest first) then random
    # due.sort(key=lambda x: (x[1], x[0])) 
    import random
    random.shuffle(due)
    return due

def update_review(file_path, quality):
    data = load_data()
    
    # Default state
    current_level = 0
    if file_path in data["reviews"]:
        current_level = data["reviews"][file_path]["level"]

    # Logic: 
    # Quality 1 (Hard/Forgot) -> Reset to Level 1
    # Quality 2 (Good) -> Level + 1
    # Quality 3 (Easy) -> Level + 2 (Jump ahead)
    
    if quality == '1': # Hard
        new_level = 1 
    elif quality == '2': # Good
        new_level = current_level + 1
    elif quality == '3': # Easy
        new_level = current_level + 2
    
    # Cap level
    if new_level >= len(INTERVALS):
        new_level = len(INTERVALS) - 1
        
    days_to_add = INTERVALS[new_level - 1] if new_level > 0 else 1
    next_date = datetime.now() + timedelta(days=days_to_add)
    
    data["reviews"][file_path] = {
        "level": new_level,
        "last_reviewed": datetime.now().strftime("%Y-%m-%d"),
        "next_review": next_date.strftime("%Y-%m-%d")
    }
    
    save_data(data)
    print(f"✅ Logged! Next review in {days_to_add} days (Level {new_level}).")

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    
    # Command: 'next'
    subparsers.add_parser('next', help='Show due problems')
    
    # Command: 'log'
    log_parser = subparsers.add_parser('log', help='Log a review')
    log_parser.add_argument('file', help='Partial or full filename')
    log_parser.add_argument('quality', choices=['1', '2', '3'], help='1=Hard, 2=Good, 3=Easy')
    
    args = parser.parse_args()
    
    if args.command == 'next':
        data = load_data()
        due = get_due_problems(data)
        print(f"\n📅 You have {len(due)} problems due for review:\n")
        for i, (path, level, status) in enumerate(due[:5]): # Show top 5
            print(f"  {i+1}. {path} [{status}]")
        print("\nTo start, type: python review_scheduler.py log <filename> <quality>")
        
    elif args.command == 'log':
        # Helper to find full path from partial string
        data = load_data()
        due = [x[0] for x in get_due_problems(data)]
        target = None
        for f in due:
            if args.file in f:
                target = f
                break
        
        if target:
            update_review(target, args.quality)
        else:
            print("❌ File not found in due list. Check the name?")

if __name__ == "__main__":
    main()