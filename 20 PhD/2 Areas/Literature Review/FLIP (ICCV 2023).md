---
aliases:
  - flip_fas
  - flip-fas
  - FLIP-FAS
tags:
  - paper
  - pad
  - to-read
authors:
  - Koushik Srivatsan
  - Muzammal Naseer
  - Karthik Nandakumar
year: 2023
venue: ICCV
paper_url: https://arxiv.org/pdf/2309.16649
code_url: https://github.com/koushiksrivats/FLIP
status: 📚 To Read
dateadded: 2025-11-28
dateread:
priority: medium
---
## What does the paper present?
Uses CLIP pretrained weights and perform finetuning.

1. We show that direct finetuning of a multimodal pre-trained ViT (e.g., CLIP image encoder) achieves better FAS generalizability without any bells and whistles.
2. We propose a new approach for robust cross-domain FAS by grounding the visual representation using natural language semantics. This is realized by aligning the image representation with an ensemble of text prompts (describing the class) during finetuning.
3. We propose a multimodal contrastive learning strategy, which enforces the model to learn more generalized features that bridge the FAS domain gap even with limited training data. This strategy leverages view-based image self-supervision and view-based cross-modal image-text similarity as additional constraints during the learning process.
4. Extensive experiments on three standard protocols demonstrate that our method significantly outperforms the state- of-the-art methods, achieving better zero-shot transfer performance than five-shot transfer of “adaptive ViTs”.

## What are my views on it?
