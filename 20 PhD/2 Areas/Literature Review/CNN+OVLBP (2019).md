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
## What does the paper present?
- **Backbone:** CNN (Pre-trained) + OVLBP (Handcrafted)
- **Loss:** Score-level fusion
- **Input:** RGB
- **Static/Dynamic:** S

Improving PAD performance by combining the strengths of deep learning (semantic features) and handcrafted descriptors (micro-texture).

1.  **Score-Level Fusion:** Fusing scores from a CNN and an OVLBP-based classifier.
2.  **OVLBP:** Using Overlapped Local Binary Patterns for texture analysis.

- **Stream 1:** OVLBP feature extraction -> Classifier.
- **Stream 2:** Pre-trained CNN -> Classifier.
- **Fusion:** Weighted sum of scores.

- **OVLBP:** A variant of LBP.

## What are my views on it?
- Fusion of complementary features is a robust strategy.

- Hybrid methods are good baselines.
