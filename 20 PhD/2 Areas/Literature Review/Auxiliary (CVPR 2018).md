---
aliases: [auxiliary_fas]
tags: [paper, pad, deep-fas-survey, auxiliary-supervision, rppg, depth-estimation]
authors: Yaojie Liu, Amin Jourabloo, Xiaoming Liu
year: CVPR 2018
venue: CVPR
paper_url: https://openaccess.thecvf.com/content_cvpr_2018/papers/Liu_Learning_Deep_Models_CVPR_2018_paper.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: high
---
## What does the paper present?
Previous deep learning approaches formulated FAS as a binary classification problem, which struggled to grasp adequate spoofing cues and generalized poorly. This paper argues for the importance of auxiliary supervision to guide learning toward discriminative and generalizable cues.

1.  **Auxiliary Supervision:** Proposes learning with auxiliary tasks (Depth estimation and rPPG estimation) alongside binary classification.
2.  **CNN-RNN Architecture:** Uses a CNN-RNN model to estimate face depth (pixel-wise) and rPPG signals (sequence-wise).
3.  **New Dataset (SiW):** Introduces the Spoof in the Wild (SiW) database with large variations in illumination, subject, and pose.
4.  **SOTA Performance:** Achieves state-of-the-art results on intra- and cross-database testing.

-   SiW (Spoof in the Wild) - Introduced in this paper.

-   Demonstrates that auxiliary supervision significantly improves generalization compared to binary supervision alone.
-   Achieves SOTA on OULU-NPU and SiW.

## What are my views on it?

