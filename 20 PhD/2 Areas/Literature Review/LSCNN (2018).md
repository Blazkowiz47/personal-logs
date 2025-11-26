tags: [paper, pad, deep-fas-survey, binary-supervision, local-features]
authors: Gustavo Botelho de Souza, João Paulo Papa, Aparecido Nilceu Marana
year: 2018
venue: SIBGRAPI
paper_url: https://ieeexplore.ieee.org/document/8614337
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** LSCNN
- **Backbone:** 9 PatchNets
- **Loss:** Binary CE loss
- **Input:** RGB
- **Static/Dynamic:** S

## Abstract
Biometrics emerged as a robust solution for security systems. However, given the dissemination of biometric applications, criminals are developing techniques to circumvent them by simulating physical or behavioral traits of legal users (spoofing attacks). Despite face being a promising characteristic due to its universality, acceptability and presence of cameras almost everywhere, face recognition systems are extremely vulnerable to such frauds since they can be easily fooled with common printed facial photographs. State-of-the-art approaches, based on Convolutional Neural Networks (CNNs), present good results in face spoofing detection. However, these methods do not consider the importance of learning deep local features from each facial region, even though it is known from face recognition that each facial region presents different visual aspects, which can also be exploited for face spoofing detection. In this work we propose a novel CNN architecture trained in two steps for such task. Initially, each part of the neural network learns features from a given facial region. Afterwards, the whole model is fine-tuned on the whole facial images. Results show that such pre-training step allows the CNN to learn different local spoofing cues, improving the performance and the convergence speed of the final model, outperforming the state-of-the-art approaches.



## Problem Statement
Biometrics emerged as a robust solution for security systems. However, given the dissemination of biometric applications, criminals are developing techniques to circumvent them by simulating physical or behavioral traits of legal users (spoofing attacks). Despite face being a promising characteristic due to its universality, acceptability and presence of cameras almost everywhere, face recognition systems are extremely vulnerable to such frauds since they can be easily fooled with common printed facial photographs. State-of-the-art approaches, based on Convolutional Neural Networks (CNNs), present good results in face spoofing detection. However, these methods do not consider the importance of learning deep local features from each facial region, even though it is known from face recognition that each facial region presents different visual aspects, which can also be exploited for face spoofing detection. In this work we propose a novel CNN architecture trained in two steps for such task. Initially, each part of the neural network learns features from a given facial region. Afterwards, the whole model is fine-tuned on the whole facial images. Results show that such pre-training step allows the CNN to learn different local spoofing cues, improving the performance and the convergence speed of the final model, outperforming the state-of-the-art approaches.


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
