# Engine cheat sheet (core.js + fp-kit.js)

A one-page map of the API, from reading `assets/core.js` and the three examples. The full drawing contract is in
`colorfigures-SKILL.md`; when this page and that one disagree, that one wins.

## Coordinates and camera
- `x` = depth (front face at `x = W`), `y` = width (+y goes viewer-left at the default view), `z` = up, ground `z = 0`.
- Default view `YAW = 45`, `PITCH = 35.26` (true iso). URL: `?yaw=200&pitch=40`, `?free=1` (no turning limit).
- `mountFigure({ size:[W,D,H], center:[x,y] })` frames the object; the frame fills ~74% width / ~88% height.
- `P(x,y,z)` -> screen point. `pd(pts3, close=true)` -> SVG path of 3D points. `depthOf(p)`.

## Shapes (all return SVG strings)
| Call | Draws |
|---|---|
| `box(x0,y0,z0,x1,y1,z1, m, shade=toneI, w)` | axis box, visible faces only |
| `extrude(profileUV, x0, x1, m)` | a rounded profile (`rrUV`) swept along x: machine bodies (cap + silhouette ink are yours) |
| `cyl(x,y,z0,z1,r, m)` | upright cylinder with top cap |
| `cylX(x0,x1,y,z,r, m)` | cylinder along x (knobs, dials) |
| `rod(a, b, r, m, shade, w, r1)` | cylinder between any two points; `r1` makes a cone |
| `loft(ringA, ringB, colourFn, flip)` | surface between two rings (`on(PZ(z), ellUV(...))`) for cups, funnels, domes |
| `openShell(A, B, colour, contents)` | far wall, contents, near wall (containers, tanks you look into) |
| `shape(pts3, colour, w)`, `line(pts3, w)`, `fill(d, c)`, `ink(d, w)`, `hullInk(pts3, w)` | flat faces and ink |
| `tx / txY(x,y,z, str, size)` | text on a front / side face (hides when the face turns away) |
| `board(x0,y0,x1,y1,h,r)` + `boardTop(...)` | a desk board; shadows clip to its top |
| `castShadow(pts3, z0, clip)` | flat blue shadow (one per object) |
| `clipTo(pts3, inner)` | clip contents to an opening |

Profiles in a plane's (u,v): `rrUV`, `rectUV`, `ellUV`, `arcUV`; planes `PX(x)`, `PY(y)`, `PZ(z)`; `on(plane, uv)`.

## Shading and colour
- `tone(n, m)` exterior (follows the light), `toneI(n, m)` interiors and props. A palette is `{l, m, d}`.
- Materials: `METAL`, `CLEAR`, `CERAMIC`, `DARK`, `matOf('#hex')`, `BOARD`, `WOOD`; fp-kit adds `FP_GOLD`, `FP_BILL`,
  `FP_CRA`, `FP_SHELTER`.
- Palettes (`PALS`): mustard, tomato, mint, cobalt, blush + fp-kit's tax, inv, ret, ins, est, fpp, navy, gold.
  Add more with `Object.assign(PALS, {...})` before `mountFigure` (they appear as colour swatches).
- `vis(n)` / `facing(n)`: is a face with normal n toward the viewer.

## Ordering (no depth buffer)
- `byDepth([{ at:[x,y,z], box:[[x0,y0,z0],[x1,y1,z1]], svg }])` sorts parts back to front for the current view.
  Every part gets a `box`. A function that draws several parts in sequence is a fixed order: return items instead.
- `nearHalf()` / `farHalf()` for rings; `openShell` for containers.

## Page and behaviour
```js
const ui = mountFigure({
  fig:'01', title:'OAS clawback', turn:'full', size:[W,D,H], center:[x,y], palette:'ret',
  state:{...}, scene:(st, m) => svg,
  buttons:[{ label, onClick(st, ui) } | { label, choices: st => [{ label, onClick, current, disabled, why }] }],
  stats: st => [{ label, value, small }],
  acts:{ name(st, el, ui){} },          // clicks on act('name', svg) groups (fire on press)
  params:(st, q) => {},                 // URL -> state for screenshots
  credit: true,                         // keep the "Made with Colorfigures" link (attribution; see DECISIONS D-004)
});
xrMount(() => ui, () => '');            // See-through + Labels switches (if the figure has an inside)
fpPage({ note:'...', asOf:'2026' });    // last: disclaimer footer + ?clean / ?bare export modes
```
- `ui.animate(dt => stillRunning)`, `ui.flash(text, ms)`, `ui.render()`, `ui.camTo(yaw, pitch)`; state is `window.__st`.
- See-through: in `scene`, `const k = ease(st.xr || 0)`; ghost the case with `xrGhost / xrGhostRings / xrUnder`,
  draw inside parts at opacity k over it; labels via `xrCallouts(items, bounds)` only when `k > .6`; surface labels
  via `tag(p3, dx, dy, text, on)`.
- Testing URLs: `?press=Label@ms,Label>Choice@ms`, `?xr=1&labels=1`, `?pal=ret`, `?clean=1`, `?bare=1`.

## fp-kit
- `FP_FACTS.tax / .ret / .home / .resp / .protect / .est`: the 2026 numbers (mirrors `docs/FACT-LEDGER-2026.md`).
- `fpFedTax(taxable)` federal tax, 2026 brackets, no credits. `fpMarginal(taxable)`.
- `fpMoney(v, dp)` -> "$1,234"; `fpK(v)` -> "$95k" / "$1.5M"; `fpPct(v, dp)` -> "15%".
- `fpCoinStack(x, y, z0, n, r, t, m)` + `fpCoinBox(...)` for its sort box.
- `FP_DOMAIN` maps domain names to palette keys.

## Gotchas found so far (add to this list)
1. **Never write a closing script tag inside core.js, fp-kit.js or a figure script, not even in a comment.** Once
   build.py inlines the file, it ends the script early (seen: "Uncaught SyntaxError: Invalid or unexpected token").
2. Pages at **560 CSS px wide or less use the phone layout** (header hidden, labels become numbered badges with a
   legend). Marketing stills must render wider than 560 CSS px; `shoot.py social` does.
3. The error check's "NaN" hit can be a false positive from base64 noise images; `shoot.py errors` strips `data:`
   URIs first.
4. `xrCallouts` puts pills either side of the object; the right column can collide with the **stats** panel at the
   top right. Give the object room (a larger `size` or `center` offset) or anchor labels lower.
5. Headless Chrome as root needs `--no-sandbox` (shoot.py adds it automatically).
6. `mountFigure` replaces `document.body`, so anything added to the page (fpPage) must run after it.
7. Chrome's `--dump-dom` with `--virtual-time-budget` **hangs while a figure animates** (screenshots don't). `shoot.py
   errors` uses Playwright (Node, `/opt/node-tools/node_modules`) when present, and also prints the stats panel and
   `window.__st`, which is the quickest numbers check.
