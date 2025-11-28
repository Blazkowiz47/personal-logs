---
aliases: [auroraguard_fas]
tags: [paper, pad, deep-fas-survey, specialized-sensor]
authors: 
year: 2019
venue: 
paper_url: https://arxiv.org/abs/1902.10311
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
## What does the paper present?
- **Backbone:** Multi-task CNN (U-Net based)
- **Loss:** Binary CE, Depth Loss, Light Regression Loss
- **Input:** Video with active light projection (RGB)
- **Static/Dynamic:** D (Active)

Passive FAS methods struggle with complex attacks and generalization. Active methods using specific hardware (IR/Depth) are expensive. This paper proposes a cost-effective active solution using the screen light.

1. **Aurora Guard (AG):** A light reflection-based FAS method that is fast, simple, and effective.
2. **Multi-task CNN:** Recovers subject's depth map and performs light CAPTCHA checking (regression).
3. **Large-scale Dataset:** Collected 12,000 live and spoofing samples with abundant imaging qualities and PAIs.

- **Input:** Sequence of frames with changing screen color (Red, Green, Blue).
- **Network:** End-to-end trainable multi-task CNN.
    - **Depth Estimation:** Recovers 3D depth map from reflection patterns.
    - **Light CAPTCHA:** Regresses the light parameters to verify they match the projected pattern.

- **Active Light Projection:** Uses the smartphone screen to project random colors.
- **Light Reflection Analysis:** Normal cues are extracted from how light reflects off the face (3D vs 2D).
- **Light CAPTCHA:** A challenge-response mechanism to ensure the light on the face matches the screen.

- **Reflection-based Liveness:** Exploiting the difference in surface normal and material properties under changing light.

- **Private Dataset:** 12,000 samples.
- **Public Datasets:** (Likely tested on others for comparison, but main focus is the new method).

- **Performance:** State-of-the-art results on the collected dataset and public benchmarks.
- **Speed:** Real-time performance on mobile devices.

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
