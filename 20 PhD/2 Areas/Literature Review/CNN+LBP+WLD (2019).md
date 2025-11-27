---
aliases: [cnnlbpwld_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method]
authors: Mohammed Khammari et al.
year: 2019
venue: IET Image Processing
paper_url: https://digital-library.theiet.org/content/journals/10.1049/iet-ipr.2018.5560
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** CNN+LBP+WLD
- **Backbone:** CNN (feature extractor)
- **Loss:** SVM Classifier
- **Input:** RGB (LBP and WLD features)
- **Static/Dynamic:** S

## Problem Statement
Biometric systems are vulnerable to presentation attacks (photo, video, mask). Deep learning models can be computationally expensive or fail to capture local texture details effectively.

## Key Contributions
1.  **Hybrid Feature Extraction:** Combines Local Binary Patterns (LBP) and Simplified Weber Local Descriptor (SWLD) with CNN models.
2.  **Complementary Features:** LBP captures edge orientations, while WLD preserves local intensity information.
3.  **SVM Classification:** Uses a non-linear SVM for the final classification of the extracted features.

## Methodology
### Architecture
- **Feature Extraction:** LBP and SWLD are used to encode local features.
- **CNN:** Used to process these features (or features are extracted from CNN, the abstract is slightly ambiguous, likely "LBP and SWLD encoded CNN models" means CNNs trained on these features or features fed into CNN). *Correction based on abstract:* "extracting the local features... encoded convolutional neural network models". It seems to imply using CNNs to learn from these descriptors or vice versa.
- **Classification:** SVM with a kernel function.

### Key Techniques
- **LBP (Local Binary Patterns):** For texture/edge orientation.
- **WLD (Weber Local Descriptor):** For local intensity information.
- **Fusion:** Combining these complementary features.

## Experiments
### Datasets Used
- Replay-Attack
- CASIA-FAS

### Results
- The approach performs better than state-of-the-art techniques (at the time) on these databases.

## Critical Analysis
### What Works Well
- Combining hand-crafted texture features (LBP, WLD) with learning-based methods (CNN/SVM) is a classic robust approach for PAD.

## Relevance to My Work
### Ideas Sparked
- The importance of preserving both edge orientation (LBP) and intensity info (WLD) is a good reminder for feature engineering.



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
