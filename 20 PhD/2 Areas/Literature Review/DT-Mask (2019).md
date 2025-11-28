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

## Quick Summary
**Method:** DT-Mask (Deep Dynamic Textures)
- **Backbone:** VGG16 (likely)
- **Loss:** Binary CE loss, Channel & Spatial discriminability
- **Input:** RGB + Optical Flow (Dynamic Textures)
- **Static/Dynamic:** D

## Problem Statement
3D mask attacks are challenging because they mimic 3D structure. However, real faces have subtle motion patterns (micro-expressions, blinking) that rigid masks lack.

## Key Contributions
1.  **Deep Dynamic Textures:** Captures subtle facial motion using deep features from video.
2.  **Joint Discriminative Learning:** Weights the discriminability of features from different spatial regions and channels to focus on the most useful motion cues.

## Methodology
### Architecture
- **Input:** Video frames (to capture motion).
- **Feature Learning:** Extracts dynamic textures.

## Experiments
### Datasets Used
- 3D Mask datasets (likely 3DMAD, HKBU-MARs).

## Critical Analysis
### What Works Well
- Motion is the Achilles' heel of rigid mask attacks.

## Relevance to My Work
### Ideas Sparked
- Dynamic texture analysis is a classic computer vision technique that is very relevant for rPPG and liveness detection.
