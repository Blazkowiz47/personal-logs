---
aliases: [stasn_fas]
tags: [paper, pad, deep-fas-survey, binary-supervision]
authors: Xiao Yang, Wenhan Luo, Linchao Bao, Yuan Gao, Dihong Gong, Shibao Zheng, Zhifeng Li, Wei Liu
year: 2019
venue: CVPR
paper_url: https://openaccess.thecvf.com/content_CVPR_2019/papers/Yang_Face_Anti-Spoofing_Model_Matters_so_Does_Data_CVPR_2019_paper.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Face Anti-Spoofing: Model Matters, so Does Data

> [!abstract]
> Face anti-spoofing is an important task in full-stack face applications including face detection, verification, and recognition. Previous approaches build models on datasets which do not simulate the real-world data well (e.g., small scale, insignificant variance, etc.). Existing models may rely on auxiliary information, which prevents these anti-spoofing solutions from generalizing well in practice. In this paper, we present a data collection solution along with a data synthesis technique to simulate digital medium-based face spoofing attacks, which can easily help us obtain a large amount of training data well reflecting the real-world scenarios. Through exploiting a novel Spatio-Temporal Anti-Spoof Network (STASN), we are able to push the performance on public face anti-spoofing datasets over state-of-the-art methods by a large margin. Since the proposed model can automatically attend to discriminative regions, it makes analyzing the behaviors of the network possible. We conduct extensive experiments and show that the proposed model can distinguish spoof faces by extracting features from a variety of regions to seek out subtle evidences such as borders, moire patterns, reflection artifacts, etc.

## Quick Summary
**Method:** STASN
- **Backbone:** ResNet50+LSTM
- **Loss:** Binary CE loss
- **Input:** RGB
- **Static/Dynamic:** D



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
