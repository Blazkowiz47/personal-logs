---
aliases: [auroraguard_fas]
tags: [paper, pad, deep-fas-survey, specialized-sensor]
authors: 
year: 2019
venue: 
paper_url: https://arxiv.org/abs/1902.10311
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

## Quick Summary
**Method:** Aurora Guard
- **Backbone:** Multi-task CNN (U-Net based)
- **Loss:** Binary CE, Depth Loss, Light Regression Loss
- **Input:** Video with active light projection (RGB)
- **Static/Dynamic:** D (Active)

## Problem Statement
Passive FAS methods struggle with complex attacks and generalization. Active methods using specific hardware (IR/Depth) are expensive. This paper proposes a cost-effective active solution using the screen light.

## Key Contributions
1. **Aurora Guard (AG):** A light reflection-based FAS method that is fast, simple, and effective.
2. **Multi-task CNN:** Recovers subject's depth map and performs light CAPTCHA checking (regression).
3. **Large-scale Dataset:** Collected 12,000 live and spoofing samples with abundant imaging qualities and PAIs.

## Methodology
### Architecture
- **Input:** Sequence of frames with changing screen color (Red, Green, Blue).
- **Network:** End-to-end trainable multi-task CNN.
- **Branches:**
    - **Depth Estimation:** Recovers 3D depth map from reflection patterns.
    - **Light CAPTCHA:** Regresses the light parameters to verify they match the projected pattern.

### Key Techniques
- **Active Light Projection:** Uses the smartphone screen to project random colors.
- **Light Reflection Analysis:** Normal cues are extracted from how light reflects off the face (3D vs 2D).
- **Light CAPTCHA:** A challenge-response mechanism to ensure the light on the face matches the screen.

### Novel Components
- **Reflection-based Liveness:** Exploiting the difference in surface normal and material properties under changing light.

## Experiments
### Datasets Used
- **Private Dataset:** 12,000 samples.
- **Public Datasets:** (Likely tested on others for comparison, but main focus is the new method).

### Results
- **Performance:** State-of-the-art results on the collected dataset and public benchmarks.
- **Speed:** Real-time performance on mobile devices.

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
