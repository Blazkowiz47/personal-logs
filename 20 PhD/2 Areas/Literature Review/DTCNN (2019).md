---
aliases: []
tags: [paper, pad, deep-fas-survey, domain-adaptation, transfer-learning]
authors: Xiaoguang Tu, Hengsheng Zhang, Mei Xie, Yao Luo, Yuefei Zhang, Zheng Ma
year: 2019
venue: arXiv
paper_url: https://arxiv.org/abs/1901.05633
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** DTCNN (Deep Transfer CNN)
- **Backbone:** AlexNet
- **Loss:** Binary CE loss, MMD loss
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Poor generalization across datasets due to variety of spoofing materials and environmental conditions. Limited labeled data in target domains.

## Key Contributions
1.  **Deep Transfer Learning:** Uses sparsely labeled data from the target domain to learn invariant features.
2.  **MMD (Maximum Mean Discrepancy):** Minimizes the distribution distance between source and target domains in the feature space.

## Methodology
### Architecture
- **Backbone:** AlexNet (fine-tuned).
- **Adaptation:** MMD loss layer.

## Experiments
### Datasets Used
- Cross-dataset benchmarks.

## Critical Analysis
### What Works Well
- MMD is a standard and effective baseline for domain adaptation.

## Relevance to My Work
### Ideas Sparked
- Semi-supervised or few-shot adaptation is very practical.
