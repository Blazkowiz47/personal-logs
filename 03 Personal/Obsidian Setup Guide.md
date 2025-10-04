# Obsidian Setup Guide - New Installation

## 📋 Prerequisites
1. Install Obsidian from https://obsidian.md
2. Clone/sync your vault to the new machine
3. Open the vault in Obsidian

## 🔌 Required Plugins

### Community Plugins to Install
Settings → Community plugins → Browse and install:

1. **Dataview** - For habit tracking and queries
2. **Templater** - For templates
3. **Calendar** - For daily note creation
4. **Periodic Notes** - For daily/weekly notes
5. **Obsidian Tracker** - For habit visualization
6. **Vimrc Support** - For Vim keybindings (optional)

After installing, **enable all** of them.

---

## ⚙️ Core Plugin Configuration

### Settings → Core Plugins

Enable these:
- ✅ **Daily notes**
- ✅ **Templates** (optional, we use Templater mostly)
- ✅ **Backlinks**
- ✅ **Outgoing links**
- ✅ **Tag pane**
- ✅ **File recovery**
- ✅ **Sync** (if using Obsidian Sync)

---

## 📝 Daily Notes Configuration

**Settings → Core plugins → Daily notes:**

- **Date format:** `YYYY-MM-DD`
- **New file location:** `01 Daily Notes`
- **Template file location:** `Templates/Daily Note Template`

---

## 📅 Periodic Notes Configuration

**Settings → Periodic Notes:**

### Daily Notes
- **Folder:** `01 Daily Notes`
- **Format:** `YYYY/YYYY-MM/YYYY-MM-DD`
- **Template:** `Templates/Daily Note Template`

### Weekly Notes
- **Folder:** `01 Daily Notes`
- **Format:** `YYYY/Weekly/YYYY-[W]ww`
- **Template:** `Templates/Weekly Review Template`

---

## 🔧 Templater Configuration

**Settings → Templater:**

### General Settings
- **Template folder location:** `Templates`
- ✅ **Trigger Templater on new file creation**
- ✅ **Enable System Commands**

### Folder Templates
Click **+ Add New** for each:

| Folder | Template |
|--------|----------|
| `10 Mobai (Work)/1 Projects` | `Templates/Work Project Template` |
| `20 PhD/1 Projects` | `Templates/PhD Project Template` |
| `30 Reading List/To Read` | `Templates/Paper Note Template` |
| `20 PhD/3 Resources` | `Templates/Concept Note Template` |

---

## 📊 Dataview Configuration

**Settings → Dataview:**

- ✅ **Enable JavaScript Queries** (optional, for advanced queries)
- ✅ **Enable Inline Queries**
- **Date Format:** `YYYY-MM-DD`

No other config needed - it works out of the box!

---

## 🗓️ Calendar Configuration

**Settings → Calendar:**

No special configuration needed. It automatically uses your Daily Notes settings.

Optional:
- **Show week number:** Enable if you want
- **Start week on Monday:** Enable if preferred

---

## ⌨️ Vim Configuration 

### Settings → Editor
- ✅ **Vim key bindings**

### Settings → Vimrc Support
- **Vimrc file name:** `.obsidian.vimrc` 

The `.obsidian.vimrc` file is already in your vault root with custom keybindings.

---

## ⌨️ Hotkeys (Optional but Recommended)

**Settings → Hotkeys**

Search and set these:

| Command                                  | Hotkey                 |     |
| ---------------------------------------- | ---------------------- | --- |
| **Templater: Insert Template**           | `Ctrl/Cmd + T`         |     |
| **Daily notes: Open today's daily note** | `Ctrl/Cmd + D`         |     |
| **Quick switcher: Open quick switcher**  | `Ctrl/Cmd + O`         |     |
| **Search: Search in all files**          | `Ctrl/Cmd + Shift + F` |     |

---
## 🎨 Appearance (Optional)

**Settings → Appearance:**
- **Base color scheme:** Light/Dark (your preference)
- **Theme:** Minimal (already installed)
- **CSS Snippets:** None required
---
## 📁 File & Links Settings
**Settings → Files & Links:**
- **Deleted files:** Move to Obsidian trash
- **Default location for new notes:** Same folder as current file
- ✅ **Automatically update internal links**
- **Use [[Wikilinks]]:** Enable
- **Default location for new attachments:** In subfolder under current folder
---
## 🔄 Sync Setup 
### Git (Free - Recommended)
1. Install **Obsidian Git** plugin
2. **Settings → Obsidian Git:**
   - ✅ **Auto backup after file change**
   - **Backup interval:** 5 minutes
   - ✅ **Auto pull on startup**
   - ✅ **Auto push**
   - **Commit message:** `vault backup: {{date}}`
---
## ✅ Verification Checklist
After setup, verify everything works:
- [ ] Open Dashboard.md - Dataview queries show data
- [ ] Press Ctrl/Cmd + D - Creates today's daily note in correct folder
- [ ] Create new note in `10 Mobai (Work)/1 Projects/` - Template auto-applies
- [ ] Press `jk` in insert mode (Vim) - Exits to normal mode
- [ ] Type `gd` on a link - Follows the link
- [ ] Calendar shows in right sidebar
- [ ] Habit Tracker shows Dataview tables
---

## 📚 Quick Reference
**Folder Structure:**
```
00 Inbox/
01 Daily Notes/
  ├── Templates/
  └── 2025/
02 Habits & Goals/
03 Personal/
10 Mobai (Work)/
  ├── 1 Projects/
  ├── 2 Areas/
  ├── 3 Resources/
  └── Archives/
20 PhD/
  ├── 1 Projects/
  ├── 2 Areas/
  ├── 3 Resources/
  └── Archives/
30 Reading List/
  ├── To Read/
  ├── Reading/
  └── Read/
Templates/
Dashboard.md
```

**Key Files:**
- `Dashboard.md` - Your command center
- `Templates/` - All templates
- `.obsidian.vimrc` - Vim configuration
---

## 🚨 Troubleshooting
**Dataview not working?**
- Check if Dataview plugin is enabled
- Make sure you're in Reading Mode (Ctrl/Cmd + E)
- Refresh view (Ctrl/Cmd + R)
**Templates not auto-applying?**
- Check Templater → Folder Templates settings
- Make sure "Trigger on new file creation" is enabled
- Folder paths must match exactly
**Daily notes in wrong location?**
- Check Periodic Notes format: `YYYY/YYYY-MM/YYYY-MM-DD`
- Check folder is `01 Daily Notes` (not full path)
**Vim not working?**
- Enable Vim key bindings in Settings → Editor
- Install Vimrc Support plugin
- Check `.obsidian.vimrc` file exists in vault root

**Last Updated:** 2025-10-04
**Vault Version:** Personal Knowledge Management System v1.0
