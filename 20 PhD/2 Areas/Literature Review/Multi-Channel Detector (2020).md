---
aliases: []
tags: [paper, pad, deep-fas-survey, multimodal]
authors: Anjith George, Sebastien Marcel
year: 2020
venue: arXiv:2006.16836 (Idiap-RR-12-2020)
paper_url: https://arxiv.org/abs/2006.16836
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

> [!abstract]
> In a typical face recognition pipeline, the task of the face detector is to localize the face region. However, the face detector localizes regions that look like a face, irrespective of the liveliness of the face, which makes the entire system susceptible to presentation attacks. In this work, we try to reformulate the task of the face detector to detect real faces, thus eliminating the threat of presentation attacks. While this task could be challenging with visible spectrum images alone, we leverage the multi-channel information available from off the shelf devices (such as color, depth, and infrared channels) to design a multi-channel face detector. The proposed system can be used as a live-face detector obviating the need for a separate presentation attack detection module, making the system reliable in practice without any additional computational overhead. The main idea is to leverage a single-stage object detection framework, with a joint representation obtained from different channels for the PAD task. We have evaluated our approach in the multi-channel WMCA dataset containing a wide variety of attacks to show the effectiveness of the proposed framework.

## Quick Summary
**Method:** Multi-Channel Detector
- **Backbone:** RetinaNet (FPN+ResNet18)
- **Loss:** Landmark regression, Focal loss
- **Input:** Grayscale-Depth-Infrared composition
- **Fusion:** Input-level



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
