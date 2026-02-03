---
---
# Run entries for video-pad experiment
# Append one YAML frontmatter block per run followed by notes
---

Example run entry (paste and edit values):

---
date: 2026-02-03
exp_id: vp-001
experiment: video-pad
commit: <git-sha>
command: python train.py --cfg cfgs/vp.yaml --seed 42
config: cfgs/vp.yaml
dataset: my-video-dataset:v1
seed: 42
status: success
metrics:
  fid: 12.3
  psnr: 28.1
artifact: artifacts/vp-001.ckpt (sha256:...)
tags: [baseline]
---
Title: Short title for this run

Hypothesis:
- add your hypothesis here

What I changed:
- bullet list of changes vs baseline

Observations:
- numeric results, qualitative notes, path to sample outputs

Next steps:
- 1) ...
