# Sweep Analysis Report

**Experiment**: fourier_filter_ocim

**User**: sushrut

**Sweep ID**: sweep_1763107821

**Generated**: 2025-11-17 11:06:54

---

## Summary

- **Total Runs**: 8
- **Completed**: 8
- **Failed**: 0
- **Success Rate**: 100.0%

# OCIM Results

| Backbone | Protocol (OCI -> M) | Protocol (ICM -> O) | Protocol (OIM -> C) | Protocol (OCM -> I) |
| -------- | ------------------- | ------------------- | ------------------- | ------------------- |
| vit_b_16 | (19.77%, 88.15%)    | (15.52%, 91.80%)    | (11.34%, 94.06%)    | (21.89%, 78.11%)    |
| vit_b_32 | (16.76%, 90.50%)    | (15.74%, 90.14%)    | (16.80%, 90.73%)    | (15.39%, 91.36%)    |

## Top Performers

### 1. backbone_vit_b_16_test_casia_seed_2025

- **test/[global] eer**: 11.3370 (best epoch: 2)
- **test/[global] apcer_at_bpcer_1_0**: 76.0741
- **test/[global] apcer_at_bpcer_3_0**: 36.0815
- **test/[global] apcer_at_bpcer_5_0**: 22.7778
- **test/accuracy**: 0.8542
- **test/auc**: 0.9406
- **test/f1**: 0.8950
- **test/loss**: 0.4899
- **validation/[global] apcer_at_bpcer_1_0**: 0.0000
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.0000
- **validation/accuracy**: 0.9998
- **validation/auc**: 1.0000
- **validation/f1**: 0.9999
- **validation/loss**: 0.2668
- **MLflow Run ID**: `clever_panda_cd8nvkg9t1`

### 2. backbone_vit_b_32_test_msu_seed_2025

- **test/[global] eer**: 12.5266 (best epoch: 1)
- **test/[global] apcer_at_bpcer_1_0**: 49.3985
- **test/[global] apcer_at_bpcer_3_0**: 37.4090
- **test/[global] apcer_at_bpcer_5_0**: 27.2242
- **test/accuracy**: 0.7864
- **test/auc**: 0.9311
- **test/f1**: 0.8322
- **test/loss**: 0.5941
- **validation/[global] apcer_at_bpcer_1_0**: 0.0000
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.0124
- **validation/accuracy**: 0.9996
- **validation/auc**: 1.0000
- **validation/f1**: 0.9997
- **validation/loss**: 0.2675
- **MLflow Run ID**: `mighty_river_1dh2kfyj83`

### 3. backbone_vit_b_32_test_oulu_seed_2025

- **test/[global] eer**: 13.3497 (best epoch: 2)
- **test/[global] apcer_at_bpcer_1_0**: 44.6840
- **test/[global] apcer_at_bpcer_3_0**: 31.7500
- **test/[global] apcer_at_bpcer_5_0**: 25.5000
- **test/accuracy**: 0.7670
- **test/auc**: 0.9234
- **test/f1**: 0.8243
- **test/loss**: 0.6406
- **validation/[global] apcer_at_bpcer_1_0**: 0.0000
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.0173
- **validation/accuracy**: 0.9999
- **validation/auc**: 1.0000
- **validation/f1**: 0.9999
- **validation/loss**: 0.2667
- **MLflow Run ID**: `nifty_tangelo_hxm371dm5c`

### 4. backbone_vit_b_32_test_casia_seed_2025

- **test/[global] eer**: 14.9963 (best epoch: 2)
- **test/[global] apcer_at_bpcer_1_0**: 87.3185
- **test/[global] apcer_at_bpcer_3_0**: 47.6667
- **test/[global] apcer_at_bpcer_5_0**: 32.6444
- **test/accuracy**: 0.8731
- **test/auc**: 0.9212
- **test/f1**: 0.9146
- **test/loss**: 0.4666
- **validation/[global] apcer_at_bpcer_1_0**: 0.0055
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.0106
- **validation/accuracy**: 0.9997
- **validation/auc**: 1.0000
- **validation/f1**: 0.9998
- **validation/loss**: 0.2670
- **MLflow Run ID**: `plum_wire_kt255m7rxy`

