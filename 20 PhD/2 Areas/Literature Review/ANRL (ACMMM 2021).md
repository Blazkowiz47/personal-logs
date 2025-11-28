---
aliases: [anrl_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization]
authors: Shubao Liu, Ke-Yue Zhang, Taiping Yao, Mingwei Bi, Shouhong Ding, Jilin Li, Feiyue Huang, Lizhuang Ma
year: ACMMM 2021
venue: ACMMM
paper_url: https://arxiv.org/abs/2108.02667
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
## What does the paper present?
- **Backbone:** DepthNet
- **Loss:** Binary CE loss, Depth loss, Inter-Domain Compatible Loss, Inter-Class Separable Loss
- **Static/Dynamic:** S

This paper proposes an Adaptive Normalized Representation Learning (ANRL) framework for domain generalization in FAS. It focuses on the feature normalization process, adaptively selecting normalization methods based on inputs to learn domain-agnostic features. It also introduces Dual Calibration Constraints to ensure inter-domain compatibility and inter-class separability.

Most DG methods focus on feature alignment but overlook the impact of normalization in the feature extraction process. Improper normalization can hinder the learning of generalized representations across diverse domains.

1.  **ANRL Framework:** Adaptively selects feature normalization methods to learn domain-agnostic and discriminative representations.
2.  **Dual Calibration Constraints:**
    -   **Inter-Domain Compatible Loss:** Aligns features from different domains.
    -   **Inter-Class Separable Loss:** Ensures separation between bonafide and spoof classes.
3.  **Performance:** Demonstrates effectiveness against SOTA competitors on standard benchmarks.

-   **Backbone:** DepthNet (likely based on ResNet or similar).
-   **Normalization:** Adaptive selection mechanism (likely switching between Batch Norm, Instance Norm, etc.).

-   **Adaptive Normalization:** Dynamically adjusting normalization statistics to handle domain shifts.
-   **Dual Calibration:** Loss functions designed to enforce domain invariance and class discriminability simultaneously.

-   Standard DG protocols (OULU-NPU, CASIA-MFSD, Idiap Replay-Attack, MSU-MFSD).

-   Achieves competitive or state-of-the-art performance on cross-domain testing.

## What are my views on it?
-   Focusing on normalization is a unique angle compared to standard adversarial learning approaches.

-   **Ideas Sparked:** Could adaptive normalization be useful for our "Filtered PAD" project? Maybe different frequency bands require different normalization strategies?
