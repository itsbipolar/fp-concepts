---
name: fp-figures
description: Turn an abstract Canadian financial-planning concept (a tax rule, a registered account, a clawback, a rollover, an estate tool, an insurance test) into a colourful, hand-inked, interactive isometric "concept machine" — one self-contained HTML page whose moving parts ARE the rule. Built on the Colorfigures engine. Use whenever the user wants to visualise, explain, illustrate or market a financial planning / wealth management / tax / retirement / estate / insurance concept for clients, a "concept machine", an "FP figure", or picks an item from docs/CONCEPT-CATALOG.md — even if they don't name the skill.
---

# FP Figures: concept machines for financial planning

Colorfigures draws real machines (a toaster, a claw machine) so people can see how they work. **FP Figures draws
machines that don't exist**: invented contraptions whose parts, paths and limits follow a financial rule exactly, so a
client watches the rule work. A TFSA is a sealed glass jar; an RRSP is a jar with a tax tap on its outlet; the OAS
clawback is a weir that skims 15 cents of every dollar spilling over a line at $95,323.

The drawing engine, its look and its drawing contract are unchanged from Colorfigures. This file adds the layer on top:
**rule -> mechanism -> figure**. Read both.

## Files
- `references/colorfigures-SKILL.md`: the upstream drawing contract (coordinates, depth sorting, see-through, labels,
  interaction, reserved names, verify). **Every rule in it still applies.** Read it before writing geometry.
- `references/metaphor-grammar.md`: how a rule becomes a machine: the money materials, the 10 machine archetypes, the
  5 metaphor tests, worked translations. Read it before writing the brief.
- `references/engine-cheatsheet.md`: the core.js + fp-kit.js API on one page, and the gotchas found so far.
- `assets/core.js`: the Colorfigures engine (upstream, unmodified). `assets/fp-kit.js`: FP palettes, `FP_FACTS`
  (the 2026 numbers), `fpFedTax`, money formatting and props, `fpPage()` (disclaimer + export modes).
- `assets/examples/`: upstream toaster (smallest), lamp, claw (dense see-through). Read toaster.html before a first figure.
- `scripts/build.py figure.html OUT.html`: inlines core.js and fp-kit.js and adds zoom, phone layout, switches.
- `scripts/shoot.py`: verify angles, press runs, error check, social stills, turntable MP4/GIF.
- Project docs (repo root): `docs/CONCEPT-CATALOG.md` (what to build), `docs/FACT-LEDGER-2026.md` (every number and
  its source), `docs/COMPLIANCE.md` (publishing rules), `docs/BRAND.md`, `docs/PIPELINE.md`,
  `docs/templates/FIGURE-BRIEF.md`.

