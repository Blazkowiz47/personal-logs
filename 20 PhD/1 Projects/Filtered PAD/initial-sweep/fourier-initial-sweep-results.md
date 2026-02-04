# Sweep Analysis Report

**Experiment**: fourier_filter_ocim

**User**: sushrut

**Sweep ID**: sweep_1762902559

**Generated**: 2025-11-17 14:47:29

---
# OCIM Results (lr: 0.001)

| Backbone | Protocol (OCI -> M) | Protocol (ICM -> O) | Protocol (OIM -> C) | Protocol (OCM -> I) |
|----------|-----------------|-----------------|-----------------|-----------------|
| resnet34 | (18.16%, 87.32%) | (17.21%, 89.20%) | (19.63%, 87.71%) | (20.44%, 82.61%) |
| vit_b_16 | (16.01%, 91.24%) | (13.12%, 91.79%) | (18.76%, 88.55%) | (20.43%, 84.48%) |
# OCIM Results (lr: 0.0001)

| Backbone | Protocol (OCI -> M) | Protocol (ICM -> O) | Protocol (OIM -> C) | Protocol (OCM -> I) |
| -------- | ------------------- | ------------------- | ------------------- | ------------------- |
| resnet34 | (18.84%, 87.56%)    | (17.03%, 90.67%)    | (18.68%, 87.50%)    | (26.28%, 77.63%)    |
| vit_b_16 | (21.86%, 83.16%)    | (16.91%, 90.08%)    | (8.38%, 96.64%)     | (19.77%, 85.85%)    |

## Summary

- **Total Runs**: 16
- **Completed**: 16
- **Failed**: 0
- **Success Rate**: 100.0%

## Top Performers

### 1. backbone_vit_b_16_testset_test_casia_lr_0.0001_seed_2025

- **test/[global] eer**: 8.3778 (best epoch: 3)
- **params.accelerator.devices**: [0, 1, 2, 3]
- **params.accelerator.gradient_accumulation_steps**: 1
- **params.accelerator.strategy**: ddp
- **params.accelerator.type**: multi_gpu
- **params.best_metric_key**: eer
- **params.callbacks.batch_visualizer.max_visualizations_per_epoch**: 10
- **params.callbacks.batch_visualizer.visualization_probability**: 0.01
- **params.callbacks.checkpoint.mode**: min
- **params.callbacks.checkpoint.monitor**: validation/[global] eer
- **params.callbacks.checkpoint.save_best**: True
- **params.callbacks.checkpoint.save_last**: True
- **params.callbacks.data_refresher.dataset_refresh_epochs**: 1
- **params.callbacks.data_refresher.enable_dataset_refresh**: True
- **params.callbacks.data_refresher.enable_frame_refresh**: True
- **params.callbacks.data_refresher.frame_refresh_epochs**: 1
- **params.callbacks.data_refresher.frame_refresh_splits**: ['train', 'validation', 'test']
- **params.callbacks.early_stopping.min_delta**: 0.001
- **params.callbacks.early_stopping.mode**: min
- **params.callbacks.early_stopping.monitor**: validation/[global] eer
- **params.callbacks.early_stopping.patience**: 5
- **params.callbacks.early_stopping.target_mode**: less_equal
- **params.callbacks.early_stopping.target_value**: 0.0
- **params.callbacks.metric_logger.log_frequency**: 1
- **params.criterions.crossentropy.label_smoothing**: 0.15
- **params.criterions.crossentropy.name**: crossentropy
- **params.dataset.augmentation.standard.height**: 224
- **params.dataset.augmentation.standard.width**: 224
- **params.dataset.batch_size**: 32
- **params.dataset.cache.cache_dir**: .cache
- **params.dataset.cache.cache_splits**: ['train', 'validation', 'test']
- **params.dataset.cache_resize.height**: 256
- **params.dataset.cache_resize.width**: 256
- **params.dataset.class_order**: ['real', 'attack']
- **params.dataset.face_detected_and_resized_cache**: True
- **params.dataset.frames_per_video**: 30
- **params.dataset.height**: 224
- **params.dataset.name**: ocim
- **params.dataset.nickname**: test_casia
- **params.dataset.num_classes**: 2
- **params.dataset.num_workers**: 2
- **params.dataset.prefetch_factor**: 2
- **params.dataset.sampler.attack_balanced.balance_method**: undersample
- **params.dataset.sampler.attack_balanced.max_samples_per_attack**: 40000
- **params.dataset.seed**: 2025
- **params.dataset.test_dataset**: Casia_fasd
- **params.dataset.use_face_detection**: True
- **params.dataset.width**: 224
- **params.experiment.description**: Experimenting with fourier filtering techniques for PAD
- **params.experiment.name**: fourier_filter
- **params.metric_managers.pad.best_metric_key**: eer
- **params.metric_managers.pad.genuine_class_idx**: 0
- **params.metric_managers.pad.name**: pad
- **params.metric_managers.pad.per_attack**: False
- **params.metric_managers.pad.verbose_metrics**: False
- **params.metric_managers.standard.name**: standard
- **params.models.fourier_filter.augmentation.high_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.low_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.rgb_zero_prob**: 0.0
- **params.models.fourier_filter.backbone**: vit_b_16
- **params.models.fourier_filter.seed**: 2025
- **params.optimizers.main.lr**: 0.0001
- **params.optimizers.main.name**: adamw
- **params.optimizers.main.weight_decay**: 1e-07
- **params.runtime.log_level**: INFO
- **params.runtime.name**: fourier_filter
- **params.runtime.output_dir**: artifacts
- **params.runtime.tags**: []
- **params.schedulers.main.name**: onecycle
- **params.seed**: 2025
- **params.trainer.fourier_filter.epochs**: 30
- **params.trainer.fourier_filter.name**: fourier_filter
- **params.trainer.fourier_filter.print_freq**: 100
- **params.trainer.fourier_filter.seed**: 2025
- **params.trainer.fourier_filter.show_progress**: True
- **params.use_mlflow**: True
- **test/[global] apcer_at_bpcer_1_0**: 63.9630
- **test/[global] apcer_at_bpcer_3_0**: 23.6889
- **test/[global] apcer_at_bpcer_5_0**: 14.6296
- **test/accuracy**: 0.8961
- **test/auc**: 0.9664
- **test/f1**: 0.9272
- **test/loss**: 0.4334
- **validation/[global] apcer_at_bpcer_1_0**: 0.0000
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.0000
- **validation/accuracy**: 1.0000
- **validation/auc**: 1.0000
- **validation/f1**: 1.0000
- **validation/loss**: 0.2666
- **MLflow Run ID**: `loyal_root_z0r7xj4kcv`

