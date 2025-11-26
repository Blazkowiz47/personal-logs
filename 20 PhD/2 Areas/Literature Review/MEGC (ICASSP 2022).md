---
aliases: []
tags: [paper, pad, deep-fas-survey, auxiliary-supervision, explainable-cues]
authors: Ying Bian, Peng Zhang, Jingjing Wang, Chunmao Wang, Shiliang Pu
year: 2022
venue: ICASSP
paper_url: https://arxiv.org/abs/2202.10187
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** MEGC
- **Supervision:** Depth, Relection, Moire, Boundary
- **Backbone:** DepthNet+Feature Enrichment
- **Input:** RGB, HSV
- **Static/Dynamic:** S

## Abstract
Although previous CNN based face anti-spoofing methods have achieved promising performance under intra-dataset testing, they suffer from poor generalization under cross-dataset testing. The main reason is that they learn the network with only binary supervision, which may learn arbitrary cues overfitting on the training dataset. To make the learned feature explainable and more generalizable, some researchers introduce facial depth and reflection map as the auxiliary supervision. However, many other generalizable cues are unexplored for face anti-spoofing, which limits their performance under cross-dataset testing. To this end, we propose a novel framework to learn multiple explainable and generalizable cues (MEGC) for face anti-spoofing. Specifically, inspired by the process of human decision, four mainly used cues by humans are introduced as auxiliary supervision including the boundary of spoof medium, moiré pattern, reflection artifacts and facial depth in addition to the binary supervision. To avoid extra labelling cost, corresponding synthetic methods are proposed to generate these auxiliary supervision maps. Extensive experiments on public datasets validate the effectiveness of these cues, and state-of-the-art performances are achieved by our proposed method.



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
