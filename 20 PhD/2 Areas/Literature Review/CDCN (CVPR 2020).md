---
aliases:
  - cdcn_fas
tags:
  - paper
  - FAS
  - CVPR
  - year_2020
  - architecture/CDC
  - method/NAS
authors:
  - Zitong Yu
  - Chenxu Zhao
  - Zezheng Wang
  - Yunxiao Qin
  - Zhuo Su
  - Xiaobai Li
  - Feng Zhou
  - Guoying Zhao
year: 2020
venue: CVPR
paper_url: https://arxiv.org/abs/2003.04092
code_url: https://github.com/ZitongYu/CDCN
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: high
---
# Searching Central Difference Convolutional Networks for Face Anti-Spoofing (CDCN)

## What does the paper present?
- **Supervision:** Depth, Binary Mask
- **Backbone:** CDCN (Custom based on CDC)
- **Input:** RGB
- **Static/Dynamic:** Static (Frame-level)

This paper introduces **Central Difference Convolution (CDC)**, a novel convolution operator that captures intrinsic detailed patterns by aggregating both intensity and gradient information. It proposes **CDCN** built with CDC and uses **Neural Architecture Search (NAS)** to discover a more powerful version, **CDCN++**, which also incorporates a **Multiscale Attention Fusion Module (MAFM)**.

Standard convolutions are weak in describing detailed fine-grained information (spoofing patterns) and are invariant to changes that might be important for FAS. Existing methods often rely on expert-designed networks or long sequences (dynamic features) which are slow.

1.  **Central Difference Convolution (CDC):** A new convolution operation that combines standard intensity-level convolution with gradient-level difference information to better capture spoofing artifacts.
2.  **CDCN & CDCN++:** A network architecture built using CDC. CDCN++ is an enhanced version discovered via Neural Architecture Search (NAS).
3.  **Multiscale Attention Fusion Module (MAFM):** A module to fuse features from different levels effectively.
4.  **Robustness:** Achieves state-of-the-art performance on intra-dataset and cross-dataset protocols (OULU-NPU, CASIA-MFSD, Replay-Attack).

- **CDC:** Replaces vanilla convolutions. It calculates the difference between the center pixel and its neighbors, combining it with the intensity value.
- **CDCN:** A deep network constructed by stacking CDC blocks.
- **CDCN++:** An optimized architecture found using NAS in a search space designed for CDC.

- **Gradient-based Features:** Explicitly modeling local gradients within the convolution operation.
- **NAS for FAS:** Automating the design of the backbone specifically for anti-spoofing tasks.

- **OULU-NPU:** 0.2% ACER in Protocol-1.
- **Cross-Dataset:** 6.5% HTER from CASIA-MFSD to Replay-Attack.

## What are my views on it?
- The CDC operator is a very intuitive and effective way to incorporate "texture" or "noise" information which is crucial for FAS, without needing separate preprocessing (like LBP).

- Can I replace standard convolutions in other backbones (like ResNet or ViT patch embeddings) with CDC-like operations?
- The idea of "intrinsic detailed patterns" aligns with my interest in frequency domain or noise-based features.

- Code is available at: https://github.com/ZitongYu/CDCN
