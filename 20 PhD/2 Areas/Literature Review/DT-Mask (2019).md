---
aliases: [dt_mask_fas]
tags: [paper, pad, deep-fas-survey, 3d-mask, dynamic-texture]
authors: Rui Shao, Xiangyuan Lan, Pong C. Yuen
year: TIFS 2019
venue: TIFS
paper_url: https://ieeexplore.ieee.org/document/8453011
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
3D mask attacks are challenging because they mimic 3D structure. However, real faces have subtle motion patterns (micro-expressions, blinking) that rigid masks lack.

1.  **Deep Dynamic Textures:** Captures subtle facial motion using deep features from video.
2.  **Joint Discriminative Learning:** Weights the discriminability of features from different spatial regions and channels to focus on the most useful motion cues.

- 3D Mask datasets (likely 3DMAD, HKBU-MARs).

## What are my views on it?
- Motion is the Achilles' heel of rigid mask attacks.

- Dynamic texture analysis is a classic computer vision technique that is very relevant for rPPG and liveness detection.
