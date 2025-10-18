# Literature Review

> **Quick Access:** [[Papers Database|📚 View All Papers]] | [[Paper Reading Workflow|📖 How to Use This System]]

## Overview
This area tracks all academic papers, research findings, and literature relevant to my PhD research in biometric security and presentation attack detection.

## Papers Database
The [[Papers Database]] contains all papers organized by:
- **Status** (To Read, Reading, Read)
- **Topic** (PAD, MAD, DeepFake, etc.)
- **Venue** (CVPR, ICCV, ECCV, Journals)
- **Year**
- **Priority**

### Quick Stats
```dataview
TABLE WITHOUT ID
	status as "Status",
	length(rows) as "Count"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper")
GROUP BY status
SORT status DESC
```

### Recently Read Papers
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	dateread as "Date Read"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND status = "✅ Read"
SORT dateread DESC
LIMIT 5
```

## Research Topics
- **Presentation Attack Detection (PAD)** - Core PhD focus
- **Morph Attack Detection (MAD)** - Related to face manipulation
- **DeepFake Detection** - Synthetic face detection
- **Face Anti-Spoofing** - General term for PAD
- **Cross-Modal Learning** - Multi-modal approaches
- **Domain Generalization** - Generalization across domains

## Key Themes & Trends
*Update as you read more papers*

### Current SOTA Approaches
- 

### Emerging Research Directions
- 

### Popular Architectures
- 

## Research Gaps Identified
*Track gaps you notice while reading*

1. 
2. 
3. 

## Potential Research Directions
*Ideas sparked from literature review*

1. 
2. 
3. 

## Conference Deadlines
Track important deadlines for paper submissions:

| Conference | Deadline | Notification | Link |
|------------|----------|--------------|------|
| CVPR 2026  |          |              |      |
| ICCV 2025  |          |              |      |
| ECCV 2026  |          |              |      |
| NeurIPS    |          |              |      |
| ICLR       |          |              |      |
| ICB        |          |              |      |

## Important Journals
- IEEE TIFS (Transactions on Information Forensics and Security)
- IET Biometrics
- IEEE TBIOM (Transactions on Biometrics, Behavior, and Identity Science)
- Pattern Recognition

## Useful Resources

### Survey Papers
- [[]] - Comprehensive PAD survey
- [[]] - Face anti-spoofing overview

### Benchmark Papers
- [[]] - Multi-dataset evaluation
- [[]] - Cross-database testing

### Foundational Papers
- [[]] - Seminal work in the field
- [[]] - Key methodology

## Related Areas
- [[../Dataset Management (OCIM)/Presentation Attack Detection Data management|PAD Datasets]]
- [[../../1 Projects/|PhD Projects]]
- [[../Experiment Tracking/Index|Experiment Tracking]]
- [[../Mathematical Foundations/Index|Mathematical Foundations]]

---

## How to Use This System
See [[Paper Reading Workflow]] for detailed instructions on:
- Adding new papers
- Reading workflow
- Taking effective notes  
- Linking papers
- Using the database

### Quick Add Checklist
When adding a new paper:
- [ ] Use Paper Note Template
- [ ] Fill all metadata fields
- [ ] Add appropriate tags (#pad, #mad, etc.)
- [ ] Set status and priority
- [ ] Save in this folder

---
Tags: #phd #literature #review #area
