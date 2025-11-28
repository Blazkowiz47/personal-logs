---
aliases: [cmpad2020_fas]
tags: [paper, pad, deep-fas-survey, continual-learning, meta-learning]
authors: Daniel Pérez-Cabo, David Jiménez-Cabello, Artur Costa-Pazo, Roberto Javier López-Sastre
year: IJCB 2020
venue: IJCB
paper_url: https://ieeexplore.ieee.org/document/9304920
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
---

## Quick Summary
**Method:** CM-PAD (Continual Meta-Learning PAD)
- **Replay or not:** with Replay
- **Backbone:** DepthNet / ResNet
- **Loss:** Meta-learning loss (Gradient alignment)
- **Input:** RGB

## Problem Statement
PAD systems need to adapt to new attack types continuously (Lifelong Learning) without forgetting previous ones (Catastrophic Forgetting).

## Key Contributions
1.  **Lifelong Learning Framework:** Formulates PAD as a lifelong learning problem.
2.  **Meta-Learning Approach:** Uses a meta-learning strategy to enable the model to adapt to new attacks.
3.  **Gradient Alignment:** Uses gradient alignment to ensure updates for new tasks don't interfere with old ones.

## Methodology
### Architecture
- Uses a meta-learning framework (likely MAML-based).

### Key Techniques
- **Continual Learning:** Adapting to new domains/attacks.
- **Meta-Learning:** Learning to learn.

## Experiments
### Datasets Used
- Standard PAD datasets (likely OULU-NPU, SiW, etc. in a sequential protocol).

## Critical Analysis
### What Works Well
- Addressing the "open set" nature of attacks is crucial.

## Relevance to My Work
### Ideas Sparked
- Continual learning is very relevant for real-world deployment.
