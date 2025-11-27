---
aliases: [slnet_fas]
tags: [paper, pad, deep-fas-survey, specialized-sensor]
authors: Yasar Abbas Ur Rehman, Lai-Man Po, Mengyang Liu
year: 2020
venue: Expert Systems with Applications
paper_url: http://www.ee.cityu.edu.hk/~lmpo/publications/2019_ESA_SLNet.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# SLNet: Stereo face liveness detection via dynamic disparity-maps and convolutional neural network

> [!abstract]
> Current state-of-the-art dual camera-based face liveness detection methods utilize either hand-crafted features, such as disparity, or deep texture features to classify a live face and face Presentation Attack (PA). However, these approaches limit the effectiveness of classifiers, particularly deep Convolutional Neural Networks (CNN) to unknown face PA in adverse scenarios. In contrast to these approaches, in this paper, we show that supervising a deep CNN classifier by learning disparity features using the existing CNN layers improves the performance and robustness of CNN to unknown types of face PA. For this purpose, we propose to supervise a CNN classifier by introducing a disparity layer within CNN to learn the dynamic disparity-maps. Subsequently, the rest of the convolutional layers, following the disparity layer, in the CNN are supervised using the learned dynamic disparity-maps for face liveness detection. We further propose a new video-based stereo face anti-spoofing database with various face PA and different imaging qualities. Experiments on the proposed stereo face anti-spoofing database are performed using various test case scenarios. The experimental results indicate that our proposed system shows promising performance and has good generalization ability.

## Quick Summary
**Method:** SLNet
- **Backbone:** 17-layer CNN
- **Loss:** Binary CE loss
- **Input:** Stereo (left&right) face images
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
