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

## Quick Summary
**Method:** CNN-LSP (Joint Discriminative Learning of Deep Dynamic Textures)
- **Backbone:** Two-stream CNN
- **Loss:** Discriminative loss
- **Input:** RGB (Spatial + Temporal/Dynamic Texture)
- **Static/Dynamic:** D

## Problem Statement
Detecting 3D mask attacks which have realistic depth and texture, making them harder than 2D attacks.

## Key Contributions
1.  **Deep Dynamic Textures (DDT):** Modeling facial micro-motion as dynamic textures.
2.  **Joint Learning:** Jointly learning spatial and temporal features.
3.  **Discriminative Loss:** Enhancing feature separability.

## Methodology
### Architecture
- **Two-stream CNN:** One for spatial, one for temporal (dynamic texture).

### Key Techniques
- **Dynamic Texture Analysis:** Capturing subtle motion patterns.

## Experiments
### Datasets Used
- 3DMAD
- HKBU-MARs

## Critical Analysis
### What Works Well
- Focusing on micro-motion (dynamic texture) is effective for 3D masks which might be rigid or move differently than real skin.

## Relevance to My Work
### Ideas Sparked
- Dynamic texture analysis is a powerful concept for PAD.
