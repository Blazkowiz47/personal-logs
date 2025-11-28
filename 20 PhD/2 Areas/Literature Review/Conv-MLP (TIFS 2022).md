---
aliases: [convmlp_fas]
tags: [paper, pad, deep-fas-survey, multimodal, architecture]
authors: Weihang Wang, Fei Wen, Haoyuan Zheng, Rendong Ying, Peilin Liu
year: TIFS 2022
venue: TIFS
paper_url: https://ieeexplore.ieee.org/document/9796574
code_url: https://github.com/WeihangWANG/Conv-MLP
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
CNNs are good at local features but struggle with long-range dependencies. Pure MLPs/Transformers are heavy. Need a balance.

1.  **Conv-MLP Architecture:** Combines local patch convolution (for local features) with global MLPs (for long-range dependencies).
2.  **Moat Loss:** A new loss function to improve discriminative representation learning and generalization.
3.  **Signal-Level Fusion:** Direct fusion of multi-modal data.

- Single and Multi-modal datasets.

## What are my views on it?
- Hybrid architectures (Conv + MLP/Transformer) are the current trend for efficiency + performance.

- Efficient backbones are crucial. The "Moat Loss" sounds interesting to investigate.
