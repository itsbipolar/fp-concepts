# Video production workflow

Use on `codex-video`. The interactive baseline remains on `codex`; its source scenes and alternatives are also preserved here. The working entry point is the project [fp-video-build skill](../.agents/skills/fp-video-build/SKILL.md), with [video direction](VIDEO-DIRECTION.md) and the existing [drawing system](STYLE-SYSTEM.md). The user asked for the supplied motion kit to be additive.

## 1. Brief and visual argument

Start with [the video brief](templates/VIDEO-BRIEF.md). Define audience, question, financial scope, output format, runtime range and the single change the viewer must understand. Research material connected consequences, including timing and types of value. Resolve comparison assumptions before animating amounts. Use current primary sources; record unavailable verification rather than inventing values.

Use [the editorial playbook](VIDEO-EDITORIAL.md) to choose a documentary angle and story form. [The curated topic bank](../video/editorial/README.md) carries relevant questions from the user's other video studio. Pick one audience per cut; the existing motion study is now a positively reviewed starting point, not a complete financial film.

Develop a few possible visual mechanisms internally, then choose the clearest. Record a short visual argument: what happens, why it happens, and what the final image reveals. Do not ask the owner to design the metaphor. A film need not reproduce the interactive screen or preserve its UI controls.

For factual films, use [the evidence workflow](VIDEO-EVIDENCE.md): keep a per-film claims ledger, link both narration and shots to claim IDs, and reproduce calculations independently. Use the [script](templates/VIDEO-SCRIPT.md), [claims](templates/VIDEO-CLAIMS.json) and [delivery](templates/VIDEO-DELIVERY.json) templates as needed. These are authoring records; no automatic claims scanner or workbook generator is installed by the cross-repository transfer.

## 2. Reference lock and beat map

View the master and relevant actual assets in the [video reference manifest](../design/within-reach/video-reference-manifest.json). Reuse them before requesting new art. For every beat, note seconds/frames, visible action, intended inference, source/assumption, camera, text, sound and what remains visible afterward. Storyboard opening, main event, connected effects, comparison if needed, and final hold.

Write narration alongside the visual argument if it helps. If supplied narration must determine the timing, inspect its actual duration and align beats to it. Check approval/authorization for a paid service in the current task rather than assuming the attached guide itself grants access. The present workspace has no configured voice-generation provider.

Keep legal sections and full formulas in the evidence/backup; the film explains what the mechanism does in plain words. A quantified financial example should include the source studio's useful one-sheet workbook with live formulas and source quotes. A silent style study does not need that financial deliverable.

## 3. Build one representative passage

Use `video/` and its pinned Node dependencies. Build from source composition files, not the rendered movie. Keep financial calculations independent of frame timing. Images come from checksum-verified copies of the source assets; generated runtime copies are ignored by Git. Do not import the kit's font-loading visual module just to get a timing utility.

Before building a whole film or generating a large asset set, render the passage that tests the hardest visual relationship. Check material and figure continuity beside the original artwork. New assets use both the master and the closest relevant component as actual image references, with the existing prompt/provenance templates. Keep original assets unchanged.

## 4. Review the rendered film

- Render representative stills and inspect them, including the transition and settled result. Check readability at phone size and the intended aspect ratio. Use a contact sheet for temporal coverage, not as a substitute for motion review.
- Check that actions have one cause, money is not duplicated, rights do not disappear, and future effects are actually marked as future. Verify quantitative calculations separately when present.
- Render the MP4; verify duration, dimensions, frame rate, codec and decoding. Inspect movement timing, continuity and end hold. Record whether audio exists and which checks ran.
- For spoken work, provide accurate captions/transcript, check synchronization and loudness, and review the picture without sound. For silent work, provide a descriptive sequence and explicitly state that it is silent.

The current tooling bundles and renders React/TypeScript. It does not perform a TypeScript typecheck. Run the checks actually applicable to a change, and describe them accurately. Add focused tests for substantive financial state or reusable timing logic when needed, not tests that merely repeat styling constants.

## 5. Deliver and resume

Save source, brief/beat map, asset provenance, review stills, MP4 and validation evidence. Keep large intermediate render caches out of Git. Update `docs/PROJECT-STATE.md` and the film's brief with approval status, checks, limitations and next step. Commit and push authorized work on `codex-video`, supplying GitHub review/download links. Do not replace the `codex` baseline or the two archived style alternatives.

Prepare applicable captions, sources, model/backup and version-specific platform copy using the delivery record. Separate creative, factual and publication review. The source studio records firm review before public posting; that concerns posting, not completion of authorized internal drafts. No posting or outreach is authorized merely by preparing a pack. Carry relevant claim subsets into recomposed shorter cuts, then track actual publication, freshness and corrections.

## Use the kit without spending context on the installer

The [archive README](../vendor/motion-kit/README.md) maps production questions to individual embedded files. `python3 scripts/read_motion_kit.py <embedded-path>` retrieves one verified section without installing it. Read only what is needed for the task: sound when adding sound, voice when working with narration, scene recipes when a transition needs one. Optional kit scripts are retained source material, not all installed or tested capabilities.

## Model routing

Keep [the existing lean routing](BUILD-WORKFLOW.md): Sol medium for bounded implementation and ordinary review; Astra high/ultra for a specific unresolved visual architecture, causal explanation or difficult correctness question; optional Luna for simple mechanical support. Main-chat selection stays in the app. Use deterministic tools for asset inventories, hashes, packaging and rendering.

When delegation is available and authorized, give one executor a fresh, short packet and disjoint files. Escalate with the concrete decision needed, not the entire history or 243 KB kit. Preserve a selected creative decision as a compact beat map before routine implementation. Do not invent token savings or spend extra review calls without a distinct unresolved question.
