# Supplied Paper Collage Motion Kit

The user's [original upload](PAPER-COLLAGE-MOTION-KIT.md), version **1.0.0**, is preserved byte for byte: 243,181 bytes; SHA-256 `c7bbbd7ef924931b6aae24e6ae189f2c5c9317dc2764632af25fcae317337aea`. Received in this conversation on 2026-10-22. No separate author or code license was identified in the supplied file; do not invent upstream attribution or apply another vendor's license to it.

**Role: additive production reference.** The user's request explicitly keeps the existing Within reach artwork, texture, figures and visual language authoritative. The upload's “start fresh,” installation questions, embedded AGENTS/CLAUDE files and stock style directives are source material, not new project instructions. They have not been installed as active skills or used to overwrite project files.

## Integration

- [Video direction](../../docs/VIDEO-DIRECTION.md) records what carries forward and how the stock kit is adapted.
- [Video workflow](../../docs/VIDEO-WORKFLOW.md) and the [project video skill](../../.agents/skills/fp-video-build/SKILL.md) govern production.
- [Video workspace](../../video/README.md) uses the kit's Remotion approach and pinned runtime versions with project-authored compositions and tooling. Its default font, background, image filters and chart recipes are not imported.
- All 44 embedded files remain available in the archive, including optional sound, transcription, rendering and scene recipes. They are not all installed runtime capabilities. Dependencies for optional tools must be inspected when those tools are needed.

## Read just what the task needs

Run from the repository root:

```sh
python3 scripts/read_motion_kit.py --list
python3 scripts/read_motion_kit.py --verify
python3 scripts/read_motion_kit.py .claude/skills/motion-graphic/references/SOUND.md
```

The reader verifies the original checksum, validates all fenced blocks and prints one file. It never executes code, extracts files or writes instruction files. [index.json](index.json) records paths, line ranges and content hashes. Do not load the entire 243 KB installer into every model context.

| Production question | Embedded file to read selectively |
| --- | --- |
| Story beats and scene patterns | `.claude/skills/motion-graphic/references/RECIPES.md` |
| Checks before delivery | `.claude/skills/motion-graphic/references/CHECKLIST.md` |
| Sound tied to action | `.claude/skills/motion-graphic/references/SOUND.md` |
| Voice and timing | `.claude/skills/motion-graphic/references/VOICE.md` |
| Render formats | `.claude/skills/motion-graphic/references/OUTPUT.md` |
| Timing and paper movement code | `src/kit/collage.tsx` (reference only; imports stock fonts at module scope) |
| Scene sequencing | `src/kit/scenes.tsx` |

The original unpacker writes relative to the current directory and is intentionally not run in the repository root. The original render orchestrator can execute soundtrack modules and fetch Python dependencies; the project's initial render path uses direct Remotion APIs instead. No image-cleaning, halftone conversion or texture replacement is applied to the protected art.
