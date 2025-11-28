---
aliases: [df_mslbp_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method, deep-forest]
authors: Rizhao Cai, Changsheng Chen
year: 2018
venue: PRL (Submitted) / arXiv
paper_url: https://arxiv.org/abs/1910.03850
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** DF-MSLBP (Deep Forest with Multi-scale LBP)
- **Backbone:** Deep Forest (gcForest)
- **Loss:** N/A (Decision Tree based)
- **Input:** HSV+YCbCr (LBP features)
- **Static/Dynamic:** S

## Problem Statement
CNNs are vulnerable to adversarial attacks. Handcrafted features combined with non-differentiable models (like Random Forests) might be more robust.

## Key Contributions
1.  **Deep Forest for FAS:** First attempt to use Deep Forest (gcForest) for Face Anti-Spoofing.
2.  **Multi-scale LBP:** Replaces the standard scanning mechanism in gcForest with MS-LBP for better texture capture.

## Methodology
### Architecture
- **gcForest:** A deep learning model based on decision trees (random forests) rather than neurons.
- **Feature Extraction:** Multi-scale LBP on HSV and YCbCr color spaces.

## Experiments
### Datasets Used
- Replay-Attack (0% EER reported).

## Critical Analysis
### What Works Well
- Exploring non-CNN deep models is interesting for security/robustness against gradients-based attacks.

## Relevance to My Work
### Ideas Sparked
- Adversarial robustness is a key angle. Non-differentiable components can block gradient flow for attackers.
