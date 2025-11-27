---
aliases: [feathernets_fas]
tags: [paper, pad, deep-fas-survey, lightweight, multimodal]
authors: Peng Zhang, Fuhao Zou, Zhiwen Wu, Nengli Dai, Skarpness Mark, Michael Fu, Juan Zhao, Kai Li
year: 2019
venue: CVPRW
paper_url: https://arxiv.org/abs/1904.09290
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** FeatherNets
- **Backbone:** Ensemble-FeatherNet
- **Loss:** Binary CE loss
- **Input:** Depth, NIR
- **Fusion:** Decision-level

## Abstract
Face Anti-spoofing gains increased attentions recently in both academic and industrial fields. With the emergence of various CNN based solutions, the multi-modal(RGB, depth and IR) methods based CNN showed better performance than single modal classifiers. However, there is a need for improving the performance and reducing the complexity. Therefore, an extreme light network architecture(FeatherNet A/B) is proposed with a streaming module which fixes the weakness of Global Average Pooling and uses less parameters. Our single FeatherNet trained by depth image only, provides a higher baseline with 0.00168 ACER, 0.35M parameters and 83M FLOPS. Furthermore, a novel fusion procedure with ``ensemble + cascade'' structure is presented to satisfy the performance preferred use cases. Meanwhile, the MMFD dataset is collected to provide more attacks and diversity to gain better generalization. We use the fusion method in the Face Anti-spoofing Attack Detection Challenge@CVPR2019 and got the result of 0.0013(ACER), 0.999(TPR@FPR=10e-2), 0.998(TPR@FPR=10e-3) and 0.9814(TPR@FPR=10e-4).



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
