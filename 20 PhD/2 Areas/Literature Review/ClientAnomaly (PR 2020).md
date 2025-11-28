aliases: [clientanomaly_fas]
tags: [paper, pad, deep-fas-survey, anomaly-detection, one-class-classification]
authors: Soroush Fatemifar, Shervin Rahimzadeh Arashloo, Muhammad Awais, Josef Kittler
year: 2020
venue: Pattern Recognition
paper_url: https://www.sciencedirect.com/science/article/pii/S0031320320304994
code_url: 
status: "📚 To Read"
dateadded: 2025-11-26
dateread:
priority: medium
## What does the paper present?
Standard binary classifiers fail on unseen attacks. Anomaly detection is better, but generic anomaly detectors ignore client-specific information.

1.  **Client-Specific Anomaly Detection:** Proposes training one-class classifiers for each client (or using client-specific thresholds).
2.  **Generic vs. Face Features:** Shows that CNNs trained for generic object recognition are better for PAD than those trained for Face Recognition (which discard texture details).

- Standard PAD datasets.

## What are my views on it?
- Personalization (Client-Specific) is a powerful way to reduce intra-class variance of the "live" class.

- Personalization is often overlooked in general PAD but is critical for high-security applications (e.g., phone unlock).
