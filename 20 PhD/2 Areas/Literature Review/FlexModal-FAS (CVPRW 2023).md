---
aliases: [flexmodal_fas_fas]
tags: [paper, pad, deep-fas-survey, flexible-modal, benchmark]
authors: Zitong Yu, Ajian Liu, Chenxu Zhao, Kevin H. M. Cheng, Xu Cheng, Guoying Zhao
year: 2023
venue: CVPRW
paper_url: https://arxiv.org/abs/2202.08192
code_url: https://github.com/ZitongYu/Flex-Modal-FAS
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** FlexModal-FAS
- **Backbone:** CDCN, ResNet50, ViT
- **Loss:** BCE loss, Pixel-wise binary loss
- **Input:** RGB, Depth, IR
- **Fusion:** Feature-level

## Abstract
Face anti-spoofing (FAS) plays a vital role in securing face recognition systems from presentation attacks. Benefitted from the maturing camera sensors, single-modal (RGB) and multi-modal (e.g., RGB+Depth) FAS has been applied in various scenarios with different configurations of sensors/modalities. Existing single- and multi-modal FAS methods usually separately train and deploy models for each possible modality scenario, which might be redundant and inefficient. Can we train a unified model, and flexibly deploy it under various modality scenarios? In this paper, we establish the first flexible-modal FAS benchmark with the principle `train one for all'. To be specific, with trained multi-modal (RGB+Depth+IR) FAS models, both intra- and cross-dataset testings are conducted on four flexible-modal sub-protocols (RGB, RGB+Depth, RGB+IR, and RGB+Depth+IR). We also investigate prevalent deep models and feature fusion strategies for flexible-modal FAS. We hope this new benchmark will facilitate the future research of the multi-modal FAS.



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
