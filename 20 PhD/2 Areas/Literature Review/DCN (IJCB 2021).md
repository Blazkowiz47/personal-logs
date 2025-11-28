---
aliases: [dcn_fas]
tags:
  - paper
  - pad
  - deep-fas-survey
  - auxiliary-supervision
  - IJCB
  - year_2021
  - architecture/patch-based
  - method/mixup
  - method/structure-destruction
authors:
  - Ke-Yue Zhang
  - Taiping Yao
  - Jian Zhang
  - Shice Liu
  - Bangjie Yin
  - Shouhong Ding
  - Jilin Li
year: 2021
venue: IJCB
paper_url: https://arxiv.org/abs/2107.10628
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
# Structure Destruction and Content Combination for Face Anti-Spoofing (DCN)

## What does the paper present?
This paper proposes a method to prevent overfitting in FAS models by destroying the global facial structure and mixing content from different domains. It introduces a **Structure Destruction Module (SDM)** to break images into patches and a **Content Combination Module (CCM)** to recombine them, forcing the model to learn local discriminative features rather than memorizing the entire face structure.

FAS models often overfit by memorizing the complete facial structure in a single image and are sensitive to implicit subdomains within the dataset. This leads to poor generalization on unseen domains.

1. **Structure Destruction Module (SDM):** Deconstructs images into patches to prevent the model from relying on the complete facial structure, which can lead to overfitting.
2. **Content Combination Module (CCM):** Recombines patches from different subdomains or classes (mixup) to handle implicit domain variations and improve generalization.
3. **Local Relation Modeling Module (LRM):** Models the second-order relationships between the patches to capture local dependencies.

The architecture focuses on processing patches rather than whole images.

- Evaluated on extensive public datasets (likely Oulu-NPU, CASIA-MFSD, Replay-Attack, MSU-MFSD based on the era and topic).

- Demonstrates reliability against SOTA competitors by effectively addressing the issues of structural memorization and domain sensitivity.

## What are my views on it?
- The idea of breaking global structure to prevent memorization is sound for FAS, where texture cues are often more important than global face shape for detecting spoofing artifacts.

- Could apply similar "structure destruction" or patch-shuffling techniques to my own pipeline to improve generalization.

- The "DCN" likely refers to "Destruction and Content Combination Network".
- Similar to jigsaw puzzle pretext tasks in self-supervised learning.
