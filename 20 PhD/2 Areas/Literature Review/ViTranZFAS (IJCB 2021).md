---
aliases: [vitranzfas]
tags: [paper, pad, deep-fas-survey, zero-shot, vit]
authors: Anjith George, Sebastien Marcel
year: 2021
venue: IEEE IJCB 2021
paper_url: https://arxiv.org/abs/2011.08019
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

## Quick Summary
**Method:** ViTranZFAS
- **Supervision:** Binary CE loss
- **Backbone:** ViT
- **Input:** RGB
- **Static/Dynamic:** S

This paper investigates the effectiveness of Vision Transformers (ViT) for the task of zero-shot face anti-spoofing. By leveraging transfer learning from a pre-trained ViT, the authors demonstrate that transformers can generalize better to unseen attacks compared to CNN-based methods, achieving state-of-the-art results on HQ-WMCA and SiW-M datasets.

## Problem Statement
Face recognition systems are vulnerable to presentation attacks (spoofing). Existing CNN-based methods often overfit to the training attacks and fail to generalize to unseen attack types (zero-shot scenarios) or new environments (cross-database).

## Key Contributions
1.  First work to explore Vision Transformers (ViT) for the specific task of Zero-Shot Face Anti-Spoofing.
2.  Demonstrates that ViT architectures generalize significantly better to unseen attacks than traditional CNNs (like ResNet).
3.  Achieves state-of-the-art performance on challenging zero-shot protocols in HQ-WMCA and SiW-M datasets.

## Methodology
### Architecture
-   **Backbone:** Vision Transformer (ViT-Base/16) pre-trained on ImageNet-21k.
-   **Input:** RGB face images resized to 224x224.
-   **Approach:** Fine-tuning the pre-trained ViT for the binary classification task (Bonafide vs. Attack).

### Key Techniques
-   **Transfer Learning:** Leveraging the rich semantic features learned by ViT on large-scale datasets to improve generalization for FAS.
-   **Attention Mechanism:** The self-attention mechanism in transformers allows the model to capture global dependencies and subtle artifacts that might be missed by the local receptive fields of CNNs.

## Experiments
### Datasets Used
-   **HQ-WMCA:** High-Quality Wide Multi-Channel Attack dataset.
-   **SiW-M:** Spoof in the Wild with Multiple Attacks.

### Results
-   **Zero-Shot Performance:** Outperforms CNN baselines (ResNet, DeepPixBiS) by a large margin on unseen attack protocols.
-   **Cross-Database:** Shows significant improvement in cross-database testing, indicating better domain generalization.

## Critical Analysis
### What Works Well
-   The use of ViT for generalization is well-motivated and empirically supported.
-   Simple yet effective approach (fine-tuning) that establishes a strong baseline for transformer-based FAS.

### Missing Pieces
-   Does not explicitly design a specialized loss function for FAS (uses standard Binary CE), relying purely on the architecture's strength.

## Relevance to My Work
-   **Direct Application:** Strong baseline for any zero-shot or domain generalization experiments.
-   **Ideas Sparked:** Can we combine the global attention of ViT with local features (like in `FMF-Inspired architecture`) to get the best of both worlds?
