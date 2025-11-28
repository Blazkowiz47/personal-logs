---
aliases: [drdg_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization, reweighting]
authors: Shubao Liu, Ke-Yue Zhang, Taiping Yao, Kekai Sheng, Shouhong Ding, Ying Tai, Jilin Li, Yuan Xie, Lizhuang Ma
year: IJCAI 2021
venue: IJCAI
paper_url: https://arxiv.org/abs/2106.16128
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
- **Backbone:** DepthNet
- **Modules:** Sample Reweighting Module, Feature Reweighting Module
- **Loss:** Binary CE loss, Depth loss, Domain loss
- **Static/Dynamic:** S

Treating all samples from multiple domains equally during training corrupts generalization because of complex and biased data distributions. Some samples have large domain bias.

1.  **Dual Reweighting:** Iteratively reweights the relative importance of samples and features.
2.  **Sample Reweighting Module:** Identifies samples with large domain bias and reduces their impact.
3.  **Feature Reweighting Module:** Focuses on these samples to extract more domain-irrelevant features via self-distillation.

- **Iterative Reweighting:** The two modules work in tandem to refine the learning process.

- **Reweighting:** A form of curriculum learning or robust optimization where "hard" or "biased" samples are down-weighted or treated differently.

- Standard cross-domain benchmarks.

## What are my views on it?
- Reweighting is a smart way to handle noisy or biased data without throwing it away.

- Could apply reweighting to my training loop to handle outliers or difficult samples.
