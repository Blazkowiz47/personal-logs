---
aliases: []
tags: [paper, pad, deep-fas-survey, anomaly-detection, one-class-classification]
authors: Soroush Fatemifar, Shervin Rahimzadeh Arashloo, Muhammad Awais, Josef Kittler
year: 2020
venue: Pattern Recognition
paper_url: https://www.sciencedirect.com/science/article/pii/S0031320320304994
code_url: 
status: "✅ Read"
dateadded: 2025-11-26
dateread: 2025-11-26
priority: medium
---

## Quick Summary
**Method:** ClientAnomaly
- **Backbone:** ResNet50 / GoogLeNet / VGG16 (Pre-trained on generic objects, not faces)
- **Loss:** One-Class Classification (OC-SVM, Mahalanobis, GMM)
- **Input:** RGB
- **Static/Dynamic:** S

## Problem Statement
Standard binary classifiers fail on unseen attacks. Anomaly detection is better, but generic anomaly detectors ignore client-specific information.

## Key Contributions
1.  **Client-Specific Anomaly Detection:** Proposes training one-class classifiers for each client (or using client-specific thresholds).
2.  **Generic vs. Face Features:** Shows that CNNs trained for generic object recognition are better for PAD than those trained for Face Recognition (which discard texture details).

## Methodology
### Architecture
- **Feature Extractor:** Pre-trained CNN (ImageNet).
- **Classifier:** Client-specific One-Class SVM or GMM.
- **Decision:** Client-specific thresholds.

### Key Techniques
- **One-Class Classification:** Modeling the "live" class distribution.
- **Client-Specific Modeling:** Personalizing the detector.

## Experiments
### Datasets Used
- Standard PAD datasets.

## Critical Analysis
### What Works Well
- Personalization (Client-Specific) is a powerful way to reduce intra-class variance of the "live" class.

## Relevance to My Work
### Ideas Sparked
- Personalization is often overlooked in general PAD but is critical for high-security applications (e.g., phone unlock).
