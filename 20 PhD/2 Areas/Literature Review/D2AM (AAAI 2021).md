---
aliases: [d2am_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization, meta-learning]
authors: Zhihong Chen, Taiping Yao, Kekai Sheng, Shouhong Ding, Ying Tai, Jilin Li, Feiyue Huang, Xinyu Jin
year: AAAI 2021
venue: AAAI
paper_url: https://ojs.aaai.org/index.php/AAAI/article/view/16199
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** D2AM (Domain Dynamic Adjustment Meta-learning)
- **Backbone:** DepthNet (likely)
- **Loss:** Meta-learning loss, MMD loss
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Existing DG methods assume known domain labels. Real-world data has mixture domains with unknown labels.

## Key Contributions
1.  **Mixture Domain DG:** Addresses the problem where domain labels are unknown.
2.  **D2AM:** Domain Dynamic Adjustment Meta-learning. Iteratively divides mixture domains via discriminative domain representation.
3.  **DRLM:** Domain Representation Learning Module using Instance Normalization (IN).

## Methodology
### Architecture
- **DRLM:** Extracts domain features.
- **Clustering:** Divides data into domains dynamically.
- **Meta-Learning:** Trains a generalizable model on these discovered domains.

### Key Techniques
- **Instance Normalization (IN):** For domain style features.
- **MMD (Maximum Mean Discrepancy):** To align distributions and reduce outlier effects.

## Experiments
### Datasets Used
- Standard cross-domain protocols.

## Critical Analysis
### What Works Well
- Handling unknown domain labels is a significant step towards "in the wild" generalization.

## Relevance to My Work
### Ideas Sparked
- Unsupervised domain discovery is a powerful concept.