### 2. backbone_vit_b_16_testset_test_casia_lr_0.001_seed_2025

- **test/[global] eer**: 12.0000 (best epoch: 2)
- **params.accelerator.devices**: [0, 1, 2, 3]
- **params.accelerator.gradient_accumulation_steps**: 1
- **params.accelerator.strategy**: ddp
- **params.accelerator.type**: multi_gpu
- **params.best_metric_key**: eer
- **params.callbacks.batch_visualizer.max_visualizations_per_epoch**: 10
- **params.callbacks.batch_visualizer.visualization_probability**: 0.01
- **params.callbacks.checkpoint.mode**: min
- **params.callbacks.checkpoint.monitor**: validation/[global] eer
- **params.callbacks.checkpoint.save_best**: True
- **params.callbacks.checkpoint.save_last**: True
- **params.callbacks.data_refresher.dataset_refresh_epochs**: 1
- **params.callbacks.data_refresher.enable_dataset_refresh**: True
- **params.callbacks.data_refresher.enable_frame_refresh**: True
- **params.callbacks.data_refresher.frame_refresh_epochs**: 1
- **params.callbacks.data_refresher.frame_refresh_splits**: ['train', 'validation', 'test']
- **params.callbacks.early_stopping.min_delta**: 0.001
- **params.callbacks.early_stopping.mode**: min
- **params.callbacks.early_stopping.monitor**: validation/[global] eer
- **params.callbacks.early_stopping.patience**: 5
- **params.callbacks.early_stopping.target_mode**: less_equal
- **params.callbacks.early_stopping.target_value**: 0.0
- **params.callbacks.metric_logger.log_frequency**: 1
- **params.criterions.crossentropy.label_smoothing**: 0.15
- **params.criterions.crossentropy.name**: crossentropy
- **params.dataset.augmentation.standard.height**: 224
- **params.dataset.augmentation.standard.width**: 224
- **params.dataset.batch_size**: 32
- **params.dataset.cache.cache_dir**: .cache
- **params.dataset.cache.cache_splits**: ['train', 'validation', 'test']
- **params.dataset.cache_resize.height**: 256
- **params.dataset.cache_resize.width**: 256
- **params.dataset.class_order**: ['real', 'attack']
- **params.dataset.face_detected_and_resized_cache**: True
- **params.dataset.frames_per_video**: 30
- **params.dataset.height**: 224
- **params.dataset.name**: ocim
- **params.dataset.nickname**: test_casia
- **params.dataset.num_classes**: 2
- **params.dataset.num_workers**: 2
- **params.dataset.prefetch_factor**: 2
- **params.dataset.sampler.attack_balanced.balance_method**: undersample
- **params.dataset.sampler.attack_balanced.max_samples_per_attack**: 40000
- **params.dataset.seed**: 2025
- **params.dataset.test_dataset**: Casia_fasd
- **params.dataset.use_face_detection**: True
- **params.dataset.width**: 224
- **params.experiment.description**: Experimenting with fourier filtering techniques for PAD
- **params.experiment.name**: fourier_filter
- **params.metric_managers.pad.best_metric_key**: eer
- **params.metric_managers.pad.genuine_class_idx**: 0
- **params.metric_managers.pad.name**: pad
- **params.metric_managers.pad.per_attack**: False
- **params.metric_managers.pad.verbose_metrics**: False
- **params.metric_managers.standard.name**: standard
- **params.models.fourier_filter.augmentation.high_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.low_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.rgb_zero_prob**: 0.0
- **params.models.fourier_filter.backbone**: vit_b_16
- **params.models.fourier_filter.seed**: 2025
- **params.optimizers.main.lr**: 0.001
- **params.optimizers.main.name**: adamw
- **params.optimizers.main.weight_decay**: 1e-07
- **params.runtime.log_level**: INFO
- **params.runtime.name**: fourier_filter
- **params.runtime.output_dir**: artifacts
- **params.runtime.tags**: []
- **params.schedulers.main.name**: onecycle
- **params.seed**: 2025
- **params.trainer.fourier_filter.epochs**: 30
- **params.trainer.fourier_filter.name**: fourier_filter
- **params.trainer.fourier_filter.print_freq**: 100
- **params.trainer.fourier_filter.seed**: 2025
- **params.trainer.fourier_filter.show_progress**: True
- **params.use_mlflow**: True
- **test/[global] apcer_at_bpcer_1_0**: 48.7259
- **test/[global] apcer_at_bpcer_3_0**: 32.5926
- **test/[global] apcer_at_bpcer_5_0**: 23.7926
- **test/accuracy**: 0.7652
- **test/auc**: 0.9261
- **test/f1**: 0.8170
- **test/loss**: 0.6591
- **validation/[global] apcer_at_bpcer_1_0**: 0.0000
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.0213
- **validation/accuracy**: 0.9998
- **validation/auc**: 1.0000
- **validation/f1**: 0.9999
- **validation/loss**: 0.2666
- **MLflow Run ID**: `khaki_nose_7vgjn34ksw`

