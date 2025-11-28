---
aliases:
  - dc_cdn_fas
tags:
  - paper
  - FAS
  - IJCAI
  - year_2021
  - architecture/CDC
  - method/augmentation
authors:
  - Zitong Yu
  - Yunxiao Qin
  - Hengshuang Zhao
  - Xiaobai Li
  - Guoying Zhao
year: 2021
venue: IJCAI
paper_url: https://arxiv.org/abs/2105.01290
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
# Dual-Cross Central Difference Network for Face Anti-Spoofing (DC-CDN)

## What does the paper present?
This paper improves upon the Central Difference Convolution (CDC) by proposing **Cross Central Difference Convolutions (C-CDC)**, which decouple the difference calculation into horizontal/vertical and diagonal directions to reduce redundancy. It builds a **Dual-Cross Central Difference Network (DC-CDN)** and introduces a **Patch Exchange (PE)** augmentation strategy.

The original CDC aggregates central difference clues from all neighbors simultaneously, which can be redundant and sub-optimized. There is a need for a more efficient and robust way to capture local detailed features.

1.  **Cross Central Difference Convolutions (C-CDC):** Decouples the local gradient calculation into two separate components (horizontal/vertical and diagonal), reducing parameters and computational cost while improving performance.
2.  **Dual-Cross Central Difference Network (DC-CDN):** A network architecture based on C-CDC.
3.  **Cross Feature Interaction Modules (CFIM):** Used for mutual relation mining and enhancing local detailed representations.
4.  **Patch Exchange (PE) Augmentation:** A simple yet effective strategy that exchanges face patches and their dense labels between random samples to create diverse domain distributions and richer patterns.

- State-of-the-art performance on the tested benchmarks.
- C-CDC outperforms full directional CDC with fewer parameters.

## What are my views on it?
- The Patch Exchange augmentation is a very clever and simple way to increase data diversity without complex generative models. It forces the model to look at local patches rather than global context, which is good for FAS.

- Code likely available (check Zitong Yu's GitHub).
