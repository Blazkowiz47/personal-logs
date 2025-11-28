---
aliases: [dsdg_dum_fas]
tags: [paper, pad, deep-fas-survey, generative-model, disentanglement]
authors: Hangtong Wu, Dan Zeng, Yibo Hu, Hailin Shi, Tao Mei
year: TIFS 2021
venue: TIFS
paper_url: https://arxiv.org/abs/2112.00568
code_url: https://github.com/JDAI-CV/FaceX-Zoo/tree/main/addition_module/DSDG
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** DSDG+DUM (Dual Spoof Disentanglement Generation + Depth Uncertainty Module)
- **Supervision:** Depth
- **Backbone:** CDCN (likely)
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Existing FAS datasets lack diversity (insufficient identities and variances), limiting generalization.

## Key Contributions
1.  **DSDG (Dual Spoof Disentanglement Generation):** Uses a VAE to disentangle identity and spoofing patterns, allowing generation of large-scale paired live/spoof images to boost diversity.
2.  **DUM (Depth Uncertainty Module):** Handles noisy generated samples (distorted faces) by estimating depth uncertainty, preventing them from harming the training.

## Methodology
### Architecture
- **VAE:** For disentanglement and generation.
- **DUM:** Lightweight module to estimate uncertainty in depth predictions.

## Experiments
### Datasets Used
- Standard benchmarks.

## Critical Analysis
### What Works Well
- "Anti-spoofing via generation" is a smart way to solve the data scarcity problem.
- Handling the quality of generated data (via uncertainty) is a crucial detail often overlooked.

## Relevance to My Work
### Ideas Sparked
- Generating synthetic attacks is a very active area. The uncertainty module is a good trick to borrow when dealing with noisy labels or data.
