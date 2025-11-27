---
aliases: [sda_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization]
authors: Jingjing Wang, Jingyi Zhang, Ying Bian, Youyi Cai, Chunmao Wang, Shiliang Pu
year: 2021
venue: AAAI
paper_url: https://arxiv.org/abs/2102.12129
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Self-Domain Adaptation for Face Anti-Spoofing

> [!abstract]
> Although current face anti-spoofing methods achieve promising results under intra-dataset testing, they suffer from poor generalization to unseen attacks. Most existing works adopt domain adaptation (DA) or domain generalization (DG) techniques to address this problem. However, the target domain is often unknown during training which limits the utilization of DA methods. DG methods can conquer this by learning domain invariant features without seeing any target data. However, they fail in utilizing the information of target data. In this paper, we propose a self-domain adaptation framework to leverage the unlabeled test domain data at inference. Specifically, a domain adaptor is designed to adapt the model for test domain. In order to learn a better adaptor, a meta-learning based adaptor learning algorithm is proposed using the data of multiple source domains at the training step. At test time, the adaptor is updated using only the test domain data according to the proposed unsupervised adaptor loss to further improve the performance. Extensive experiments on four public datasets validate the effectiveness of the proposed method.

## Quick Summary
**Method:** SDA
- **Backbone:** DepthNet
- **Loss:** Binary CE & Depth loss, Reconstruction loss, Orthogonality regularization
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
