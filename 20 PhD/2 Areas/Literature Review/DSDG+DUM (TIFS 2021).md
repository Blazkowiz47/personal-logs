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
## What does the paper present?
Existing FAS datasets lack diversity (insufficient identities and variances), limiting generalization.

1.  **DSDG (Dual Spoof Disentanglement Generation):** Uses a VAE to disentangle identity and spoofing patterns, allowing generation of large-scale paired live/spoof images to boost diversity.
2.  **DUM (Depth Uncertainty Module):** Handles noisy generated samples (distorted faces) by estimating depth uncertainty, preventing them from harming the training.

- Standard benchmarks.

## What are my views on it?
- "Anti-spoofing via generation" is a smart way to solve the data scarcity problem.
- Handling the quality of generated data (via uncertainty) is a crucial detail often overlooked.

- Generating synthetic attacks is a very active area. The uncertainty module is a good trick to borrow when dealing with noisy labels or data.
