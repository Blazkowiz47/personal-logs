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
# Flexible-Modal Face Anti-Spoofing - A Benchmark

> [!abstract] **One-Liner**
> Train a "One-for-all" model on RGB+Depth+Infrared modalities with a single backbone and three feature fusion strategies.

## 💡 Core Concept
**Problem:** Developing a single model which can be deployed flexibly with different modalities (e.g., only RGB available, or RGB+Depth).
**Solution:** A unified framework with specific fusion strategies that handle missing modalities via dropout during training.

**Key Contributions:**
1. First flexible-modal benchmark.
2. **Cross-attention fusion module** to efficiently mine cross-modal clues.
3. Insight: Modality dropout works well for intra-testing but poorly for cross-testing.

## ⚙️ Methodology
**Architecture:**
- **Backbone:** Single shared backbone.
- **Fusion Strategies:**
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

**Training Strategy:**
- **Modality Dropout:** Randomly zero out modalities during training to mimic missing sensors in deployment.
- **Settings:** Finetuned for 30 epochs, halving LR after 20th.

## 📊 Results & Analysis
**Datasets:** [[CASIA-SURF]], [[CeFA]], [[WMCA]]

**Performance:**
- **Best Case:** When all three modalities are available.
- **Generalization:** "Bad performance in general... Cross dataset sucks to generalise."
- **Failure Mode:** The model struggles when the domain shifts (cross-testing), likely because it overfits to the specific sensor characteristics of the training set.

## 🧠 Critical Review
| **Strengths** | **Limitations** |
| :--- | :--- |
| Flexible deployment (handles missing sensors). | Poor cross-dataset generalization. |
| Simple, unified architecture. | |

**My Take:**
The idea of "One-for-all" is practical for industry, but the reliance on modality dropout seems insufficient for true domain generalization. The cross-attention mechanism is the most interesting part.

## 🧪 Experimental Ideas & Logs
*Connect this paper to my experiments.*

- **Idea:** What if we use Fourier transform images (low pass / high pass) as 2 modalities instead of physical sensors?
- **Related Experiment:** [[Experiment - Frequency Modalities for Flex-FAS]] (Proposed)
- **Hypothesis:** Frequency domain might be more robust to domain shifts than raw pixel depth/IR.

## 🔗 References
- **Code:** [GitHub](https://github.com/ZitongYu/Flex-Modal-FAS)
- **Related Papers:**
	- [[CASIA-SURF]] (Dataset)
	- [[CeFA]] (Dataset)
	- [[WMCA]] (Dataset)
