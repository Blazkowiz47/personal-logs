# 🏠 Dashboard

## 📅 Quick Access
- [[Current Goals]] - Q4 2025 objectives
- [[Habit Tracker]] - Daily routine tracking
- [[My Ideal Routine]] - Target schedule
- Today: [[{{date:YYYY-MM-DD}}]]

## 🎯 Active Work Projects
```dataview
LIST
FROM "10 Mobai (Work)/1 Projects"
WHERE file.name != "1 Projects"
```

## 🔬 Active PhD Projects
```dataview
LIST
FROM "20 PhD/1 Projects"
WHERE file.name != "1 Projects"
```

## 📋 Work Areas
- [[PAD Algorithm Development/Index|PAD Algorithm]]
- [[Pipeline Maintenance/Index|Pipeline Refactoring]]
- [[SOTA Research Tracking/Index|SOTA Research]]
- [[Daily Standups/Index|Standups]]

## 🎓 PhD Areas
- [[Literature Review/Index|Literature Review]]
- [[Mathematical Foundations/Index|Math Foundations]]
- [[Dataset Management (OCIM)/Index|OCIM Datasets]]
- [[Experiment Tracking/Index|Experiments]]
- [[Writing Practice/Index|Writing Skills]]

## 📥 Inbox (Process Weekly)
```dataview
TABLE file.mtime as "Modified"
FROM "00 Inbox"
SORT file.mtime DESC
LIMIT 10
```

## 📚 Reading List
### Currently Reading
```dataview
LIST
FROM "30 Reading List/Reading"
```

### To Read Next
```dataview
LIST
FROM "30 Reading List/To Read"
LIMIT 5
```

## 🏃 This Week's Habits
```dataview
TABLE WITHOUT ID
  file.link as "Date",
  choice(contains(string(file.tasks), "Wake up at 6:00") AND meta(file.tasks).completed, "✅", "❌") as "6AM",
  choice(contains(string(file.tasks), "Gym") AND meta(file.tasks).completed, "✅", "❌") as "Gym",
  choice(contains(string(file.tasks), "PhD Work") AND meta(file.tasks).completed, "✅", "❌") as "PhD",
  choice(contains(string(file.tasks), "NoFap") AND meta(file.tasks).completed, "✅", "❌") as "NoFap"
FROM "01 Daily Notes"
WHERE file.day >= date(today) - dur(7 days)
SORT file.name DESC
```

## 📝 Recent Notes
```dataview
TABLE file.mtime as "Modified"
FROM "" AND -"Templates" AND -".obsidian"
SORT file.mtime DESC
LIMIT 10
```

---
*Your command center - Start here every day*
