import os
import re

directory = "/Users/sushrutpatwardhan/Documents/obsidian-vault/20 PhD/2 Areas/Literature Review"
exclude_files = [
    "Index.md",
    "Deep Learning for Face Anti-Spoofing - A Survey.md",
    "Papers Database.md.backup",
    "Flexible-Modal Face Anti-Spoofing - A Benchmark.md",
    "Neuroscience to Deep Learning Papers.md",
    "Dino v3.md" # This looked like a note but might not follow the template, I'll check it later or just process it.
]

# Define the mapping
group1_headers = [
    "Quick Summary",
    "Problem Statement",
    "Key Contributions",
    "Methodology",
    "Experiments",
    "Implementation Notes",
    "Related Papers"
]

group2_headers = [
    "Strengths",
    "Limitations",
    "Critical Analysis",
    "Relevance to My Work",
    "Questions & Future Directions",
    "Notes & Highlights",
    "Meeting Notes",
    "Action Items",
    "Notes" # Found in 3DPC-Net
]

def parse_file(content):
    # Split frontmatter and body
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return None, None
    
    frontmatter = match.group(1)
    body = match.group(2)
    return frontmatter, body

def extract_sections(body):
    # Find all headers level 2
    # We assume headers are ## Header Name
    # We capture the header name and the content following it until the next header
    
    sections = {}
    
    # Split by headers
    # This regex looks for lines starting with ## 
    parts = re.split(r'(^## .+$)', body, flags=re.MULTILINE)
    
    # parts[0] is content before first header (usually title)
    pre_header_content = parts[0]
    
    current_header = None
    
    for part in parts[1:]:
        if part.startswith("## "):
            current_header = part.strip("# ").strip()
            sections[current_header] = ""
        else:
            if current_header:
                sections[current_header] += part
            else:
                # This shouldn't happen if split works as expected with capturing group
                pass
                
    return pre_header_content, sections

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        
    frontmatter, body = parse_file(content)
    if not frontmatter:
        print(f"Skipping {filepath}: No frontmatter found")
        return

    pre_header_content, sections = extract_sections(body)
    
    new_body = pre_header_content
    
    # Build Section 1
    section1_content = ""
    for header in group1_headers:
        if header in sections and sections[header].strip():
            section1_content += f"### {header}\n{sections[header].strip()}\n\n"
            
    # Build Section 2
    section2_content = ""
    for header in group2_headers:
        if header in sections and sections[header].strip():
            section2_content += f"### {header}\n{sections[header].strip()}\n\n"
            
    # If we found any content for the new sections, append them
    # If not, we might be processing a file that doesn't follow the template.
    # In that case, we should probably preserve the original body or put it all in section 1?
    # Let's assume if we found NO known headers, we put everything in "What does the paper present?"
    
    if not section1_content and not section2_content:
        # Check if there are other headers we missed
        if sections:
            # Put everything in section 1
            for header, text in sections.items():
                 section1_content += f"### {header}\n{text.strip()}\n\n"
        else:
            # No headers found, put raw body in section 1 (excluding pre-header which is usually title)
            # Actually pre_header_content is already added.
            # If body had no headers, extract_sections puts everything in pre_header_content?
            # No, split returns the whole string in parts[0] if no delimiter found.
            pass

    new_body += "\n## What does the paper present?\n"
    if section1_content:
        new_body += section1_content
    else:
        new_body += "*One-sentence summary of what this paper does*\n\n"

    new_body += "## What are my views on it?\n"
    if section2_content:
        new_body += section2_content
    else:
        new_body += "*My thoughts on the paper*\n\n"
        
    new_content = f"---\n{frontmatter}\n---\n{new_body}"
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

def main():
    for filename in os.listdir(directory):
        if filename.endswith(".md") and filename not in exclude_files:
            filepath = os.path.join(directory, filename)
            try:
                process_file(filepath)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
