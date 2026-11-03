import re

def clean_tree(input_file, output_file):
    exclude_patterns = [
        r'node_modules',
        r'__pycache__',
        r'\.git',
        r'\.next',
        r'dist',
        r'build',
        r'\.vercel',
        r'\.agent',
        r'\.gemini',
        r'\.vscode',
        r'package-lock\.json',
        r'project_structure.*\.txt'
    ]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    filtered_lines = []
    skip_depth = -1
    
    for line in lines:
        # Check indentation depth to see if we should continue skipping
        match = re.search(r'([+|\\ ]---|[| ])', line)
        if match:
            depth = line.find(match.group(0))
        else:
            depth = 0
            
        if skip_depth != -1:
            if depth > skip_depth:
                continue
            else:
                skip_depth = -1
        
        # Check if line contains any exclude pattern
        should_exclude = any(re.search(pattern, line) for pattern in exclude_patterns)
        
        if should_exclude:
            # If it's a directory (starts with +---), skip its children too
            if '+---' in line:
                skip_depth = depth
            continue
            
        filtered_lines.append(line)
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

if __name__ == "__main__":
    clean_tree('project_structure_utf8.txt', 'cleaned_structure.txt')
