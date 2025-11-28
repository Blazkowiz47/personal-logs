import os
import re

directory = "/Users/sushrutpatwardhan/Documents/obsidian-vault/20 PhD/2 Areas/Literature Review"
exclude_files = [
    "Index.md",
    "Deep Learning for Face Anti-Spoofing - A Survey.md",
    "Papers Database.md.backup",
    "Flexible-Modal Face Anti-Spoofing - A Benchmark.md",
    "Neuroscience to Deep Learning Papers.md",
    "Dino v3.md"
]

def clean_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split frontmatter and body
    match = re.match(r'^(---\n.*?\n---\n)(.*)', content, re.DOTALL)
    if not match:
        print(f"Skipping {filepath}: No frontmatter found")
        return
    
    frontmatter = match.group(1)
    body = match.group(2)
    
    # Find the title (first # heading)
    title_match = re.search(r'^# .+$', body, re.MULTILINE)
    title = title_match.group(0) if title_match else ""
    
    # Extract blockquotes/callouts between title and first ## section
    pre_content = ""
    if title:
        after_title = body[title_match.end():]
        section1_match = re.search(r'^## What does the paper present\?', after_title, re.MULTILINE)
        if section1_match:
            pre_content = after_title[:section1_match.start()].strip()
    
    # Find section 1 content
    section1_match = re.search(r'^## What does the paper present\?\n(.*?)(?=^## What are my views on it\?|\Z)', body, re.MULTILINE | re.DOTALL)
    section1_content = section1_match.group(1).strip() if section1_match else ""
    
    # Find section 2 content
    section2_match = re.search(r'^## What are my views on it\?\n(.*)', body, re.MULTILINE | re.DOTALL)
    section2_content = section2_match.group(1).strip() if section2_match else ""
    
    def clean_section(text):
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            stripped = line.strip()
            
            # Skip ANY line that starts with "- **" (bullet with bold label)
            if re.match(r'^[-*]\s*\*\*', stripped):
                continue
            
            # Skip numbered items that are just "1. **Label:** short text"
            if re.match(r'^\d+\.\s+\*\*[^*]+\*\*:', stripped):
                continue
            
            cleaned_lines.append(line)
        
        # Join lines
        result = '\n'.join(cleaned_lines)
        
        # Remove multiple consecutive newlines
        result = re.sub(r'\n{3,}', '\n\n', result)
        
        return result.strip()
    
    section1_clean = clean_section(section1_content)
    section2_clean = clean_section(section2_content)
    
    # Build new content
    new_body = ""
    if title:
        new_body = f"{title}\n\n"
    if pre_content:
        new_body += f"{pre_content}\n\n"
    
    new_body += "## What does the paper present?\n"
    if section1_clean:
        new_body += f"{section1_clean}\n\n"
    else:
        new_body += "\n"
    
    new_body += "## What are my views on it?\n"
    if section2_clean:
        new_body += f"{section2_clean}\n"
    else:
        new_body += "\n"
    
    new_content = frontmatter + new_body
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Cleaned {filepath}")

def main():
    for filename in os.listdir(directory):
        if filename.endswith(".md") and filename not in exclude_files:
            filepath = os.path.join(directory, filename)
            try:
                clean_file(filepath)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
