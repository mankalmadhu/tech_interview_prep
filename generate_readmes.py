
import os
import pathlib

ROOT_DIR = '/Users/madhuahobalan/workspace/tech_interview_prep/PracticeDSA'

def generate_readme_content(dir_name, files):
    content = f"# {dir_name.capitalize()}\n\n"
    content += "This directory contains practice problems related to this topic.\n\n"
    content += "## Files\n\n"
    if not files:
        content += "No python files in this directory.\n"
    else:
        for file in sorted(files):
            content += f"- `{file}`\n"
    return content

def main():
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip the root PracticeDSA folder itself as we manually created a README there
        if root == ROOT_DIR:
            continue
            
        # skip __pycache__ or .git or .venv
        if '__pycache__' in root or '.git' in root or '.venv' in root:
            continue
            
        current_dir_name = os.path.basename(root)
        
        # Filter for relevant files (e.g., .py)
        python_files = [f for f in files if f.endswith('.py') and f != '__init__.py']
        
        readme_path = os.path.join(root, 'README.md')
        
        # Create README if it doesn't exist
        if not os.path.exists(readme_path):
            print(f"Creating README.md for {root}")
            content = generate_readme_content(current_dir_name, python_files)
            with open(readme_path, 'w') as f:
                f.write(content)
        else:
            print(f"README.md already exists for {root}, skipping.")

if __name__ == "__main__":
    main()
