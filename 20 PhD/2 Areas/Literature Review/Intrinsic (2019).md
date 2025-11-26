---
aliases: []
tags: [paper, pad, deep-fas-survey, hybrid-method, 3d-mask-attack]
authors: Lei Li, Zhaoqiang Xia, Xiaoyue Jiang, Yupeng Ma, Fabio Roli, Xiaoyi Feng
year: 2020
venue: IET Biometrics
paper_url: https://onlinelibrary.wiley.com/doi/10.1049/iet-bmt.2019.0155
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** Intrinsic
- **Backbone:** 1D-CNN
- **Loss:** Trained with SVM
- **Input:** Reflection (Intrinsic Image Decomposition)
- **Static/Dynamic:** D

## Abstract
Face presentation attacks have become a major threat against face recognition systems and many countermeasures have been proposed over the past decade. However, most of them are devoted to 2D face presentation attack detection, rather than 3D face masks. Unlike the real face, the 3D face mask is usually made of resin materials and has a smooth surface, resulting in reflectance differences. Therefore, in this study, the authors propose a novel 3D face mask presentation attack detection method based on analysis of image reflectance. In the proposed method, the face image is first processed with intrinsic image decomposition algorithm to compute its reflectance image. Then, the intensity distribution histograms are extracted from three orthogonal planes to represent the intensity differences of reflectance images between the real face and 3D face mask. After that, given that the reflectance image of a smooth surface is more sensitive to illumination changes, 1D convolutional neural network is used to characterise how different materials or surfaces react differently to illumination changes. Extensive experiments with the public available 3DMAD database demonstrate the effectiveness of the proposed method for distinguishing a face mask from the real one and show that the detection performance outperforms other state-of-the-art methods.



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
