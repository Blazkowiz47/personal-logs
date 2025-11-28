---
aliases: [compactnet_fas]
tags: [paper, pad, deep-fas-survey, binary-supervision]
authors: Lei Li, Zhaoqiang Xia, Xiaoyue Jiang, Fabio Roli, Xiaoyi Feng
year: 2020
venue: Neurocomputing
paper_url: https://www.sciencedirect.com/science/article/pii/S0925231220308237
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** CompactNet
- **Backbone:** VGG19 (Feature Extractor)
- **Loss:** Points-to-Center Triplet Loss
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Standard color spaces (RGB, HSV) are designed for display, not discrimination. Existing features might not be compact enough for PAD.

## Key Contributions
1.  **Compact Space Learning:** Proposes a "progressive space generator" to learn a compact feature space tailored for PAD.
2.  **Points-to-Center Triplet Loss:** A loss function to minimize intra-class distance and maximize inter-class distance with a margin.

## Methodology
### Architecture
- **Generator:** Layer-by-layer transformation to a compact space.
- **Feature Extractor:** Pre-trained model extracts features from this compact space.

### Key Techniques
- **Metric Learning:** Optimizing the feature space directly.

## Experiments
### Datasets Used
- Replay-Attack
- OULU-NPU
- HKBU-MARs V1

## Critical Analysis
### What Works Well
- Learning a task-specific color/feature space is a valid approach, similar to learning a color transformation.

## Relevance to My Work
### Ideas Sparked
- Feature space compactness is key for generalization.
