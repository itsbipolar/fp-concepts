# FP Concepts: project memory

**What this is:** interactive, hand-inked isometric "concept machines" that explain Canadian financial-planning
concepts (tax, retirement, estate, insurance, investments) to high-net-worth clients, for education and marketing.
Built on the Colorfigures engine (MIT). The machines are invented; **their mechanics are the rules**.

## Start here
- Making a figure -> follow the skill **`.claude/skills/fp-figures/SKILL.md`** (it points to everything else).
- What to build -> `docs/CONCEPT-CATALOG.md` (top picks at the top).
- Numbers -> `docs/FACT-LEDGER-2026.md` and `FP_FACTS` in `.claude/skills/fp-figures/assets/fp-kit.js` (change both).
- Commands -> `docs/PIPELINE.md`. Why things are the way they are -> `docs/DECISIONS.md`. Status -> `docs/ROADMAP.md`.

## Layout
```
.claude/skills/fp-figures/   the skill: SKILL.md, engine (assets/core.js, upstream), fp-kit.js, build.py, shoot.py,
                             references/ (metaphor grammar, engine cheat sheet, upstream Colorfigures SKILL.md)
docs/                        vision, catalog, fact ledger, sources, compliance, brand, pipeline, roadmap, decisions,
                             templates/FIGURE-BRIEF.md
figures/<slug>/              BRIEF.md, figure.html, dist/ (built page + exports); figures/_smoke = toolchain canary
sources/vN-<slug>/           versioned idea sources; v0 = CFP crash notes (HTML + notes.txt)
vendor/colorfigures.zip      pristine upstream skill
```

## Rules that always apply
1. **Truth first:** a figure may simplify but never contradict the rule. Every number comes from the ledger, with a
   source version and a re-check date; unsourced claims are marked UNSOURCED and block publishing.
2. **One machine, one idea**, built around the misconception it breaks.
3. **Brief before code** (`figures/<slug>/BRIEF.md`), with hand-worked persona numbers the figure must reproduce.
4. **Upstream drawing contract applies in full** (`references/colorfigures-SKILL.md`): every part sorted with a box,
   faces only when facing, see-through over the ghost, verify from every angle before `turn:'full'`.
5. **Education, not advice:** `fpPage()` disclaimer on every figure; compliance checklist before publishing; no
   government logos, no real client data, fictional personas only.
6. **Names:** never declare core.js reserved names in a figure; fp-kit globals start with `FP`/`fp`; figure globals
   take a short prefix. Never write a closing script tag inside an inlined script, even in a comment.
7. **Sources are versioned** (v0, v1...): new material goes through `docs/SOURCES.md` (file, register, mine, ledger).
8. Keep this memory current: after each figure, update the catalog status, roadmap, cheat-sheet gotchas and
   decisions.

## Environment notes
- Chromium: `/opt/pw-browsers/chromium` (cloud container; needs `--no-sandbox` as root, shoot.py handles it).
  ffmpeg is available for turntable clips.
- Pages <= 560 CSS px wide switch to the phone layout; marketing stills render wider (shoot.py social).

## Current status (update me)
- v0 foundation complete (2026-10-22).
- Fig. 01 OAS clawback (`figures/oas-clawback/`): invented-machine style; the owner found it too much to decode
  (D-009). Plain charts were rejected too (D-010).
- **Direction now (proposed, D-011): everyday analogies** — read `docs/VISUAL-DIRECTION.md` before any figure.
  Fig. 02 `figures/seeds-or-harvest/` (RRSP vs TFSA as two garden beds) is the prototype; waiting for the owner.
- **Language rules are permanent (D-012):** plain sentences a 9th grader follows, dollars not invented units.
- Open items: firm name/colours (`docs/BRAND.md`), compliance house rules (`docs/COMPLIANCE.md`), v1 sources.
