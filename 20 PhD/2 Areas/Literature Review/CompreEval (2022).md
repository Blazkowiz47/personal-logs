aliases: [compreeval_fas]
tags: [paper, pad, deep-fas-survey, multimodal, benchmark]
authors: Anjith George, David Geissbuhler, Sebastien Marcel
year: 2022
venue: arXiv
paper_url: https://arxiv.org/abs/2202.10286
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
## What does the paper present?
Lack of understanding of which sensors (modalities) are most effective for PAD against various attacks. High cost of multi-sensor systems requires optimal selection.

1.  **Large-Scale Evaluation:** Evaluates 14 different sensing modalities (RGB, NIR, SWIR, Depth, Thermal, etc.).
2.  **Dataset:** Uses a multi-channel PAD dataset (likely HQ-WMCA or similar internal dataset).
3.  **Analysis:** Provides pointers for sensor selection based on performance against 2D, 3D, and partial attacks.

- Multi-channel PAD dataset (likely HQ-WMCA).

## What are my views on it?
- Essential reference for anyone building hardware for PAD. SWIR and Thermal are often highlighted as robust.

- If I have access to SWIR/Thermal data, I should use it. If not, I should know the limitations of RGB-only.
