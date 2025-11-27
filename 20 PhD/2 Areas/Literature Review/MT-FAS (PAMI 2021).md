---
aliases: [mt_fas_fas]
tags: [paper, pad, deep-fas-survey, generative-model, meta-learning]
authors: Yunxiao Qin, Zitong Yu, Longbin Yan, Zezheng Wang, Chenxu Zhao, Zhen Lei
year: 2021
venue: TPAMI
paper_url: https://ieeexplore.ieee.org/document/9462562
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** MT-FAS
- **Supervision:** ZeroMap (live), LearnableMap (Spoof)
- **Backbone:** DepthNet
- **Input:** RGB
- **Static/Dynamic:** S

## Abstract
Face anti-spoofing (FAS) is essential to secure face recognition systems. Recently, deep learning based methods have shown promising results. However, most existing methods are supervised by predefined binary labels (live/spoof) or pixel-wise maps (e.g., depth map), which may not be optimal for learning discriminative features. In this paper, we propose a novel Meta-Teacher FAS (MT-FAS) method to train a meta-teacher for supervising the FAS model. Specifically, the meta-teacher is trained to learn a bilevel optimization problem, where the outer loop optimizes the teacher to generate better supervision signals for the student (FAS model), and the inner loop updates the student under the supervision of the teacher. The teacher learns to generate pixel-wise supervision maps that are more effective than the predefined ones. Extensive experiments on four public datasets demonstrate the effectiveness of our proposed method.



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
