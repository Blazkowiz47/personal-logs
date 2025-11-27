---
aliases: [cnnlbptop_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method]
authors: A. Alotaibi and A. Mahmood
year: 2017
venue: ICB
paper_url: https://ieeexplore.ieee.org/document/7984552
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** CNN LBP-TOP
- **Backbone:** 5-layer CNN
- **Loss:** Binary CE loss, SVM
- **Input:** RGB
- **Static/Dynamic:** D (Dynamic)

## Problem Statement
Distinguishing between genuine faces and spoofing attacks (print, replay) using both spatial and temporal information.

## Key Contributions
1.  **Hybrid Architecture:** Combines CNN for spatial feature extraction with LBP-TOP for dynamic texture analysis.
2.  **Dynamic Texture:** Uses LBP-TOP to capture temporal variations in video sequences.

## Methodology
### Architecture
- **Spatial Stream:** CNN extracts deep features from frames.
- **Temporal Stream:** LBP-TOP extracts dynamic texture features from video blocks.
- **Fusion:** Features are likely fused and classified (possibly with SVM as noted in the template).

### Key Techniques
- **LBP-TOP:** Local Binary Patterns on Three Orthogonal Planes (XY, XT, YT) to capture motion/texture changes over time.

## Experiments
### Datasets Used
- Likely CASIA-FAS, Replay-Attack (standard for that time).

## Critical Analysis
### What Works Well
- Combining deep learning (CNN) with hand-crafted temporal features (LBP-TOP) was a common and effective strategy before full 3D CNNs or RNNs became dominant.

## Relevance to My Work
### Ideas Sparked
- The concept of explicitly modeling dynamic texture (micro-motions) is still relevant.
