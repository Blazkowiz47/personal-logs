---
aliases: [cr_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization, causal-learning]
authors: Guanghao Zheng, Yuchen Liu, Wenrui Dai, Chenglin Li, Junni Zou, Hongkai Xiong
year: ICASSP 2023
venue: ICASSP
paper_url: https://ieeexplore.ieee.org/document/10096866
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** CRFAS (Causal Representations for Face Anti-Spoofing)
- **Backbone:** ResNet18
- **Loss:** Supervised Contrastive Loss (for counterfactual generation), Backdoor Adjustment
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Existing DG methods (adversarial/metric learning) are flawed from a causal view. Domain-invariant features don't generalize well theoretically.

## Key Contributions
1.  **Causal Perspective:** Models FAS data generation via Structural Causal Model (SCM).
2.  **Backdoor Adjustment:** Extracts causal features using backdoor adjustment without prior assumptions.
3.  **Counterfactual Feature Generation:** Uses supervised contrastive loss to generate realistic counterfactual features for the adjustment.

## Methodology
### Architecture
- **Causal Feature Extractor:** Learned via backdoor adjustment.
- **Counterfactual Generator:** Generates counterfactual samples to de-confound the domain influence.

### Key Techniques
- **Structural Causal Model (SCM):** Modeling the causal graph.
- **Backdoor Adjustment:** A causal inference technique.

## Experiments
### Datasets Used
- Standard cross-domain protocols (OULU-NPU, CASIA-FASD, etc.).

## Critical Analysis
### What Works Well
- Causal inference is a theoretically grounded way to handle domain shifts, moving beyond simple statistical alignment.

## Relevance to My Work
### Ideas Sparked
- Causal modeling might be the next step after standard DG.
