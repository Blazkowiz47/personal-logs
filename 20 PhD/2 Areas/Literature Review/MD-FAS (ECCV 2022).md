---
aliases: [mdfas]
tags: [paper, pad, deep-fas-survey, domain-generalization, multi-domain-learning]
authors: Xiao Guo, Yaojie Liu, Anil Jain, Xiaoming Liu
year: 2022
venue: ECCV
paper_url: https://arxiv.org/pdf/2208.11148.pdf
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** MD-FAS
- **Backbone:** PhySTD
- **Loss:** CE loss, Binary Mask loss, Source & Target distillation loss
- **Static/Dynamic:** S

## Abstract
In this work, we study multi-domain learning for face anti-spoofing(MD-FAS), where a pre-trained FAS model needs to be updated to perform equally well on both source and target domains while only using target domain data for updating. We present a new model for MD-FAS, which addresses the forgetting issue when learning new domain data, while possessing a high level of adaptability. First, we devise a simple yet effective module, called spoof region estimator(SRE), to identify spoof traces in the spoof image. Such spoof traces reflect the source pre-trained model's responses that help upgraded models combat catastrophic forgetting during updating. Unlike prior works that estimate spoof traces which generate multiple outputs or a low-resolution binary mask, SRE produces one single, detailed pixel-wise estimate in an unsupervised manner. Secondly, we propose a novel framework, named FAS-wrapper, which transfers knowledge from the pre-trained models and seamlessly integrates with different FAS models. Lastly, to help the community further advance MD-FAS, we construct a new benchmark based on SIW, SIW-Mv2 and Oulu-NPU, and introduce four distinct protocols for evaluation, where source and target domains are different in terms of spoof type, age, ethnicity, and illumination. Our proposed method achieves superior performance on the MD-FAS benchmark than previous methods. Our code and newly curated SIW-Mv2 are publicly available.



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
