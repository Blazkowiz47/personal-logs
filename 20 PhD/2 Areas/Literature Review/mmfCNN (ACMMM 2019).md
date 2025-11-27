---
aliases: []
tags: [paper, pad, deep-fas-survey, multimodal]
authors: Huafeng Kuang, Rongrong Ji, Hong Liu, Shengchuan Zhang, Xiaoshuai Sun, Feiyue Huang, Baochang Zhang
year: 2019
venue: ACM MM 2019
paper_url: https://dl.acm.org/doi/10.1145/3343031.3351001
code_url: https://github.com/SkyKuang/Face-anti-spoofing
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

## Quick Summary
**Abstract:** Face anti-spoofing detection is critical to guarantee the security of biometric face recognition systems. Despite extensive advances in facial anti-spoofing based on single-model image, little work has been devoted to multi-modal anti-spoofing, which is however widely encountered in real-world scenarios. Following the recent progress, this paper mainly focuses on multi-modal face anti-spoofing and aims to solve the following two challenges: (1) how to effectively fuse multi-modal information; and (2) how to effectively learn distinguishable features despite single cross-entropy loss. We propose a novel Multi-modal Multi-layer Fusion Convolutional Neural Network (mmfCNN), which targets at finding a discriminative model for recognizing the subtle differences between live and spoof faces. The mmfCNN can fully use different information provided by diverse modalities, which is based on a weight-adaptation aggregation approach. Specifically, we utilize a multi-layer fusion model to further aggregate the features from different layers, which fuses the low-, mid- and high-level information from different modalities in a unified framework. Moreover, a novel Average Binary Center (ABC) loss is proposed to maximize the dissimilarity between the features of live and spoof faces, which helps to stabilize the training to generate a robust and discriminative model.

**Method:** mmfCNN (Multi-modal Multi-layer Fusion CNN)
- **Backbone:** ResNet34
- **Loss:** Binary CE loss, Binary Center Loss
- **Input:** RGB, NIR, Depth, HSV, YCbCr
- **Fusion:** Feature-level



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
