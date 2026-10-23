# Verification: every figure has a receipt

This adapts Summit AI's discipline (`reference/summit/skill/canadian-tax.SKILL.md`,
`reference/summit/tax-knowledge/README.md`) to video. A video is worse than a bad calculator: it is repeated with
confidence, and it can't be patched once posted. So **nothing is stated that isn't in the claims ledger, and nothing
is in the ledger without a primary source read on a recorded date.**

## 1 · The ledger: `projects/<slug>/claims.json`
The template is `templates/fp/claims.template.json`. `tools/claims.mjs` checks it.
```json
{
  "slug": "cda-explained",
  "as_of": "2026-10-22",                // the date the video's facts are true on
  "tax_year": 2026,
  "jurisdictions": ["CA", "ON"],
  "review": { "by": "", "credentials": "", "on": "", "note": "" },   // the human sign-off (Stage 8)
  "claims": [
    {
      "id": "cda-def",
      "kind": "rule",                    // rule | figure | rate | date | calc | authority | definition
      "statement": "A private corporation's capital dividend account tracks amounts it can pay out to Canadian-resident shareholders tax-free.",
      "on_screen": "CAPITAL DIVIDEND ACCOUNT",  // what the video shows (optional)
      "spoken": "the capital dividend account",  // the phrase in the script (optional)
      "value": null, "unit": null,
      "jurisdiction": "CA",
      "tier": "T1",                      // T1 statute · T2 regulation · T3 case law · T4 CRA position · T5 practice · T6 unsettled
      "behaviour": "COMPUTE",            // COMPUTE | COMPUTE_WITH_CAVEAT | GATE | DECLINE
      "source": {
        "url": "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-89.html",
        "title": "Income Tax Act s. 89(1) 'capital dividend account'",
        "publisher": "Justice Laws",
        "retrieved_on": "2026-10-22",
        "quote": "capital dividend account of a corporation at any particular time means the amount, if any, by which …"
      },
      "supporting": [],                  // secondary sources (articles, guides); never alone
      "pack_ref": null,                  // { "id": "ca.…", "year": 2025 } when Summit's pack holds the value
      "summit_ref": "CORP-09",           // the catalogue/dossier id
      "status": "verified",              // verified | needs-review | declined
      "note": ""
    }
  ]
}
```
A **calc** claim reproduces a worked number from other claims:
```json
{ "id": "ex-tax", "kind": "calc", "statement": "Tax on the example's $100,000 at the 2026 rate",
  "calc": { "expr": "income * rate", "vars": { "income": 100000, "rate": "@sbd-rate" } },
  "value": 9000, "unit": "CAD", "illustrative": true, "status": "verified" }
```
`@id` pulls another claim's `value`. The tool recomputes the expression (it allows only numbers, `+ - * / ( )`,
`min`, `max`, `round` and `floor`) and fails if the result doesn't match `value` within a cent. Illustrative
inputs (the invented family's income) need `illustrative: true` and no source.

## 2 · Tier and behaviour → what the video says
| Summit behaviour | When | On screen | In the narration |
|---|---|---|---|
| **COMPUTE** | statute or regulation all the way (T1/T2) | the figure, its year, the section | state it plainly |
| **COMPUTE_WITH_CAVEAT** | rests on a CRA position or practice (T4/T5) | the figure plus the badge "CRA'S STATED POSITION" | "CRA's position is…; a court isn't bound by it" |
| **GATE** | a court's multi-factor test (PSB, reasonableness, interest deductibility, residency, association, capital vs income, Pecore) | the factors, an empty verdict box | "this depends on the facts; here's what's weighed" |
| **DECLINE** | unsettled (post-2024 GAAR, the post-mortem pipeline, TOSI's reasonable return), or a legal opinion | "UNSETTLED" stamp, and who to ask | "nobody can give you a number for this, and here's why" |

The weakest link wins: a figure built on a T3 characterisation is a T3 output.
**Never write "CRA requires"** for a folio position. **Tax Court Informal Procedure** decisions are not precedent:
don't cite them as the rule.

## 3 · Sources
**Primary (can carry a claim alone)**: canada.ca (CRA, Finance, ESDC for CPP/OAS), laws-lois.justice.gc.ca,
budget.canada.ca, fin.gc.ca, revenuquebec.ca, retraitequebec.gouv.qc.ca, legisquebec.gouv.qc.ca, provincial
government sites (ontario.ca, gov.bc.ca, alberta.ca, …), e-laws.ontario.ca, the courts (scc-csc.ca,
decisions.fca-caf.gc.ca, decision.tcc-cci.gc.ca, canlii.org), the securities regulators (securities-administrators.ca,
osc.ca, ciro.ca), fpcanada.ca (the Projection Assumption Guidelines), statcan.gc.ca and bankofcanada.ca.
`tools/claims.mjs` keeps the list (`PRIMARY`). Add a domain there with a comment when a new official one is needed.

**Secondary (supporting only)**: firm and law-firm articles, CPA Canada and STEP, the news, Summit's dossiers. These
help find and explain a rule. They never carry one alone.

**Summit's pack** (`reference/summit/tax-knowledge/parameters/<year>.json`) is a pointer to the source URL. It is
UNVERIFIED by its own label. If `pack_ref` is set, the tool compares values and **errors on a mismatch**: then
either the pack is wrong (note it, and tell Mo so Summit's `CHANGELOG` can be fixed) or the video is.

## 4 · Freshness
- `retrieved_on` older than **120 days** at export → re-verify (the tool errors).
- The video's `tax_year` must match each figure's year, or the figure is labelled with its own year on screen.
- **Calendar**: CRA indexation for next year is published each November (re-check every threshold); the federal
  budget and provincial budgets come February–April; prescribed rates change quarterly (announced about three weeks
  before the quarter); OAS amounts change quarterly; the FP Canada/IQPF guidelines come yearly (usually spring).
  `tools/freshness.mjs` lists published videos whose claims fall in a changed category so they get a pinned
  correction or a re-cut.
- A **proposed** measure (a budget, draft legislation) is labelled "PROPOSED" with the date. It's never stated as law.

## 5 · Worked examples
- Use an **illustrative family**, labelled every time it appears. Round inputs ($250,000, not $247,312).
- Keep both sides on the same basis: after-tax vs after-tax, real vs nominal, today's dollars vs future dollars.
  Say which.
- Charge every cost (the interest on a loan, the insurance premium, the penalty to break a mortgage).
- Combined rates (federal + provincial) name the province and the year.
- Know the traps from Summit's own defects (`reference/summit/docs/VERIFIED-DEFECTS.md`, canadian-tax skill §10):
  no AMT in the year of death; a T2's balances are closing balances; aggregate by owner, not household; dates are
  calendar dates; the inclusion rate applies exactly once.

## 6 · What the tool checks (`node tools/claims.mjs <slug>`)
1. The schema: required fields, a valid tier and behaviour, ISO dates.
2. Sources: a primary domain, the date retrieved, a quote (at least 20 characters).
3. Freshness (120 days at export), and the tax-year labels.
4. Calcs recompute.
5. Pack cross-check, when `pack_ref` is set and the snapshot exists.
6. Script linkage: every `{c:id}` in `SCRIPT.md` exists; every figure in the spoken paragraph (digits, "%", "$" and
   number words like "thousand") sits in a sentence with a tag; the tags are stripped into `voice.txt`.
7. Behaviour language: a GATE or DECLINE claim can't carry a `value`; a COMPUTE_WITH_CAVEAT claim needs the caveat
   phrase in the script sentence that uses it ("CRA" or "position").
8. The sign-off: `review.by` and `review.on` are filled at export (`--stage export`).
