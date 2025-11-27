---
aliases: [dcdca_ppcr_fas]
tags: [paper, pad, deep-fas-survey, continual-learning, domain-generalization]
authors: Rizhao Cai, Yawen Cui, Zhi Li, Zitong Yu, Haoliang Li, Yongjian Hu, Alex Kot
year: 2023
venue: arXiv
paper_url: https://arxiv.org/abs/2303.09914
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** DCDCA+PPCR (Rehearsal-Free Domain Continual FAS)
- **Replay or not:** Rehearsal-Free
- **Backbone:** ViT
- **Loss:** BCE loss, Proxy Prototype Contrastive Regularization (PPCR)
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Continual learning in FAS usually requires replay buffers (storing old data), which is a privacy risk. Existing methods suffer from catastrophic forgetting without replay.

## Key Contributions
1.  **Rehearsal-Free DCL:** First method for Domain Continual Learning (DCL) in FAS without storing previous data.
2.  **DCDCA (Dynamic Central Difference Convolutional Adapter):** Adapts ViT models to new domains efficiently.
3.  **PPCR (Proxy Prototype Contrastive Regularization):** Constrains learning using proxy prototypes to prevent forgetting previous domain knowledge.

## Methodology
### Architecture
- **Backbone:** Vision Transformer (ViT).
- **Adapter:** DCDCA inserted into ViT blocks.

### Key Techniques
- **Proxy Prototypes:** Storing prototypes instead of raw images to preserve privacy and memory.

## Experiments
### Datasets Used
- Standard cross-domain benchmarks in a sequential setting.

## Critical Analysis
### What Works Well
- Rehearsal-free methods are the future for privacy-sensitive applications like Face ID.

## Relevance to My Work
### Ideas Sparked
- Using adapters for continual learning is a very efficient strategy (parameter-efficient fine-tuning).
