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

## Quick Summary
**Method:** Conv-MLP
- **Backbone:** Hybrid (Conv + MLP)
- **Loss:** Binary CE Loss, Moat Loss
- **Input:** RGB, Depth, NIR
- **Fusion:** Input-level (Signal-level)

## Problem Statement
CNNs are good at local features but struggle with long-range dependencies. Pure MLPs/Transformers are heavy. Need a balance.

## Key Contributions
1.  **Conv-MLP Architecture:** Combines local patch convolution (for local features) with global MLPs (for long-range dependencies).
2.  **Moat Loss:** A new loss function to improve discriminative representation learning and generalization.
3.  **Signal-Level Fusion:** Direct fusion of multi-modal data.

## Methodology
### Architecture
- **Local Branch:** Convolutional layers.
- **Global Branch:** MLP layers.

### Key Techniques
- **Moat Loss:** Likely a margin-based loss.

## Experiments
### Datasets Used
- Single and Multi-modal datasets.

## Critical Analysis
### What Works Well
- Hybrid architectures (Conv + MLP/Transformer) are the current trend for efficiency + performance.

## Relevance to My Work
### Ideas Sparked
- Efficient backbones are crucial. The "Moat Loss" sounds interesting to investigate.
