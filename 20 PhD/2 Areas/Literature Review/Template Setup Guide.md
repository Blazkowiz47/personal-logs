# 🚀 Template Setup Guide

This guide will walk you through setting up the paper note template system in Obsidian.

## Prerequisites

You need these Obsidian plugins (already installed in your vault):
- ✅ **Dataview** - For automatic paper organization
- ✅ **Templater** - For using templates with dynamic dates
- ✅ **Core Templates** - Obsidian's built-in template system

## Step-by-Step Setup

### 1. Configure Templater Plugin

1. Open Settings (⚙️) → Community Plugins → Templater → Options
2. Set **Template folder location** to: `Templates`
3. Enable these options:
   - ✅ **Trigger Templater on new file creation**
   - ✅ **Automatic jump to cursor**
4. Set **Date format** to: `YYYY-MM-DD`
5. Click **Save**

### 2. Configure Core Templates (Alternative)

If you prefer using Core Templates:
1. Open Settings → Core Plugins → Enable **Templates**
2. Go to Settings → Templates
3. Set **Template folder location** to: `Templates`
4. Set **Date format** to: `YYYY-MM-DD`

### 3. Test the Template

#### Method A: Using Templater (Recommended)
1. Navigate to `20 PhD/2 Areas/Literature Review/`
2. Create a new note (Ctrl/Cmd + N)
3. Name it (e.g., "Test Paper.md")
4. Press `Ctrl/Cmd + T` or type `/templater` in command palette
5. Select **Paper Note Template**
6. The template should fill in with today's date automatically

#### Method B: Using Core Templates
1. Navigate to `20 PhD/2 Areas/Literature Review/`
2. Create a new note (Ctrl/Cmd + N)
3. Name it (e.g., "Test Paper.md")
4. Press `Ctrl/Cmd + P` to open command palette
5. Type "Insert template"
6. Select **Paper Note Template**
7. Manually replace `{{date:YYYY-MM-DD}}` with today's date

### 4. Verify Dataview is Working

1. Open `Papers Database.md`
2. You should see dataview code blocks like:
   ```dataview
   TABLE ...
   FROM "20 PhD/2 Areas/Literature Review"
   WHERE contains(tags, "paper")
   ```
3. Once you add papers, they will automatically appear in these tables

## Quick Usage Guide

### Adding Your First Paper

Let's add a paper step-by-step:

#### Example: Adding a PAD Paper

1. **Create the note**
   - Go to `20 PhD/2 Areas/Literature Review/`
   - Create new note: `Attention Network for Face Anti-Spoofing.md`

2. **Insert template**
   - Use Ctrl/Cmd + T (Templater) or insert template command
   - Select Paper Note Template

3. **Fill in the frontmatter**
   ```yaml
   ---
   aliases: [AttNet]
   tags: [paper, pad, attention, face-antispoofing]
   authors: John Doe et al.
   year: 2024
   venue: CVPR 2024
   paper_url: https://arxiv.org/abs/...
   code_url: https://github.com/...
   status: "📚 To Read"
   dateadded: 2025-10-18
   dateread: 
   priority: high
   ---
   ```

4. **Fill the title**
   ```markdown
   # Attention Network for Face Anti-Spoofing
   ```

5. **Quick summary (most important!)**
   ```markdown
   ## Quick Summary
   This paper proposes an attention-based network for PAD that focuses on discriminative regions to detect presentation attacks.
   ```

6. **Save the file** (Ctrl/Cmd + S)

7. **Check Papers Database**
   - Open `Papers Database.md`
   - Your paper should now appear in "📚 To Read" section
   - It will also appear in "Presentation Attack Detection" section

#### Example: Adding an Architecture Paper

1. **Create the note**
   ```
   Vision Transformer for Image Classification.md
   ```

2. **Frontmatter**
   ```yaml
   ---
   aliases: [ViT]
   tags: [paper, transformer, vit, architecture, computer-vision, foundational]
   authors: Dosovitskiy et al.
   year: 2021
   venue: ICLR 2021
   paper_url: https://arxiv.org/abs/2010.11929
   code_url: https://github.com/google-research/vision_transformer
   status: "✅ Read"
   dateadded: 2025-10-18
   dateread: 2025-10-18
   priority: high
   ---
   ```

## Common Tagging Patterns

### For PAD Papers
```yaml
tags: [paper, pad, face-antispoofing]
```
**Add based on content:**
- Cross-domain → `#domain-adaptation`
- Multi-modal → `#multimodal`
- Novel dataset → `#dataset`
- Benchmark study → `#benchmark`

### For Architecture Papers
```yaml
tags: [paper, architecture, computer-vision]
```
**Add specific architecture:**
- CNN-based → `#cnn #resnet` or `#mobilenet`
- Transformer → `#transformer #vit`
- Attention mechanism → `#attention`
- Foundational paper → `#foundational`

