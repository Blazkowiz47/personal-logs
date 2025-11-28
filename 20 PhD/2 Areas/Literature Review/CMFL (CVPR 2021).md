aliases:
  - cmfl_fas
tags:
  - paper
  - FAS
  - CVPR
  - year_2021
  - multimodal
  - loss-function
authors:
  - Anjith George
  - Sébastien Marcel
year: 2021
venue: CVPR
paper_url: https://arxiv.org/abs/2103.00948
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
# Cross Modal Focal Loss for RGBD Face Anti-Spoofing (CMFL)

## What does the paper present?
This paper proposes a novel loss function, **Cross Modal Focal Loss (CMFL)**, for RGB-D Face Anti-Spoofing. It addresses the issue where one modality (e.g., RGB) might overfit or dominate the learning. CMFL dynamically modulates the loss contribution of each channel based on the confidence of the individual channels, encouraging the model to learn complementary information from both modalities.

Multi-channel PAD methods often fail to generalize because they may overfit to one modality (usually RGB) or fail to effectively leverage the complementary information from additional channels (like Depth) when data is limited.

1.  **Cross Modal Focal Loss (CMFL):** A loss function that adjusts the weight of each modality's loss based on how well that modality is currently performing (confidence).
2.  **Robustness:** Improves generalization to unseen attacks by preventing the model from relying solely on the easiest modality.

- Uses a multi-stream architecture where each stream processes a different modality (RGB, Depth).
- The streams are trained jointly with the CMFL.

- WMCA (Wide Multi-Channel Presentation Attack)

- Demonstrates effectiveness on these datasets, showing better generalization than standard cross-entropy or independent training.

## What are my views on it?
- The idea of dynamically balancing modalities is crucial. Often, depth channels are noisy or sparse, and RGB is too easy to overfit. This loss seems to handle that trade-off elegantly.

- If I use multi-modal data (e.g., RGB + IR), I should consider this loss to ensure my model actually uses the IR channel and doesn't just ignore it.

- Anjith George and Sébastien Marcel are from Idiap, known for the WMCA dataset.
