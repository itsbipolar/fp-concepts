/* ============================================================
   fp-kit: shared helpers for FP Concepts figures. Load it with its own script tag (src="fp-kit.js") right after
   the core.js one; scripts/build.py inlines both. (Never write a closing script tag inside this file, not even in a
   comment: once inlined it would end the page's script early.) Every global here starts with FP / fp so it never clashes with core.js
   (see the reserved-name list in references/colorfigures-SKILL.md).

   What it gives a figure:
   - palettes: the six planning domains + brand-neutral wealth tones, added to PALS (so they show as swatches)
   - FP_FACTS: the 2026 numbers a figure may use. ONE place to update when figures index. Mirrors
     docs/FACT-LEDGER-2026.md; every value there carries its source. Never hard-code a rule number in a figure.
   - fpFedTax(): federal tax on taxable income with the 2026 brackets (no credits, no provincial tax)
   - fpMoney / fpPct: number formatting for stats and labels (plain ASCII only: the figure font has no symbols)
   - FP_GOLD / FP_BILL / FP_CRA materials and fpCoinStack(): money props
   - fpPage({...}): call once after mountFigure(): the disclaimer + as-of footer, and the ?clean=1 / ?bare=1
     export modes used by scripts/shoot.py for social images
   ============================================================ */

/* ---------- palettes (l = lit, m = mid, d = dark), keyed for st.pal / ?pal= ---------- */
Object.assign(PALS, {
  tax:  { l:'#ef7f78', m:'#d65f59', d:'#4c1f1e' },   // Tax           (crash-notes colour #DC3E44)
  inv:  { l:'#6fb0ec', m:'#4c8fd0', d:'#14304d' },   // Investments   (#0679D6)
  ret:  { l:'#f59a5a', m:'#d9783a', d:'#4d2510' },   // Retirement    (#E25A00)
  ins:  { l:'#b493dc', m:'#9372bf', d:'#33234a' },   // Insurance     (#8546BF)
  est:  { l:'#7cc9a0', m:'#58a87f', d:'#173a29' },   // Estate        (#23895A)
  fpp:  { l:'#a3aec0', m:'#7f8a9e', d:'#262d38' },   // Process / cash & debt (#3A4556)
  navy: { l:'#7f9bc9', m:'#5d7bb0', d:'#1d2a48' },   // brand-neutral wealth tones
  gold: { l:'#e9c46a', m:'#c9a24a', d:'#4a3b16' },
});
const FP_DOMAIN = { process:'fpp', tax:'tax', investments:'inv', retirement:'ret', insurance:'ins', estate:'est' };

/* ---------- materials for props ---------- */
const FP_GOLD = { l:'#f6d46b', m:'#d9ae3f', d:'#7a5a12' };     // coins
const FP_BILL = { l:'#a9d8a0', m:'#82bb7a', d:'#2f5a2a' };     // banknotes (generic green, never a real note design)
const FP_CRA  = { l:'#c9c3b6', m:'#a59f92', d:'#4f4a42' };     // "tax collector" parts: neutral grey, never government branding
const FP_SHELTER = { l:'#cfe9f0', m:'#a8d0da', d:'#5d8a96' };  // tax-sheltered glass

/* ---------- the fact ledger (2026 tax year unless noted). Source: v0 CFP crash notes, figures checked Oct 1, 2026.
   Federal figures only. Provincial tax, Quebec rules and anything indexed quarterly must be re-checked before publishing. */
