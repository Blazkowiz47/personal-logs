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
## What does the paper present?
PAD systems need to adapt to new attack types continuously (Lifelong Learning) without forgetting previous ones (Catastrophic Forgetting).

1.  **Lifelong Learning Framework:** Formulates PAD as a lifelong learning problem.
2.  **Meta-Learning Approach:** Uses a meta-learning strategy to enable the model to adapt to new attacks.
3.  **Gradient Alignment:** Uses gradient alignment to ensure updates for new tasks don't interfere with old ones.

- Uses a meta-learning framework (likely MAML-based).

- Standard PAD datasets (likely OULU-NPU, SiW, etc. in a sequential protocol).

## What are my views on it?
- Addressing the "open set" nature of attacks is crucial.

- Continual learning is very relevant for real-world deployment.
