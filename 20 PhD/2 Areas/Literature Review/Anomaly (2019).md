---
aliases: []
tags: [paper, pad, deep-fas-survey, anomaly-detection]
authors: 
year: 2019
venue: 
paper_url: https://openaccess.thecvf.com/content_CVPRW_2019/papers/CFS/Perez-Cabo_Deep_Anomaly_Detection_for_Generalized_Face_Anti-Spoofing_CVPRW_2019_paper.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

## Quick Summary
**Method:** Deep Anomaly Detection
- **Backbone:** ResNet50
- **Loss:** Metric-Softmax Loss, Triplet Focal Loss
- **Input:** RGB
- **Approach:** One-Class Classification (Anomaly Detection)

## Problem Statement
FAS is typically treated as binary classification, but "spoof" attacks are unbounded and diverse, while "live" faces are consistent. Generalization to unseen attacks is a major challenge.

## Key Contributions
1. **Anomaly Detection Formulation:** Reformulates Generalized PAD (GPAD) as an anomaly detection problem.
2. **Metric-Softmax Loss:** Guides learning towards discriminative embeddings on a hypersphere.
3. **Triplet Focal Loss:** Regularization to push anomalies away from the live center, focusing on hard examples.
4. **Few-Shot Estimation:** Introduces a posteriori probability estimation without training a classifier.

## Methodology
### Architecture
- **Backbone:** ResNet-50.
- **Framework:** Deep Metric Learning.

### Key Techniques
- **Metric-Softmax:** A loss function to enforce compactness of the "live" class in the embedding space.
- **Triplet Focal Loss:** Ensures a margin between live and spoof samples, handling class imbalance and hard examples.
- **Inference:** Distance to the learned "live center" determines the score.

### Novel Components
- **GPAD as Anomaly Detection:** Shifting from binary classification to one-class learning.

## Experiments
### Datasets Used
- **GRAD-GPAD:** Aggregated dataset for Generalized PAD.

### Results
- **Performance:** Outperforms state-of-the-art methods on the GRAD-GPAD framework, showing better generalization.

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
