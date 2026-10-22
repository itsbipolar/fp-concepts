# Pipeline: brief -> figure -> verify -> export

All commands run from the repo root. Tested in this repo's cloud container on 2026-10-22 (Python 3, Chromium at
`/opt/pw-browsers/chromium`, ffmpeg). On a Mac, set `CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"`
if it isn't found automatically.

```bash
SK=.claude/skills/fp-figures
SLUG=oas-clawback                                   # the figure's folder name
```

## 1. Start a figure
```bash
mkdir -p figures/$SLUG/dist
cp docs/templates/FIGURE-BRIEF.md figures/$SLUG/BRIEF.md       # fill it in before any code
```
Then write `figures/$SLUG/figure.html` (copy the shell from `figures/_smoke/figure.html`).
While drafting you can open the unbuilt page with `core.js` and `fp-kit.js` copied next to it, but building is
quicker: build, open `dist/<slug>.html` in a browser.

## 2. Build
```bash
python3 $SK/scripts/build.py figures/$SLUG/figure.html figures/$SLUG/dist/$SLUG.html
```

## 3. Verify
```bash
python3 $SK/scripts/shoot.py errors figures/$SLUG/dist/$SLUG.html "Label@300,Other@1500" "income=140000"
#   prints errors (must be none), NaN (must be false), the stats panel and window.__st: compare with the brief
python3 $SK/scripts/shoot.py verify figures/$SLUG/dist/$SLUG.html figures/$SLUG/shots       # 7 angles x closed/see-through + phone
python3 $SK/scripts/shoot.py press  figures/$SLUG/dist/$SLUG.html figures/$SLUG/shots "Label@300,Other@1500"
```
Look at every shot (and 2–3x crops of parts), using the checklist in `references/colorfigures-SKILL.md` (Verify)
plus:
- **Numbers:** run `errors` with the persona state (`?income=...`) and compare the printed stats with the brief's hand
  calculation; look at the shot too.
- **Labels** don't collide with the stats panel or buttons.
- **Disclaimer** is visible under the figure.

Shots are working files: `figures/*/shots/` is git-ignored.

## 4. Export marketing assets
```bash
python3 $SK/scripts/shoot.py social figures/$SLUG/dist/$SLUG.html figures/$SLUG/dist "income=140000"
python3 $SK/scripts/shoot.py spin   figures/$SLUG/dist/$SLUG.html figures/$SLUG/dist
```
For a carousel, call `social` once per state (closed, mid-action via `press=`, `xr=1&labels=1`, the result) into
`dist/carousel-N/`.

## 5. Ship
- Compliance pass (`docs/COMPLIANCE.md`), approval reference in the brief.
- Commit `figures/$SLUG/` (brief, figure, dist), update `docs/CONCEPT-CATALOG.md` status and `docs/ROADMAP.md`.
- Tag the approved commit: `git tag pub/$SLUG/YYYY-MM-DD`.

## Toolchain check
`figures/_smoke` is the canary. After touching `core.js`, `fp-kit.js` or `build.py`:
```bash
python3 $SK/scripts/build.py figures/_smoke/figure.html figures/_smoke/dist/smoke.html
python3 $SK/scripts/shoot.py errors figures/_smoke/dist/smoke.html "Earn@300"
```
Unit check of the tax helper (expected: 50,000 -> 7,000; 150,000 -> 28,758.53):
```bash
node -e "global.PALS={};global.cyl=()=>'';const k=new Function(require('fs').readFileSync('$SK/assets/fp-kit.js','utf8')+';return{fpFedTax}')();for(const i of[50000,150000])console.log(i,k.fpFedTax(i).toFixed(2))"
```
