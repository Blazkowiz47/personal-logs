---
aliases: [saplc_fas]
tags: [paper, pad, deep-fas-survey, auxiliary-supervision]
authors: Wenyun Sun, Yu Song, Changsheng Chen, Jiwu Huang, Alex C. Kot
year: 2020
venue: IEEE Transactions on Information Forensics and Security (TIFS)
paper_url: https://ieeexplore.ieee.org/document/9056824
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
# Face Spoofing Detection Based on Local Ternary Label Supervision in Fully Convolutional Networks

> [!abstract]
> Face verification systems are prone to spoofing attacks on photos, videos, and 3D masks. Face spoofing detection, i.e., face anti-spoofing, face liveness detection, or face presentation attack detection, is an important task for securing face verification systems in practice and presents many challenges. In this paper, a state-of-the-art face spoofing detection method based on a depth-based Fully Convolutional Network (FCN) is revisited. Different supervision schemes, including global and local label supervisions, are comprehensively investigated. A generic theoretical analysis and associated simulation are provided to demonstrate that local label supervision is more suitable than global label supervision for local tasks with insufficient training samples, such as the face spoofing detection task. Based on the analysis, the Spatial Aggregation of Pixel-level Local Classifiers (SAPLC), which is composed of an FCN part and an aggregation part, is proposed. The FCN part predicts the pixel-level ternary labels, which include the genuine foreground, the spoofed foreground, and the undetermined background. Then, these labels are aggregated together to yield an accurate image-level decision. Furthermore, to quantitatively evaluate the proposed SAPLC, experiments are carried out on the CASIA-FASD, Replay-Attack, OULU-NPU, and SiW datasets. The experiments show that the proposed SAPLC outperforms the representative deep networks, including two globally supervised CNNs, one depth-based FCN, two FCNs with binary labels, and two FCNs with ternary labels, and achieves competitive performances close to some state-of-the-art method performances under various common protocols. Overall, the results empirically verify the advantage of the proposed pixel-level local label supervision scheme.

## What does the paper present?
- **Supervision:** TernaryMap
- **Backbone:** DepthNet
- **Input:** RGB, HSV
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
