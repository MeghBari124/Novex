import os

def generate_tree(startpath, exclude_dirs, exclude_files):
    tree_lines = []
    for root, dirs, files in os.walk(startpath):
        # Filter directories in-place
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        
        if level > 0:
            tree_lines.append(f"{indent}{os.path.basename(root)}/")
        
        sub_indent = '│   ' * level + '├── '
        for i, f in enumerate(files):
            if f in exclude_files or f.startswith('.') or f.endswith('.pyc') or f.endswith('.pkl'):
                continue
            # If it's the last file in the directory, use a different branch symbol
            if i == len(files) - 1 and not dirs:
                 symbol = '└── '
            else:
                 symbol = '├── '
            tree_lines.append(f"{'│   ' * level}{symbol}{f}")
            
    return tree_lines

if __name__ == "__main__":
    project_root = r"d:\DEGREE\ACADEMIC\HACKTHON\Let_Go_3.0"
    exclude_dirs = {'node_modules', '__pycache__', '.git', '.next', 'dist', 'build', '.vercel', '.agent', '.gemini', '.vscode', 'dev-dist'}
    exclude_files = {'package-lock.json', 'project_structure.txt', 'project_structure_utf8.txt', 'cleaned_structure.txt', 'filter_tree.py', 'tree_generator.py'}
    
    tree = generate_tree(project_root, exclude_dirs, exclude_files)
    
    with open('PROJECT_STRUCTURE.md', 'w', encoding='utf-8') as f:
        f.write("# Project Directory Structure\n\n")
        f.write("```text\n")
        f.write("Let_Go_3.0/\n")
        for line in tree:
            f.write(line + "\n")
        f.write("```\n")
