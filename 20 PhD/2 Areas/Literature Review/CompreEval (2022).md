---
aliases: [compreeval_fas]
tags: [paper, pad, deep-fas-survey, multimodal, benchmark]
authors: Anjith George, David Geissbuhler, Sebastien Marcel
year: 2022
venue: arXiv
paper_url: https://arxiv.org/abs/2202.10286
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** CompreEval (Comprehensive Evaluation)
- **Backbone:** MC-PixBiS (Multi-Channel Pixel-wise Binary Supervision)
- **Loss:** BCE + Pixel-wise Loss
- **Input:** RGB, Depth, NIR, SWIR, Thermal (14 modalities total)
- **Fusion:** Input-level / Model-level

## Problem Statement
Lack of understanding of which sensors (modalities) are most effective for PAD against various attacks. High cost of multi-sensor systems requires optimal selection.

## Key Contributions
1.  **Large-Scale Evaluation:** Evaluates 14 different sensing modalities (RGB, NIR, SWIR, Depth, Thermal, etc.).
2.  **Dataset:** Uses a multi-channel PAD dataset (likely HQ-WMCA or similar internal dataset).
3.  **Analysis:** Provides pointers for sensor selection based on performance against 2D, 3D, and partial attacks.

## Methodology
### Architecture
- **MC-PixBiS:** A multi-channel version of PixBiS.

### Key Techniques
- **Multi-modal Analysis:** Systematic ablation of channels.

## Experiments
### Datasets Used
- Multi-channel PAD dataset (likely HQ-WMCA).

## Critical Analysis
### What Works Well
- Essential reference for anyone building hardware for PAD. SWIR and Thermal are often highlighted as robust.

## Relevance to My Work
### Ideas Sparked
- If I have access to SWIR/Thermal data, I should use it. If not, I should know the limitations of RGB-only.
