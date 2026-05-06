import os
import re

new_code_path = r'c:\Users\pc30r\Desktop\Anki_Automation-main\Anki_gui.py'
with open(new_code_path, 'r', encoding='utf-8') as f:
    new_code = f.read().strip()

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the python code inside the markdown or HTML
    pattern = r'(?s)import tkinter as tk.*?if __name__ == "__main__":\s*main\(\)'
    
    new_content, count = re.subn(pattern, new_code.replace('\\', '\\\\'), content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Failed to find target in {filepath}")

update_file(r'c:\Users\pc30r\Desktop\Anki_Automation-main\index.html')
update_file(r'c:\Users\pc30r\Desktop\Anki_Automation-main\ANKI_AUTOMAÇÃO\tutorial_extracted.txt')

# Also copy Anki_gui.py to the subfolder
import shutil
shutil.copy2(new_code_path, r'c:\Users\pc30r\Desktop\Anki_Automation-main\ANKI_AUTOMAÇÃO\anki_gui.py')
print("Copied to subfolder")
