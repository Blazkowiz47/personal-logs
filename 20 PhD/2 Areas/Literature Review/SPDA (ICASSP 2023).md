---
aliases: [spda_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization]
authors: Zhiyi Chen, Yao Lu, Xinzhe Deng, Jia Meng, Shengchuan Zhang, Liujuan Cao
year: 2023
venue: ICASSP
paper_url: https://ieeexplore.ieee.org/document/10095730
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Self-Paced Partial Domain-Aware Learning for Face Anti-Spoofing

> [!abstract]
> With the widespread deployment of face authentication systems, domain generalization (DG) based face anti-spoofing (FAS) security approaches have drawn growing attention. Existing generalization-based methods always attempt to extract domain-invariant task information from data and eliminate domain-dependent information from representation space. However, they neglect that domain-related information may also contain helpful features for the classification task. To address this issue, we propose a self-paced partial domain-aware framework (SPDA) to preserve domain-related features helpful for the discrimination of fake and real faces, thereby increasing generalization for unseen domains. Specifically, a training strategy based on contrastive learning is adopted to construct domain-adapted and domain-aware task-related representation spaces. Then, a partial domain-aware adaptation module (PDA) is proposed to preserve valuable domain-related information for the task features that the network considers useful for mixture-domain classification. In addition, the proposed self-paced method(SCM) continuously explores potential clusters with insufficient representation to enhance further the feature extractor’s capability and the effectiveness of the PDA module. Extensive experiments demonstrate the effectiveness of our method compared to SOTA algorithms.

## Quick Summary
**Method:** SPDA
- **Backbone:** ResNet18
- **Loss:** BCE loss, Domain loss, Self-paced Cluster Mining loss, orthogonal loss
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
