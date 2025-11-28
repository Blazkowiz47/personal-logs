# Literature Review

> My PhD research paper database for **Presentation Attack Detection**, network architectures, and computer vision.

## Quick Stats
```dataview
TABLE WITHOUT ID
	status as "Status",
	length(rows) as "Count"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper")
GROUP BY status
```

## Papers by Status

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

## Papers by Research Area

### Presentation Attack Detection (Core)
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

### Network Architectures
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "architecture") OR contains(tags, "cnn") OR contains(tags, "transformer") OR contains(tags, "vit")
SORT status ASC, year DESC
```

### Computer Vision Fundamentals
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "computer-vision") OR contains(tags, "cv-fundamentals")
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

### Multi-Modal / Cross-Modal Learning
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

### Attention Mechanisms
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "attention")
SORT status ASC, year DESC
```

### Loss Functions & Training
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "loss-function") OR contains(tags, "training")
SORT status ASC, year DESC
```

### Feature Learning & Representation
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	status as "Status",
	year as "Year",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "feature-learning") OR contains(tags, "representation")
SORT status ASC, year DESC
```



## Papers by Venue

### Top CV Conferences
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

### Biometrics & Security
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	status as "Status",
	venue as "Venue"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "paper") AND (contains(venue, "TIFS") OR contains(venue, "IET") OR contains(venue, "Biometrics") OR contains(venue, "ICB") OR contains(venue, "IJCB") OR contains(venue, "TBIOM"))
SORT year DESC
```

### arXiv Preprints
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	status as "Status",
	dateadded as "Added"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(venue, "arXiv")
SORT year DESC, dateadded DESC
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

## Foundational Papers
```dataview
TABLE WITHOUT ID
	file.link as "Paper",
	year as "Year",
	venue as "Venue",
	status as "Status"
FROM "20 PhD/2 Areas/Literature Review"
WHERE contains(tags, "foundational")
SORT year ASC
```

---

## Status Guide:
	- "✅ Read", "✅" 
	- "📖 Reading", "📖"
	- "📚 To Read", "📚"

## Tag Guide

### Primary Research Area
- `#pad` - Presentation Attack Detection

### Network Architectures
- `#cnn` - Convolutional Neural Networks
- `#transformer` - Transformer architectures
- `#vit` - Vision Transformers
- `#resnet` - ResNet and variants
- `#mobilenet` - MobileNet architectures
- `#efficientnet` - EfficientNet models
- `#architecture` - General architecture papers

### Computer Vision Techniques
- `#computer-vision` - General CV papers
- `#attention` - Attention mechanisms
- `#feature-learning` - Feature extraction/learning
- `#representation` - Representation learning
- `#image-processing` - Image processing techniques

### Training & Optimization
- `#loss-function` - Novel loss functions
- `#training` - Training strategies
- `#optimization` - Optimization methods
- `#data-augmentation` - Augmentation techniques

### PAD-Specific
- `#domain-adaptation` - Cross-domain PAD
- `#generalization` - Generalization to unseen attacks
- `#multimodal` - Multi-modal PAD
- `#cross-modal` - Cross-modal learning
- `#zero-shot` - Zero-shot PAD

### Special Categories
- `#benchmark` - Benchmark/evaluation papers
- `#survey` - Survey/review papers
- `#dataset` - Papers introducing datasets
- `#foundational` - Foundational/seminal papers
- `#to-implement` - To be implemented
- `#high-priority` - High priority reading

## Quick Links
- [[../../1 Projects/|PhD Projects]]
- [[../Experiment Tracking/Index|Experiment Tracking]]
- [[../Dataset Management (OCIM)/Presentation Attack Detection Data management|PAD Datasets]]

---
Tags: #phd #literature #area
