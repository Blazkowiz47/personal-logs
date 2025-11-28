#!/usr/bin/env python3
"""
Clean up template content from paper notes, keeping only meaningful content.
Goes through each file one by one as requested.
"""
import os
import re
from pathlib import Path

LITERATURE_DIR = Path("/Users/sushrutpatwardhan/Documents/obsidian-vault/20 PhD/2 Areas/Literature Review")

# Template content patterns to remove
TEMPLATE_PATTERNS = [
    r"What problem does this paper address\?",
    r"\*Describe the model/approach\*",
    r"\*What's new/different from prior work\?\*",
    r"\*Key metrics and performance\*",
    r"\*What components were tested\?\*",
    r"\*Anything useful for implementing this\*",
    r"\*My thoughts on the paper\*",
    r"\*How does this relate to my PAD research\?\*",
    r"\*Discussions with advisor/colleagues about this paper\*",
    r"- Figure X:",
    r"---\n\*\*Reading Progress:\*\*\n(?:- \[[ x]\] (?:Abstract|Introduction|Related Work|Methodology|Experiments|Conclusion|Supplementary Material)\n?)+",
]

# Lines to remove completely
LINES_TO_REMOVE = [
    "What problem does this paper address?",
    "*Describe the model/approach*",
    "*What's new/different from prior work?*",
    "*Key metrics and performance*",
    "*What components were tested?*",
    "*Anything useful for implementing this*",
    "*My thoughts on the paper*",
    "*How does this relate to my PAD research?*",
    "*Discussions with advisor/colleagues about this paper*",
    "- Figure X:",
    "- [[]]",
    ">",
    "$$",
    "- [ ]",
    "---",
    "**Reading Progress:**",
    "- [ ] Abstract",
    "- [ ] Introduction", 
    "- [ ] Related Work",
    "- [ ] Methodology",
    "- [ ] Experiments",
    "- [ ] Conclusion",
    "- [ ] Supplementary Material",
    "- [x] Abstract",
    "- [x] Introduction",
    "- [x] Related Work",
    "- [x] Methodology",
    "- [x] Experiments",
    "- [x] Conclusion",
    "- [x] Supplementary Material",
]

def clean_file(filepath):
    """Clean a single file of template remnants."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Split into lines
    lines = content.split('\n')
    cleaned_lines = []
    
    skip_next_empty = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Skip template lines
        if stripped in LINES_TO_REMOVE:
            skip_next_empty = True
            continue
        
        # Skip empty lines after removed template lines
        if skip_next_empty and stripped == '':
            continue
        
        skip_next_empty = False
        cleaned_lines.append(line)
    
    # Rejoin and clean up multiple empty lines
    content = '\n'.join(cleaned_lines)
    content = re.sub(r'\n{4,}', '\n\n\n', content)  # Max 2 empty lines
    
    # Clean trailing whitespace
    content = content.rstrip() + '\n'
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    files_to_skip = ['Index.md', 'Deep Learning for Face Anti-Spoofing - A Survey.md', 'Papers Database.md.backup']
    
    cleaned_count = 0
    for filepath in sorted(LITERATURE_DIR.glob('*.md')):
        if filepath.name in files_to_skip:
            continue
        
        if clean_file(filepath):
            print(f"Cleaned: {filepath.name}")
            cleaned_count += 1
        else:
            print(f"Already clean: {filepath.name}")
    
    print(f"\n✅ Cleaned {cleaned_count} files")

if __name__ == '__main__':
    main()
