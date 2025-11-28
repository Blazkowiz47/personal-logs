---
aliases: [cnnlsp_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method]
authors: Rui Shao, Xiangyuan Lan, Pong C. Yuen
year: TIFS 2019
venue: TIFS
paper_url: https://ieeexplore.ieee.org/document/8626161
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
- **Backbone:** Two-stream CNN
- **Loss:** Discriminative loss
- **Input:** RGB (Spatial + Temporal/Dynamic Texture)
- **Static/Dynamic:** D

Detecting 3D mask attacks which have realistic depth and texture, making them harder than 2D attacks.

1.  **Deep Dynamic Textures (DDT):** Modeling facial micro-motion as dynamic textures.
2.  **Joint Learning:** Jointly learning spatial and temporal features.
3.  **Discriminative Loss:** Enhancing feature separability.

- **Two-stream CNN:** One for spatial, one for temporal (dynamic texture).

- **Dynamic Texture Analysis:** Capturing subtle motion patterns.

- 3DMAD

## What are my views on it?
- Focusing on micro-motion (dynamic texture) is effective for 3D masks which might be rigid or move differently than real skin.

- Dynamic texture analysis is a powerful concept for PAD.
