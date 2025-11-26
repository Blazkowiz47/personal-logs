---
aliases: []
tags: [paper, pad, deep-fas-survey, anomaly-detection, one-class-classification]
authors: Anjith George, Sébastien Marcel
year: 2021
venue: TIFS
paper_url: https://ieeexplore.ieee.org/document/9153044
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** MCCNN
- **Backbone:** LightCNN
- **Loss:** Binary CE loss, Contrastive loss
- **Input:** Grayscale, IR, Depth, Thermal

## Abstract
Face recognition has evolved as a widely used biometric modality. However, its vulnerability against presentation attacks poses a significant security threat. Though presentation attack detection (PAD) methods try to address this issue, they often fail in generalizing to unseen attacks. In this work, we propose a new framework for PAD using a one-class classifier, where the representation used is learned with a Multi-Channel Convolutional Neural Network (MCCNN). A novel loss function is introduced, which forces the network to learn a compact embedding for bonafide class while being far from the representation of attacks. A one-class Gaussian Mixture Model is used on top of these embeddings for the PAD task. The proposed framework introduces a novel approach to learn a robust PAD system from bonafide and available (known) attack classes. This is particularly important as collecting bonafide data and simpler attacks are much easier than collecting a wide variety of expensive attacks. The proposed system is evaluated on the publicly available WMCA multi-channel face PAD database, which contains a wide variety of 2D and 3D attacks. Further, we have performed experiments with MLFP and SiW-M datasets using RGB channels only. Superior performance in unseen attack protocols shows the effectiveness of the proposed approach. Software, data, and protocols to reproduce the results are made available publicly.



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
