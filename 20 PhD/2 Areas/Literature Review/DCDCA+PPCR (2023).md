---
aliases: [dcdca_ppcr_fas]
tags: [paper, pad, deep-fas-survey, continual-learning, domain-generalization]
authors: Rizhao Cai, Yawen Cui, Zhi Li, Zitong Yu, Haoliang Li, Yongjian Hu, Alex Kot
year: 2023
venue: arXiv
paper_url: https://arxiv.org/abs/2303.09914
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
Continual learning in FAS usually requires replay buffers (storing old data), which is a privacy risk. Existing methods suffer from catastrophic forgetting without replay.

1.  **Rehearsal-Free DCL:** First method for Domain Continual Learning (DCL) in FAS without storing previous data.
2.  **DCDCA (Dynamic Central Difference Convolutional Adapter):** Adapts ViT models to new domains efficiently.
3.  **PPCR (Proxy Prototype Contrastive Regularization):** Constrains learning using proxy prototypes to prevent forgetting previous domain knowledge.

- Standard cross-domain benchmarks in a sequential setting.

## What are my views on it?
- Rehearsal-free methods are the future for privacy-sensitive applications like Face ID.

- Using adapters for continual learning is a very efficient strategy (parameter-efficient fine-tuning).
