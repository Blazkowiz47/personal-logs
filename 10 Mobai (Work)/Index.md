# 🏢 Mobai Work Dashboard

> "Manage yourself, not the company."

## 🎯 Active Projects
```dataview
TABLE status, priority, deadline
FROM "10 Mobai (Work)/1 Projects"
WHERE contains(tags, "project") AND status != "Completed"
SORT priority DESC, deadline ASC
```

## 🛠️ Areas of Responsibility
- [[2 Areas/PAD Algorithm Development/Index|🧠 PAD Development]] - *My core domain*
- [[2 Areas/Pipeline Maintenance/Index|🔧 Pipeline Maintenance]] - *Keeping the lights on*

## ⚡ Quick Actions
- [[../../Templates/Work Project Template|➕ New Project]]

## 📝 Recent Notes
```dataview
LIST
FROM "10 Mobai (Work)"
WHERE file.name != "Index"
SORT file.mtime DESC
LIMIT 10
```

---
## 🧠 Career & Growth
- **Role:** Research Scientist / Engineer
- **Focus:** PAD, Deep Learning, Scalable Pipelines
- **Goals:**
	- [ ] Deliver scalable `pad_candidate` pipeline
	- [ ] Publish internal research on Score Fusion
	- [ ] Bridge PhD research with company needs (safely)

