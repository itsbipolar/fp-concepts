# Audience, positioning, pillars and series

Research log with URLs: `RESEARCH-LOG.md` (October 22, 2026). Most market sources are agency and vendor blogs.
They are treated as **directional**, and our own analytics (`analytics/`) overrule them once we have data.

## 1 · Who it's for
| Audience | Who | What they want from a video | Where |
|---|---|---|---|
| **A · Families** | Owner-managers (Opco + Holdco + trust), incorporated physicians and dentists, law and accounting partners, executives with equity pay, retirees with $2M+, inheritors. HNW → UHNW. | "Is my accountant or advisor doing this? What's the question I should ask?" Clarity on mechanics they've heard named in meetings (freeze, CDA, IPP, pipeline). | YouTube (search plus long-form), Instagram, LinkedIn for professionals |
| **B · Advisors** | MFO teams, wealth advisors, CFP® professionals, CPAs, estate lawyers, insurance specialists. **This is Summit AI's market.** | A clean visual way to explain a mechanic to a client; edge cases; "what changed". | LinkedIn (native video, 30–90 s, captions on), YouTube |
| **C · Sophisticated DIY** | People who've outgrown TFSA vs RRSP content | Depth, with sources | YouTube, TikTok search |

Write each video for **one** of them. A family video says "your company" and "your estate". An advisor video says "your
client's file", "the question to ask", "what to check".

## 2 · The landscape (what exists, October 2026)
- **Retail Canadian personal finance** is crowded: budgeting, credit cards, TFSA vs RRSP, FIRE and ETFs. Large
  creators include No Budget Babe (Nicole Victoria, about 2M followers across platforms), Christopher Liew/Wealthawesome
  (~767k on TikTok), Preet Banerjee, and Passive Income Investing (~247k on YouTube).
- **Evidence-based investing**: Ben Felix (~528k subscribers per a 2026 directory) and the Rational Reminder podcast
  (PWL Capital), and The Plain Bagel (Richard Coffin, CFA and CFP® professional). These are deep, but on investing,
  not owner-manager tax and estates.
- **Advisor-led channels**: Aaron Wealth Management, Well Built Wealth and Ferguson Financial Planning. Mostly
  talking-head videos for retail, retirement-focused.
- **Institutions and firms**: bank private-wealth podcasts (BMO's *Beyond the Portfolio*), UBS family-office
  podcasts, law-firm blogs (Miller Thomson, Barrett Tax Law) and CPA/tax-lawyer articles. Deep, but text, audio
  or a talking head, and rarely visual.
- **What's missing**: an animated, receipt-driven, Canadian-specific explainer of the *mechanics* that drive
  HNW outcomes (integration, the passive-income grind, the CDA, RDTOH, freezes, the 21-year rule, double tax at
  death, pipelines, the insured annuity, US estate tax for Canadians, IPPs). That's our lane.
- **Regulator context**: CSA/CIRO Staff Notice 31-369 (December 11, 2025) puts finfluencers on notice. A channel that
  visibly shows its sources and stays educational is on the right side of that line, and that is a brand advantage.

## 3 · Pillars (rotate through them; no pillar twice in a row)
| Pillar | Summit areas | Examples |
|---|---|---|
| **1 · The owner's money** | CORP, CF, SUC, TAX | Salary or dividends, the passive-income grind, the CDA, RDTOH, shareholder loans and 15(2), TOSI, the estate freeze, the LCGE and QSBC purification, IPPs |
| **2 · The two deaths** | EST, INS (estate), XB-02 | Deemed disposition, double tax on private shares, the 164(6) loss carryback and pipelines (DECLINE topics), probate by province, the 21-year rule, second-to-die insurance, US estate tax for Canadians |
| **3 · Retirement with real money** | RET, INV | RRIF meltdown, OAS recovery tax, CPP at 60, 65 or 70, pension splitting, decumulation order, commuted value vs pension, the Holdco as a pension, the insured annuity |
| **4 · Families and generations** | FAM, EST, PHI, DEBT | Prescribed-rate loans, the family trust, helping a child buy a home, equalising heirs, the cottage, special-needs planning (Henson trusts, RDSP), giving securities in kind, DAFs vs private foundations |
| **5 · What changed** | any (event-driven) | Budget measures, indexation each November, prescribed-rate changes each quarter, new case law, the capital gains inclusion rate saga. Short and timely; the receipt is the new text. |
| **6 · Myth vs statute** | any | "CRA says…" (a stated position) vs what the Act says; common half-truths ("my company can pay my insurance tax-free"). T1 vs T4 on screen is unique to us. |

## 4 · Series (formats; each one varies its visual system so the channel isn't template-made)
Series names are internal (never on screen; the close is the DISCLAIMER card). Every series is built as **collage
acting** (FORMAT.md §3, the reference piece SalaryVsDividend v3); the signature visual below is its recurring metaphor.
| Series | Cut | Length | Shape | Signature visual |
|---|---|---|---|---|
| **The Receipt** | vertical | 35–60 s | one rule → the statute highlighted → one worked number → the kicker | the Justice Laws page as a torn paper strip, with the yellow highlight sweeping |
| **The Ledger** | vertical or square | 45–75 s | one decision (e.g. salary vs dividend) → two columns → where the money goes → the result | ledger cards that stack and total, with the `CountUp` hero number |
| **Two Deaths** | horizontal | 4–8 min | an illustrative family → the first death → the second death → the tax, probate and liquidity → what planning changes | the timeline with two stamps; money flows as green cut-outs |
| **The Family File** | horizontal | 6–10 min | a case study across pillars (an invented household, labelled) | the family map / org chart, revisited each act |
| **Myth vs Statute** | vertical | 30–45 s | the claim (strike) → what the law says → what CRA says → why it matters | a split page: the CRA folio vs the Act, with tier badges |
| **What Changed** | vertical | 20–40 s | the date → the old → the new → who it hits | the date stamp and a before/after strip |
| **No Single Number** | vertical or horizontal | 45–120 s | why a GATE/DECLINE topic can't be computed → the factors → who decides | the factor checklist with an empty "verdict" box (honesty as the hook) |

Long-form first when possible: one explainer yields 3–5 shorts (each with its own hook, and standalone).

## 5 · Scoring an idea (Stage 1)
Score each candidate 1–5 and add them up:
- **Stakes**: how many dollars or how much family risk it moves for audience A (Summit's tier 1 ≈ high)
- **Mystery**: it's named in meetings but rarely understood (high for the CDA, RDTOH, freezes, pipelines)
- **Visualisability**: objects can act it out: money flowing and being cut, a comparison on a scale, a metaphor for the kicker
- **Verifiability**: COMPUTE/CAVEAT topics are easy; GATE/DECLINE suit the "No Single Number" series only
- **Timeliness**: a season or a change (RRSP deadline, year-end, budget, indexation, quarterly prescribed rate)
- **Search pull**: people type it ("salary vs dividend Canada", "OAS clawback", "estate freeze")
- **Performance**: once `analytics/` has data, `tools/analytics.mjs` gives a multiplier by pillar and series

## 6 · The Summit link (audience B)
On LinkedIn, and only there, an advisor video can close with Summit as the source of the mechanics ("from the Summit AI
planning catalogue"). That's only once Mo has approved the wording and Summit has a public page. Never claim that
Summit computes something it doesn't yet compute (Summit's own `KNOWN-GAPS` and the canadian-tax skill §7 apply to
marketing copy).