### 3. backbone_vit_b_16_testset_test_oulu_lr_0.001_seed_2025

- **test/[global] eer**: 13.1245 (best epoch: 1)
- **params.accelerator.devices**: [0, 1, 2, 3]
- **params.accelerator.gradient_accumulation_steps**: 1
- **params.accelerator.strategy**: ddp
- **params.accelerator.type**: multi_gpu
- **params.best_metric_key**: eer
- **params.callbacks.batch_visualizer.max_visualizations_per_epoch**: 10
- **params.callbacks.batch_visualizer.visualization_probability**: 0.01
- **params.callbacks.checkpoint.mode**: min
- **params.callbacks.checkpoint.monitor**: validation/[global] eer
- **params.callbacks.checkpoint.save_best**: True
- **params.callbacks.checkpoint.save_last**: True
- **params.callbacks.data_refresher.dataset_refresh_epochs**: 1
- **params.callbacks.data_refresher.enable_dataset_refresh**: True
- **params.callbacks.data_refresher.enable_frame_refresh**: True
- **params.callbacks.data_refresher.frame_refresh_epochs**: 1
- **params.callbacks.data_refresher.frame_refresh_splits**: ['train', 'validation', 'test']
- **params.callbacks.early_stopping.min_delta**: 0.001
- **params.callbacks.early_stopping.mode**: min
- **params.callbacks.early_stopping.monitor**: validation/[global] eer
- **params.callbacks.early_stopping.patience**: 5
- **params.callbacks.early_stopping.target_mode**: less_equal
- **params.callbacks.early_stopping.target_value**: 0.0
- **params.callbacks.metric_logger.log_frequency**: 1
- **params.criterions.crossentropy.label_smoothing**: 0.15
- **params.criterions.crossentropy.name**: crossentropy
- **params.dataset.augmentation.standard.height**: 224
- **params.dataset.augmentation.standard.width**: 224
- **params.dataset.batch_size**: 32
- **params.dataset.cache.cache_dir**: .cache
- **params.dataset.cache.cache_splits**: ['train', 'validation', 'test']
- **params.dataset.cache_resize.height**: 256
- **params.dataset.cache_resize.width**: 256
- **params.dataset.class_order**: ['real', 'attack']
- **params.dataset.face_detected_and_resized_cache**: True
- **params.dataset.frames_per_video**: 30
- **params.dataset.height**: 224
- **params.dataset.name**: ocim
- **params.dataset.nickname**: test_oulu
- **params.dataset.num_classes**: 2
- **params.dataset.num_workers**: 2
- **params.dataset.prefetch_factor**: 2
- **params.dataset.sampler.attack_balanced.balance_method**: undersample
- **params.dataset.sampler.attack_balanced.max_samples_per_attack**: 40000
- **params.dataset.seed**: 2025
- **params.dataset.test_dataset**: Oulu
- **params.dataset.use_face_detection**: True
- **params.dataset.width**: 224
- **params.experiment.description**: Experimenting with fourier filtering techniques for PAD
- **params.experiment.name**: fourier_filter
- **params.metric_managers.pad.best_metric_key**: eer
- **params.metric_managers.pad.genuine_class_idx**: 0
- **params.metric_managers.pad.name**: pad
- **params.metric_managers.pad.per_attack**: False
- **params.metric_managers.pad.verbose_metrics**: False
- **params.metric_managers.standard.name**: standard
- **params.models.fourier_filter.augmentation.high_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.low_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.rgb_zero_prob**: 0.0
- **params.models.fourier_filter.backbone**: vit_b_16
- **params.models.fourier_filter.seed**: 2025
- **params.optimizers.main.lr**: 0.001
- **params.optimizers.main.name**: adamw
- **params.optimizers.main.weight_decay**: 1e-07
- **params.runtime.log_level**: INFO
- **params.runtime.name**: fourier_filter
- **params.runtime.output_dir**: artifacts
- **params.runtime.tags**: []
- **params.schedulers.main.name**: onecycle
- **params.seed**: 2025
- **params.trainer.fourier_filter.epochs**: 30
- **params.trainer.fourier_filter.name**: fourier_filter
- **params.trainer.fourier_filter.print_freq**: 100
- **params.trainer.fourier_filter.seed**: 2025
- **params.trainer.fourier_filter.show_progress**: True
- **params.use_mlflow**: True
- **test/[global] apcer_at_bpcer_1_0**: 52.7037
- **test/[global] apcer_at_bpcer_3_0**: 31.5775
- **test/[global] apcer_at_bpcer_5_0**: 24.6800
- **test/accuracy**: 0.7663
- **test/auc**: 0.9179
- **test/f1**: 0.8118
- **test/loss**: 0.6818
- **validation/[global] apcer_at_bpcer_1_0**: 0.0000
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.0000
- **validation/accuracy**: 0.9999
- **validation/auc**: 1.0000
- **validation/f1**: 0.9999
- **validation/loss**: 0.2672
- **MLflow Run ID**: `amiable_reggae_dz19smttmt`

