# Figures

One folder per concept machine:

```
figures/<slug>/
  BRIEF.md          the rule, sources, mapping, persona numbers, tests, compliance (from docs/templates/FIGURE-BRIEF.md)
  figure.html       the source: loads core.js + fp-kit.js, one inline script
  dist/<slug>.html  the built, self-contained page (commit it)
  dist/*.png|mp4|gif marketing exports (commit the approved ones)
  shots/            verification screenshots (git-ignored)
```

| Fig. | Slug | Catalog ID | Status |
|---|---|---|---|
| 00 | `_smoke` | — | toolchain canary, not for publishing |
| 01 | `oas-clawback` | R1 | verified; awaiting owner review and compliance |

How to make one: `.claude/skills/fp-figures/SKILL.md`; commands: `docs/PIPELINE.md`.
