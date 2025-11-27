---
aliases: [or_da_fas]
tags: [paper, pad, deep-fas-survey, domain-adaptation]
authors: Haoliang Li, Wen Li, Hong Cao, Shiqi Wang, Feiyue Huang, Alex C. Kot
year: 2018
venue: IEEE Transactions on Information Forensics and Security (TIFS)
paper_url: https://ieeexplore.ieee.org/document/8279564
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

> [!abstract]
> This paper addresses the problem of face anti-spoofing in cross-scenario settings where training and testing data come from different distributions (domains). The authors propose an **Unsupervised Domain Adaptation (UDA)** method to learn a generalized feature representation. The method trains a deep neural network (AlexNet backbone) that simultaneously minimizes the classification error on the labeled source domain and the **Maximum Mean Discrepancy (MMD)** between the source and unlabeled target domains. By minimizing MMD, the network learns features that are invariant to the domain shift (e.g., different cameras, lighting), thereby improving performance on the target domain without requiring target labels.

## Quick Summary
**Method:** OR-DA
- **Backbone:** AlexNet
- **Loss:** Binary CE loss, MMD loss
- **Static/Dynamic:** S



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
