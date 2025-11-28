---
aliases: [contrastiveevt_fas]
tags: [paper, pad, deep-fas-survey, anomaly-detection, open-set]
authors: Xin Dong, Hao Liu, Weiwei Cai, Pengyuan Lv, Zekuan Yu
year: 2021
venue: ACM MM
paper_url: https://dl.acm.org/doi/abs/10.1145/3474085.3475538
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** ContrastiveEVT (OSFA - Open Set Face Anti-Spoofing)
- **Backbone:** Multi-task framework
- **Loss:** Identity-aware Contrastive Loss + EVT-based Open Set Loss
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Standard PAD assumes closed-set attacks. Unseen attacks (Open Set) cause performance degradation. Domain generalization tries to align domains but might fail on unseen attack types.

## Key Contributions
1.  **Open Set Framework:** Formulates FAS as an open set recognition problem.
2.  **Extreme Value Theory (EVT):** Uses EVT to model the tail distribution of known classes to detect outliers (unseen attacks).
3.  **Identity-Aware Contrastive Learning:** Prevents confusion between unseen attacks and hard examples (e.g., same identity).

## Methodology
### Architecture
- **Multi-task:** Parallel branches for known class classification and unseen attack detection.

### Key Techniques
- **EVT:** Statistical modeling of extreme values (outliers).
- **Contrastive Learning:** For compact representations.

## Experiments
### Datasets Used
- Four datasets (likely OULU, CASIA, Replay, SiW).

## Critical Analysis
### What Works Well
- EVT is a classic tool for open set recognition, applied here to PAD.

## Relevance to My Work
### Ideas Sparked
- Open set recognition is the realistic setting for PAD.
