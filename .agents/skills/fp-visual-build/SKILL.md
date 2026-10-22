---
name: fp-visual-build
description: Build or extend FP Concepts interactive financial illustrations using the approved Within reach drawing style, connected causal effects, reference-driven image generation and economical agent routing.
---

# FP visual build

Project-authored skill. Paths below are relative to the repository root. This skill assembles the project's active workflow; it does not replace the user's instructions.

## Start with the smallest useful context

1. Read `AGENTS.md`, `docs/PROJECT-STATE.md` and the target lesson's brief. Use the current checkout on `codex`.
2. For a new lesson, read `docs/INTERACTION-PRINCIPLES.md`, `docs/STYLE-SYSTEM.md` and `docs/BUILD-WORKFLOW.md`. For a narrow fix, read only the relevant guidance and files; do not reload history or unrelated lessons.
3. Before artwork work, view the approved master and the relevant components listed in `design/within-reach/asset-manifest.json`. Inspect pictures, not filenames alone. Read `docs/templates/IMAGE-PROMPT.md` only when generating/editing assets.
4. Use the installed `frontend-design` skill for a new or redesigned interface. Keep the approved drawing language fixed; routine implementation is not an invitation to reopen style selection.

## Design and build

- Start a new lesson with `docs/templates/LESSON-BRIEF.md`. Research the causal map and verify the rules before quantifying. The builder originates the visual ideas.
- One decision can reveal immediate, connected and later effects. Sequence attention and preserve outcomes in one coherent scene. Distinguish money from liabilities, rights and future benefits.
- Reuse suitable approved assets. For a new subject, use the fixed style prompt plus a specific subject/action block and actual reference images. Review one representative asset in its scene before generating a whole family. Record the exact generation request using `docs/templates/ASSET-RECORD.json`; never invent missing historical model/seed information.
- Keep financial calculation state separate from animation. Replay, reset and rapid switching must preserve consistent results.
- Use source files for edits. Do not read embedded `play.html`, `review.html`, ZIPs or GIFs into model context when their source already exists.

## Route work deliberately

`docs/BUILD-WORKFLOW.md` specifies the default: Sol for scoped implementation, Astra only for a hard unresolved creative/financial problem, Luna optionally for simple bounded support. Use shell tools for deterministic work. These are available-model choices, not app configuration changes.

If delegation helps, use a fresh agent with an explicit supported model/effort and a compact `docs/templates/AGENT-TASK.md` packet. Avoid full-history forks that inherit Astra Ultra. Assign disjoint files. Do not create a team for a task one agent can finish efficiently. Use an independent review when the financial/interaction risk warrants it, not as a ceremonial extra pass.

## Finish and leave a clean handoff

1. Check the relevant financial examples, important interaction invariants, keyboard/touch/reduced motion and desktop/phone screenshots. Compare artwork to the actual reference. Run only checks appropriate to the change; docs-only edits do not need browser regression runs.
2. Run `python3 scripts/check_visual_system.py` after changing this workflow, tokens or the reference catalog. This validates files and protected hashes, not aesthetic similarity or financial correctness.
3. For the existing prototype, `python3 explorations/within-reach/package_review.py` rebuilds offline HTML and ZIP after source/asset changes. The style-frame archive has its own `package_review.py`; leave it alone unless it changed.
4. Update the lesson brief and `docs/PROJECT-STATE.md` with the concrete result, checks, blockers and next action. Keep logs compact; record measured usage only when available.
5. Commit and push completed authorized work on `codex`. Provide GitHub view/download links so review survives cloud resets. Preserve all original style frames.
