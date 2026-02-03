# pad-research

Project root for PAD research experiments (video-pad and recursion-image-pad).

Purpose
- Active development and reproducible experiment artifacts for PAD ideas.
- Keep detailed run logs, reproducible reproducers, and per-experiment bug trackers here.

Where things live
- Video-pad experiment: `20 PhD/1 Projects/pad-research/video-pad/`
- Recursion-image-pad experiment: `20 PhD/1 Projects/pad-research/recursion-image-pad/`

Conventions
- Experiment prefixes: `vp` = video-pad, `rim` = recursion-image-pad.
- Run id: `<prefix>-NNN` (e.g. `vp-001`) or timestamped `vp-20260203-01`.
- Bug id: `<prefix>-bug-###` (e.g. `vp-bug-001`).
- Fix id: `<prefix>-fix-###` (e.g. `vp-fix-001`).

Quick start
1. Add a run entry to the experiment's `runs.md` immediately after a run finishes.
2. If a bug appears, add it to `bugs.md` and put a minimal reproducer in `reproducers/`.
3. When fixed, add a `fixes.md` entry that references the bug id and verification steps.

Bug checklist (project-wide)
- Use the one-line checklist format in each experiment's `bugs.md` for quick tracking. Example template:

  `- [ ] <id> — <short title> — cmd: `<command>` — expected: <what should happen> — actual: <what happens> — notes: <path or short context>`

Run entry example
- See each experiment's `runs.md` for a recommended example run entry (YAML frontmatter + notes). Add runs immediately after completion to preserve reproducibility metadata (commit, command, dataset, artifact checksum).
