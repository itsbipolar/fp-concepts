# Decisions log

Newest last. Each entry: what was decided, why, and what would change it.

**D-001 (2026-10-22) Build on Colorfigures as a project skill, engine untouched.**
The upstream engine already solves the hard parts (free camera, depth sorting, see-through, labels, phone layout).
We add a layer (`fp-figures` skill, `fp-kit.js`) instead of forking `core.js`, so engine updates drop in
(`UPSTREAM.md`). The skill lives in `.claude/skills/` so every Claude Code session in this repo loads it.

**D-002 (2026-10-22) Concept machines are invented contraptions, faithful to the rule.**
Not diagrams on a board and not literal scenes (no people, no offices): machines whose physics behave like the rule.
The ten archetypes in the metaphor grammar are the starting vocabulary.

**D-003 (2026-10-22) One fact ledger, mirrored in code.**
Numbers drift every year; the same number appears in many figures. All rule numbers live in
`docs/FACT-LEDGER-2026.md` (with source) and `FP_FACTS` (for code). Next year: a `FACT-LEDGER-2027.md` and an
updated `FP_FACTS`, then rebuild every figure.

**D-004 (2026-10-22) Keep attribution.**
Colorfigures is MIT: the copyright notice must travel with copies. `build.py` stamps an attribution comment into
every built page, and interactive pages keep the "Made with Colorfigures" link by default. Marketing stills
(`?clean=1`) hide it, which is fine since the stills are images, not copies of the software.

**D-005 (2026-10-22) A disclaimer line is the one text exception.**
Upstream forbids explanation text on the page. Client-facing financial material needs a disclaimer and an as-of
date, so `fpPage()` adds one small line under the figure (also pinned in exports). Everything else stays on buttons
and labels.

**D-006 (2026-10-22) Federal figures only, unless a source covers the province.**
v0 is federal (with Ontario probate and Quebec withholding notes). Figures state "federal" in the disclaimer note.

**D-007 (2026-10-22) Sources are versioned.**
v0 = CFP crash notes. Every later document is v1, v2... in `sources/`, registered in `SOURCES.md`, and every catalog
row and ledger row cites the version it came from.

**D-008 (2026-10-22) Moved the uploaded files.**
`colorfigures.zip` -> `vendor/colorfigures.zip` (pristine upstream); `CFP crash notes.html` ->
`sources/v0-cfp-crash-notes/` with a `notes.txt` text extraction for search.

**D-009 (2026-10-22) Owner review of Fig. 01: an invented machine is too much.**
"Wrapping my head around a whole cylindrically engineered system is just doing too much." The figure is correct but
must be learned before it teaches. Kept in the repo as a reference; not for publishing as is.

**D-010 (2026-10-22) Plain charts rejected.**
Four quick non-physical sketches (`explorations/visual-directions.html`): "still confusing... basic charts... what does
'your income 122 dots' even mean". Charts lack the delight of Colorfigures; abstract units mean nothing.

**D-011 (2026-10-22, proposed) Everyday analogies.**
Explain each rule with one familiar everyday scene drawn in the Colorfigures style (Fig. 02: two garden beds, "tax the
seeds or tax the harvest"). Pending the owner's verdict. Details: `docs/VISUAL-DIRECTION.md`.

**D-012 (2026-10-22) Language rules are permanent.**
Plain sentences, "you", dollars, the real term once, no invented units; every label must read as a phrase on its own.

**D-013 (2026-10-22) A one-sentence story line under the scene.**
A second, deliberate exception to "no text on the page" (after the disclaimer, D-005): a plain sentence that changes
with each step (`fpStory`), because a 9th grader needs the "why" in words, not only in pictures.


**2026-10-22 — Review still art direction before another lesson.**
The owner rejected garden translation, numerical displays, overly literal streetscapes, and disconnected abstract studies. The agreed approach uses recognisable stylised subjects whose eventual behaviour will teach the relationship. Three static company/owner/money frames now test woodcut, sculpture and cut paper. No style is approved. The user authorized GitHub/web research and skill installation; a pinned Apache-2.0 Anthropic frontend-design skill is installed for Codex. Review files are committed and shared through GitHub because workspace paths were inaccessible and an environment restart lost uncommitted experiments.


**2026-10-22 — Within reach selected; alternatives retained.**
The owner chose the recommended cut-paper **Within reach** direction for active development and explicitly asked to keep **The colossus** and **Separate bodies** for possible later use. Preserve all three original style frames. The first ownership interaction is in development at `explorations/within-reach/`; its completion, validation and lesson approval are separate from this visual selection.


**Within reach: first ownership interaction implemented.**
Company, owner and one highlighted payment are separate layers. Movement reveals ownership groups; a deliberate dividend action transfers the highlighted payment to the owner. Personal-tax wording stays narrow and recognises the dividend tax credit. Repeated transfer, interrupted reset and conflicting input are guarded. Original alternative style frames remain intact. This implements the selected style but still awaits review of teaching effectiveness.