### 4. backbone_resnet34_testset_test_msu_lr_0.0001_seed_2025

- **test/[global] eer**: 13.5446 (best epoch: 10)
- **params.accelerator.devices**: [0, 1, 2, 3]
- **params.accelerator.gradient_accumulation_steps**: 1
- **params.accelerator.strategy**: ddp
- **params.accelerator.type**: multi_gpu
- **params.best_metric_key**: eer
- **params.callbacks.batch_visualizer.max_visualizations_per_epoch**: 10
- **params.callbacks.batch_visualizer.visualization_probability**: 0.01
- **params.callbacks.checkpoint.mode**: min
- **params.callbacks.checkpoint.monitor**: validation/[global] eer
- **params.callbacks.checkpoint.save_best**: True
- **params.callbacks.checkpoint.save_last**: True
- **params.callbacks.data_refresher.dataset_refresh_epochs**: 1
- **params.callbacks.data_refresher.enable_dataset_refresh**: True
- **params.callbacks.data_refresher.enable_frame_refresh**: True
- **params.callbacks.data_refresher.frame_refresh_epochs**: 1
- **params.callbacks.data_refresher.frame_refresh_splits**: ['train', 'validation', 'test']
- **params.callbacks.early_stopping.min_delta**: 0.001
- **params.callbacks.early_stopping.mode**: min
- **params.callbacks.early_stopping.monitor**: validation/[global] eer
- **params.callbacks.early_stopping.patience**: 5
- **params.callbacks.early_stopping.target_mode**: less_equal
- **params.callbacks.early_stopping.target_value**: 0.0
- **params.callbacks.metric_logger.log_frequency**: 1
- **params.criterions.crossentropy.label_smoothing**: 0.15
- **params.criterions.crossentropy.name**: crossentropy
- **params.dataset.augmentation.standard.height**: 224
- **params.dataset.augmentation.standard.width**: 224
- **params.dataset.batch_size**: 32
- **params.dataset.cache.cache_dir**: .cache
- **params.dataset.cache.cache_splits**: ['train', 'validation', 'test']
- **params.dataset.cache_resize.height**: 256
- **params.dataset.cache_resize.width**: 256
- **params.dataset.class_order**: ['real', 'attack']
- **params.dataset.face_detected_and_resized_cache**: True
- **params.dataset.frames_per_video**: 30
- **params.dataset.height**: 224
- **params.dataset.name**: ocim
- **params.dataset.nickname**: test_msu
- **params.dataset.num_classes**: 2
- **params.dataset.num_workers**: 2
- **params.dataset.prefetch_factor**: 2
- **params.dataset.sampler.attack_balanced.balance_method**: undersample
- **params.dataset.sampler.attack_balanced.max_samples_per_attack**: 40000
- **params.dataset.seed**: 2025
- **params.dataset.test_dataset**: Msu_mfsd
- **params.dataset.use_face_detection**: True
- **params.dataset.width**: 224
- **params.experiment.description**: Experimenting with fourier filtering techniques for PAD
- **params.experiment.name**: fourier_filter
- **params.metric_managers.pad.best_metric_key**: eer
- **params.metric_managers.pad.genuine_class_idx**: 0
- **params.metric_managers.pad.name**: pad
- **params.metric_managers.pad.per_attack**: False
- **params.metric_managers.pad.verbose_metrics**: False
- **params.metric_managers.standard.name**: standard
- **params.models.fourier_filter.augmentation.high_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.low_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.rgb_zero_prob**: 0.0
- **params.models.fourier_filter.backbone**: resnet34
- **params.models.fourier_filter.seed**: 2025
- **params.optimizers.main.lr**: 0.0001
- **params.optimizers.main.name**: adamw
- **params.optimizers.main.weight_decay**: 1e-07
- **params.runtime.log_level**: INFO
- **params.runtime.name**: fourier_filter
- **params.runtime.output_dir**: artifacts
- **params.runtime.tags**: []
- **params.schedulers.main.name**: onecycle
- **params.seed**: 2025
- **params.trainer.fourier_filter.epochs**: 30
- **params.trainer.fourier_filter.name**: fourier_filter
- **params.trainer.fourier_filter.print_freq**: 100
- **params.trainer.fourier_filter.seed**: 2025
- **params.trainer.fourier_filter.show_progress**: True
- **params.use_mlflow**: True
- **test/[global] apcer_at_bpcer_1_0**: 77.4296
- **test/[global] apcer_at_bpcer_3_0**: 45.6866
- **test/[global] apcer_at_bpcer_5_0**: 25.2934
- **test/accuracy**: 0.8636
- **test/auc**: 0.9262
- **test/f1**: 0.9089
- **test/loss**: 0.4655
- **validation/[global] apcer_at_bpcer_1_0**: 0.0000
- **validation/[global] apcer_at_bpcer_3_0**: 0.0000
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.0124
- **validation/accuracy**: 0.9999
- **validation/auc**: 1.0000
- **validation/f1**: 0.9999
- **validation/loss**: 0.2667
- **MLflow Run ID**: `mango_kitchen_yhgns32lkd`

