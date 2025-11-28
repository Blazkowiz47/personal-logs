---
aliases:
  - fmf_fas
tags:
  - paper
  - pad
  - to-read
  - "#vit"
  - transformers
  - multimodal
  - attention
authors: Zitong Yu, Ajian Liu, Chenxu Zhao, Kevin H. M. Cheng, Xu Cheng, Guoying Zhao
year: "2022"
venue: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition
paper_url: https://arxiv.org/pdf/2202.08192
code_url: https://github.com/ZitongYu/Flex-Modal-FAS
status: ✅ Read
dateadded: 2025-10-18
dateread: 2025-11-20
priority: high
---
## Quick Summary
Train a "One-for-all" model on RGB+Depth+Infrared modalities with a single backbone and three feature fusion strategies.

## Problem Statement
What problem does this paper address?
Developing a single model which can be deployed flexibly with different modalities.

## Key Contributions
1. First flexible-modal benchmark.
2. Cross-attention fusion module to efficiently mine cross-modal clues for flexible-modal deployment.
3. Found out that the modality dropout strategy works well in flex-modal intra-testings but poorly in flex-modal cross-testings.

## Experiments
### Datasets Used
- [[CASIA-SURF]]
- [[CeFA]]
- [[WMCA]]

### Results
bad performance in general.
when all three modalities are used while testing it works best.
- Cross dataset sucks to generalise.

## Implementation Notes

### Architecture Details
#### 3 Ways of fusion:
- Direct concatenation fusion:
	- F$_{fuse}$ = ReLU(BN(Conv(Concat(F$_{RGB}$, F$_{Depth}$, F$_{IR}$))))
	Default method.
    
- Squeeze-and-excitation fusion:
	- F$^{SE}_{RGB}$ = F$_{RGB}$ $\times$ $\sigma$(FC(ReLU(FC(AvgPool(F$_{RGB}$)))))
	- F$^{SE}_{Depth}$ = F$_{Depth}$ $\times$ $\sigma$(FC(ReLU(FC(AvgPool(F$_{Depth}$)))))
	- F$^{SE}_{IR}$ = F$_{IR}$ $\times$ $\sigma$(FC(ReLU(FC(AvgPool(F$_{IR}$)))))
	- F$_{fuse}$ = ReLU(BN(Conv(Concat(F$^{SE}_{RGB}$,F$^{SE}_{Depth}$,F$^{SE}_{IR}$))))
	Intermediate channel numbers are reduced to one eighth of original channels.
- Cross-attention fusion:
    - F$^{CA}_{Depth}$ = Softmax(F$_{Depth}$(F$_{RGB}$)$^{T}$)F$_{RGB}$
    - F$^{CA}_{IR}$ = Softmax(F$_{IR}$(F$_{RGB}$)$^{T}$)F$_{RGB}$
    - F$_{fuse}$ = ReLU(BN(Conv(F$_{RGB}$+F$^{CA}_{Depth}$+F$^{CA}_{IR}$))) # element wise addition

Missing modalities are simply blocked as zeros in testing phase and to mimic these scenarios random dropout of modalities is done during the training.

### Training Details
- Finetuned for 30 epochs with epoch halving after 20th epoch.


### Ablation Studies
*What components were tested?*


## Strengths
-
-

## Limitations
-
-

## Critical Analysis
*My thoughts on the paper*

### What Works Well
-

### Concerns/Criticisms
-

### Missing Pieces
-

## Relevance to My Work
*How does this relate to my PAD research?*


## Meeting Notes
*Discussions with advisor/colleagues about this paper*


## Action Items
- [ ]
- [ ]

---
**Reading Progress:**
- [x] Abstract
- [x] Introduction
- [x] Related Work
- [x] Methodology
- [x] Experiments
- [x] Conclusion
- [x] Supplementary Material
