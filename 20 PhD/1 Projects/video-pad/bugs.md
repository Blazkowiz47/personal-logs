---
---
# Bug checklist (video-pad)

Use a short checklist-style tracker for active bugs. Keep each bug to one line with a minimal command/path and expected vs actual. When fixed, tick the box and add a short note inline.

Open bugs

- [ ] vp-bug-001 — OOM during pad_to_size() — cmd: `python pad.py --input samples/clip.mp4` — expected: completes — actual: OOM on GPU — notes: small clip only

How to add a bug (one line)

`- [ ] <id> — <short title> — cmd: \\`<command>\\` — expected: <what should happen> — actual: <what happens> — notes: <short context or sample path>`

When fixed

- Replace `- [ ]` with `- [x]` and append ` — fixed: <short summary>` with the commit id or reference.

Examples

- [x] vp-bug-000 — minor log typo — cmd: `python run.py` — expected: no stderr — actual: spammy log — fixed: removed debug prints (commit abc123)

---
