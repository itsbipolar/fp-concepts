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
