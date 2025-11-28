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
FAS techniques typically fail to generalize to new samples due to large variability in backgrounds, lighting, camera resolutions, and spoof materials. This paper tackles the generalization problem by learning domain-agnostic features.

1.  **Class-Conditional Domain Discriminator:** Proposes a module that, coupled with a gradient reversal layer, tries to generate live and spoof features that are discriminative but robust to domain variability.
2.  **Domain Agnostic Learning:** Explicitly aligns the feature distributions of different domains (datasets) to learn a common feature space.
3.  **Image and Video Support:** Validated on both image-based and video-based FAS tasks.

-   Likely cross-dataset protocols (e.g., OULU-NPU, CASIA, Replay-Attack).

-   Shows effectiveness over existing techniques in terms of numerical improvement and feature visualization (t-SNE).

## What are my views on it?
