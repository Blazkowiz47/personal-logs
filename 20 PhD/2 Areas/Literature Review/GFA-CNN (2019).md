---
aliases: [gfa_cnn_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization, multi-task-learning]
authors: Xiaoguang Tu, Zheng Ma, Jian Zhao, Guodong Du, Mei Xie, Jiashi Feng
year: 2020
venue: ACM TIST
paper_url: https://dl.acm.org/doi/abs/10.1145/3402446
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** GFA-CNN
- **Backbone:** VGG16
- **Loss:** Total Pairwise Confusion Loss, Softmax Loss
- **Input:** RGB
- **Static/Dynamic:** S

## Abstract
Face anti-spoofing aims to detect presentation attack to face recognition--based authentication systems. It has drawn growing attention due to the high security demand. The widely adopted CNN-based methods usually well recognize the spoofing faces when training and testing spoofing samples display similar patterns, but their performance would drop drastically on testing spoofing faces of novel patterns or unseen scenes, leading to poor generalization performance. Furthermore, almost all current methods treat face anti-spoofing as a prior step to face recognition, which prolongs the response time and makes face authentication inefficient. In this article, we try to boost the generalizability and applicability of face anti-spoofing methods by designing a new generalizable face authentication CNN (GFA-CNN) model with three novelties. First, GFA-CNN introduces a simple yet effective total pairwise confusion loss for CNN training that properly balances contributions of all spoofing patterns for recognizing the spoofing faces. Second, it incorporate a fast domain adaptation component to alleviate negative effects brought by domain variation. Third, it deploys filter diversification learning to make the learned representations more adaptable to new scenes. In addition, the proposed GFA-CNN works in a multi-task manner—it performs face anti-spoofing and face recognition simultaneously. Experimental results on five popular face anti-spoofing and face recognition benchmarks show that GFA-CNN outperforms previous face anti-spoofing methods on cross-test protocols significantly and also well preserves the identity information of input face images.



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
