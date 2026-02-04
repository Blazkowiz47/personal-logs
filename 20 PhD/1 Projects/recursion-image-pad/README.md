# recursion-image-pad

Objective
- Explore recursion-based image padding techniques to generate plausible content for missing regions.

Where to find things
- Runs: `runs.md` (qualitative notes + quantitative table)
- Learnings: `learnings.md`
- Bugs: `bugs.md` (checklist-style)
- Artifacts: store externally — put short references/URLs in run entries, not files in this repo
- Tests: none (keep repo lightweight)

Run example
```
python train.py --cfg cfgs/rim.yaml --seed 42
```

Quantitative table template (copy into `runs.md`)

| metric | value | notes |
|---|---:|---|
| FID |  | lower is better |
| PSNR |  | |
| SSIM |  | |
| Runtime (s) |  | per image |

Usage
- Paste the table into the run entry after the YAML frontmatter and qualitative notes. Keep the README as a quick reference only.
