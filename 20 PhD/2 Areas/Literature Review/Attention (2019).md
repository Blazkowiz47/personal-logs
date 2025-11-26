---
aliases: []
tags: [paper, pad, deep-fas-survey, multimodal]
authors: 
year: 2019
venue: 
paper_url: https://openaccess.thecvf.com/content_CVPRW_2019/html/CFS/Wang_Multi-Modal_Face_Presentation_Attack_Detection_via_Spatial_and_Channel_Attentions_CVPRW_2019_paper.html
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

## Quick Summary
**Method:** Multi-Modal Attention
- **Backbone:** ResNet18 (Multi-stream)
- **Loss:** Center Loss, Softmax Loss
- **Input:** RGB, Depth, IR
- **Fusion:** Feature-level with Attention

## Problem Statement
Traditional PAD approaches lack generalization due to limited modalities and subjects. Simple concatenation of modalities is suboptimal as not all features are equally important.

## Key Contributions
1. **Multi-Modal Fusion:** Proposes an end-to-end approach fusing RGB, Depth, and IR.
2. **Spatial and Channel Attention:** Introduces attention modules to select discriminative features spatially and across channels.
3. **Performance:** Achieves promising results on the CASIA-SURF dataset.

## Methodology
### Architecture
- **Backbone:** ResNet-18 based multi-stream network.
- **Branches:** 4 branches: RGB, Depth, IR, and Fused (9-channel input).
- **Fusion:** Features from all branches are concatenated and fed into shared layers.

### Key Techniques
- **Spatial Attention:** Focuses on the face region and suppresses background noise.
- **Channel Attention:** Re-weights feature channels to emphasize informative maps.
- **Loss Functions:** Joint optimization with Center Loss (intra-class compactness) and Softmax Loss (inter-class separability).

### Novel Components
- **Attention-based Fusion:** Applying attention before fusion to refine features.

## Experiments
### Datasets Used
- **CASIA-SURF:** A large-scale multi-modal dataset.

### Results
- **Performance:** The method demonstrates superior performance on CASIA-SURF compared to single-modal or simple fusion baselines.

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
