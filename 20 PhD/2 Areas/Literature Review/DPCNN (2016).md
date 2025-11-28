---
aliases: [dpcnn_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method, partial-cnn]
authors: Lei Li, Xiaoyi Feng, Z. Boulkenafet, Zhaoqiang Xia, Mingming Li, A. Hadid
year: 2016
venue: IPTA
paper_url: https://ieeexplore.ieee.org/document/7821013
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** DPCNN (Deep Partial CNN)
- **Backbone:** VGG-Face (Partial)
- **Loss:** SVM (Hinge Loss)
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Early deep learning methods for FAS were computationally expensive and prone to overfitting on small datasets.

## Key Contributions
1.  **Partial CNN:** Uses a pre-trained VGG-Face model but only fine-tunes/uses parts of it to extract features.
2.  **SVM Classifier:** Uses an SVM on top of the deep features for final classification, which was common in the transition era from handcrafted to deep learning.

## Methodology
### Architecture
- **Feature Extractor:** VGG-Face (truncated).
- **Classifier:** SVM.

## Experiments
### Datasets Used
- CASIA-FASD, Replay-Attack.

## Critical Analysis
### What Works Well
- Using SVMs on top of deep features is a robust way to handle small datasets.

## Relevance to My Work
### Ideas Sparked
- Historical context: shows the evolution from handcrafted -> hybrid (Deep+SVM) -> End-to-End Deep Learning.

## Quick Summary
**Method:** DPCNN (Deep Partial CNN)
- **Title:** An original face anti-spoofing approach using partial convolutional neural network
- **Backbone:** VGG-Face
- **Loss:** Trained with SVM
- **Input:** RGB
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
