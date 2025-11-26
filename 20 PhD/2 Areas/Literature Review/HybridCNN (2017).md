---
aliases: []
tags: [paper, pad, deep-fas-survey, hybrid-method, part-based]
authors: Lei Li, et al.
year: 2017
venue: FADS
paper_url: https://ieeexplore.ieee.org/document/8253209
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** HybridCNN
- **Backbone:** VGG-Face (Hybrid CNN for facial parts)
- **Loss:** Trained with SVM
- **Input:** RGB (Facial parts)
- **Static/Dynamic:** S

## Abstract
Face anti-spoofing techniques have been developed several years since the face recognition systems were successfully applied. Existing approaches in this topic merely use the entire region of human face. However, different facial parts always have different structures and the full-face model maybe weaken the discrepancy of the specific parts. So training the specific model for each facial part can improve the performance of anti-spoofing. Motivated by this, in this paper, we propose a new method of face anti-spoofing leveraging hybrid convolutional neural network (CNN) for facial parts. The main procedure of our work can be summarized as follows: (i) We divide the face into several parts; (ii) Based on different parts, training the corresponding CNN model of each part, which will constitute the hybrid CNN; (iii) Concatenating the last layer of the hybrid model to train a SVM classifier; (iv) By the SVM to distinguish the real and fake faces. We tested the effectiveness of our method on two public available databases, Replay-Attack and CASIA, and the experiments show our proposed method can obtain satisfactory results with respect to the state-of-the- art methods.



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
