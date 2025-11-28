---
aliases: [basn_fas]
tags: [paper, pad, deep-fas-survey, auxiliary-supervision, domain-generalization]
authors: Taewook Kim, YongHyun Kim, Inhan Kim, Daijin Kim
year: ICCVW 2019
venue: ICCVW
paper_url: https://openaccess.thecvf.com/content_ICCVW_2019/papers/DFW/Kim_BASN_Enriching_Feature_Representation_Using_Bipartite_Auxiliary_Supervisions_for_Face_ICCVW_2019_paper.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
- **Supervision:** Bipartite Auxiliary (Depth, Reflection/etc.)
- **Backbone:** CNN
- **Input:** RGB
- **Static/Dynamic:** S

To be applicable to unconstrained real-world environments, FAS methods require robust generalization capabilities. This paper aims to improve generalization to unseen environments by guiding networks to learn generalizable features.

1.  **Bipartite Auxiliary Supervision:** Suggests using bipartite auxiliary supervision to properly guide networks.
2.  **BASN Architecture:** Proposes the Bipartite Auxiliary Supervision Network (BASN) that comprehensively utilizes the suggested supervision.
3.  **Generalization:** Demonstrates robust generalization ability to unseen environments.

-   **BASN:** A network designed to enrich feature representation using auxiliary tasks.
-   **Bipartite Supervision:** Likely involves learning complementary tasks (e.g., depth and another modality like reflection or binary mask) to enforce learning of robust features.

-   **Auxiliary Supervision:** Using additional supervision signals beyond binary labels.
-   **Feature Enrichment:** Enhancing the feature space to be more discriminative for live vs. spoof.

-   Public benchmark datasets (likely OULU-NPU, SiW, etc.)

-   Achieves state-of-the-art performances on benchmark datasets.
-   Shows improved generalization.

## What are my views on it?
-   **Generalization Focus:** Explicitly targets the generalization problem in FAS.
-   **Auxiliary Tasks:** Builds on the success of auxiliary supervision (like depth/rPPG) but refines it with a "bipartite" approach.

-   **Auxiliary Supervision:** Relevant for understanding how different auxiliary tasks can be combined or structured (bipartite) to improve performance.
