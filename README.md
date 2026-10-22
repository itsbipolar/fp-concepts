# fp-concepts

**Latest build:** [Salary or dividend](explorations/salary-or-dividend/README.md) — one payment changes tax treatment, the CPP earnings record and next year's RRSP room. [Download and try the visual prototype](https://github.com/itsbipolar/fp-concepts/raw/refs/heads/codex/explorations/salary-or-dividend/salary-or-dividend.zip). Quantified tax outcomes remain pending primary-source verification.

**Selected direction:** [Within reach](explorations/within-reach/README.md), the cut-paper treatment of company ownership, now has a working interaction. [Download and try it](https://github.com/itsbipolar/fp-concepts/raw/refs/heads/codex/explorations/within-reach/within-reach.zip). **The colossus** and **Separate bodies** remain in the [style-frame archive](explorations/style-frames/README.md) for possible future use. [Download all three style frames](https://github.com/itsbipolar/fp-concepts/raw/refs/heads/codex/explorations/style-frames/style-frames.zip).

## Start a new chat

Attach this repository and use branch `codex`. The repository's [AGENTS.md](AGENTS.md) is the entry point; [project state](docs/PROJECT-STATE.md) carries the compact handoff. A useful opening instruction is:

> Use the fp-visual-build project skill on codex to build [financial concept]. Follow the approved Within reach references and the model-routing workflow. Develop the visual explanation from the financial relationships.

For unfinished work, replace “build [financial concept]” with “continue [lesson path] from its brief and project state.” A chat without repository access cannot retrieve this workflow automatically.

- [Drawing, texture and figure rules](docs/STYLE-SYSTEM.md), [reference assets](design/within-reach/asset-manifest.json) and [style tokens](design/within-reach/style-tokens.json).
- [Build phases and model routing](docs/BUILD-WORKFLOW.md), [interaction principles](docs/INTERACTION-PRINCIPLES.md) and [project skill](.agents/skills/fp-visual-build/SKILL.md).
- Templates for [lesson briefs](docs/templates/LESSON-BRIEF.md), [image prompts](docs/templates/IMAGE-PROMPT.md), [asset provenance](docs/templates/ASSET-RECORD.json) and [bounded agent tasks](docs/templates/AGENT-TASK.md).

Recommended main model for routine work: **Sol, medium**. Reserve **Astra high/ultra** for the difficult visual or causal decisions described in the routing guide. The app/user selects the main model; the workflow directs subagents where supported. It does not install or change model settings.

Check the portable kit with `python3 scripts/check_visual_system.py` (no dependencies beyond Python 3.9+). It checks references, hashes, palette anchors and local links; visual fidelity still needs screenshot review. New generated art uses the approved image references and saved prompts; reusing existing assets provides exact visual continuity.

## Historical concept-machine approach

The following records the earlier implementation. Its invented-machine workflow applies to legacy figures; use the current project skill for new work.


**Concept machines for Canadian financial planning.** Colourful, hand-inked isometric contraptions you can turn
around, look inside and operate, whose moving parts follow a real planning rule: the OAS clawback as a weir that
skims 15% of everything spilling over $95,323, an estate freeze as a block of ice with new shares sprouting from it,
death and taxes as a toll bridge with a spousal bypass lane. Made for client education and marketing in Canadian
wealth management.

Built on [Colorfigures](https://april-zhu.com/colorfigures) by April Zhu (MIT), which draws real machines (toasters,
claw machines) the same way.

## How it works
1. Pick a concept from the [catalog](docs/CONCEPT-CATALOG.md).
2. Write a brief: the rule, its numbers ([fact ledger](docs/FACT-LEDGER-2026.md)), the misconception, and the
   mapping from rule to machine ([metaphor grammar](.claude/skills/fp-figures/references/metaphor-grammar.md)).
3. Build the figure with the [fp-figures skill](.claude/skills/fp-figures/SKILL.md): one self-contained HTML page.
4. Verify it from every angle and check its numbers; run the [compliance checklist](docs/COMPLIANCE.md).
5. Export stills and a turntable clip for social ([pipeline](docs/PIPELINE.md)).

## Repo map
| Path | What |
|---|---|
| `CLAUDE.md` | project memory for Claude Code sessions |
| `.claude/skills/fp-figures/` | the skill, engine, kit and scripts |
| `docs/` | [vision](docs/VISION.md), [catalog](docs/CONCEPT-CATALOG.md), [facts](docs/FACT-LEDGER-2026.md), [sources](docs/SOURCES.md), [compliance](docs/COMPLIANCE.md), [brand](docs/BRAND.md), [pipeline](docs/PIPELINE.md), [roadmap](docs/ROADMAP.md), [decisions](docs/DECISIONS.md) |
| `figures/` | one folder per figure |
| `sources/` | versioned source material (v0: CFP crash notes) |
| `vendor/` | the original Colorfigures skill zip |

Figures are educational illustrations, not financial, tax or legal advice.
