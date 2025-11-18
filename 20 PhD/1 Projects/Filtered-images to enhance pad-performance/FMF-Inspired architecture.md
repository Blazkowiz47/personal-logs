---
aliases: []
tags:
  - phd
  - project
  - research
  - vit
  - attention
  - fourier
status: 🟡 In Progress
start_date: 2025-10-18
---
# Use of low/high pass filtered images along with rgb images for spoof-detection

## Research Question
*What question are you trying to answer?*
Can low-high pass filtered images aid in improving the spoof detection performance?

## Status
🟢 Active
## Timeline
- **Start Date:** 2025-10-18
- **Target Completion:** 2025-10-25
- **Milestone Dates:** 

## Motivation
Observation: When we remove 1%, 5% and 20% of the lower frequencies (post fourier transform), the resultant images do contain several camera specific artefacts like blob patterns, and also specifically for screen attacks, the moire-patterns or the grid structure is strikingly visible.

## Hypothesis
Providing the filtered images may aid the deep-learning model to focus on relevant features more compared to simple rgb. 
As [[Flexible-Modal Face Anti-Spoofing - A Benchmark|fmf-pad]] worked good in gathering cues from multiple domains, similar strategy should be ideal to make model focus on 


## Methodology
### Approach
-   

### Datasets
- 

### Models/Techniques
- 

## Literature Review
### Key Papers
- [[]]
- [[]]

### Research Gaps
- 

## Experiments

### Experiment 1:
**Date:** 2025-11-12
**Hypothesis:** Just a initial sweep with default settings for initial check for feasibility.
**Setup:**
- Dataset: OCIM
- Model: vit_b_16, resnet34
- Hyperparameters: BS: 32x4 , adamw optimizer lr: 1e-3, 1e-4

**Results:**  [[fourier-initial-sweep-results]]

### Experiment 2 - a:
**Date:** 2025-11-14
**Hypothesis:** Checking the resnet variants with SGD optimizer.
**Setup:**
- Dataset: OCIM
- Model: resnet18, resnet34 and resnet50
- Hyperparameters: 
	- BS: 32x4 , 
	- SGD backbone: 0.005 lr, head: 0.05 lr

**Results:**  [[fourier-initial-resnet-sweep]]
**Analysis:**
- Worth exploring
- Will change the learning rates of backbones and heads

### Experiment 2 - b:
**Date:** 2025-11-17
**Hypothesis:** Checking the vit variants with SGD optimizer
**Setup:**
- Dataset: OCIM
- Model: vit_b_16, vit_b_32
- Hyperparameters: 
	- BS: 32x4 , 
	- SGD backbone: 0.005 lr, head: 0.05 lr

**Results:**  [[fourier-initial-vit-sweep]]
**Analysis:**
- It seems that vit_b_32 gives more consistent results compared to vit_b_16. 
- resnet variants don't perform remarkably well compared to vit variants.

**Conclusion:**
- It seems the sgd optimizer is not suited for the training, AdamW works best.
### Experiment 3:
**Date:** 2025-11-17
**Hypothesis:** Using vit backbones train on larger dataset (100_000 per attack) 
**Setup:**
- Dataset: OCIM
- Model: vit_b_16, vit_b_32
- Hyperparameters: 
	- BS: 32x4 , 
	- AdamW 
		- lr: 1e-5 (backbone), 1e-3 (head)
		- weight_decay: 1e-7 (backbone), 1e-5 (head)
	- Augmentation (Removed center crop, now directly resized to (224,224))

**Results:**  [[fourier-vit-experiment-2]]
**Analysis:**
- It seems that vit_b_32 gives more consistent results compared to vit_b_16. 
- resnet variants don't perform remarkably well compared to vit variants.

**Conclusion:**
- It seems the sgd optimizer is not suited for the training, AdamW works best.

### Experiment 3 - b:
**Date:** 2025-11-18
**Hypothesis:** Using vit backbones train on entire dataset with more augmentations.  
**Setup:**
- Dataset: OCIM
- Model: vit_b_16, vit_b_32
- Hyperparameters: 
	- BS: 32x4 , 
	- AdamW 
		- lr: 1e-5 (backbone), 1e-3 (head)
		- weight_decay: 1e-7 (backbone), 1e-5 (head)
	- Augmentation (Removed center crop, now directly resized to (224,224))

**Results:**  [[fourier-vit-experiment-2]]
**Analysis:**
- It seems that vit_b_32 gives more consistent results compared to vit_b_16. 
- resnet variants don't perform remarkably well compared to vit variants.

**Conclusion:**
- It seems the sgd optimizer is not suited for the training, AdamW works best.
## Results Summary

| Experiment | Dataset | Model | Metric | Result | Notes |
|------------|---------|-------|--------|--------|-------|
|            |         |       |        |        |       |

## Code & Implementation
**Repository:**
**Branch:**
**Key Scripts:**
- 

## Related Concepts
- [[]]
- [[]]

## Related Areas
- [[Literature Review/Index]]
- [[Experiment Tracking/Index]]

## Challenges/Blockers
- 

## Next Steps
- [ ] 
- [ ] 

## Potential Contributions
- Novel method:
- Improved performance:
- New insights:

## Publication Plan
**Target Venue:**
**Draft Status:**
**Co-authors:**

## Learnings & Insights
*What did you discover?*

#### For later help
🔴 Blocked / ✅ Complete