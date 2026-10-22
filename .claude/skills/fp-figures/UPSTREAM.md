# Upstream: Colorfigures

This skill is built on **Colorfigures** by April Zhu (MIT), from `vendor/colorfigures.zip` (added to the repo in
commit `1d29a1f`). Colorfigures itself is built on ISO-GLOW (April Zhu, MIT), which is built on iso-figure by
Tolga Cohce (MIT). Licence: `LICENSE` in this folder. Upstream pages: https://april-zhu.com/colorfigures

| File here | Upstream file | Changed? |
|---|---|---|
| `assets/core.js` | `colorfigures/assets/core.js` | no: keep it byte-identical so upstream updates drop in |
| `assets/examples/*.html` | `colorfigures/assets/examples/*` | no |
| `references/colorfigures-SKILL.md` | `colorfigures/SKILL.md` | no (renamed so this skill's SKILL.md is the entry point) |
| `references/colorfigures-README.md` | `colorfigures/README.md` | no |
| `scripts/build.py` | `colorfigures/scripts/build.py` | **yes**: also inlines `fp-kit.js`; stamps an MIT attribution comment after the doctype |
| `assets/fp-kit.js`, `scripts/shoot.py`, `SKILL.md`, `references/metaphor-grammar.md`, `references/engine-cheatsheet.md` | none | new for this project |

## Updating the engine
1. Unzip the new Colorfigures release to a scratch folder.
2. Replace `assets/core.js`, `assets/examples/`, `references/colorfigures-SKILL.md` with the new versions.
3. Diff the new `scripts/build.py` against ours and re-apply the two FP changes (the fp-kit inline block and NOTICE).
4. Check the reserved-name list in the new SKILL.md against `fp-kit.js` (all ours start with `FP`/`fp`).
5. Rebuild `figures/_smoke` and every shipped figure; run `shoot.py errors` on each.
6. Log the update in `docs/DECISIONS.md`.
