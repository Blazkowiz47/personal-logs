---
aliases: [freqspatialtempnet_fas]
tags: [paper, pad, deep-fas-survey, binary-supervision, frequency-domain]
authors: Ying Huang, Wenwei Zhang, Jinzhuo Wang
year: 2020
venue: arXiv
paper_url: https://arxiv.org/abs/2002.03723
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** FreqSpatialTempNet
- **Backbone:** ResNet18
- **Loss:** Binary CE loss
- **Input:** RGB, HSV, Spectral
- **Static/Dynamic:** D

## Abstract
Face anti-spoofing is crucial for the security of face recognition system, by avoiding invaded with presentation attack. Previous works have shown the effectiveness of using depth and temporal supervision for this task. However, depth supervision is often considered only in a single frame, and temporal supervision is explored by utilizing certain signals which is not robust to the change of scenes. In this work, motivated by two stream ConvNets, we propose a novel two stream FreqSaptialTemporalNet for face anti-spoofing which simultaneously takes advantage of frequent, spatial and temporal information. Compared with existing methods which mine spoofing cues in multi-frame RGB image, we make multi-frame spectrum image as one input stream for the discriminative deep neural network, encouraging the primary difference between live and fake video to be automatically unearthed. Extensive experiments show promising improvement results using the proposed architecture. Meanwhile, we proposed a concise method to obtain a large amount of spoofing training data by utilizing a frequent augmentation pipeline, which contributes detail visualization between live and fake images as well as data insufficiency issue when training large networks.



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
