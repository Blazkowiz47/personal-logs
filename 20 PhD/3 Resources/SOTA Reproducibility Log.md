# 📊 SOTA Reproducibility Log

> **Tracking performance of SOTA methods with available code/checkpoints.**
> *Metrics: EER (Equal Error Rate), AUC (Area Under Curve), TPR@FPR (True Positive Rate at False Positive Rate).*

## 1. Oulu-NPU
*Protocol: ICMO (unless specified)*

| Method | Protocol | EER (%) | AUC (%) | TPR@1% | TPR@5% |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CF-FAS** | icmo | 20.033 | 80.209 | 0.000 | 0.000 |
| **DGUA-FAS** | icmo | 14.681 | 93.762 | 46.934 | 70.354 |
| **LMFD-FAS** | icmo | 16.238 | 91.463 | 0.000 | 66.463 |
| **FLIP-FAS** | icmo | **5.522** | **98.643** | **83.058** | **94.028** |
| **JPD-FAS** | all | 5.470 | 98.641 | 70.897 | 93.853 |
| **IADG-FAS** | icmo | 12.190 | 93.631 | 58.602 | 80.352 |
| **GACD-FAS** | icmo | 9.776 | 96.692 | 52.938 | 81.558 |

## 2. CASIA-FASD
*Protocol: OIMC (unless specified)*

| Method | Protocol | EER (%) | AUC (%) | TPR@1% | TPR@5% |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CF-FAS** | oimc | 13.851 | 89.742 | 0.000 | 67.894 |
| **DGUA-FAS** | oimc | 14.187 | 93.991 | 58.675 | 70.702 |
| **LMFD-FAS** | oimc | 25.730 | 82.627 | 23.751 | 48.897 |
| **FLIP-FAS** | oimc | **4.080** | **99.258** | **83.772** | **97.111** |
| **JPD-FAS** | all | 15.581 | 91.985 | 58.459 | 72.532 |
| **IADG-FAS** | oimc | 16.711 | 91.038 | 26.219 | 58.753 |
| **GACD-FAS** | oimc | 14.796 | 92.090 | 14.122 | 68.260 |

## 3. MSU-MFSD
*Protocol: OCIM (unless specified)*

| Method | Protocol | EER (%) | AUC (%) | TPR@1% | TPR@5% |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CF-FAS** | ocim | 10.106 | 95.404 | 40.778 | 76.001 |
| **DGUA-FAS** | ocim | 10.646 | 96.003 | 50.942 | 81.682 |
| **LMFD-FAS** | ocim | 18.239 | 90.319 | 25.413 | 47.869 |
| **FLIP-FAS** | ocim | **10.331** | 95.855 | **63.774** | **84.310** |
| **JPD-FAS** | all | 16.393 | 91.987 | 36.796 | 64.788 |
| **IADG-FAS** | ocim | 27.763 | 79.117 | 4.642 | 42.602 |
| **GACD-FAS** | ocim | 10.409 | **96.653** | 51.242 | 83.251 |

## 4. Idiap (Replay-Attack)
*Protocol: OCMI (unless specified)*

| Method | Protocol | EER (%) | AUC (%) | TPR@1% | TPR@5% |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CF-FAS** | ocmi | 19.095 | 82.174 | 32.671 | 57.931 |
| **DGUA-FAS** | ocmi | 12.255 | 94.829 | 55.647 | 76.812 |
| **LMFD-FAS** | ocmi | 19.249 | 88.687 | 27.884 | 50.916 |
| **FLIP-FAS** | ocmi | **3.141** | **99.633** | **91.368** | **98.449** |
| **JPD-FAS** | all | 19.064 | 82.062 | 0.000 | 0.000 |
| **IADG-FAS** | ocmi | 41.141 | 61.424 | 0.448 | 6.765 |
| **GACD-FAS** | ocmi | 4.363 | 98.984 | 75.953 | 96.545 |

---
Tags: #phd #sota #benchmark #reproducibility #metrics
