---
---
# Run entries for recursion-image-pad experiment
# Append one YAML frontmatter block per run followed by notes
---

Example run entry (paste and edit values):

---
date: 2026-02-03
exp_id: rim-001
experiment: recursion-image-pad
commit: <git-sha>
command: python train.py --cfg cfgs/rim.yaml --seed 42
config: cfgs/rim.yaml
dataset: my-image-dataset:v1
seed: 42
status: success
metrics:
  fid: 9.2
  ssim: 0.82
artifact: artifacts/rim-001.ckpt (sha256:...)
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

Quantitative metrics (table template)

| metric | value | notes |
|---|---:|---|
| FID |  | e.g. lower is better; reference eval script/command |
| PSNR |  | |
| SSIM |  | |
| Runtime (s) |  | per image |

Notes
- Paste the small table into the run entry after the YAML frontmatter. Keep qualitative observations above and the quantitative table here for quick scanning and copy/paste into reports.