### For CV Technique Papers
```yaml
tags: [paper, computer-vision]
```
**Add based on technique:**
- Feature learning → `#feature-learning`
- Novel loss → `#loss-function`
- Training method → `#training`
- Data augmentation → `#data-augmentation`

## Updating Status While Reading

### Starting to Read
```yaml
status: "📖 Reading"
```

### Finished Reading
```yaml
status: "✅ Read"
dateread: 2025-10-18
```

## Using the System Daily

### Morning Routine (5 minutes)
1. Open [[Papers Database]]
2. Check "📚 To Read" section
3. Pick 1-2 papers for the day
4. Update their status to "📖 Reading"

### Reading Session
1. Open the paper note
2. Fill sections as you read
3. Focus on:
   - Quick Summary (1 sentence)
   - Key Contributions (3-5 points)
   - Relevance to My Work

### After Reading
1. Update status to "✅ Read"
2. Add `dateread: YYYY-MM-DD`
3. Link related papers in "Related Papers" section
4. Check Papers Database to see it in "✅ Read" section

## Keyboard Shortcuts

| Action | Shortcut | Description |
|--------|----------|-------------|
| New note | Ctrl/Cmd + N | Create new note |
| Insert template | Ctrl/Cmd + T | Templater insert |
| Quick switcher | Ctrl/Cmd + O | Open any note |
| Command palette | Ctrl/Cmd + P | All commands |
| Search | Ctrl/Cmd + Shift + F | Search vault |
| Graph view | Ctrl/Cmd + G | See connections |

## Troubleshooting

### Template dates not working?
- **Solution**: Make sure Templater plugin is enabled and configured
- **Alternative**: Use Core Templates and manually replace dates

### Papers not appearing in Database?
- **Check**: Is the note in `20 PhD/2 Areas/Literature Review/` folder?
- **Check**: Does frontmatter have `tags: [paper, ...]`?
- **Check**: Is Dataview plugin enabled?

### Dataview showing empty tables?
- **Reason**: No papers added yet, or papers don't have required tags
- **Solution**: Add a test paper following examples above

### Links not working?
- **Check**: Use correct wiki-link format: `[[Note Name]]`
- **Check**: File exists in vault
- **Tip**: Ctrl/Cmd + Click to create note if it doesn't exist

## Advanced Tips

### Creating Quick Add Hotkey
1. Settings → Hotkeys
2. Search "Templater: Create new note from template"
3. Assign a hotkey (e.g., Ctrl/Cmd + Shift + N)
4. Now you can quickly create papers with template

### Using Aliases
Add short names to quickly reference papers:
```yaml
aliases: [ResNet, ResNet-50]
```
Now you can link with `[[ResNet]]` instead of full title

### Connecting Papers
When you find related papers, link them:
```markdown
## Related Papers
- [[Vision Transformer]] - Uses similar approach
- [[Cross-Domain PAD Survey]] - Comprehensive overview
```

### Weekly Review Template
Create a note for weekly review:
```markdown
# Week of 2025-10-14

## Papers Read This Week
```dataview
LIST
FROM "20 PhD/2 Areas/Literature Review"
WHERE dateread >= date("2025-10-14") AND dateread <= date("2025-10-20")
```

## Key Insights
- 
```

## Quick Reference

**Files You Need:**
- ✅ `Templates/Paper Note Template.md` - Template for new papers
- ✅ `Papers Database.md` - Auto-organized database
- ✅ `Index.md` - Main literature review hub
- ✅ `Paper Reading Workflow.md` - Complete guide
- ✅ `Quick Reference.md` - Fast lookup

**Essential Fields in Frontmatter:**
```yaml
tags: [paper, pad]  # Always include 'paper' + topic
status: "📚 To Read"  # Update as you read
dateadded: 2025-10-18  # When added
year: 2024  # Publication year
venue: CVPR 2024  # Where published
```

**Most Important Sections:**
1. Quick Summary (1 sentence - do first!)
2. Key Contributions (3-5 points)
3. Relevance to My Work (why it matters)

## Getting Help

- **Full workflow**: [[Paper Reading Workflow]]
- **Quick tips**: [[Quick Reference]]
- **Main hub**: [[Index]]
- **Database**: [[Papers Database]]

## Next Steps

1. ✅ Complete this setup guide
2. [ ] Add 2-3 test papers using the template
3. [ ] Check they appear in Papers Database
4. [ ] Read [[Paper Reading Workflow]] for detailed usage
5. [ ] Start reading and tracking papers!

---

🎉 **You're all set!** Start adding papers and the system will automatically organize them for you.

**Pro tip**: Keep [[Quick Reference]] pinned for easy access while reading papers.