### 5. backbone_resnet34_testset_test_oulu_lr_0.0001_seed_2025

- **test/[global] eer**: 13.6677 (best epoch: 14)
- **params.accelerator.devices**: [0, 1, 2, 3]
- **params.accelerator.gradient_accumulation_steps**: 1
- **params.accelerator.strategy**: ddp
- **params.accelerator.type**: multi_gpu
- **params.best_metric_key**: eer
- **params.callbacks.batch_visualizer.max_visualizations_per_epoch**: 10
- **params.callbacks.batch_visualizer.visualization_probability**: 0.01
- **params.callbacks.checkpoint.mode**: min
- **params.callbacks.checkpoint.monitor**: validation/[global] eer
- **params.callbacks.checkpoint.save_best**: True
- **params.callbacks.checkpoint.save_last**: True
- **params.callbacks.data_refresher.dataset_refresh_epochs**: 1
- **params.callbacks.data_refresher.enable_dataset_refresh**: True
- **params.callbacks.data_refresher.enable_frame_refresh**: True
- **params.callbacks.data_refresher.frame_refresh_epochs**: 1
- **params.callbacks.data_refresher.frame_refresh_splits**: ['train', 'validation', 'test']
- **params.callbacks.early_stopping.min_delta**: 0.001
- **params.callbacks.early_stopping.mode**: min
- **params.callbacks.early_stopping.monitor**: validation/[global] eer
- **params.callbacks.early_stopping.patience**: 5
- **params.callbacks.early_stopping.target_mode**: less_equal
- **params.callbacks.early_stopping.target_value**: 0.0
- **params.callbacks.metric_logger.log_frequency**: 1
- **params.criterions.crossentropy.label_smoothing**: 0.15
- **params.criterions.crossentropy.name**: crossentropy
- **params.dataset.augmentation.standard.height**: 224
- **params.dataset.augmentation.standard.width**: 224
- **params.dataset.batch_size**: 32
- **params.dataset.cache.cache_dir**: .cache
- **params.dataset.cache.cache_splits**: ['train', 'validation', 'test']
- **params.dataset.cache_resize.height**: 256
- **params.dataset.cache_resize.width**: 256
- **params.dataset.class_order**: ['real', 'attack']
- **params.dataset.face_detected_and_resized_cache**: True
- **params.dataset.frames_per_video**: 30
- **params.dataset.height**: 224
- **params.dataset.name**: ocim
- **params.dataset.nickname**: test_oulu
- **params.dataset.num_classes**: 2
- **params.dataset.num_workers**: 2
- **params.dataset.prefetch_factor**: 2
- **params.dataset.sampler.attack_balanced.balance_method**: undersample
- **params.dataset.sampler.attack_balanced.max_samples_per_attack**: 40000
- **params.dataset.seed**: 2025
- **params.dataset.test_dataset**: Oulu
- **params.dataset.use_face_detection**: True
- **params.dataset.width**: 224
- **params.experiment.description**: Experimenting with fourier filtering techniques for PAD
- **params.experiment.name**: fourier_filter
- **params.metric_managers.pad.best_metric_key**: eer
- **params.metric_managers.pad.genuine_class_idx**: 0
- **params.metric_managers.pad.name**: pad
- **params.metric_managers.pad.per_attack**: False
- **params.metric_managers.pad.verbose_metrics**: False
- **params.metric_managers.standard.name**: standard
- **params.models.fourier_filter.augmentation.high_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.low_freq_zero_prob**: 0.0
- **params.models.fourier_filter.augmentation.rgb_zero_prob**: 0.0
- **params.models.fourier_filter.backbone**: resnet34
- **params.models.fourier_filter.seed**: 2025
- **params.optimizers.main.lr**: 0.0001
- **params.optimizers.main.name**: adamw
- **params.optimizers.main.weight_decay**: 1e-07
- **params.runtime.log_level**: INFO
- **params.runtime.name**: fourier_filter
- **params.runtime.output_dir**: artifacts
- **params.runtime.tags**: []
- **params.schedulers.main.name**: onecycle
- **params.seed**: 2025
- **params.trainer.fourier_filter.epochs**: 30
- **params.trainer.fourier_filter.name**: fourier_filter
- **params.trainer.fourier_filter.print_freq**: 100
- **params.trainer.fourier_filter.seed**: 2025
- **params.trainer.fourier_filter.show_progress**: True
- **params.use_mlflow**: True
- **test/[global] apcer_at_bpcer_1_0**: 58.0950
- **test/[global] apcer_at_bpcer_3_0**: 28.6762
- **test/[global] apcer_at_bpcer_5_0**: 23.5875
- **test/accuracy**: 0.8180
- **test/auc**: 0.9233
- **test/f1**: 0.8605
- **test/loss**: 0.5641
- **validation/[global] apcer_at_bpcer_1_0**: 0.1805
- **validation/[global] apcer_at_bpcer_3_0**: 0.0129
- **validation/[global] apcer_at_bpcer_5_0**: 0.0000
- **validation/[global] eer**: 0.3882
- **validation/accuracy**: 0.9956
- **validation/auc**: 0.9996
- **validation/f1**: 0.9971
- **validation/loss**: 0.2739
- **MLflow Run ID**: `dynamic_boot_6ksg2jyynt`

