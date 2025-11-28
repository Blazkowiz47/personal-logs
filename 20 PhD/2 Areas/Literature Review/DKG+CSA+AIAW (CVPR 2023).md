---
aliases: [dkg_csa_aiaw_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization, instance-aware]
authors: Qianyu Zhou, Ke-Yue Zhang, Taiping Yao, Xuequan Lu, Ran Yi, Shouhong Ding, Lizhuang Ma
year: CVPR 2023
venue: CVPR
paper_url: https://arxiv.org/abs/2304.05640
code_url: https://github.com/qianyuzqy/IADG
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
- **Components:** DKG (Dynamic Kernel Generator), CSA (Categorical Style Assembly), AIAW (Asymmetric Instance Adaptive Whitening)
- **Backbone:** DepthNet (likely)
- **Loss:** BCE loss, Depth loss, AIAW loss
- **Input:** RGB
- **Static/Dynamic:** S

Existing DG methods rely on coarse-grained domain labels, which are subjective and don't reflect real distributions. They align at the domain level, ignoring instance-level style variations.

1.  **Instance-Aware DG (IADG):** Aligns features at the instance level without domain labels.
2.  **AIAW (Asymmetric Instance Adaptive Whitening):** Adaptively eliminates style-sensitive feature correlations.
3.  **DKG (Dynamic Kernel Generator):** Extracts instance-specific features.
4.  **CSA (Categorical Style Assembly):** Generates style-diversified features to improve robustness.

- **AIAW:** Whitening transformation to remove style information.
- **DKG & CSA:** Modules to handle instance-specific styles.

- Standard cross-domain benchmarks.

## What are my views on it?
- Moving away from "domain labels" is the right direction. "Domains" in FAS are often just different camera sensors or lighting conditions, which are continuous, not discrete.

- Instance-level alignment is more granular and potentially more powerful than domain-level alignment.
