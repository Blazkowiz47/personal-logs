---
aliases: [facebagnet_fas]
tags: [paper, pad, deep-fas-survey, multimodal, patch-based]
authors: Tao Shen, Yuyu Huang, Zhijun Tong
year: 2019
venue: CVPRW
paper_url: https://openaccess.thecvf.com/content_CVPRW_2019/html/CFS/Shen_FaceBagNet_Bag-Of-Local-Features_Model_for_Multi-Modal_Face_Anti-Spoofing_CVPRW_2019_paper.html
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** FaceBagNet
- **Backbone:** Multi-stream CNN
- **Loss:** Binary CE loss
- **Input:** RGB, Depth, NIR face patches
- **Fusion:** Feature-level

## Abstract
Face anti-spoofing detection is a crucial procedure in biometric face recognition systems. State-of-the-art approaches, based on Convolutional Neural Networks (CNNs), present good results in this field. However, previous works focus on one single modal data with limited number of subjects. The recently published CASIA-SURF dataset is the largest dataset that consists of 1000 subjects and 21000 video clips with 3 modalities (RGB, Depth and IR). In this paper, we propose a multi-stream CNN architecture called FaceBagNet to make full use of this data. The input of FaceBagNet is patch-level images which contributes to extract spoof-specific discriminative information. In addition, in order to prevent overfitting and for better learning the fusion features, we design a Modal Feature Erasing (MFE) operation on the multi-modal features which erases features from one randomly selected modality during training. As the result, our approach wins the second place in CVPR 2019 ChaLearn Face Anti-spoofing attack detection challenge. Our final submission gets the score of 99.8052% (TPR@FPR = 10e-4) on the test set.



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
