---
aliases:
  - SSDG
tags:
  - paper
  - FAS
  - CVPR
  - year_2020
  - domain-generalization
  - method/adversarial-learning
  - method/triplet-loss
authors:
  - Yunpei Jia
  - Jie Zhang
  - Shiguang Shan
  - Xilin Chen
year: 2020
venue: CVPR
paper_url: http://arxiv.org/abs/2004.14043
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Single-Side Domain Generalization for Face Anti-Spoofing (SSDG)

## Quick Summary
**Method:** SSDG (Single-Side Domain Generalization)
- **Backbone:** ResNet18 (typically)
- **Loss:** Binary CE loss, Single-Side Adversarial Loss, Asymmetric Triplet Loss
- **Input:** RGB
- **Static/Dynamic:** Static

This paper proposes a **Single-Side Domain Generalization (SSDG)** framework. Unlike traditional DG which tries to align all domains (real and fake), SSDG argues that fake faces from different domains have large distribution discrepancies. Therefore, it forces **real faces** to be compact and indistinguishable across domains (single-side alignment), while allowing **fake faces** to be dispersed but compact within their own domains.

## Problem Statement
Existing DG methods try to extract common features for both real and fake faces across domains. However, "fake" is not a single class; it varies hugely (print, replay, mask, etc.) across datasets. Forcing all fakes to map to the same feature space is difficult and may hurt performance.

## Key Contributions
1.  **Single-Side Domain Generalization (SSDG):** A framework that aligns only the real faces across domains while treating fakes differently.
2.  **Single-Side Adversarial Learning:** A feature generator is trained to fool a discriminator only on real faces (making them domain-invariant), but not on fake faces.
3.  **Asymmetric Triplet Loss:** Pulls real faces together and pushes fake faces away, but also enforces separation between fakes of different domains if necessary (or just ensures fakes are separated from reals).
4.  **Feature and Weight Normalization:** Used to improve generalization.

## Methodology
### Architecture
- **Generator:** Extracts features.
- **Discriminator:** Tries to distinguish domains, but only for real samples (or the adversarial loss is only applied to reals).
- **Classifier:** Performs the binary real/fake classification.

### Key Techniques
- **Asymmetric Optimization:** Treating the "live" class (which is consistent) differently from the "spoof" class (which is diverse).

## Experiments
### Datasets Used
- OULU-NPU
- CASIA-MFSD
- Replay-Attack
- MSU-MFSD

### Results
- Outperforms SOTA methods on four public databases in DG protocols (Leave-One-Out).

## Critical Analysis
### What Works Well
- The insight that "live faces are all alike; every spoof face is spoof in its own way" (Anna Karenina principle applied to FAS) is very strong and biologically plausible.

## Relevance to My Work
### Ideas Sparked
- This "one-class" or "asymmetric" thinking is crucial. When designing my own loss functions, I should ensure I'm not forcing all attacks to look the same in feature space.

## Notes & Highlights
- Code is released online (need to find the link).