## Workflow
1. **Pick the concept** from `docs/CONCEPT-CATALOG.md` (or add it there first). One figure = one idea.
2. **Write the brief** at `figures/<slug>/BRIEF.md` from `docs/templates/FIGURE-BRIEF.md`, before any code:
   - *The rule, plain:* 1–3 sentences a client would understand.
   - *The rule, exact:* the steps, tests and numbers, each number taken from `docs/FACT-LEDGER-2026.md` (add it there
     with its source if missing). Anything not in a source is marked **UNSOURCED** and must be sourced before publishing.
   - *The misconception* it corrects (the crash notes' "Trap" boxes are a goldmine): the figure must make the wrong
     belief visibly wrong.
   - *Mapping table:* every rule component -> one machine part, with what moves and why (see the grammar).
   - *Persona and numbers:* a fictional client with round, realistic HNW numbers and the expected results worked by hand.
   - *Buttons* (2–5 client decisions or life events, in order), *stats* (the computed dollars), *see-through parts*
     (the mechanics of the "why"), *labels* (the real terms: TFSA, ACB, FMV, CDA).
   - Run the **5 metaphor tests** (grammar file) and write the answers in the brief.
3. **Write the figure** at `figures/<slug>/figure.html`: shell, `<script src="core.js">`, `<script src="fp-kit.js">`,
   one inline script. At the top of the script: the notes, the rule steps and the parts list (as upstream asks), then
   geometry, then `mountFigure({...})`, `xrMount(...)` if it has a see-through, and last `fpPage({...})`.
   - All rule numbers come from `FP_FACTS` (add new ones to fp-kit.js **and** the ledger together). No magic numbers.
   - Stats are computed live from state with the same formula as the brief; the hand-worked persona must reproduce.
   - `params(st, q)` reads every interesting state from the URL (`?income=150000&split=1`) for screenshots.
4. **Build:** `python3 .claude/skills/fp-figures/scripts/build.py figures/<slug>/figure.html figures/<slug>/dist/<slug>.html`
5. **Verify** (`docs/PIPELINE.md` has the commands): every angle closed and see-through, a press run, the error check,
   a phone shot, and the **numbers check**: load the persona's URL state, read the stats in the shot, compare with the
   brief's hand calculation. Fix and repeat (at most 3 rounds), then add `turn:'full'`.
6. **Compliance pass** against `docs/COMPLIANCE.md`; record the result in the brief.
7. **Export** marketing assets with `shoot.py social` / `shoot.py spin` into `figures/<slug>/dist/`.
8. **Log it:** update the figure's row in `docs/CONCEPT-CATALOG.md` (status), `docs/ROADMAP.md`, and any new
   lesson in `references/engine-cheatsheet.md` or a decision in `docs/DECISIONS.md`.

## Truth first, for rules
Upstream says "research the real object". Here the object is a rule, so:
- **Every moving path is a real path of money or ownership.** Money only flows where the rule lets it: contribution ->
  account -> growth -> withdrawal -> tax. If a dollar can't legally go somewhere, there is no pipe there.
- **Every limit is a physical limit at the right number**: a fill line, a gate width, a counter's last tooth. Scale the
  machine so the numbers read (a level line at $95,323 sits at the height that value implies on the same scale as
  the income column).
- **Order of operations is the order of the machine**: gross-up before the marginal rate before the credit; total
  income -> net income (the clawback reads here) -> taxable income.
- **Time is a real clock**: deadlines, schedules and waiting periods are counters, calendars or ratchets with the real
  count of steps (HBP = 15 teeth; spousal RRSP = 3 calendar-year drums).
- **Who owns what is visible**: every container carries a nameplate (YOU, SPOUSE, CHILD, ESTATE, TRUST, OPCO).
  The tax collector is a neutral grey box labelled TAX (never a government logo, crest or wordmark).
- **Simplify openly, never wrongly.** Leave out provincial tax, credits or edge cases if needed, say so in the
  disclaimer note (`fpPage({ note })`) — but nothing drawn may contradict the rule.

## Look (FP additions)
- Domain palettes in fp-kit: `tax`, `inv`, `ret`, `ins`, `est`, `fpp` (from the crash-notes colour code) plus `navy`,
  `gold`. Set `palette:` to the concept's domain. Money props: `FP_GOLD` coins (`fpCoinStack`), `FP_BILL` notes,
  `FP_SHELTER` glass for tax-sheltered containers, `FP_CRA` grey for anything the tax system takes.
- Machines stand on a `board()` (a desk-top contraption) unless they are big "plant" machines.
- Text: plain ASCII. `$` and `%` are fine; no emoji, no arrows, no special symbols (they render as blobs).

## Interaction (FP additions)
- **Buttons are client decisions or life events** ("Turn 65", "Withdraw $40k from RRIF", "Split pension",
  "Freeze the company", "Pass away"). A press runs the real step; out-of-order presses explain (`ui.flash`).
- **Stats are the money that matters**: tax paid, OAS kept, grant received, value frozen. Big number top right.
- **The aha is a contrast**: let the client run the wrong way and the right way (withdraw from RRIF vs TFSA) and see
  the stat change. Design the buttons around that contrast.
- No advice wording on buttons ("You should..."): neutral verbs only.

## When to use something else
- A real physical object (a vault, a coin counter) with no rule: upstream Colorfigures rules alone are enough.
- A chart of numbers over time (a projection): use a chart, not a machine (see the dataviz skill).