const FP_FACTS = {
  asOf: '2026',
  checked: '2026-10-01',
  source: 'v0: CFP crash notes (2026 figures checked against CRA, ESDC, CIPF, CDIC, Assuris on Oct 1, 2026)',
  tax: {
    brackets: [[58523, .14], [117045, .205], [181440, .26], [258482, .29], [Infinity, .33]],   // [upper bound, rate]
    lowestRate: .14, bpa: 16452, bpaMin: 14829, ageAmount: 9208, pensionAmount: 2000,
    cgInclusion: .5,
    eligGrossUp: .38, eligDTC: .1502, nonEligGrossUp: .15, nonEligDTC: .0903,                  // DTC as % of grossed-up
    lcge: 1275000, sbdLimit: 500000,
    amtExemption: 181440, amtRate: .205, amtCarryYears: 7,
    prescribedRate: .03,                     // Q4 2026, quarterly
    tfsaAnnual: 7000, tfsaCumulative: 109000, // cumulative = 18+ in 2009, never contributed
    donation: { first200: .14, above200: .29, top: .33, limitPctNI: .75, deathPctNI: 1 },
    instalmentThreshold: 3000,
  },
  ret: {
    rrspLimit: 33810, rrspPct: .18, rrspBuffer: 2000, mpLimit: 35390, dbMaxPerYear: 3932.22, dpspMax: 17695,
    ybe: 3500, ympe: 74600, yampe: 85000, cppRate: .0595, cpp2Rate: .04,
    cppMax65: 1507.65, cppEarlyPerMonth: .006, cppLatePerMonth: .007, cppMin: 60, cppMax: 70,
    cppDeathBenefit: 2500,
    oasClawThreshold: 95323, oasClawRate: .15, oasGone6574: 155320, oasGone75: 161320,
    oasMax6574: 762.50, oasMax75: 838.75,                                                     // monthly, Oct-Dec 2026 (indexed quarterly)
    oasDeferPerMonth: .006, oasFullYears: 40, oasMinYears: 10,
    gisSingleMax: 1138.90, gisSingleIncomeCap: 23112, gisReductionPerDollar: .5,
    rrifMinUnder71: age => 1 / (90 - age),
    rrifTable: { 71: .0528, 75: .0582, 80: .0682, 85: .0851, 90: .1192, 95: .20 },
    spousalAttributionYears: 3,
    withholding: [[5000, .10], [15000, .20], [Infinity, .30]],                                // lump-sum RRSP, outside Quebec
  },
  home: {
    hbpMax: 60000, hbpRepayYears: 15, fhsaAnnual: 8000, fhsaLifetime: 40000, fhsaCarryMax: 8000, fhsaYears: 15,
    gdsGuide: .32, tdsGuide: .40, gdsCmhc: .39, tdsCmhc: .44, locInTds: .03,
    stressFloor: .0525, stressAdd: .02, insuredCap: 1500000,
    downTiers: [[500000, .05], [1500000, .10], [Infinity, .20]],
  },
  resp: { lifetime: 50000, cesgRate: .20, cesgOn: 2500, cesgYear: 500, cesgYearCatchUp: 1000, cesgLifetime: 7200,
    contribYears: 31, closeYears: 35, clbMax: 2000, aipExtraTax: .20 },
  protect: { cdic: 100000, cipf: 1000000, assurisDeath: 1000000 },
  est: { ontarioEatPer1000: 15, ontarioEatFreeFirst: 50000, trustDeemedYears: 21, greMonths: 36,
    usExemption: 15000000, usUnifiedCredit: 5945800, usTopRate: .40, us706Threshold: 60000 },
};

/* federal tax on taxable income, 2026 brackets; no credits (subtract them yourself: amount x FP_FACTS.tax.lowestRate) */
function fpFedTax(taxable, brackets = FP_FACTS.tax.brackets){
  let tax = 0, lo = 0;
  for (const [hi, r] of brackets){ if (taxable > lo) tax += (Math.min(taxable, hi) - lo) * r; lo = hi; }
  return tax;
}
/* marginal federal rate at an income */
const fpMarginal = (taxable, brackets = FP_FACTS.tax.brackets) => (brackets.find(([hi]) => taxable < hi) || brackets[brackets.length - 1])[1];

/* ---------- formatting (ASCII only) ---------- */
const fpMoney = (v, dp = 0) => (v < 0 ? '-$' : '$') + Math.abs(v).toLocaleString('en-CA', { minimumFractionDigits: dp, maximumFractionDigits: dp });
const fpK = v => Math.abs(v) >= 1e6 ? '$' + (v / 1e6).toFixed(v % 1e6 ? 2 : 0).replace(/\.?0+$/, '') + 'M' : Math.abs(v) >= 1e3 ? '$' + Math.round(v / 1e3) + 'k' : fpMoney(v);
const fpPct = (v, dp = 0) => (v * 100).toFixed(dp) + '%';

/* ---------- props ---------- */
// a stack of n coins standing on (x, y, z0): one convex column, so the caller sorts it as one part with box fpCoinBox(...)
function fpCoinStack(x, y, z0, n, r = 4, t = 1.1, m = FP_GOLD){
  if (n <= 0) return '';
  let s = cyl(x, y, z0, z0 + n*t, r, m, toneI, 1.1, 20);
  // the coin edges as fine rings on the side facing the viewer
  let rings = ''; const [a0, a1] = nearHalf();
  for (let i = 1; i < n; i++){ const z = z0 + i*t, pts = [];
    for (let k = 0; k <= 10; k++){ const a = (a0 + (a1 - a0)*k/10)*Math.PI/180; pts.push([x + r*Math.cos(a), y + r*Math.sin(a), z]); }
    rings += pd(pts, false); }
  if (rings) s += `<path d="${rings}" fill="none" stroke="${INK}" stroke-width=".5" opacity=".55"/>`;
  return s;
}
const fpCoinBox = (x, y, z0, n, r = 4, t = 1.1) => [[x - r, y - r, z0], [x + r, y + r, z0 + Math.max(n, 1)*t]];

