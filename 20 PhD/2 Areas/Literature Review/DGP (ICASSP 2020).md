---
aliases: [dgp_fas]
tags: [paper, pad, deep-fas-survey, domain-adaptation]
authors: Amir Mohammadi, Sushil Bhattacharjee, Sébastien Marcel
year: ICASSP 2020
venue: ICASSP
paper_url: https://ieeexplore.ieee.org/document/9053685
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** DGP (Domain Guided Pruning)
- **Backbone:** DenseNet161
- **Loss:** Feature divergence measure, BinaryMask loss
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
PAD systems fail to generalize to new domains (datasets). Collecting PA data in the target domain is difficult/expensive.

## Key Contributions
1.  **One-Class Domain Adaptation:** Adapts to a target domain using only bona fide samples (minimal information).
2.  **Domain Guided Pruning:** Prunes the network to adapt it to the target domain.

## Methodology
### Architecture
- **Backbone:** DenseNet161.
- **Pruning:** Adapts the network by pruning filters that are not useful for the target domain.

## Experiments
### Datasets Used
- Cross-dataset evaluations.

## Critical Analysis
### What Works Well
- One-class adaptation is very practical because getting real face data is easy, but getting spoof data for a specific new environment is hard.

## Relevance to My Work
### Ideas Sparked
- Pruning as an adaptation mechanism is an interesting alternative to fine-tuning.
