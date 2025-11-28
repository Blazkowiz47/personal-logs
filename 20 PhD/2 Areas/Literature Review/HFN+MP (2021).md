---
aliases: [hfn_mp_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization, meta-learning]
authors: Rizhao Cai, Zhi Li, Renjie Wan, Haoliang Li, Yongjian Hu, Alex ChiChung Kot
year: 2022
venue: TIFS
paper_url: https://arxiv.org/abs/2110.06753
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** HFN+MP
- **Backbone:** Two-stream ResNet50
- **Loss:** Binary CE loss, MSE loss
- **Static/Dynamic:** S

## Abstract
Face Anti-Spoofing (FAS) is essential to secure face recognition systems and has been extensively studied in recent years. Although deep neural networks (DNNs) for the FAS task have achieved promising results in intra-dataset experiments with similar distributions of training and testing data, the DNNs' generalization ability is limited under the cross-domain scenarios with different distributions of training and testing data. To improve the generalization ability, recent hybrid methods have been explored to extract task-aware handcrafted features (e.g., Local Binary Pattern) as discriminative information for the input of DNNs. However, the handcrafted feature extraction relies on experts' domain knowledge, and how to choose appropriate handcrafted features is underexplored. To this end, we propose a learnable network to extract Meta Pattern (MP) in our learning-to-learn framework. By replacing handcrafted features with the MP, the discriminative information from MP is capable of learning a more generalized model. Moreover, we devise a two-stream network to hierarchically fuse the input RGB image and the extracted MP by using our proposed Hierarchical Fusion Module (HFM). We conduct comprehensive experiments and show that our MP outperforms the compared handcrafted features. Also, our proposed method with HFM and the MP can achieve state-of-the-art performance on two different domain generalization evaluation benchmarks.



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
