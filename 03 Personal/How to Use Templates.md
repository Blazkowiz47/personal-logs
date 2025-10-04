# How to Use Templates in Obsidian

## Method 1: Using Templater Plugin (Recommended)

### Step 1: Configure Templater
Already done! Your template folder is set to `01 Daily Notes/Templates`

But you should also add:
**Settings → Templater → Folder Templates:**
- Add: `30 Reading List/Templates` folder

### Step 2: Create Note from Template

**Option A: Templater Command**
1. Create a new note (Ctrl/Cmd + N)
2. Press Ctrl/Cmd + P (Command Palette)
3. Type "Templater: Insert Template"
4. Choose your template

**Option B: Right-click Template**
1. Right-click on the template file (e.g., "Paper Note Template.md")
2. Select "Templater: Create new note from template"
3. New note created with template content!

**Option C: Hotkey (Best for frequent use)**
1. Go to Settings → Hotkeys
2. Search "Templater: Insert Template"
3. Assign a hotkey (e.g., Ctrl/Cmd + T)
4. Use hotkey in any new note

## Method 2: Using Core Templates Plugin

**Step 1: Enable Core Templates**
Settings → Core plugins → Enable "Templates"

**Step 2: Configure**
Settings → Templates:
- Template folder location: `30 Reading List/Templates`

**Step 3: Insert Template**
1. Create new note
2. Press Ctrl/Cmd + P
3. Type "Insert template"
4. Choose template

## Quick Workflow Examples

### Creating a Paper Note
1. Go to `30 Reading List/To Read/`
2. Create new note: "ArcFace Face Recognition"
3. Press Ctrl/Cmd + P → "Templater: Insert Template"
4. Choose "Paper Note Template"
5. Fill in the aliases at top:
   ```yaml
   aliases: [ArcFace, arcface, ARCFACE, ArcFace Loss]
   ```
6. Fill in the rest!

### Creating a Concept Note
1. Go to `20 PhD/3 Resources/`
2. Create new note: "Contrastive Learning"
3. Insert template
4. Add aliases:
   ```yaml
   aliases: [contrastive loss, SimCLR approach, self-supervised contrastive]
   ```

## Pro Tips

### 1. Aliases
Always add aliases for:
- Different capitalizations (ArcFace, arcface, ARCFACE)
- Abbreviations (ResNet, Residual Network)
- Common misspellings
- Alternative names

### 2. Tags
Use consistent tags:
- Papers: `#paper #pad #cvpr2024`
- Concepts: `#concept #deeplearning #loss-function`
- Work: `#work #mobai #project`
- PhD: `#phd #experiment #ocim`

### 3. Links
Link everything:
- Papers cite other papers: `[[Related Paper Name]]`
- Concepts link to papers: `[[Paper that introduced this]]`
- Notes link to areas: `[[PAD Algorithm Development/Index]]`

### 4. Template Variables
Templater supports:
- `{{date:YYYY-MM-DD}}` - Today's date
- `{{date:YYYY-MM-DD HH:mm}}` - Date with time
- `{{title}}` - Note title

## My Recommendation

**For Paper Notes:**
1. Create note in `30 Reading List/To Read/`
2. Name it: `[First Author Year] - Paper Title`
   - Example: `Deng 2019 - ArcFace Additive Angular Margin Loss`
3. Insert Paper Note Template
4. Add aliases for common variations
5. Move to `Reading/` when you start
6. Move to `Read/` when done

**For Concept Notes:**
1. Create in `20 PhD/3 Resources/`
2. Name it clearly: `ArcFace Loss`, `Contrastive Learning`, etc.
3. Insert Concept Note Template
4. Link to papers that use it

---
Need help? Check the templates in:
- `01 Daily Notes/Templates/`
- `30 Reading List/Templates/`
