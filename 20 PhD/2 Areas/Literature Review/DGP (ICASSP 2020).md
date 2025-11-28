aliases: [dgp_fas]
tags: [paper, pad, deep-fas-survey, domain-adaptation]
authors: Amir Mohammadi, Sushil Bhattacharjee, Sébastien Marcel
year: ICASSP 2020
venue: ICASSP
paper_url: https://ieeexplore.ieee.org/document/9053685
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
## What does the paper present?
PAD systems fail to generalize to new domains (datasets). Collecting PA data in the target domain is difficult/expensive.

1.  **One-Class Domain Adaptation:** Adapts to a target domain using only bona fide samples (minimal information).
2.  **Domain Guided Pruning:** Prunes the network to adapt it to the target domain.

- Cross-dataset evaluations.

## What are my views on it?
- One-class adaptation is very practical because getting real face data is easy, but getting spoof data for a specific new environment is hard.

- Pruning as an adaptation mechanism is an interesting alternative to fine-tuning.
