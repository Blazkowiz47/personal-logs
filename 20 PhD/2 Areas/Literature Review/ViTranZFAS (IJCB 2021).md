aliases: [vitranz_fas]
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
## What does the paper present?
This paper investigates the effectiveness of Vision Transformers (ViT) for the task of zero-shot face anti-spoofing. By leveraging transfer learning from a pre-trained ViT, the authors demonstrate that transformers can generalize better to unseen attacks compared to CNN-based methods, achieving state-of-the-art results on HQ-WMCA and SiW-M datasets.

Face recognition systems are vulnerable to presentation attacks (spoofing). Existing CNN-based methods often overfit to the training attacks and fail to generalize to unseen attack types (zero-shot scenarios) or new environments (cross-database).

1.  First work to explore Vision Transformers (ViT) for the specific task of Zero-Shot Face Anti-Spoofing.
2.  Demonstrates that ViT architectures generalize significantly better to unseen attacks than traditional CNNs (like ResNet).
3.  Achieves state-of-the-art performance on challenging zero-shot protocols in HQ-WMCA and SiW-M datasets.

## What are my views on it?
-   The use of ViT for generalization is well-motivated and empirically supported.
-   Simple yet effective approach (fine-tuning) that establishes a strong baseline for transformer-based FAS.

-   Does not explicitly design a specialized loss function for FAS (uses standard Binary CE), relying purely on the architecture's strength.
