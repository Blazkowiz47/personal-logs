---
aliases:
  - flip_fas
  - flip-fas
  - FLIP-FAS
tags:
  - paper
  - pad
  - to-read
authors:
  - Koushik Srivatsan
  - Muzammal Naseer
  - Karthik Nandakumar
year: 2023
venue: ICCV
paper_url: https://arxiv.org/pdf/2309.16649
code_url: https://github.com/koushiksrivats/FLIP
status: 📚 To Read
dateadded: 2025-11-28
dateread:
priority: medium
---

## Quick Summary
Uses CLIP pretrained weights and perform finetuning.

## Problem Statement
What problem does this paper address?

## Key Contributions
1. We show that direct finetuning of a multimodal pre-trained ViT (e.g., CLIP image encoder) achieves better FAS generalizability without any bells and whistles.
2. We propose a new approach for robust cross-domain FAS by grounding the visual representation using natural language semantics. This is realized by aligning the image representation with an ensemble of text prompts (describing the class) during finetuning.
3. We propose a multimodal contrastive learning strategy, which enforces the model to learn more generalized features that bridge the FAS domain gap even with limited training data. This strategy leverages view-based image self-supervision and view-based cross-modal image-text similarity as additional constraints during the learning process.
4. Extensive experiments on three standard protocols demonstrate that our method significantly outperforms the state- of-the-art methods, achieving better zero-shot transfer performance than five-shot transfer of “adaptive ViTs”.

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
