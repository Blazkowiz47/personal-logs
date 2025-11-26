---
aliases: []
tags: [paper, pad, deep-fas-survey, multimodal, cross-modality-translation]
authors: Ajian Liu, Zichang Tan, Jun Wan, Yanyan Liang, Zhen Lei, Guodong Guo, Stan Z. Li
year: 2021
venue: TIFS
paper_url: https://ieeexplore.ieee.org/document/9374963
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** MA-Net
- **Backbone:** CycleGAN, ResNet18
- **Loss:** Binary CE loss, GAN loss
- **Input:** RGB, NIR
- **Fusion:** Feature-level

## Abstract
Face Presentation Attack Detection (PAD) approaches based on multi-modal data have been attracted increasingly by the research community. However, they require multi-modal face data consistently involved in both the training and testing phases. It would severely limit the applicability due to the most Face Anti-spoofing (FAS) systems are only equipped with Visible (VIS) imaging devices, i.e., RGB cameras. Therefore, how to use other modality (i.e., Near-Infrared (NIR)) to assist the performance improvement of VIS-based PAD is significant for FAS. In this work, we first discuss the big gap of performances among different modalities even though the same backbone network is applied. Then, we propose a novel Cross-modal Auxiliary (CMA) framework for the VIS-based FAS task. The main trait of CMA is that the performance can be greatly improved with the help of other modality while no other modality is required in the testing stage. The proposed CMA consists of a Modality Translation Network (MT-Net) and a Modality Assistance Network (MA-Net). The former aims to close the visible gap between different modalities via a generative model that maps inputs from one modality (i.e., RGB) to another (i.e., NIR). The latter focuses on how to use the translated modality (i.e., target modality) and RGB modality (i.e., source modality) together to train a discriminative PAD model. Extensive experiments are conducted to demonstrate that the proposed framework can push the state-of-the-art (SOTA) performances on both multi-modal datasets (i.e., CASIA-SURF, CeFA, and WMCA) and RGB-based datasets (i.e., OULU-NPU, and SiW).



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
