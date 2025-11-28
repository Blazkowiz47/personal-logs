---
aliases: [slnet_fas]
tags: [paper, pad, deep-fas-survey, specialized-sensor]
authors: Yasar Abbas Ur Rehman, Lai-Man Po, Mengyang Liu
year: 2020
venue: Expert Systems with Applications
paper_url: http://www.ee.cityu.edu.hk/~lmpo/publications/2019_ESA_SLNet.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
# SLNet: Stereo face liveness detection via dynamic disparity-maps and convolutional neural network

> [!abstract]
> Current state-of-the-art dual camera-based face liveness detection methods utilize either hand-crafted features, such as disparity, or deep texture features to classify a live face and face Presentation Attack (PA). However, these approaches limit the effectiveness of classifiers, particularly deep Convolutional Neural Networks (CNN) to unknown face PA in adverse scenarios. In contrast to these approaches, in this paper, we show that supervising a deep CNN classifier by learning disparity features using the existing CNN layers improves the performance and robustness of CNN to unknown types of face PA. For this purpose, we propose to supervise a CNN classifier by introducing a disparity layer within CNN to learn the dynamic disparity-maps. Subsequently, the rest of the convolutional layers, following the disparity layer, in the CNN are supervised using the learned dynamic disparity-maps for face liveness detection. We further propose a new video-based stereo face anti-spoofing database with various face PA and different imaging qualities. Experiments on the proposed stereo face anti-spoofing database are performed using various test case scenarios. The experimental results indicate that our proposed system shows promising performance and has good generalization ability.

## What does the paper present?
- **Backbone:** 17-layer CNN
- **Loss:** Binary CE loss
- **Input:** Stereo (left&right) face images
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
