---
aliases: [spmt_ssd_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method]
authors: Xiao Song, Xu Zhao, Liangji Fang, Tianwei Lin
year: 2019
venue: Pattern Recognition
paper_url: https://www.sciencedirect.com/science/article/pii/S0031320318303182
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Discriminative representation combinations for accurate face spoofing detection

> [!abstract]
> Three discriminative representations for face presentation attack detection are introduced in this paper. Firstly we design a descriptor called spatial pyramid coding micro-texture (SPMT) feature to characterize local appearance information. Secondly we utilize the SSD, which is a deep learning framework for detection, to excavate context cues and conduct end-to-end face presentation attack detection. Finally we design a descriptor called template face matched binocular depth (TFBD) feature to characterize stereo structures of real and fake faces. For accurate presentation attack detection, we also design two kinds of representation combinations. Firstly, we propose a decision-level cascade strategy to combine SPMT with SSD. Secondly, we use a simple score fusion strategy to combine face structure cues (TFBD) with local micro-texture features (SPMT). To demonstrate the effectiveness of our design, we evaluate the representation combination of SPMT and SSD on three public datasets, which outperforms all other state-of-the-art methods. In addition, we evaluate the representation combination of SPMT and TFBD on our dataset and excellent performance is also achieved.

## Quick Summary
**Method:** SPMT+SSD
- **Backbone:** VGG16
- **Loss:** Binary CE loss, SVM, bbox regression
- **Input:** RGB, Landmarks
- **Static/Dynamic:** S



## Problem Statement
What problem does this paper address?


## Key Contributions
1. 
2. 
3. 

## Methodology
### Architecture
*Describe the model/approach*


### Key Techniques
- 
- 

### Novel Components
*What's new/different from prior work?*


## Experiments
### Datasets Used
- 
- 

### Results
*Key metrics and performance*

| Dataset | Metric | Result | Baseline |
|---------|--------|--------|----------|
|         |        |        |          |

### Ablation Studies
*What components were tested?*


## Strengths
- 
- 

## Limitations
- 
- 

## Critical Analysis
*My thoughts on the paper*

### What Works Well
- 

### Concerns/Criticisms
- 

### Missing Pieces
- 

## Relevance to My Work
*How does this relate to my PAD research?*

### Direct Applications
- 

### Ideas Sparked
- 

### Techniques to Borrow
- 

## Implementation Notes
*Anything useful for implementing this*

### Architecture Details
- 

### Hyperparameters
- 

### Training Details
- 

### Reproducibility Notes
- 

## Related Papers
### Cited By This Paper
- [[]]

### Papers That Cite This
- [[]]

### Similar Approaches
- [[]]

## Questions & Future Directions
### Open Questions
- 

### Extension Ideas
- 

### Experimental Ideas
- 

## Notes & Highlights
### Key Quotes
> 

### Figures to Remember
- Figure X: 

### Equations
$$
$$

## Meeting Notes
*Discussions with advisor/colleagues about this paper*


## Action Items
- [ ] 
- [ ] 

---
**Reading Progress:** 
- [ ] Abstract
- [ ] Introduction
- [ ] Related Work
- [ ] Methodology
- [ ] Experiments
- [ ] Conclusion
- [ ] Supplementary Material
