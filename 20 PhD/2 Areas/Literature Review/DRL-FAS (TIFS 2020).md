---
aliases: [drl_fas]
tags: [paper, pad, deep-fas-survey, reinforcement-learning, attention]
authors: Rizhao Cai, Haoliang Li, Shiqi Wang, Changsheng Chen, Alex Chichung Kot
year: TIFS 2020
venue: TIFS
paper_url: https://ieeexplore.ieee.org/document/9205636
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
Humans glance globally first, then focus on local regions to detect spoofing. Standard CNNs process the whole image at once or use fixed patches.

1.  **RL-based Attention:** Uses Deep Reinforcement Learning to sequentially explore local patches that are most discriminative for spoofing.
2.  **Recurrent Mechanism:** An RNN aggregates information from the sequence of explored patches.
3.  **Global-Local Fusion:** Fuses global image features with the sequentially learned local features.

- Standard benchmarks.

## What are my views on it?
- Mimicking human visual attention (saccades) is a biologically plausible way to improve efficiency and accuracy.

- Sequential attention could be useful for video-based PAD, selecting key frames or regions.