## Metric Statistics

| Metric | Mean ?? Std | Min | Max |
|--------|-----------|-----|-----|
| test/[global] apcer_at_bpcer_1_0 | 77.8840 ?? 19.0374 | 48.7259 | 98.7800 |
| test/[global] apcer_at_bpcer_3_0 | 61.9851 ?? 27.0940 | 23.6889 | 95.9667 |
| test/[global] apcer_at_bpcer_5_0 | 52.2149 ?? 27.7044 | 14.6296 | 92.3967 |
| test/[global] eer | 16.8654 ?? 4.1829 | 8.3778 | 24.3200 |
| test/accuracy | 0.8386 ?? 0.0535 | 0.7152 | 0.9030 |
| test/auc | 0.8887 ?? 0.0445 | 0.7972 | 0.9664 |
| test/f1 | 0.8856 ?? 0.0510 | 0.7607 | 0.9414 |
| test/loss | 0.5261 ?? 0.0961 | 0.4309 | 0.7402 |
| validation/[global] apcer_at_bpcer_1_0 | 0.0196 ?? 0.0542 | 0.0000 | 0.1805 |
| validation/[global] apcer_at_bpcer_3_0 | 0.0025 ?? 0.0074 | 0.0000 | 0.0277 |
| validation/[global] apcer_at_bpcer_5_0 | 0.0008 ?? 0.0031 | 0.0000 | 0.0123 |
| validation/[global] eer | 0.0625 ?? 0.1324 | 0.0000 | 0.4101 |
| validation/accuracy | 0.9991 ?? 0.0016 | 0.9950 | 1.0000 |
| validation/auc | 1.0000 ?? 0.0001 | 0.9996 | 1.0000 |
| validation/f1 | 0.9994 ?? 0.0010 | 0.9969 | 1.0000 |
| validation/loss | 0.2683 ?? 0.0026 | 0.2666 | 0.2739 |

