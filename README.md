# fp-concepts

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
