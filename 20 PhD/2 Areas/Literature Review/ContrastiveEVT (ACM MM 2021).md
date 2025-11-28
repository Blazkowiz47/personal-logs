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
## What does the paper present?
- **Backbone:** Multi-task framework
- **Loss:** Identity-aware Contrastive Loss + EVT-based Open Set Loss
- **Input:** RGB
- **Static/Dynamic:** S

Standard PAD assumes closed-set attacks. Unseen attacks (Open Set) cause performance degradation. Domain generalization tries to align domains but might fail on unseen attack types.

1.  **Open Set Framework:** Formulates FAS as an open set recognition problem.
2.  **Extreme Value Theory (EVT):** Uses EVT to model the tail distribution of known classes to detect outliers (unseen attacks).
3.  **Identity-Aware Contrastive Learning:** Prevents confusion between unseen attacks and hard examples (e.g., same identity).

- **Multi-task:** Parallel branches for known class classification and unseen attack detection.

- **EVT:** Statistical modeling of extreme values (outliers).
- **Contrastive Learning:** For compact representations.

- Four datasets (likely OULU, CASIA, Replay, SiW).

## What are my views on it?
- EVT is a classic tool for open set recognition, applied here to PAD.

- Open set recognition is the realistic setting for PAD.
