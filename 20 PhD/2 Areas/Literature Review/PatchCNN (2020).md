---
aliases: []
tags: [paper, pad, deep-fas-survey, binary-supervision]
authors: Waldir R. Almeida, Fernanda A. Andaló, Rafael Padilha, Gabriel Bertocco, William Dias, Ricardo da S. Torres, Jacques Wainer, Anderson Rocha
year: 2020
venue: PLOS ONE
paper_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0238058
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Detecting face presentation attacks in mobile devices with a patch-based CNN and a sensor-aware loss function

> [!abstract]
> With the widespread use of biometric authentication comes the exploitation of presentation attacks, possibly undermining the effectiveness of these technologies in real-world setups. One example takes place when an impostor, aiming at unlocking someone else’s smartphone, deceives the built-in face recognition system by presenting a printed image of the user. In this work, we study the problem of automatically detecting presentation attacks against face authentication methods, considering the use-case of fast device unlocking and hardware constraints of mobile devices. To enrich the understanding of how a purely software-based method can be used to tackle the problem, we present a solely data-driven approach trained with multi-resolution patches and a multi-objective loss function crafted specifically to the problem. We provide a careful analysis that considers several user-disjoint and cross-factor protocols, highlighting some of the problems with current datasets and approaches. Such analysis, besides demonstrating the competitive results yielded by the proposed method, provides a better conceptual understanding of the problem. To further enhance efficacy and discriminability, we propose a method that leverages the available gallery of user data in the device and adapts the method decision-making process to the user’s and the device’s own characteristics. Finally, we introduce a new presentation-attack dataset tailored to the mobile-device setup, with real-world variations in lighting, including outdoors and low-light sessions, in contrast to existing public datasets.

## Quick Summary
**Method:** PatchCNN
- **Backbone:** SqueezeNet v1.1
- **Loss:** Binary CE loss, Triplet loss
- **Input:** RGB
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
