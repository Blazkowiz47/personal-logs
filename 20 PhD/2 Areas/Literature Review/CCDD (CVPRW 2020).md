---
aliases: [ccdd_fas]
tags: [paper, pad, deep-fas-survey, domain-generalization, domain-agnostic]
authors: Suman Saha, Wenhao Xu, Menelaos Kanakis, Stamatios Georgoulis, Yuhua Chen, Danda Pani Paudel, Luc Van Gool
year: CVPRW 2020
venue: CVPRW
paper_url: https://openaccess.thecvf.com/content_CVPRW_2020/papers/w48/Saha_Domain_Agnostic_Feature_Learning_for_Image_and_Video_Based_Face_CVPRW_2020_paper.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
- **Supervision:** Domain Adversarial Training
- **Backbone:** CNN (Image) / CNN-RNN (Video)
- **Input:** RGB
- **Static/Dynamic:** Both (Image and Video based)

FAS techniques typically fail to generalize to new samples due to large variability in backgrounds, lighting, camera resolutions, and spoof materials. This paper tackles the generalization problem by learning domain-agnostic features.

1.  **Class-Conditional Domain Discriminator:** Proposes a module that, coupled with a gradient reversal layer, tries to generate live and spoof features that are discriminative but robust to domain variability.
2.  **Domain Agnostic Learning:** Explicitly aligns the feature distributions of different domains (datasets) to learn a common feature space.
3.  **Image and Video Support:** Validated on both image-based and video-based FAS tasks.

-   **Feature Extractor:** Extracts features from input (CNN for images, CNN+RNN for video).
-   **Label Classifier:** Predicts Live/Spoof.
-   **Domain Discriminator:** Tries to predict which domain (dataset) the sample came from.
-   **Gradient Reversal Layer (GRL):** Used to reverse the gradients from the domain discriminator, forcing the feature extractor to learn features that *confuse* the domain discriminator (i.e., domain-invariant features).

-   **Adversarial Domain Adaptation:** Using GRL to make features indistinguishable across domains.
-   **Class-Conditional:** The domain discriminator likely conditions on the class label (Live/Spoof) to ensure that alignment happens *within* classes (aligning Live-DomainA with Live-DomainB, not just global alignment).

-   Likely cross-dataset protocols (e.g., OULU-NPU, CASIA, Replay-Attack).

-   Shows effectiveness over existing techniques in terms of numerical improvement and feature visualization (t-SNE).

-   **GRL:** Standard component in domain adaptation (from Ganin et al.).
-   **Class-Conditional:** Requires passing the label (or predicted label) to the discriminator.

## What are my views on it?
-   **Generalization:** Directly addresses the domain shift problem, which is the main bottleneck in FAS.
-   **Versatility:** Applicable to both spatial and temporal models.

-   **Domain Generalization:** A key technique for robust FAS. The "Class-Conditional" aspect is important because simply aligning domains might merge Live and Spoof distributions if not careful.
