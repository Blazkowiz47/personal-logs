# Daily Standups

## Quick Create
Use Templater to create today's standup: 
- Right-click "Standup Template.md" 
- Select "Templater: Create new note from template"

Or manually create notes Mon-Fri.

## This Week's Standups
\`\`\`dataview
LIST
FROM "10 Mobai (Work)/2 Areas/Daily Standups/2025"
WHERE file.day >= date(today) - dur(7 days)
SORT file.name DESC
\`\`\`

## Standup Archive
\`\`\`dataview
TABLE file.day as "Date"
FROM "10 Mobai (Work)/2 Areas/Daily Standups/2025"
SORT file.name DESC
LIMIT 30
\`\`\`

---
Tags: #work #standup #meetings #area
