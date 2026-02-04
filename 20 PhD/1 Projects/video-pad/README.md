# video-pad

Objective
- Explore video-based padding techniques to improve temporal consistency for PAD.

Where to find things
- Runs: `runs.md` (qualitative notes + quantitative table)
- Learnings: `learnings.md`
- Bugs: `bugs.md` (checklist-style)
- Artifacts: store externally — put short references/URLs in run entries, not files in this repo
- Tests: none (keep repo lightweight)

Notes
- Inbox ideas: `../../../../../../00 Inbox/new video pad idea.md`
- Keep bug reports minimal: a short command or small sample path and expected vs actual output is enough. Avoid creating extra reproducer files unless absolutely necessary.

Run example
```
python train.py --cfg cfgs/vp.yaml --seed 42
```
