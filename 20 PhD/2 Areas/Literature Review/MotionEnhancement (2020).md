---
aliases: [motionenhancement_fas]
tags: [paper, pad, deep-fas-survey, binary-supervision, motion-enhancement]
authors: Zitong Yu, Benjia Zhou, Jun Wan, Pong C. Yuen, Haibin Ling, Guoying Zhao
year: 2020
venue: TIFS
paper_url: https://ieeexplore.ieee.org/document/9203944
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** MotionEnhancement
- **Backbone:** VGGface+LSTM
- **Loss:** Binary CE loss
- **Input:** RGB
- **Static/Dynamic:** D

## Abstract
Face anti-spoofing (FAS) plays a vital role in securing face recognition systems. Most existing methods focus on extracting spatial features from static images or stacking spatial features from video frames, ignoring the fine-grained motion information that is crucial for distinguishing live faces from spoofing attacks (e.g., print, replay). In this paper, we propose a Motion-Enhanced Video Representation (MEVR) learning framework for FAS. Specifically, we design a Motion Enhancement Module (MEM) to capture short-term motion cues between adjacent frames and a Video Representation Network (VRN) to aggregate long-term spatiotemporal features. The MEM can be plugged into existing CNN backbones to enhance their sensitivity to motion. We also introduce a cross-entropy loss and a contrastive loss to supervise the training. Experimental results on three large-scale datasets show that our method achieves state-of-the-art performance.



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
