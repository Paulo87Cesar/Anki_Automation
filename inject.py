import re

with open('new_code.py', 'r', encoding='utf-8') as f:
    new_code = f.read().strip()

def replace_in_file(filepath, pattern, new_content):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We look for the python code block starting with `import tkinter as tk` and ending with `if __name__ == "__main__":\n    main()`
    
    # Regex to find the block
    regex = re.compile(r'import tkinter as tk.*?if __name__ == "__main__":\s*main\(\)', re.DOTALL)
    
    new_content_full = new_content
    
    content, count = regex.subn(new_content_full, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced in {filepath}")
    else:
        print(f"Pattern not found in {filepath}")

replace_in_file('index.html', '', new_code)
replace_in_file('ANKI_AUTOMAÇÃO/tutorial_extracted.txt', '', new_code)
