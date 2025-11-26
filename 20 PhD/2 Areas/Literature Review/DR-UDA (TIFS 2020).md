---
aliases: []
tags: [paper, pad, deep-fas-survey, domain-adaptation]
authors: Guoqing Wang, Hu Han, Shiguang Shan, Xilin Chen
year: TIFS 2020
venue: IEEE Transactions on Information Forensics and Security (TIFS)
paper_url: https://ieeexplore.ieee.org/abstract/document/9116802
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

## Quick Summary
**Method:** DR-UDA
- **Title:** Unsupervised Adversarial Domain Adaptation for Cross-Domain Face Presentation Attack Detection
- **Backbone:** ResNet18
- **Loss:** Center&Triplet loss, Adversarial loss, Disentangled loss
- **Static/Dynamic:** S

## Abstract
Face presentation attack detection (PAD) is essential for securing the widely used face recognition systems. Most of the existing PAD methods do not generalize well to unseen scenarios because labeled training data of the new domain is usually not available. In light of this, we propose an unsupervised domain adaptation with disentangled representation (DR-UDA) approach to improve the generalization capability of PAD into new scenarios. DR-UDA consists of three modules, i.e., ML-Net, UDA-Net and DR-Net. ML-Net aims to learn a discriminative feature representation using the labeled source domain face images via metric learning. UDA-Net performs unsupervised adversarial domain adaptation in order to optimize the source domain and target domain encoders jointly, and obtain a common feature space shared by both domains. As a result, the source domain PAD model can be effectively transferred to the unlabeled target domain for PAD. DR-Net further disentangles the features irrelevant to specific domains by reconstructing the source and target domain face images from the common feature space. Therefore, DR-UDA can learn a disentangled representation space which is generative for face images in both domains and discriminative for live vs. spoof classification. The proposed approach shows promising generalization capability in several public-domain face PAD databases.



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
