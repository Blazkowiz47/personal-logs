---
aliases: [cnnlbptop_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method]
authors: A. Alotaibi and A. Mahmood
year: 2017
venue: ICB
paper_url: https://ieeexplore.ieee.org/document/7984552
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
- **Backbone:** 5-layer CNN
- **Loss:** Binary CE loss, SVM
- **Input:** RGB
- **Static/Dynamic:** D (Dynamic)

Distinguishing between genuine faces and spoofing attacks (print, replay) using both spatial and temporal information.

1.  **Hybrid Architecture:** Combines CNN for spatial feature extraction with LBP-TOP for dynamic texture analysis.
2.  **Dynamic Texture:** Uses LBP-TOP to capture temporal variations in video sequences.

- **Spatial Stream:** CNN extracts deep features from frames.
- **Temporal Stream:** LBP-TOP extracts dynamic texture features from video blocks.
- **Fusion:** Features are likely fused and classified (possibly with SVM as noted in the template).

- **LBP-TOP:** Local Binary Patterns on Three Orthogonal Planes (XY, XT, YT) to capture motion/texture changes over time.

- Likely CASIA-FAS, Replay-Attack (standard for that time).

## What are my views on it?
- Combining deep learning (CNN) with hand-crafted temporal features (LBP-TOP) was a common and effective strategy before full 3D CNNs or RNNs became dominant.

- The concept of explicitly modeling dynamic texture (micro-motions) is still relevant.
