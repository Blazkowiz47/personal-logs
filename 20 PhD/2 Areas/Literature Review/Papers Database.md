---
tags: [phd, literature, papers, database]
---

# Papers Database

This page tracks all research papers I've read or plan to read for my PhD research.

## Quick Stats
```dataview
TABLE WITHOUT ID
	choice(status = "✅ Read", "✅", choice(status = "📖 Reading", "📖", "📚")) as "📊",
	length(rows) as "Count"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper")
GROUP BY status
```

## Papers by Status

### 📚 To Read
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	authors as "Authors",
	year as "Year",
	venue as "Venue",
	dateadded as "Added"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND status = "📚 To Read"
SORT year DESC, dateadded DESC
```

### 📖 Currently Reading
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	authors as "Authors",
	year as "Year",
	venue as "Venue",
	dateadded as "Added"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND status = "📖 Reading"
SORT dateadded DESC
```

### ✅ Read
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	authors as "Authors",
	year as "Year",
	venue as "Venue",
	dateread as "Date Read"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND status = "✅ Read"
SORT dateread DESC, year DESC
```

## Papers by Topic

### Presentation Attack Detection (PAD)
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "pad")
SORT status ASC, year DESC
```

### Morph Attack Detection (MAD)
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "mad")
SORT status ASC, year DESC
```

### DeepFake Detection
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "deepfake")
SORT status ASC, year DESC
```

### Multi-Modal / Cross-Modal
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "multimodal") OR contains(tags, "cross-modal")
SORT status ASC, year DESC
```

### Domain Adaptation / Generalization
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "domain-adaptation") OR contains(tags, "generalization")
SORT status ASC, year DESC
```

## Papers by Venue

### Top Conferences
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	status as "Status",
	authors as "Authors"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND (contains(venue, "CVPR") OR contains(venue, "ICCV") OR contains(venue, "ECCV") OR contains(venue, "NeurIPS") OR contains(venue, "ICLR"))
SORT venue ASC, year DESC
```

### Biometrics & Security Journals
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	status as "Status",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND (contains(venue, "TIFS") OR contains(venue, "IET") OR contains(venue, "Biometrics") OR contains(venue, "ICB"))
SORT year DESC
```

## Papers by Year

```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	venue as "Venue",
	status as "Status",
	authors as "Authors"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper")
SORT year DESC, venue ASC
```

## Recently Added
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue",
	dateadded as "Added"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper")
SORT dateadded DESC
LIMIT 10
```

## Papers with Code
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	code_url as "Code"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND code_url
SORT year DESC
```

## Papers to Implement
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "to-implement")
SORT year DESC
```

## High Priority Papers
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue",
	dateadded as "Added"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "high-priority")
SORT dateadded DESC
```

---

## How to Use This Database

1. **Adding a new paper**: Use the Paper Note Template in `/Templates/Paper Note Template.md`
2. **Update status**: Change the status field in the frontmatter to:
   - `📚 To Read` - Papers in your reading queue
   - `📖 Reading` - Currently reading
   - `✅ Read` - Finished reading and summarized
3. **Tag appropriately**: Use relevant tags like #pad, #mad, #deepfake, #multimodal, etc.
4. **Add implementation tag**: Use #to-implement for papers you want to replicate

## Quick Links
- [[Index|Literature Review Index]]
- [[../../1 Projects/|PhD Projects]]
- [[../Experiment Tracking/Index|Experiment Tracking]]
