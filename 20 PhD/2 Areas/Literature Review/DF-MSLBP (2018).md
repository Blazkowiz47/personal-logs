---
aliases: [df_mslbp_fas]
tags: [paper, pad, deep-fas-survey, hybrid-method, deep-forest]
authors: Rizhao Cai, Changsheng Chen
year: 2018
venue: PRL (Submitted) / arXiv
paper_url: https://arxiv.org/abs/1910.03850
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---
## What does the paper present?
CNNs are vulnerable to adversarial attacks. Handcrafted features combined with non-differentiable models (like Random Forests) might be more robust.

1.  **Deep Forest for FAS:** First attempt to use Deep Forest (gcForest) for Face Anti-Spoofing.
2.  **Multi-scale LBP:** Replaces the standard scanning mechanism in gcForest with MS-LBP for better texture capture.

- Replay-Attack (0% EER reported).

## What are my views on it?
- Exploring non-CNN deep models is interesting for security/robustness against gradients-based attacks.

- Adversarial robustness is a key angle. Non-differentiable components can block gradient flow for attackers.
