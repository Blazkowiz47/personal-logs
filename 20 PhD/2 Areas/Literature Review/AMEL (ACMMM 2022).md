---
aliases:
  - amel_fas
tags:
  - paper
  - FAS
  - ACMMM
  - year_2022
  - domain-generalization
  - method/mixture-of-experts
  - method/meta-learning
authors:
  - Qianyu Zhou
  - Ke-Yue Zhang
  - Taiping Yao
  - Ran Yi
  - Shouhong Ding
  - Lizhuang Ma
year: 2022
venue: ACM MM
paper_url: https://arxiv.org/abs/2207.09868
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Adaptive Mixture of Experts Learning for Generalizable Face Anti-Spoofing (AMEL)

## Quick Summary
**Method:** AMEL (Adaptive Mixture of Experts Learning)
- **Backbone:** Mixture of Experts (MoE) framework
- **Loss:** CE loss, Depth loss, Feature consistency loss
- **Input:** RGB
- **Static/Dynamic:** Static

This paper proposes an **Adaptive Mixture of Experts Learning (AMEL)** framework for Domain Generalization (DG) in FAS. It argues that existing DG methods focus too much on domain-invariant features and neglect domain-specific characteristics. AMEL uses **Domain-Specific Experts (DSE)** to learn unique features for each source domain and a **Dynamic Expert Aggregation (DEA)** module to adaptively combine them for unseen target domains based on domain relevance.

## Problem Statement
Standard DG methods try to find a common feature space for all domains, which might be suboptimal because different domains (and attack types) have distinct characteristics. Ignoring these specific traits limits generalization.

## Key Contributions
1.  **Adaptive Mixture of Experts Learning (AMEL):** A framework that leverages both domain-invariant and domain-specific information.
2.  **Domain-Specific Experts (DSE):** Experts trained to specialize in individual source domains.
3.  **Dynamic Expert Aggregation (DEA):** A mechanism to weight the contributions of different experts based on how similar the target input is to the source domains.
4.  **Meta-Learning Integration:** Used to train the aggregation module to generalize to unseen domains.

## Methodology
### Architecture
- **Experts:** Multiple networks, each expert on a specific domain.
- **Gating Network (DEA):** Decides how much to trust each expert for a given input.

### Key Techniques
- **Mixture of Experts (MoE):** A classic ensemble technique applied to DG.
- **Meta-Learning:** Simulating domain shift during training to prepare for the real test.

## Experiments
### Datasets Used
- OULU-NPU
- CASIA-MFSD
- Replay-Attack
- MSU-MFSD

### Results
- Outperforms SOTA competitors on standard DG protocols.

## Critical Analysis
### What Works Well
- The MoE approach makes a lot of sense for FAS because "spoof" is such a diverse category. A print attack expert might not be good at mask attacks, so having specialized experts and a router is a logical step.

## Relevance to My Work
### Ideas Sparked
- I could implement a simple MoE where I have one expert for "print", one for "replay", and one for "mask", if I have labels for those.

## Notes & Highlights
- Accepted to ACM Multimedia 2022.

