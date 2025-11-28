---
aliases: [dtn_fas]
tags: [paper, pad, deep-fas-survey, zero-shot, anomaly-detection]
authors: Yaojie Liu, Joel Stehouwer, Amin Jourabloo, Xiaoming Liu
year: CVPR 2019
venue: CVPR
paper_url: https://openaccess.thecvf.com/content_CVPR_2019/html/Liu_Deep_Tree_Learning_for_Zero-Shot_Face_Anti-Spoofing_CVPR_2019_paper.html
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
Zero-Shot Face Anti-spoofing (ZSFA): Detecting unknown spoof attacks that were not seen during training. Previous works only studied 1-2 types.

1.  **Deep Tree Network (DTN):** Learns to partition spoof samples into semantic sub-groups in an unsupervised fashion.
2.  **Zero-Shot Detection:** Routes input to the most similar spoof cluster or detects it as unknown/live.
3.  **Diverse Attack Dataset:** Introduces a dataset with 13 types of spoof attacks.

- SiW-M (Spoof in the Wild - Multi-attack).

## What are my views on it?
- Treating PAD as an anomaly detection or zero-shot problem is the most realistic setup.

- The SiW-M dataset is the gold standard for zero-shot testing. I must use it.
