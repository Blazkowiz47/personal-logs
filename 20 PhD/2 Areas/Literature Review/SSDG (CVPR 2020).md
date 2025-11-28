---
aliases:
  - ssdg_fas
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

> [!abstract]
> Existing domain generalization methods for face anti-spoofing endeavor to extract common differentiation features to improve the generalization. However, due to large distribution discrepancies among fake faces of different domains, it is difficult to seek a compact and generalized feature space for the fake faces. In this work, we propose an end-to-end single-side domain generalization framework (SSDG) to improve the generalization ability of face anti-spoofing. The main idea is to learn a generalized feature space, where the feature distribution of the real faces is compact while that of the fake ones is dispersed among domains but compact within each domain. Specifically, a feature generator is trained to make only the real faces from different domains undistinguishable, but not for the fake ones, thus forming a single-side adversarial learning. Moreover, an asymmetric triplet loss is designed to constrain the fake faces of different domains separated while the real ones aggregated. The above two points are integrated into a unified framework in an end-to-end training manner, resulting in a more generalized class boundary, especially good for samples from novel domains. Feature and weight normalization is incorporated to further improve the generalization ability. Extensive experiments show that our proposed approach is effective and outperforms the state-of-the-art methods on four public databases.

## What does the paper present?
- **Backbone:** ResNet18 (typically)
- **Loss:** Binary CE loss, Single-Side Adversarial Loss, Asymmetric Triplet Loss
- **Input:** RGB
- **Static/Dynamic:** Static

This paper proposes a **Single-Side Domain Generalization (SSDG)** framework. Unlike traditional DG which tries to align all domains (real and fake), SSDG argues that fake faces from different domains have large distribution discrepancies. Therefore, it forces **real faces** to be compact and indistinguishable across domains (single-side alignment), while allowing **fake faces** to be dispersed but compact within their own domains.

Existing DG methods try to extract common features for both real and fake faces across domains. However, "fake" is not a single class; it varies hugely (print, replay, mask, etc.) across datasets. Forcing all fakes to map to the same feature space is difficult and may hurt performance.

1.  **Single-Side Domain Generalization (SSDG):** A framework that aligns only the real faces across domains while treating fakes differently.
2.  **Single-Side Adversarial Learning:** A feature generator is trained to fool a discriminator only on real faces (making them domain-invariant), but not on fake faces.
3.  **Asymmetric Triplet Loss:** Pulls real faces together and pushes fake faces away, but also enforces separation between fakes of different domains if necessary (or just ensures fakes are separated from reals).
4.  **Feature and Weight Normalization:** Used to improve generalization.

- **Generator:** Extracts features.
- **Discriminator:** Tries to distinguish domains, but only for real samples (or the adversarial loss is only applied to reals).
- **Classifier:** Performs the binary real/fake classification.

- **Asymmetric Optimization:** Treating the "live" class (which is consistent) differently from the "spoof" class (which is diverse).

- Outperforms SOTA methods on four public databases in DG protocols (Leave-One-Out).

## What are my views on it?
- The insight that "live faces are all alike; every spoof face is spoof in its own way" (Anna Karenina principle applied to FAS) is very strong and biologically plausible.

- This "one-class" or "asymmetric" thinking is crucial. When designing my own loss functions, I should ensure I'm not forcing all attacks to look the same in feature space.

- Code is released online (need to find the link).
