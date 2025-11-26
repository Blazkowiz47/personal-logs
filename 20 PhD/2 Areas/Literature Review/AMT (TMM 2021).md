---
aliases:
  - AMT
tags:
  - paper
  - FAS
  - TMM
  - year_2021
  - multimodal
  - method/modality-translation
  - method/gan
authors:
  - Zhi Li
  - Haoliang Li
  - Xin Luo
  - Yongjian Hu
  - Kwok-Yan Lam
  - Alex C. Kot
year: 2021
venue: TMM
paper_url: https://arxiv.org/abs/2110.09108
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

# Asymmetric Modality Translation For Face Presentation Attack Detection (AMT)

## Quick Summary
**Method:** AMT (Asymmetric Modality Translation)
- **Backbone:** Translator (Encoder-Decoder) + Discriminator
- **Loss:** BCE loss, Pixel-wise binary loss, Reconstruction loss, Asymmetric Modality Translation Loss
- **Input:** RGB + (NIR / Thermal / Depth)
- **Fusion:** Feature/Image level (via translation)

This paper proposes a framework based on **Asymmetric Modality Translation** for bi-modality FAS. It translates images from one modality (e.g., RGB) to another (e.g., Depth or IR) using an asymmetric translator, and then fuses them. It also introduces an **Illumination Normalization Module** based on **Pattern of Local Gravitational Force (PLGF)**.

## Problem Statement
Generalization across domains (especially varying illumination) is difficult. Existing multi-modal methods might not fully exploit the relationship between modalities or handle missing modalities well.

## Key Contributions
1.  **Asymmetric Modality Translation:** Translating one modality to another to establish connections and potentially fill in missing information.
2.  **Modality Fusion Scheme:** Fusing the translated modality with the original paired image.
3.  **Illumination Normalization (PLGF):** A preprocessing step to reduce the impact of lighting variations.

## Methodology
### Architecture
- **Translator:** An asymmetric encoder-decoder structure.
- **Fusion:** Combining the real and "hallucinated" or translated modality.

### Key Techniques
- **Generative Translation:** Similar to CycleGAN or Pix2Pix but tailored for FAS.
- **PLGF:** A specific handcrafted feature for illumination invariance.

## Experiments
### Datasets Used
- Validated on three public datasets (likely CASIA-SURF, OULU-NPU, etc.).

### Results
- Effective in detecting various attacks and robust to illumination changes.

## Critical Analysis
### What Works Well
- Modality translation is a clever way to do "data augmentation" or "domain adaptation". If you can translate RGB to Depth accurately for live faces but fail for spoof faces (because spoofs don't have depth), the translation error itself becomes a spoof cue.

## Relevance to My Work
### Ideas Sparked
- The idea of "translation error as a feature" is powerful. If I train a model to predict Depth from RGB, it should fail on a photo attack.

## Notes & Highlights
- Published in IEEE Transactions on Multimedia (TMM).

