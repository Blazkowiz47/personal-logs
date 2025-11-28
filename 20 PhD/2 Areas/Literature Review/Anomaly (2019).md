---
aliases: [anomaly_fas]
tags: [paper, pad, deep-fas-survey, anomaly-detection]
authors: 
year: 2019
venue: 
paper_url: https://openaccess.thecvf.com/content_CVPRW_2019/papers/CFS/Perez-Cabo_Deep_Anomaly_Detection_for_Generalized_Face_Anti-Spoofing_CVPRW_2019_paper.pdf
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread: 
priority: medium
---
## What does the paper present?
FAS is typically treated as binary classification, but "spoof" attacks are unbounded and diverse, while "live" faces are consistent. Generalization to unseen attacks is a major challenge.

1. **Anomaly Detection Formulation:** Reformulates Generalized PAD (GPAD) as an anomaly detection problem.
2. **Metric-Softmax Loss:** Guides learning towards discriminative embeddings on a hypersphere.
3. **Triplet Focal Loss:** Regularization to push anomalies away from the live center, focusing on hard examples.
4. **Few-Shot Estimation:** Introduces a posteriori probability estimation without training a classifier.

## What are my views on it?
