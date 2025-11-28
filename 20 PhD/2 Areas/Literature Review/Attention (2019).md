---
aliases: [attention_fas]
tags: [paper, pad, deep-fas-survey, multimodal]
authors: 
year: 2019
venue: 
paper_url: https://openaccess.thecvf.com/content_CVPRW_2019/html/CFS/Wang_Multi-Modal_Face_Presentation_Attack_Detection_via_Spatial_and_Channel_Attentions_CVPRW_2019_paper.html
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
## What does the paper present?
- **Backbone:** ResNet18 (Multi-stream)
- **Loss:** Center Loss, Softmax Loss
- **Input:** RGB, Depth, IR
- **Fusion:** Feature-level with Attention

Traditional PAD approaches lack generalization due to limited modalities and subjects. Simple concatenation of modalities is suboptimal as not all features are equally important.

1. **Multi-Modal Fusion:** Proposes an end-to-end approach fusing RGB, Depth, and IR.
2. **Spatial and Channel Attention:** Introduces attention modules to select discriminative features spatially and across channels.
3. **Performance:** Achieves promising results on the CASIA-SURF dataset.

- **Backbone:** ResNet-18 based multi-stream network.
- **Branches:** 4 branches: RGB, Depth, IR, and Fused (9-channel input).
- **Fusion:** Features from all branches are concatenated and fed into shared layers.

- **Spatial Attention:** Focuses on the face region and suppresses background noise.
- **Channel Attention:** Re-weights feature channels to emphasize informative maps.
- **Loss Functions:** Joint optimization with Center Loss (intra-class compactness) and Softmax Loss (inter-class separability).

- **Attention-based Fusion:** Applying attention before fusion to refine features.

- **CASIA-SURF:** A large-scale multi-modal dataset.

- **Performance:** The method demonstrates superior performance on CASIA-SURF compared to single-modal or simple fusion baselines.

*What components were tested?*

*Anything useful for implementing this*

- [[]]

- [[]]

- [[]]

## What are my views on it?
*My thoughts on the paper*

*How does this relate to my PAD research?*

>

- Figure X:

$$
$$

*Discussions with advisor/colleagues about this paper*

- [ ]
- [ ]

---
**Reading Progress:**
- [ ] Abstract
- [ ] Introduction
- [ ] Related Work
- [ ] Methodology
- [ ] Experiments
- [ ] Conclusion
- [ ] Supplementary Material
