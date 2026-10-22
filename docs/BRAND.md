# Brand and output formats

## Look (inherited from Colorfigures, keep it)
Warm paper (#f2efe7), one heavy ink (#231e16), flat three-tone shading, a blue cast shadow (#41538f), a hand-drawn
wobble and grain, monospace type. This look is the hook; don't add gradients, photos or stock icons.

## Colour by planning domain
Each figure takes its domain's palette (fp-kit `PALS` keys), mirroring the colour code of the v0 crash notes, so a
series reads as one system:

| Domain | Key | Light / mid / dark |
|---|---|---|
| Process, cash and debt | `fpp` | #a3aec0 / #7f8a9e / #262d38 |
| Tax | `tax` | #ef7f78 / #d65f59 / #4c1f1e |
| Investments | `inv` | #6fb0ec / #4c8fd0 / #14304d |
| Retirement | `ret` | #f59a5a / #d9783a / #4d2510 |
| Insurance | `ins` | #b493dc / #9372bf / #33234a |
| Estate | `est` | #7cc9a0 / #58a87f / #173a29 |
| Brand-neutral | `navy`, `gold` | for covers, series art, firm-branded pieces |

Money: gold coins (`FP_GOLD`), green notes (`FP_BILL`), sheltered glass (`FP_SHELTER`), tax grey (`FP_CRA`).
Accents as upstream: green/red status lights, dark screens with green text.

## Firm branding (to fill in)
| Item | Value |
|---|---|
| Firm / practice name | _TBD_ |
| Brand colours | _TBD: add as a PALS entry in fp-kit.js if wanted_ |
| Logo use | outside the figure only (page header, post frame), never on the machine |
| Disclaimer wording | see `docs/COMPLIANCE.md` house rules |
| Credit line | keep "Made with Colorfigures" on the interactive page (attribution, see DECISIONS D-004); stills use `?clean=1` |

## Naming and voice
- Series name (working): **"How it works: concept machines"**; each figure is "Fig. NN — <concept>".
- Machine names are plain and slightly playful: "The clawback weir", "The freeze-dryer", "The toll bridge".
- Labels are the real terms in capitals (TFSA, ACB, FMV, CDA, DTC). Buttons are verbs.
- Post copy: one line of hook (the misconception), one line of the rule, the link. No jargon without the figure.

## Output formats (`scripts/shoot.py`)
| Asset | Size | Use |
|---|---|---|
| Interactive page | one HTML file | website, client email, meeting on a tablet |
| `feed-1080x1350.png` | 4:5 portrait | LinkedIn / Instagram feed |
| `square-1080.png` | 1:1 | carousels, newsletter |
| `wide-1920x1080.png` | 16:9 | presentations, YouTube thumbnail, website hero |
| `spin.mp4` / `spin.gif` | 720 x 720, 3 s turntable | social video, email GIF |
| Carousel (manual) | 3–5 stills: closed -> action -> see-through + labels -> result stat | the explainer post |

URL states make the frames: e.g. `?clean=1&income=140000`, `?clean=1&xr=1&labels=1`, `?bare=1` for art only.
