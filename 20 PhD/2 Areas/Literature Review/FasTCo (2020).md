---
aliases: [fastco_fas]
tags: [paper, pad, deep-fas-survey, binary-supervision, temporal-consistency]
authors: Xiang Xu, Yuanjun Xiong, Wei Xia
year: 2020
venue: arXiv
paper_url: https://arxiv.org/abs/2006.06756
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** FasTCo
- **Backbone:** ResNet50 or MobileNetV2
- **Loss:** Multi-class CE loss, Temporal Consistency loss, Class Consistency loss
- **Input:** RGB
- **Static/Dynamic:** D

## Abstract
In this paper, we focus on improving the online face liveness detection system to enhance the security of the downstream face recognition system. Most of the existing frame-based methods are suffering from the prediction inconsistency across time. To address the issue, a simple yet effective solution based on temporal consistency is proposed. Specifically, in the training stage, to integrate the temporal consistency constraint, a temporal self-supervision loss and a class consistency loss are proposed in addition to the softmax cross-entropy loss. In the deployment stage, a training-free non-parametric uncertainty estimation module is developed to smooth the predictions adaptively. Beyond the common evaluation approach, a video segment-based evaluation is proposed to accommodate more practical scenarios. Extensive experiments demonstrated that our solution is more robust against several presentation attacks in various scenarios, and significantly outperformed the state-of-the-art on multiple public datasets by at least 40% in terms of ACER. Besides, with much less computational complexity (33% fewer FLOPs), it provides great potential for low-latency online applications.



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
