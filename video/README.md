# Within reach — motion study 01

The established cut-paper artwork, now staged for a film. This is a **nine-second silent style calibration**, not a completed salary/dividend explainer. It tests continuity of the actual texture and figures, a payment's movement, and a wider view that introduces the older owner.

**[Download / play the MP4](https://github.com/itsbipolar/fp-concepts/raw/refs/heads/codex-video/video/review/within-reach-motion-study.mp4)** · [Six-frame sequence](review/contact-sheet.png) · [Final frame](review/frame-269.png)

![Within reach in motion: payment today, older owner later](review/frame-269.png)

The movie is H.264 MP4, 1280×720, 30 fps, 9 seconds, with no audio track. Download it if GitHub opens a file page rather than a player. No code or server is required to watch it.

## What is installed

- A working isolated **Remotion 4.0.497 / React 19.2.8** workspace with a lockfile, editable [composition](src/WithinReach.tsx), [brief and beat map](BRIEF.md), asset preparation, still rendering and MP4 export.
- The original company, owner, payment and latest older-owner PNGs, referenced through [checksums](asset-manifest.json). Runtime copies are regenerated under ignored `public/assets/`; the source artwork is unchanged.
- A local Liberation Sans Bold font matching the project's quiet sans-serif interface approach; its SIL OFL notice is in [public/fonts/LICENSE.txt](public/fonts/LICENSE.txt). Rendering needs no font CDN, image API or voice provider.
- [Video direction](../docs/VIDEO-DIRECTION.md), [workflow](../docs/VIDEO-WORKFLOW.md), [video skill](../.agents/skills/fp-video-build/SKILL.md) and [reference manifest](../design/within-reach/video-reference-manifest.json) for consistent future work.
- The exact [uploaded motion kit](../vendor/motion-kit/README.md), indexed for selective reading. Its production sequence and Remotion approach inform this workspace. Stock imagery, font loaders, image conversions and installer instructions are not imported. Optional sound/transcription helpers remain in the archive, not installed capabilities.

## Reproduce

Prerequisites: Node.js/npm, an installed Chrome/Chromium, Python 3 and FFmpeg/ffprobe. Tested with Node 24 and the managed environment's `/usr/bin/chromium`. Use the committed lockfile:

```sh
cd video
npm ci
npm run check    # prepares assets, bundles and renders six PNGs
npm run render   # renders those PNGs and the silent MP4
npm run verify   # checks actual outputs, then creates the contact sheet
npm run studio  # optional interactive Remotion timeline
```

For a browser installed elsewhere, set `REMOTION_BROWSER_EXECUTABLE` to its full path before running check/render. The scripts do not automatically download a browser. The managed session used `npm ci --cache /tmp/fp-video-npm` when a writable cache was needed. `npm run check` is a render/bundle check, **not a TypeScript typecheck**. It does not refresh the MP4; use render then verify for delivery.

`review/` contains the portable MP4, PNGs, contact sheet, [render input/output hashes](review/render-manifest.json) and [validation results](review/validation.json). `.cache/`, `node_modules/`, `out/` and prepared asset copies are ignored. Fonts and assets load locally. Image/text decoding is awaited before capture; a missing font or image fails rendering.

## Read the sequence

At the opening, a figure leans on the blue company. One orange payment lifts out and moves to his open hand. The composition widens; the same character at a later age appears with an ivory sheet marked “Later.” The money stays with the present-day owner. The final image holds for approximately two seconds.

This tests an editorial transition from today's action toward later consequences. It does not specify a payment type, calculate a tax result, show pension growth or claim that the paper represents a cash balance. The next financial film needs its own sourced causal explanation, scene changes, and narration/captions if appropriate.

## Review status

The actual opening, transfer, reframing and settled renders were inspected against the source art. Material, palette, complete silhouettes and original character identities are retained; code text is separate from the pixels. Output checks verify hashes, dimensions, 270 decoded frames, duration, silent stream and final hold. [Native browser playback](review/playback.json) reached the end with zero dropped frames and no media error. Detailed scope is in [the brief](BRIEF.md).

The user responded positively to this motion study (“okay its good”). It is the current starting point for motion; a complete financial film needs its own factual and creative review. The interactive baseline remains on [`codex`](https://github.com/itsbipolar/fp-concepts/tree/codex). Both [alternative style frames](../explorations/style-frames/README.md) are preserved.

The next film also uses the integrated [editorial playbook](../docs/VIDEO-EDITORIAL.md), [topic bank](editorial/README.md), and [evidence/delivery workflow](../docs/VIDEO-EVIDENCE.md), selectively adapted from the user's other video studio.
