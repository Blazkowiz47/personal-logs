---
tags: [experiment, idea, pad, frequency-domain]
status: 🟡 Planned
date_created: 2025-11-28
---

# Experiment - Frequency Modalities for Flex-FAS

**Linked Papers:** [[fmf_fas]]

## 🔬 Hypothesis
Using **Fourier Transform** derived images (e.g., Low Pass Filtered and High Pass Filtered versions) as separate modalities in a Flexible-Modal framework will improve domain generalization compared to using raw RGB/Depth/IR.

**Why?**
- High-frequency components often contain spoofing artifacts (blur, moiré patterns).
- Low-frequency components capture the semantic face structure.
- Separating them might force the model to learn these distinct cues more robustly than a single RGB input.

## ⚙️ Setup
- **Base Model:** Flex-Modal FAS (from [[fmf_fas]])
- **Dataset:** [[CASIA-SURF]] (or Oulu-NPU for single modality test first)
- **Modalities:**
    1. **RGB** (Original)
    2. **LPF** (Low Pass Filtered RGB)
    3. **HPF** (High Pass Filtered RGB)

## 📝 Implementation Plan
- [ ] Implement on-the-fly FFT transform in the dataloader.
- [ ] Create a custom `FlexModal` config that accepts 3 inputs (RGB, LPF, HPF).
- [ ] Train baseline (RGB only).
- [ ] Train experimental model (RGB + LPF + HPF) with modality dropout.

## 📊 Results Log
| Run ID | Modalities | Train Set | Test Set | ACER (%) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | |

## 🧠 Analysis
*To be filled after experiments...*
