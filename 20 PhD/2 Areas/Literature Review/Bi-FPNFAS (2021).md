---
aliases: [bi_fpn_fas]
tags: [paper, pad, deep-fas-survey, auxiliary-supervision, fourier-spectra, feature-pyramid]
authors: Koushik Roy, Md. Hasan, Labiba Rupty, Md. Sourave Hossain, Shirshajit Sengupta, Shehzad Noor Taus, Nabeel Mohammed
year: 2021
venue: Sensors (MDPI)
paper_url: https://www.mdpi.com/1424-8220/21/8/2799
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
Face anti-spoofing (FAS) models often fail to generalize due to environmental variances. Existing pixel-wise supervision methods (like DeepPixBis) use multi-scale features but don't fully leverage Feature Pyramid Networks (FPN) for semantic robustness. This paper aims to use BiFPN for multi-scale feature extraction and Fourier spectra for texture-based auxiliary supervision.

1.  **Bi-FAS:** Proposes a multi-scaled approach using EfficientNet + BiFPN for pixel-wise supervision.
2.  **Bi-FAS-S (Fourier Branch):** Extends the model with a self-supervised auxiliary branch that reconstructs the Fourier spectra of the input image from the pyramid features.
3.  **SOTA on OULU-NPU Protocol IV:** Achieves an ACER of 2.92% on the hardest protocol (Protocol IV) of OULU-NPU, outperforming existing pixel-wise methods.
4.  **Squared Cropping:** Finds that using squared bounding boxes (instead of tight crops) improves performance by preserving aspect ratio and reducing artifacts.

-   Self-acquired dataset (3 subjects)

## What are my views on it?

