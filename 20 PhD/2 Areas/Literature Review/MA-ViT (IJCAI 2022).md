---
aliases: [ma_vit_fas]
tags: [paper, pad, deep-fas-survey, flexible-modal, vision-transformer]
authors: Ajian Liu, Yanyan Liang
year: 2022
venue: IJCAI
paper_url: https://www.ijcai.org/proceedings/2022/0165.pdf
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** MA-ViT
- **Backbone:** ViT-S/16
- **Loss:** Binary CE Loss on image and modality
- **Input:** RGB, Depth, NIR
- **Fusion:** Input&Feature-level

## Abstract
The existing multi-modal face anti-spoofing (FAS) frameworks are designed based on two strategies: halfway and late fusion. However, the former requires test modalities consistent with the training input, which seriously limits its deployment scenarios. And the latter is built on multiple branches to process different modalities independently, which limits their use in applications with low memory or fast execution requirements. In this work, we present a single branch based Transformer framework, namely Modality-Agnostic Vision Transformer (MA-ViT), which aims to improve the performance of arbitrary modal attacks with the help of multi-modal data. Specifically, MA-ViT adopts the early fusion to aggregate all the available training modalities’ data and enables flexible testing of any given modal samples. Further, we develop the Modality-Agnostic Transformer Block (MATB) in MA-ViT, which consists of two stacked attentions named Modal-Disentangle Attention (MDA) and Cross-Modal Attention (CMA), to eliminate modality-related information for each modal sequences and supplement modality-agnostic liveness features from another modal sequences, respectively. Experiments demonstrate that the single model trained based on MA-ViT can not only flexibly evaluate different modal samples, but also outperforms existing single-modal frameworks by a large margin, and approaches the multi-modal frameworks introduced with smaller FLOPs and model parameters.



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
