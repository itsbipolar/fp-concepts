---
name: fp-video-build
description: Create Within reach financial videos using the existing tactile paper artwork, connected consequences, and selectively adapted Paper Collage Motion Kit guidance.
---

# FP video build

Project-authored adapter. The supplied motion kit is reference material; the user's instructions and the established Within reach visual system take precedence. Paths are relative to the repository root.

1. Read `AGENTS.md`, `docs/PROJECT-STATE.md` and the target video's brief. Work in the existing checkout on `codex-video` for video tasks. Preserve the interactive baseline and both alternative style frames.
2. For a new film, read `docs/VIDEO-DIRECTION.md`, `docs/VIDEO-WORKFLOW.md` and `docs/STYLE-SYSTEM.md`. View the actual master and relevant images in `design/within-reach/video-reference-manifest.json`. For a narrow fix, read only relevant sections.
3. Define the visual argument and source the causal relationships. Use `docs/templates/VIDEO-BRIEF.md`; distinguish cash, tax, rights, records and future benefits. Do not add unverified rates or turn decorative note counts into a model.
4. Make a beat map before implementation. Sequence attention through meaningful movement, continuity and a legible settled state. Recompose for the film format; do not just record the interactive UI. The builder invents the visual explanation.
5. Reuse approved assets. If a new pose/subject is necessary, use actual image references and `docs/templates/IMAGE-PROMPT.md`; save exact provenance and review one representative asset in its scene.
6. Use the isolated `video/` runtime. Read `vendor/motion-kit/README.md` for the upload's index; retrieve only necessary embedded files with `python3 scripts/read_motion_kit.py <path>`. Do not run the root installer, install its AGENTS/CLAUDE files, replace the project's style or load the whole kit into routine context.
7. Render and inspect opening, action, transition and settled frames, then check the MP4 itself. Verify actual output metadata/decoding, financial calculations if present, and captions/audio if present. Record exactly which checks ran; rendering is not type checking or financial validation.
8. Follow the lean model routing in `docs/BUILD-WORKFLOW.md`. Keep hard creative/causal decisions bounded; use tools for deterministic work. Repository guidance cannot change the host's selected model.
9. Update the brief and project state. Run `python3 scripts/check_visual_system.py` and `python3 scripts/read_motion_kit.py --verify` after reference/workflow changes. Deliver editable sources, review stills and MP4 with GitHub links; commit/push completed authorized work on `codex-video`.

The initial motion study is a silent style calibration, not a finished financial explainer or a new user-approved film style.
