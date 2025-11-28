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
- **Supervision:** Pixel-wise (Binary) + Auxiliary (Fourier Spectra Reconstruction)
- **Backbone:** EfficientNet-B0 + BiFPN (Bi-directional Feature Pyramid Network)
- **Input:** RGB (Squared crops)
- **Static/Dynamic:** S (Frame-level)

Face anti-spoofing (FAS) models often fail to generalize due to environmental variances. Existing pixel-wise supervision methods (like DeepPixBis) use multi-scale features but don't fully leverage Feature Pyramid Networks (FPN) for semantic robustness. This paper aims to use BiFPN for multi-scale feature extraction and Fourier spectra for texture-based auxiliary supervision.

1.  **Bi-FAS:** Proposes a multi-scaled approach using EfficientNet + BiFPN for pixel-wise supervision.
2.  **Bi-FAS-S (Fourier Branch):** Extends the model with a self-supervised auxiliary branch that reconstructs the Fourier spectra of the input image from the pyramid features.
3.  **SOTA on OULU-NPU Protocol IV:** Achieves an ACER of 2.92% on the hardest protocol (Protocol IV) of OULU-NPU, outperforming existing pixel-wise methods.
4.  **Squared Cropping:** Finds that using squared bounding boxes (instead of tight crops) improves performance by preserving aspect ratio and reducing artifacts.

-   **Backbone:** EfficientNet-B0 (pre-trained on ImageNet).
-   **Feature Extractor:** BiFPN (Bi-directional Feature Pyramid Network) fuses features from levels 3, 4, 5.
-   **Pixel-wise Branch:** Sigmoid activation on the feature maps of pyramids P3, P4, P5 to generate a "realness" score map. The final score is the mean of these maps.
-   **Fourier Branch (Auxiliary):** A generator network takes the pyramid features and tries to reconstruct the 2D Fourier spectra of the original input image.
    -   **Hypothesis:** Bonafide images have more high-frequency components (brighter Fourier spectra) than spoof images (which are smoother/blurred).
    -   **Loss:** Reconstruction loss (MSE) between generated and ground-truth Fourier spectra.

-   **BiFPN:** Allows top-down and bottom-up feature fusion for better multi-scale representation.
-   **Fourier Domain Supervision:** Forces the network to learn texture/frequency cues that distinguish live (high freq) from spoof (low freq).
-   **Pixel-wise Supervision:** Similar to DeepPixBis, but applied to BiFPN outputs.

-   Self-acquired dataset (3 subjects)

-   **OULU-NPU Protocol IV:** ACER 2.92% (Bi-FAS-S), significantly better than DeepPixBis and A-DeepPixBis.
-   **Generalization:** Good performance on inter-dataset testing (OULU-NPU <-> Replay-Mobile).
-   **Ablation:** The Fourier branch (Bi-FAS-S) consistently improved over the baseline Bi-FAS, especially on difficult samples.

## What are my views on it?
-   **Performance:** Excellent results on the challenging OULU-NPU Protocol IV.
-   **Novelty:** First use of BiFPN and Fourier spectra reconstruction for pixel-wise FAS.
-   **Efficiency:** Uses EfficientNet-B0, making it relatively lightweight.

-   **Face Detection Dependency:** Relies on RetinaFace; fails if face detection fails (e.g., motion blur).
-   **Dataset Size:** The self-acquired dataset is very small (3 subjects).

-   **Frequency Domain:** Strong evidence that frequency domain analysis (Fourier) is a powerful auxiliary task for FAS.
-   **Feature Pyramids:** BiFPN is a modern alternative to standard FPN/U-Net structures for multi-scale fusion.
-   **Protocol IV:** The low error rate on Protocol IV is a strong benchmark to compare against.