## Visualizations

### Metric Evolution

![test/[global] eer](plots/metric_evolution_test_[global] eer.png)

![test/auc](20%20PhD/1%20Projects/Filtered%20PAD/initial-sweep/plots/metric_evolution_test_auc.png)

![test/f1](20%20PhD/1%20Projects/Filtered%20PAD/initial-sweep/plots/metric_evolution_test_f1.png)

![test/[global] apcer_at_bpcer_5_0](plots/metric_evolution_test_[global] apcer_at_bpcer_5_0.png)

![test/[global] apcer_at_bpcer_3_0](plots/metric_evolution_test_[global] apcer_at_bpcer_3_0.png)

![test/[global] apcer_at_bpcer_1_0](plots/metric_evolution_test_[global] apcer_at_bpcer_1_0.png)

![test/loss](20%20PhD/1%20Projects/Filtered%20PAD/initial-sweep/plots/metric_evolution_test_loss.png)

![test/accuracy](20%20PhD/1%20Projects/Filtered%20PAD/initial-sweep/plots/metric_evolution_test_accuracy.png)

![validation/loss](20%20PhD/1%20Projects/Filtered%20PAD/vit_initial_sweep/plots/metric_evolution_validation_loss.png)

![validation/[global] eer](plots/metric_evolution_validation_[global] eer.png)

### Metric Distributions

![Distributions](20%20PhD/1%20Projects/Filtered%20PAD/initial-sweep/plots/metric_distributions.png)

### Best Epochs

![Best Epochs](20%20PhD/1%20Projects/Filtered%20PAD/initial-sweep/plots/best_epochs.png)

