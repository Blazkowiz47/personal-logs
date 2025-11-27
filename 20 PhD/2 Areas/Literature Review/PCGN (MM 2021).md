---
aliases: [pcgn_fas]
tags: [paper, pad, deep-fas-survey, binary-supervision]
authors: Sheng Li, Xun Zhu, Guorui Feng, Xinpeng Zhang, Zhenxing Qian
year: 2021
venue: ACM Multimedia (MM)
paper_url: https://dl.acm.org/doi/10.1145/3474085.3475305
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Diffusing the Liveness Cues for Face Anti-spoofing

> [!abstract]
> Face anti-spoofing is an important step for secure face recognition. One of the main challenges is how to learn and build a general classifier that is able to resist various presentation attacks. Recently, the patch-based face anti-spoofing schemes are shown to be able to improve the robustness of the classifier. These schemes extract subtle liveness cues from small local patches independently, which do not fully exploit the correlations among the patches. In this paper, we propose a Patch-based Compact Graph Network (PCGN) to diffuse the subtle liveness cues from all the patches. Firstly, the image is encoded into a compact graph by connecting each node with its backward neighbors. We then propose an asymmetrical updating strategy to update the compact graph. Such a strategy aggregates the node based on whether it is a sender or receiver, which leads to better message-passing. The updated graph is eventually decoded for making the final decision. We conduct the experiments on four public databases with four intra-database protocols and eight cross-database protocols, the results of which demonstrate the effectiveness of our PCGN for face anti-spoofing.

## Quick Summary
**Method:** PCGN
- **Backbone:** ResNet101+GCN
- **Loss:** CE Loss for node and edge
- **Input:** RGB whole image
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
