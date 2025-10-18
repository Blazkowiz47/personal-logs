# 📋 Paper Tracking - Quick Reference

## Essential Files

| File | Purpose |
|------|---------|
| [[Index\|Literature Review Index]] | Main hub for all literature |
| [[Papers Database]] | Searchable database of all papers |
| [[Paper Reading Workflow]] | Complete guide to the system |
| Paper Note Template | Template for new paper notes |

## Adding a Paper - Fast Track

1. **Create**: Use Paper Note Template
2. **Name**: Save as "Paper Title.md" in Literature Review folder
3. **Fill Frontmatter**:
```yaml
tags: [paper, pad]  # Add topic tags
authors: Author Name et al.
year: 2024
venue: CVPR 2024
status: "📚 To Read"
dateadded: 2025-10-18
```
4. **Done!** Paper appears in database automatically

## Status Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 📚 To Read | Queued | Just added, plan to read |
| 📖 Reading | In progress | Currently reading |
| ✅ Read | Complete | Finished & summarized |

## Essential Tags

### Topic Tags
- `#pad` - Presentation Attack Detection
- `#mad` - Morph Attack Detection
- `#deepfake` - DeepFake Detection
- `#multimodal` - Multi-modal methods
- `#domain-adaptation` - Domain generalization

### Priority Tags
- `#high-priority` - Must read soon
- `#to-implement` - Want to implement
- `#benchmark` - Benchmark/evaluation paper
- `#survey` - Survey/review paper
- `#dataset` - Dataset paper

## Reading Checklist

### Quick Read (10 min)
- [ ] Title, abstract, figures
- [ ] Quick Summary (1 sentence)
- [ ] Key contributions

### Normal Read (45 min)
- [ ] Full paper
- [ ] Complete all sections
- [ ] Link related papers

### Deep Read (2 hours)
- [ ] Everything + supplementary
- [ ] Critical analysis
- [ ] Implementation notes

## Key Sections to Fill

### Must Fill
1. **Quick Summary** - One sentence
2. **Key Contributions** - 3-5 points
3. **Relevance to My Work** - How it relates
4. **Status** - Update as you read

### Should Fill
5. **Problem Statement** - What gap?
6. **Methodology** - How it works
7. **Results** - Key findings
8. **Critical Analysis** - Your thoughts

### Nice to Fill
9. **Implementation Notes** - If relevant
10. **Related Papers** - Link to others
11. **Questions/Ideas** - Future directions

## Useful Dataview Queries

### Find Unread PAD Papers
```dataview
LIST
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "pad") AND status = "📚 To Read"
```

### Recent Papers (2024+)
```dataview
TABLE year, venue
FROM "20 PhD/2 Areas/Literature Review"
WHERE year >= 2024
SORT year DESC
```

### High Priority Queue
```dataview
LIST
FROM "20 PhD/2 Areas/Literature Review"  
WHERE contains(tags, "high-priority")
```

## Daily Workflow

### Morning (10 min)
- [ ] Check Papers Database
- [ ] Pick 1-2 papers for today
- [ ] Set reading goals

### Reading Time
- [ ] Read with template open
- [ ] Fill sections as you go
- [ ] Take notes on key ideas

### End of Day (5 min)
- [ ] Update status
- [ ] Link related papers
- [ ] Add to weekly review

## Weekly Goals

- 📖 Read: 5-7 papers
- ✍️ Summarize: All papers read
- 🔗 Link: Connect related papers
- 💡 Review: Extract key themes

## Common Shortcuts

| Action | Shortcut |
|--------|----------|
| New paper from template | CMD+T (Templater) |
| Search papers | CMD+O |
| View graph | CMD+G |
| Open database | CMD+P → "Papers Database" |

## Emergency Checklist

Starting from scratch?
1. Open [[Paper Reading Workflow]]
2. Follow "Quick Start" section
3. Add 2-3 papers to practice
4. Check Papers Database to see them appear

## Tips

1. **One sentence summary** is most important - do this first!
2. **Critical analysis** separates notes from summaries
3. **Link early and often** - connections matter
4. **Update status immediately** - don't let it lag
5. **Review weekly** - stay on top of trends

## Help

- **Full Guide**: [[Paper Reading Workflow]]
- **Database**: [[Papers Database]]
- **Main Hub**: [[Index|Literature Review Index]]

---

💡 **Pro Tip**: Keep this page pinned for quick reference while reading papers!