### 5. backbone_vit_b_16_test_msu_seed_2025

- **test/[global] eer**: 15.2463 (best epoch: 1)
- **test/[global] apcer_at_bpcer_1_0**: 89.0874
- **test/[global] apcer_at_bpcer_3_0**: 48.7764
- **test/[global] apcer_at_bpcer_5_0**: 28.3392
- **test/accuracy**: 0.8514
- **test/auc**: 0.9226
- **test/f1**: 0.8942
- **test/loss**: 0.4835
- **validation/[global] apcer_at_bpcer_1_0**: 0.0000
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.1393
- **validation/accuracy**: 0.9986
- **validation/auc**: 1.0000
- **validation/f1**: 0.9991
- **validation/loss**: 0.2683
- **MLflow Run ID**: `helpful_steelpan_vhgdmmkyv3`

## Metric Statistics

| Metric | Mean ?? Std | Min | Max |
|--------|-----------|-----|-----|
| test/[global] apcer_at_bpcer_1_0 | 74.6661 ?? 21.9824 | 44.6840 | 100.0000 |
| test/[global] apcer_at_bpcer_3_0 | 50.0947 ?? 22.3935 | 31.7500 | 100.0000 |
| test/[global] apcer_at_bpcer_5_0 | 38.2518 ?? 25.4167 | 22.7778 | 99.9633 |
| test/[global] eer | 14.8131 ?? 2.6429 | 11.3370 | 20.1417 |
| test/accuracy | 0.8426 ?? 0.0561 | 0.7670 | 0.9224 |
| test/auc | 0.9105 ?? 0.0400 | 0.8136 | 0.9406 |
| test/f1 | 0.8878 ?? 0.0492 | 0.8243 | 0.9549 |
| test/loss | 0.5153 ?? 0.0878 | 0.3991 | 0.6406 |
| validation/[global] apcer_at_bpcer_1_0 | 0.0007 ?? 0.0019 | 0.0000 | 0.0055 |
| validation/[global] apcer_at_bpcer_3_0 | 0.0000 ?? 0.0000 | 0.0000 | 0.0000 |
| validation/[global] apcer_at_bpcer_5_0 | 0.0000 ?? 0.0000 | 0.0000 | 0.0000 |
| validation/[global] eer | 0.0235 ?? 0.0472 | 0.0000 | 0.1393 |
| validation/accuracy | 0.9997 ?? 0.0005 | 0.9986 | 1.0000 |
| validation/auc | 1.0000 ?? 0.0000 | 1.0000 | 1.0000 |
| validation/f1 | 0.9998 ?? 0.0003 | 0.9991 | 1.0000 |
| validation/loss | 0.2671 ?? 0.0005 | 0.2666 | 0.2683 |

## Visualizations

### Metric Evolution

![validation/[global] apcer_at_bpcer_5_0](plots/metric_evolution_validation_[global] apcer_at_bpcer_5_0.png)

![test/[global] eer](plots/metric_evolution_test_[global] eer.png)

![validation/f1](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/metric_evolution_validation_f1.png)

![test/f1](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/metric_evolution_test_f1.png)

![validation/loss](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/metric_evolution_validation_loss.png)

![validation/auc](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/metric_evolution_validation_auc.png)

![test/auc](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/metric_evolution_test_auc.png)

![test/[global] apcer_at_bpcer_3_0](plots/metric_evolution_test_[global] apcer_at_bpcer_3_0.png)

![test/[global] apcer_at_bpcer_5_0](plots/metric_evolution_test_[global] apcer_at_bpcer_5_0.png)

![test/accuracy](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/metric_evolution_test_accuracy.png)

### Metric Distributions

![Distributions](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/metric_distributions.png)

### Best Epochs

![Best Epochs](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/best_epochs.png)
