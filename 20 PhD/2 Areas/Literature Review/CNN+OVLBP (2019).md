---
aliases: [cnnovlbp_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method]
authors: Omid Sharifi
year: 2019
venue: IJIGSP
paper_url: http://www.mecs-press.org/ijigsp/ijigsp-v11-n2/IJIGSP-V11-N2-2.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** CNN+OVLBP
- **Backbone:** CNN (Pre-trained) + OVLBP (Handcrafted)
- **Loss:** Score-level fusion
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Improving PAD performance by combining the strengths of deep learning (semantic features) and handcrafted descriptors (micro-texture).

## Key Contributions
1.  **Score-Level Fusion:** Fusing scores from a CNN and an OVLBP-based classifier.
2.  **OVLBP:** Using Overlapped Local Binary Patterns for texture analysis.

## Methodology
### Architecture
- **Stream 1:** OVLBP feature extraction -> Classifier.
- **Stream 2:** Pre-trained CNN -> Classifier.
- **Fusion:** Weighted sum of scores.

### Key Techniques
- **OVLBP:** A variant of LBP.

## Experiments
### Datasets Used
- CASIA-FASD
- Replay-Attack

## Critical Analysis
### What Works Well
- Fusion of complementary features is a robust strategy.

## Relevance to My Work
### Ideas Sparked
- Hybrid methods are good baselines.
