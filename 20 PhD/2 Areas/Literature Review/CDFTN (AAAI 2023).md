aliases: [cdftn_fas]
tags: [paper, pad, deep-fas-survey, domain-adaptation]
authors: Haixiao Yue, Keyao Wang, Guosheng Zhang, Haocheng Feng, Junyu Han, Errui Ding, Jingdong Wang
year: AAAI 2023
venue: AAAI
paper_url: https://arxiv.org/abs/2212.03651
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
## What does the paper present?
This paper proposes a domain adaptation method that generates pseudo-labeled samples by disentangling "liveness features" (domain-invariant) from "content features" (domain-specific). It uses a cyclic translation process to synthesize images that look like the target domain but preserve the liveness information from the source, enabling robust training on unlabeled target domains.

Domain adaptation in FAS is challenging because domain differences (illumination, camera, etc.) are often entangled with liveness features. Existing methods struggle to achieve perfect disentanglement, leading to poor generalization on unseen scenarios.

1.  **CDFTN:** A novel framework for cross-scenario FAS that cyclically disentangles liveness and content features.
2.  **Pseudo-Label Generation:** Synthesizes high-quality pseudo-labeled samples combining source liveness with target content.
3.  **Multi-Target Adaptation:** Extends the framework to leverage data from multiple unlabeled target domains simultaneously.

-   Standard cross-domain protocols (e.g., OULU-NPU, CASIA-MFSD, Idiap Replay-Attack, MSU-MFSD).

-   Outperforms state-of-the-art domain adaptation methods on several public benchmarks.

## What are my views on it?
-   The idea of synthesizing training samples that "look" like the target domain is powerful for reducing the domain gap.
