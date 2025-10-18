---
aliases: [pipeline refactoring, pad_candidate refactor, refactoring project]
tags: [work, project, mobai, pipeline, refactoring]
status: 🟡 In Progress
start_date: 2025-10-04
---

# Pipeline Refactoring

## Project Goal
Refactor pad_candidate repository to be scalable for PAD, MAD, DeepFake detection, and any deep learning research model.

## Status
🟡 Planning Phase

## Timeline
- **Start Date:** 2025-10-07
- **Target Completion:** 2025-10-21
- **Deadline:** 

## Background
Current pad_candidate repo has stitched pipelines (preprocessing, training, evaluation, research bench) that work but need refactoring for better scalability.

## Scope
### In Scope
- [x] PAD (Presentation Attack Detection)
- [x] MAD (Morph Attack Detection)
- [ ] DeepFake Detection
- [x] Generic deep learning research pipeline

### Out of Scope
- Production deployment (separate task)
- Frontend changes

## Current Architecture Issues
- [x] Tight coupling between components
- [x] Hardcoded PAD-specific logic
- [x] Duplicate code across pipelines
- [x] Difficult to add new attack types
- [x] Config management needs improvement

## Target Architecture

### Design Principles
1. **Separation of Concerns**
   - Data loading
   - Model training
   - Evaluation
   - Experimentation

2. **Modularity**
   - Pluggable components
   - Abstract interfaces
   - Config-driven

3. **Scalability**
   - Easy to add new attack types
   - Reusable components

### Proposed Structure
```
pad_candidate/
├── data/
│   ├── loaders/
│   ├── transforms/
│   └── datasets/
├── models/
│   ├── architectures/
│   ├── losses/
│   └── metrics/
├── training/
│   ├── trainer.py
│   ├── callbacks/
│   └── schedulers/
├── evaluation/
│   ├── evaluator.py
│   ├── fusion/
│   └── metrics/
├── research/
│   └── experiments/
└── configs/
    ├── pad/
    ├── mad/
    └── deepfake/
```

## Implementation Phases

### Phase 1: Architecture Design ✏️
- [x] Define abstract interfaces
- [x] Design config system
- [x] Document component interactions
- [x] Review with team

### Phase 2: Core Refactoring 🔨
- [x] Refactor data pipeline
- [x] Refactor training loop
- [x] Refactor evaluation pipeline
- [x] Update config management

### Phase 3: Attack Type Support 🎯
- [x] Ensure PAD still works
- [x] Add MAD support
- [x] Add DeepFake support
- [x] Generic attack type interface

### Phase 4: Testing & Documentation 📝
- [x] Unit tests for components
- [x] Integration tests
- [ ] Update documentation
- [ ] Migration guide

### Phase 5: PhD Pipeline Separation 🎓
- [ ] Create separate PhD pipeline
- [ ] Identical architecture
- [ ] Separate configs
- [ ] Independent experiments

## Technical Decisions

### Config System
**Decision:** Use Hydra for configuration management
**Reasoning:** 
- Hierarchical configs
- Easy overrides
- Type checking

### Code Organization
**Decision:** Modular packages with clear interfaces
**Reasoning:**
- Easy to test
- Easy to extend
- Clear dependencies

## Code & Implementation
**Repository:** pad_candidate
**Branch:** `refactor/scalable-pipeline`
**Key Files:**
- `design_doc.md`
- `architecture.md`

## Related Areas
- [[Pipeline Maintenance/Index|Pipeline Maintenance Area]]
- [[PAD Algorithm Development/Index]]

## Dependencies
- Must coordinate with: [[Score Fusion Analysis/Index]]
- Blocks: PhD pipeline creation

## Learnings
*Document insights as you refactor*


---
**Last Updated:** 2025-10-04

## Related Notes
- See [[Pipeline Maintenance/Index]] for ongoing maintenance tasks
- Link to specific refactoring notes in this folder
