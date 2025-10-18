# Literature Review

> **Quick Access:** [[Papers Database|📚 View All Papers]] | [[Paper Reading Workflow|📖 How to Use This System]] | [[Quick Reference|⚡ Quick Reference]]

## Overview
This area tracks all academic papers and research findings for my PhD research in **Presentation Attack Detection (PAD)**, including related topics in network architectures and computer vision.

## Research Focus

### Primary Research Area
**🎯 Presentation Attack Detection (PAD)** - My core PhD research focus
- Face anti-spoofing methods
- Liveness detection
- Cross-domain generalization
- Novel attack detection

### Supporting Research Areas
**🏗️ Network Architectures**
- CNN architectures (ResNet, EfficientNet, MobileNet)
- Vision Transformers (ViT)
- Attention mechanisms
- Novel architectural designs

**👁️ Computer Vision Fundamentals**
- Feature learning and representation
- Image processing techniques
- Multi-modal learning
- Domain adaptation

## Papers Database
The [[Papers Database]] contains all papers organized by:
- **Status** (To Read, Reading, Read)
- **Research Area** (PAD, Architectures, CV Fundamentals, etc.)
- **Venue** (CVPR, ICCV, ECCV, TIFS, etc.)
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
	dateread as "Date Read",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND status = "✅ Read"
SORT dateread DESC
LIMIT 5
```

### Current Reading Queue
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	venue as "Venue",
	year as "Year"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND (status = "📖 Reading" OR status = "📚 To Read")
SORT status DESC, year DESC
LIMIT 10
```

## Key Themes & Trends
*Update as you read more papers*

### In PAD Research
- 

### In Network Architectures
- 

### In Computer Vision
- 

## Research Gaps Identified
*Track gaps you notice while reading*

### PAD-Specific Gaps
1. 
2. 
3. 

### Architecture/Method Gaps
1. 
2. 
3. 

## Potential Research Directions
*Ideas sparked from literature review*

### Short-term (Next 6 months)
1. 
2. 
3. 

### Long-term (PhD Duration)
1. 
2. 
3. 

## Conference & Journal Deadlines

### Computer Vision Conferences
| Conference | Deadline | Notification | Focus |
|------------|----------|--------------|-------|
| CVPR 2026  |          |              | CV, PAD |
| ICCV 2025  |          |              | CV, PAD |
| ECCV 2026  |          |              | CV, PAD |
| NeurIPS    |          |              | ML, Architectures |
| ICLR       |          |              | ML, Architectures |

### Biometrics & Security
| Venue | Deadline | Notification | Focus |
|-------|----------|--------------|-------|
| ICB   |          |              | PAD, Biometrics |
| IJCB  |          |              | PAD, Biometrics |
| BTAS  |          |              | PAD, Biometrics |

### Important Journals
- **IEEE TIFS** - Transactions on Information Forensics and Security
- **IEEE TBIOM** - Transactions on Biometrics, Behavior, and Identity Science
- **IET Biometrics** - Biometrics journal
- **Pattern Recognition** - CV and ML methods
- **IJCV** - International Journal of Computer Vision

## Important Paper Collections

### Foundational PAD Papers
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "foundational") AND contains(tags, "pad")
SORT year ASC
```

### Foundational Architecture Papers
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "foundational") AND contains(tags, "architecture")
SORT year ASC
```

### Survey Papers
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "survey")
SORT year DESC
```

### Benchmark Papers
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "benchmark")
SORT year DESC
```

## Related Areas in Vault
- [[../Dataset Management (OCIM)/Presentation Attack Detection Data management|PAD Datasets]]
- [[../../1 Projects/|PhD Projects]]
- [[../Experiment Tracking/Index|Experiment Tracking]]
- [[../Mathematical Foundations/Index|Mathematical Foundations]]
- [[../../3 Resources/|Research Resources]]

---

## How to Use This System

### Quick Start
1. **Read the guide**: Check [[Paper Reading Workflow]] for complete instructions
2. **Add a paper**: Use the Paper Note Template
3. **Tag properly**: Use appropriate tags (see guide below)
4. **Update status**: As you read, update the status field
5. **Link papers**: Connect related papers together

### Tagging Guide for Your Research

#### When Reading PAD Papers
Use tags: `#paper #pad #face-antispoofing`

Add specific tags based on content:
- Domain generalization → `#domain-adaptation #generalization`
- Multi-modal methods → `#multimodal #cross-modal`
- Novel datasets → `#dataset`

#### When Reading Architecture Papers
Use tags: `#paper #architecture #computer-vision`

Add specific architecture tags:
- CNNs → `#cnn` (+ specific: `#resnet`, `#mobilenet`, `#efficientnet`)
- Transformers → `#transformer #vit`
- Attention → `#attention`

#### When Reading CV Fundamentals
Use tags: `#paper #computer-vision`

Add specific technique tags:
- Feature learning → `#feature-learning #representation`
- Loss functions → `#loss-function`
- Training methods → `#training #optimization`

### Priority Tags
- `#high-priority` - Must read soon
- `#foundational` - Seminal papers in the field
- `#to-implement` - Papers to implement
- `#survey` - Review/survey papers
- `#benchmark` - Benchmark/evaluation papers

---

## Quick Add Checklist
When adding a new paper:
- [ ] Use Paper Note Template
- [ ] Fill title and metadata (authors, year, venue, URLs)
- [ ] Set status: `📚 To Read`
- [ ] Add primary tag: `#paper` + `#pad` or `#architecture` or `#computer-vision`
- [ ] Add specific technique tags
- [ ] Set priority if needed
- [ ] Save in `20 PhD/2 Areas/Literature Review/` folder

---

Tags: #phd #literature #review #area
