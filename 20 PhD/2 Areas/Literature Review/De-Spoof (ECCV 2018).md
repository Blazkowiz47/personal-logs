---
aliases: [de_spoof_fas]
tags: [paper, pad, deep-fas-survey, generative-model, noise-modeling, de-spoofing]
authors: Amin Jourabloo, Yaojie Liu, Xiaoming Liu
year: 2018
venue: ECCV
paper_url: https://arxiv.org/abs/1807.09968
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** De-Spoof (Face De-Spoofing)
- **Supervision:** Depth, BinaryMask, FourierMap (Spoof Noise)
- **Backbone:** DSNet (De-Spoofing Net), DepthNet
- **Input:** RGB, HSV
- **Static/Dynamic:** S

## Abstract
Many prior face anti-spoofing works develop discriminative models for recognizing the subtle differences between live and spoof faces. Those approaches often regard the image as an indivisible unit, and process it holistically, without explicit modeling of the spoofing process. In this work, motivated by the noise modeling and denoising algorithms, we identify a new problem of face de-spoofing, for the purpose of anti-spoofing: inversely decomposing a spoof face into a spoof noise and a live face, and then utilizing the spoof noise for classification. A CNN architecture with proper constraints and supervisions is proposed to overcome the problem of having no ground truth for the decomposition. We evaluate the proposed method on multiple face anti-spoofing databases. The results show promising improvements due to our spoof noise modeling. Moreover, the estimated spoof noise provides a visualization which helps to understand the added spoof noise by each spoof medium.



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
