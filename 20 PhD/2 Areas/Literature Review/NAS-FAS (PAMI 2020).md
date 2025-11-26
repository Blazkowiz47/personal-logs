---
aliases:
  - NAS-FAS
tags:
  - paper
  - FAS
  - PAMI
  - year_2020
  - method/NAS
  - architecture/CDC
  - dataset/CASIA-SURF-3DMask
authors:
  - Zitong Yu
  - Jun Wan
  - Yunxiao Qin
  - Xiaobai Li
  - Stan Z. Li
  - Guoying Zhao
year: 2020
venue: TPAMI
paper_url: https://arxiv.org/abs/2011.02062
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---

> [!abstract]
> Face anti-spoofing (FAS) plays a vital role in securing face recognition systems. Existing methods heavily rely on the expert-designed networks, which may lead to a sub-optimal solution for FAS task. Here we propose the first FAS method based on neural architecture search (NAS), called NAS-FAS, to discover the well-suited task-aware networks. Unlike previous NAS works mainly focus on developing efficient search strategies in generic object classification, we pay more attention to study the search spaces for FAS task. The challenges of utilizing NAS for FAS are in two folds: the networks searched on 1) a specific acquisition condition might perform poorly in unseen conditions, and 2) particular spoofing attacks might generalize badly for unseen attacks. To overcome these two issues, we develop a novel search space consisting of central difference convolution and pooling operators. Moreover, an efficient static-dynamic representation is exploited for fully mining the FAS-aware spatio-temporal discrepancy. Besides, we propose Domain/Type-aware Meta-NAS, which leverages cross-domain/type knowledge for robust searching. Finally, in order to evaluate the NAS transferability for cross datasets and unknown attack types, we release a large-scale 3D mask dataset, namely CASIA-SURF 3DMask, for supporting the new 'cross-dataset cross-type' testing protocol. Experiments demonstrate that the proposed NAS-FAS achieves state-of-the-art performance on nine FAS benchmark datasets with four testing protocols.

# NAS-FAS: Static-Dynamic Central Difference Network Search for Face Anti-Spoofing

## Quick Summary
**Method:** NAS-FAS
- **Supervision:** Depth, Binary Mask
- **Backbone:** NAS-searched (based on CDC)
- **Input:** RGB (Static and Dynamic)
- **Static/Dynamic:** Static-Dynamic

This paper proposes **NAS-FAS**, the first method to use **Neural Architecture Search (NAS)** to discover task-aware networks for FAS. It introduces a novel search space based on **Central Difference Convolution (CDC)** and pooling operators. It also proposes a **Static-Dynamic Representation** to mine spatio-temporal discrepancies and a **Domain/Type-aware Meta-NAS** for robust searching.

## Problem Statement
Expert-designed networks may be sub-optimal for FAS. Existing NAS methods focus on generic classification and don't address the specific challenges of FAS:
1.  Generalization to unseen acquisition conditions (domains).
2.  Generalization to unseen attack types.

## Key Contributions
1.  **NAS-FAS:** The first NAS-based approach for FAS.
2.  **CDC Search Space:** A search space tailored for FAS using Central Difference Convolutions.
3.  **Static-Dynamic Representation:** Exploiting both static (spatial) and dynamic (temporal) cues efficiently.
4.  **Domain/Type-aware Meta-NAS:** A meta-learning approach to guide the search process for better generalization.
5.  **CASIA-SURF 3DMask Dataset:** A large-scale 3D mask dataset released to support a new "cross-dataset cross-type" testing protocol.

## Methodology
### Architecture
- **Search Space:** Includes various CDC operations (different kernel sizes, sparsity) and pooling.
- **Meta-NAS:** Uses meta-learning to find an architecture that adapts well to new domains/types.

### Key Techniques
- **Neural Architecture Search:** Automating the design of the backbone.
- **Meta-Learning:** Improving the search process itself.

## Experiments
### Datasets Used
- OULU-NPU
- SiW
- CASIA-MFSD
- Replay-Attack
- CASIA-SURF 3DMask (New)
- ... (9 datasets total)

### Results
- State-of-the-art performance on nine benchmark datasets.

## Critical Analysis
### What Works Well
- The combination of NAS with a domain-specific operator (CDC) is very powerful. It avoids the "black box" nature of generic NAS by constraining it to operations known to work well for texture/gradients.

## Relevance to My Work
### Ideas Sparked
- The "Static-Dynamic" representation is interesting. How do they combine them? Is it just two branches?
- The new 3D Mask dataset is a valuable resource if I focus on mask attacks.

## Notes & Highlights
- Published in TPAMI (IEEE Transactions on Pattern Analysis and Machine Intelligence), which is a top-tier journal.

