---
aliases: []
tags: [paper, pad, deep-fas-survey, domain-adaptation]
authors: Yunxiao Qin, Weiguo Zhang, Jingping Shi, Zezheng Wang, Longbin Yan
year: 2020
venue: Neurocomputing
paper_url: https://www.sciencedirect.com/science/article/pii/S0925231220313540
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

> [!abstract]
> Existing face anti-spoofing (FAS) methods usually train a deep network-based detector on collected living and spoofing faces recorded with several reserved face capture conditions (e.g., reserved devices and scenes). Due to this data-driven approach, the trained detector performs well in detecting spoofing faces recorded with reserved capture conditions. However, as faces recorded with different conditions will differ to a greater or lesser degree, the detector’s performance may decline in real FAS applications in which faces are recorded with new capture conditions. To avoid the detector’s performance decline in real applications, we propose that the detector should efficiently adapt itself to any new application by fully utilizing the easy-collecting living faces in this application. We call this problem a one-class adaptation (OCA) problem for FAS. In this paper, we develop a novel one-class adaptation face anti-spoofing (OCA-FAS) method for the OCA problem. Specifically, OCA-FAS solves the OCA problem by training a meta-learner on OCA tasks for learning adaptation with only living faces. In addition, a novel meta loss function search (MLS) strategy that searches for better loss function to help the meta-learner solving OCA tasks is presented in OCA-FAS. To evaluate the developed OCA-FAS, we propose a benchmark with three protocols to test the detector’s performance on the OCA aspect. Our experiments show that compared with existing state-of-the-art FAS methods, OCA-FAS performs much better on not only our proposed benchmark but also existing benchmarks.

## Quick Summary
**Method:** OCA-FAS
- **Backbone:** DepthNet
- **Loss:** Binary CE loss, Pixel-wise binary loss
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
