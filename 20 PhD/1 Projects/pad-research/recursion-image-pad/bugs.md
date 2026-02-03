---
---
# Bug checklist (recursion-image-pad)

Use a short checklist-style tracker for active bugs. Keep each bug to one line with a minimal command/path and expected vs actual. When fixed, tick the box and add a short note inline.

Open bugs

- [ ] rim-bug-001 — artifact mismatch on edge-case images — cmd: `python pad_recursion.py --input samples/img1.png` — expected: reasonable fill — actual: obvious seam — notes: high-frequency textures

How to add a bug (one line)

`- [ ] <id> — <short title> — cmd: \\`<command>\\` — expected: <what should happen> — actual: <what happens> — notes: <short context or sample path>`

When fixed

- Replace `- [ ]` with `- [x]` and append ` — fixed: <short summary>` with the commit id or reference.

Examples

- [x] rim-bug-000 — small visual artifact — cmd: `python pad.py` — expected: clean fill — actual: small seam — fixed: smoothing added (commit def456)

---
