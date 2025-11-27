---
aliases: [saplc_fas]
tags: [paper, pad, deep-fas-survey, auxiliary-supervision]
authors: Wenyun Sun, Yu Song, Changsheng Chen, Jiwu Huang, Alex C. Kot
year: 2020
venue: IEEE Transactions on Information Forensics and Security (TIFS)
paper_url: https://ieeexplore.ieee.org/document/9056824
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Face Spoofing Detection Based on Local Ternary Label Supervision in Fully Convolutional Networks

> [!abstract]
> Face verification systems are prone to spoofing attacks on photos, videos, and 3D masks. Face spoofing detection, i.e., face anti-spoofing, face liveness detection, or face presentation attack detection, is an important task for securing face verification systems in practice and presents many challenges. In this paper, a state-of-the-art face spoofing detection method based on a depth-based Fully Convolutional Network (FCN) is revisited. Different supervision schemes, including global and local label supervisions, are comprehensively investigated. A generic theoretical analysis and associated simulation are provided to demonstrate that local label supervision is more suitable than global label supervision for local tasks with insufficient training samples, such as the face spoofing detection task. Based on the analysis, the Spatial Aggregation of Pixel-level Local Classifiers (SAPLC), which is composed of an FCN part and an aggregation part, is proposed. The FCN part predicts the pixel-level ternary labels, which include the genuine foreground, the spoofed foreground, and the undetermined background. Then, these labels are aggregated together to yield an accurate image-level decision. Furthermore, to quantitatively evaluate the proposed SAPLC, experiments are carried out on the CASIA-FASD, Replay-Attack, OULU-NPU, and SiW datasets. The experiments show that the proposed SAPLC outperforms the representative deep networks, including two globally supervised CNNs, one depth-based FCN, two FCNs with binary labels, and two FCNs with ternary labels, and achieves competitive performances close to some state-of-the-art method performances under various common protocols. Overall, the results empirically verify the advantage of the proposed pixel-level local label supervision scheme.

## Quick Summary
**Method:** SAPLC
- **Supervision:** TernaryMap
- **Backbone:** DepthNet
- **Input:** RGB, HSV
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
