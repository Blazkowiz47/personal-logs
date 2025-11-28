---
aliases: [xface_pad_fas]
tags: [paper, pad, deep-fas-survey, binary-supervision]
authors: Hengameh Mirzaalian, Mohamed E. Hussein, Leonidas Spinoulas, Jonathan May, Wael Abd-Almageed
year: 2021
venue: IEEE FG 2021
paper_url: https://arxiv.org/abs/2111.04862
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
## What does the paper present?
**Abstract:** A large number of deep neural network based techniques have been developed to address the challenging problem of face presentation attack detection (PAD). Whereas such techniques' focus has been on improving PAD performance in terms of classification accuracy and robustness against unseen attacks and environmental conditions, there exists little attention on the explainability of PAD predictions. In this paper, we tackle the problem of explaining PAD predictions through natural language. Our approach passes feature representations of a deep layer of the PAD model to a language model to generate text describing the reasoning behind the PAD prediction. Due to the limited amount of annotated data in our study, we apply a light-weight LSTM network as our natural language generation model. We investigate how the quality of the generated explanations is affected by different loss functions, including the commonly used word-wise cross entropy loss, a sentence discriminative loss, and a sentence semantic loss. We perform our experiments using face images from a dataset consisting of 1,105 bona-fide and 924 presentation attack samples. Our quantitative and qualitative results show the effectiveness of our model for generating proper PAD explanations through text as well as the power of the sentence-wise losses. To the best of our knowledge, this is the first introduction of a joint biometrics-NLP task.

**Method:** XFace-PAD (Explaining Face Presentation Attack Detection Using Natural Language)
- **Backbone:** ResNet50, ViT
- **Loss:** Binary CE loss, word-wise CE loss, a sentence discriminative loss, and a sentence semantic loss
- **Input:** RGB
- **Static/Dynamic:** S

What problem does this paper address?

*Describe the model/approach*

*What's new/different from prior work?*

*Key metrics and performance*

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
