---
aliases: [face_revelio_fas]
tags: [paper, pad, deep-fas-survey, specialized-sensor, active-illumination]
authors: Habiba Farrukh, Reham Mohamed Aburas, Siyuan Cao, He Wang
year: 2020
venue: MobiCom
paper_url: https://dl.acm.org/doi/10.1145/3372224.3419206
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** Face-Revelio
- **Backbone:** Siamese-AlexNet
- **Loss:** L1 distance
- **Input:** Four flash lights displayed on four quarters of a screen
- **Static/Dynamic:** D

## Abstract
Facial authentication mechanisms are gaining traction on smartphones because of their convenience and increasingly good performance of face recognition systems. However, mainstream systems use traditional 2D face recognition technologies, which are vulnerable to various spoofing attacks. Existing systems perform liveness detection via specialized hardware, such as infrared dot projectors and dedicated cameras. Although effective, such methods do not align well with the smartphone industry's desire to maximize screen space. This paper presents a new liveness detection system, FaceRevelio, for commodity smartphones with a single front camera. It utilizes the smartphone screen to illuminate a user's face from multiple directions. The facial images captured under varying illumination enable the recovery of the face surface normals via photometric stereo, which can then be integrated into a 3D shape. We leverage the facial depth features of this 3D surface to distinguish a human face from its 2D counterpart. On top of this, we change the screen via a light passcode consisting of a combination of random light patterns to provide security against replay attacks. We evaluate FaceRevelio with 30 users trying to authenticate under various lighting conditions and with a series of 2D spoofing attacks. The results show that using a passcode of 1s, FaceRevelio achieves a mean EER of 1.4% and 0.15% against photo and video attacks, respectively.



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