/* ---------- page: disclaimer footer + export modes ----------
   fpPage({ asOf, note, firm }) after mountFigure(...) (and after xrMount if used).
   ?clean=1 hides the controls row, zoom chip and footer credit (for marketing stills);
   ?bare=1 also hides the buttons, stats and switches (just the object). */
function fpPage(opt = {}){
  const q = new URLSearchParams(location.search), html = document.documentElement;
  const css = document.createElement('style');
  css.textContent = `.fp-note{width:100%;max-width:760px;margin:10px 0 0;font-size:10.5px;line-height:1.45;color:var(--muted);letter-spacing:.02em;text-align:left}
    .fp-note b{color:var(--ink);font-weight:700}
    html.fp-clean .controls, html.fp-clean .zchip, html.fp-clean .made-with{display:none!important}
    html.fp-clean{background:var(--paper)} html.fp-clean body{min-height:100vh}
    html.fp-clean .fp-note{position:fixed;left:16px;right:16px;bottom:10px;width:auto;max-width:none;margin:0;background:var(--paper)}
    html.fp-bare .actions, html.fp-bare #btns, html.fp-bare .stats, html.fp-bare .vset, html.fp-bare .kpad, html.fp-bare .lgd, html.fp-bare body > header{display:none!important}`;
  document.head.appendChild(css);
  if (q.get('clean') === '1' || q.get('bare') === '1') html.classList.add('fp-clean');
  if (q.get('bare') === '1') html.classList.add('fp-bare');
  const p = document.createElement('p'); p.className = 'fp-note';
  const body = opt.body != null ? opt.body : `Simplified for illustration: federal rules and ${opt.asOf || FP_FACTS.asOf} figures`
    + ` unless stated; provincial rules (and Quebec's) differ, and figures change each year.`;
  p.innerHTML = `<b>Educational illustration, not advice.</b> ${body} ${opt.note ? opt.note + ' ' : ''}`
    + `Speak with a qualified professional about your situation.${opt.firm ? ' ' + opt.firm : ''}`;
  const anchor = document.querySelector('.controls') || document.querySelector('.stage');
  if (anchor) anchor.after(p);
  return p;
}

/* ---------- story line: one plain-English sentence under the scene that changes with each step ----------
   fpStory(ui, st => 'text'): call after mountFigure (and xrMount). It re-reads the text on every render. Keep it to
   one or two short sentences a 9th grader can follow; say what just happened and why, in dollars. */
function fpStory(ui, text){
  const el = document.createElement('p'); el.className = 'fp-story'; el.setAttribute('aria-live', 'polite');
  const css = document.createElement('style');
  css.textContent = `.fp-story{width:100%;max-width:760px;min-height:3.2em;margin:2px 0 14px;font-size:14.5px;line-height:1.5;text-align:center;
      color:var(--ink);letter-spacing:.01em;text-wrap:balance}
    .fp-story b{font-weight:800} html.fp-bare .fp-story{display:none}
    @media (max-width:560px){.fp-story{font-size:13.5px;text-align:left}}`;
  document.head.appendChild(css);
  (document.querySelector('.stage') || document.body).after(el);
  const r0 = ui.render; ui.render = () => { r0(); const t = text(ui.st); if (el._t !== t){ el._t = t; el.innerHTML = t; } };
  ui.render();
  return el;
}

/* ---------- a row of label pills under the board, for parts whose labels would otherwise cross the scene ----------
   fpRowTags(items, ground): items [{ at:[x,y,z], text, on }], ground = 3D points of the board outline (the row sits
   just below its lowest point on screen). Pills keep their parts' left-to-right order and stay clear of the zoom chip.
   Use it with xrCallouts for the parts on the left (first used in Fig. 01). */
function fpRowTags(items, ground){
  if (!items.length) return '';
  const k = INK_K, u = window.LBL_U ? LBL_U() : 0, fs = u ? 10*u : 8.6*k, gap = 5*k;
  const vb = document.getElementById('fig').viewBox.baseVal;
  const rowY = Math.max(...ground.map(p => P(...p)[1])) + 4*k;
  const its = items.map(it => { const [X, Y] = P(...it.at); return { ...it, X, Y, w: u ? 17*u*1.3 : it.text.length*fs*.62 + fs*1.5 }; }).sort((a, b) => a.X - b.X);
  let x = -1e9; for (const it of its){ it.px = Math.max(it.X, x + gap + it.w/2); x = it.px + it.w/2; }
  const over = x - (vb.x + vb.width * (u ? .98 : .85)); if (over > 0) for (const it of its) it.px -= over;
  return its.map(it => tag(it.at, (it.px - it.X)/k, (rowY - it.Y)/k, it.text, it.on)).join('');
}
