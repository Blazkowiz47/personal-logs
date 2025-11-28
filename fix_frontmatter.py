#!/usr/bin/env python3
"""
Fix frontmatter by adding --- delimiters where missing
"""
import re
from pathlib import Path

LITERATURE_DIR = Path("/Users/sushrutpatwardhan/Documents/obsidian-vault/20 PhD/2 Areas/Literature Review")

def fix_frontmatter(filepath):
    """Add missing --- frontmatter delimiters."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file starts with frontmatter (aliases: or tags:) without ---
    if content.startswith('aliases:') or content.startswith('tags:'):
        # Find where frontmatter ends (first blank line followed by # or ## )
        # Or look for where actual content starts
        lines = content.split('\n')
        frontmatter_end = 0
        in_frontmatter = True
        
        for i, line in enumerate(lines):
            # Frontmatter ends when we hit an empty line followed by content
            # or when we hit a markdown header
            if line.startswith('#'):
                frontmatter_end = i
                break
            if line.startswith('> [!'):  # Callout block
                frontmatter_end = i
                break
        
        if frontmatter_end > 0:
            # Insert --- at beginning and after frontmatter
            lines.insert(0, '---')
            lines.insert(frontmatter_end + 1, '---')
            content = '\n'.join(lines)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    
    return False

def main():
    files_to_skip = ['Index.md', 'Deep Learning for Face Anti-Spoofing - A Survey.md', 'Papers Database.md.backup']
    
    fixed_count = 0
    for filepath in sorted(LITERATURE_DIR.glob('*.md')):
        if filepath.name in files_to_skip:
            continue
        
        if fix_frontmatter(filepath):
            print(f"Fixed: {filepath.name}")
            fixed_count += 1
    
    print(f"\n✅ Fixed {fixed_count} files")

if __name__ == '__main__':
    main()
