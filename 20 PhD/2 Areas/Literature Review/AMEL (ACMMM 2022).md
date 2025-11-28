aliases:
  - amel_fas
tags:
  - paper
  - FAS
  - ACMMM
  - year_2022
  - domain-generalization
  - method/mixture-of-experts
  - method/meta-learning
authors:
  - Qianyu Zhou
  - Ke-Yue Zhang
  - Taiping Yao
  - Ran Yi
  - Shouhong Ding
  - Lizhuang Ma
year: 2022
venue: ACM MM
paper_url: https://arxiv.org/abs/2207.09868
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
# Adaptive Mixture of Experts Learning for Generalizable Face Anti-Spoofing (AMEL)

## What does the paper present?
This paper proposes an **Adaptive Mixture of Experts Learning (AMEL)** framework for Domain Generalization (DG) in FAS. It argues that existing DG methods focus too much on domain-invariant features and neglect domain-specific characteristics. AMEL uses **Domain-Specific Experts (DSE)** to learn unique features for each source domain and a **Dynamic Expert Aggregation (DEA)** module to adaptively combine them for unseen target domains based on domain relevance.

Standard DG methods try to find a common feature space for all domains, which might be suboptimal because different domains (and attack types) have distinct characteristics. Ignoring these specific traits limits generalization.

1.  **Adaptive Mixture of Experts Learning (AMEL):** A framework that leverages both domain-invariant and domain-specific information.
2.  **Domain-Specific Experts (DSE):** Experts trained to specialize in individual source domains.
3.  **Dynamic Expert Aggregation (DEA):** A mechanism to weight the contributions of different experts based on how similar the target input is to the source domains.
4.  **Meta-Learning Integration:** Used to train the aggregation module to generalize to unseen domains.

- Outperforms SOTA competitors on standard DG protocols.

## What are my views on it?
- The MoE approach makes a lot of sense for FAS because "spoof" is such a diverse category. A print attack expert might not be good at mask attacks, so having specialized experts and a router is a logical step.

- I could implement a simple MoE where I have one expert for "print", one for "replay", and one for "mask", if I have labels for those.

- Accepted to ACM Multimedia 2022.
