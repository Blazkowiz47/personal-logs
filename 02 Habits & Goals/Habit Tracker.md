# Habit Tracker 2025

## 🎯 Daily Habits

### Morning Routine (6:00 - 8:00 AM)
- 🌅 Wake up at 6:00 AM
- 🪥 Brush by 6:15 AM
- 💧 Drink water
- 🧘 Shambhavi Mahamudra (40 min)
- 🍳 Prepare food
- 🚗 Leave by 8:00 AM

### Work (8:00 AM - 3:00 PM)
- 💼 Daily standup
- 🧠 Deep work on PAD
- 📊 Progress tracking

### Evening Routine (3:00 - 8:00 PM)
- 🏃 Gym (30 min) after work
- 🚿 Bath
- 🧘 Shambhavi Mahamudra short (25 min)
- ❤️ Time with wife (dinner & stroll)

### PhD Work (8:00 - 10:00 PM)
- 🔬 Research/reading
- ✍️ Daily log writing
- 📚 Paper summaries

### Night Routine (10:00 - 11:00 PM)
- ❤️ Quality time with wife
- 🌙 Sleep by 11:00 PM

### Wellness
- 🚫 NoFap tracking

## 📊 Weekly Tracking

### This Week's Progress
```dataview
TABLE WITHOUT ID
  file.link as "Date",
  choice(contains(string(file.tasks), "Wake up at 6:00"), "✅", "❌") as "6AM",
  choice(contains(string(file.tasks), "Shambhavi Mahamudra (40 min)") AND meta(file.tasks).completed, "✅", "❌") as "AM🧘",
  choice(contains(string(file.tasks), "Gym") AND meta(file.tasks).completed, "✅", "❌") as "💪",
  choice(contains(string(file.tasks), "Shambhavi Mahamudra evening") AND meta(file.tasks).completed, "✅", "❌") as "PM🧘",
  choice(contains(string(file.tasks), "PhD Work"), "✅", "❌") as "🔬",
  choice(contains(string(file.tasks), "NoFap"), "✅", "❌") as "🚫"
FROM "01 Daily Notes"
WHERE file.day >= date(today) - dur(7 days)
SORT file.name DESC
```

### Monthly Overview
```dataview
TABLE WITHOUT ID
  dateformat(file.day, "yyyy-MM") as "Month",
  length(filter(file.tasks, (t) => contains(string(t), "Wake up at 6:00") AND t.completed)) as "6AM Wake",
  length(filter(file.tasks, (t) => contains(string(t), "Shambhavi Mahamudra (40 min)") AND t.completed)) as "AM Meditation",
  length(filter(file.tasks, (t) => contains(string(t), "Gym") AND t.completed)) as "Gym",
  length(filter(file.tasks, (t) => contains(string(t), "PhD Work") AND t.completed)) as "PhD",
  length(filter(file.tasks, (t) => contains(string(t), "NoFap") AND t.completed)) as "NoFap Days"
FROM "01 Daily Notes"
WHERE file.day >= date(today) - dur(90 days)
GROUP BY dateformat(file.day, "yyyy-MM")
SORT rows.file.name DESC
```

## 🔥 Current Streaks
**6 AM Wake:** ___ days
**Morning Meditation:** ___ days
**Gym:** ___ days
**Evening Meditation:** ___ days
**PhD Work:** ___ days
**NoFap:** ___ days
**Daily Logs:** ___ days

## 🎯 This Month's Goals
- [ ] Wake at 6 AM - 25/30 days
- [ ] Morning Shambhavi - 25/30 days
- [ ] Gym - 25/30 days
- [ ] Evening Shambhavi - 25/30 days
- [ ] PhD 2hrs - 25/30 days
- [ ] NoFap - 30/30 days
- [ ] Daily logging - 30/30 days

## 💡 Tips
- Set multiple alarms for 6 AM
- Prepare gym clothes night before
- Keep meditation space clean
- Block 8-10 PM calendar for PhD
- Journal immediately after PhD work
- Track NoFap in private section

---
Tags: #habits #tracking #routine
