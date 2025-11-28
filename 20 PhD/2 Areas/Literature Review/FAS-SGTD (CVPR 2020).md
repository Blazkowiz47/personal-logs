aliases:
  - sgtd_fas
tags:
  - paper
  - FAS
  - CVPR
  - year_2020
  - architecture/spatio-temporal
  - method/gradient-based
authors:
  - Zezheng Wang
  - Zitong Yu
  - Chenxu Zhao
  - Xiangyu Zhu
  - Yunxiao Qin
  - Qiusheng Zhou
  - Feng Zhou
  - Zhen Lei
year: 2020
venue: CVPR
paper_url: https://arxiv.org/abs/2003.08061
code_url: https://github.com/clks-wzz/FAS-SGTD
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
# Deep Spatial Gradient and Temporal Depth Learning for Face Anti-spoofing (FAS-SGTD)

## What does the paper present?
This paper proposes a method that leverages **Spatial Gradient** and **Temporal Depth** information. It argues that stacked vanilla convolutions discard detailed discriminative clues (like gradient magnitude). It introduces a **Residual Spatial Gradient Block (RSGB)** to capture these details and a **Spatio-Temporal Propagation Module (STPM)** to model the temporal dynamics of 3D moving faces.

1.  Vanilla convolutions may smooth out or discard fine-grained spatial gradient information which is crucial for distinguishing real skin from spoof mediums (paper, screen).
2.  Single-frame methods neglect the temporal dynamics of 3D faces.

1.  **Residual Spatial Gradient Block (RSGB):** A block that explicitly computes and processes spatial gradients to capture fine-grained spoofing patterns.
2.  **Spatio-Temporal Propagation Module (STPM):** Efficiently encodes spatio-temporal information from multiple frames.
3.  **Contrastive Depth Loss:** A novel loss function for more accurate depth supervision.
4.  **Double-modal Anti-spoofing Dataset (DMAD):** A new dataset collected by the authors (though less standard than OULU).

- DMAD (Custom)

- State-of-the-art results on the five benchmark datasets.

## What are my views on it?
- The focus on "gradients" is a recurring theme in successful FAS papers (like CDCN). It seems that texture analysis is more robust than semantic analysis for this task.

- The RSGB block is another way to implement "texture-aware" convolutions. I should compare this with CDC (Central Difference Convolution).

- Code available at: https://github.com/clks-wzz/FAS-SGTD
