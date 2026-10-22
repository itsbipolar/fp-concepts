# Compliance and publishing guardrails (Canada)

These figures are client education and marketing for a Canadian wealth-management practice. This page is a working
checklist, **not legal or regulatory advice**: the firm's compliance department (and its dealer, MGA or regulator
rules) has the final word. Confirm the rules that bind you and record them here as "house rules".

## Every figure, before publishing
- [ ] **Education, not advice.** No recommendation, no "you should", no product names or tickers unless compliance
      approved them. Buttons use neutral verbs ("Withdraw from RRIF", not "Do this to save tax").
- [ ] **Disclaimer present:** `fpPage()` adds "Educational illustration, not advice..." with the as-of year.
      Add a `note` for every simplification (e.g. "Federal tax only; credits ignored").
- [ ] **Dated figures:** every number traced to a `FACT-LEDGER-2026.md` row, re-checked against the official source
      within 30 days of publishing; date written in the brief.
- [ ] **Fictional personas only.** No client names, likenesses, real balances or anything identifying (privacy law:
      PIPEDA / provincial equivalents). Round numbers.
- [ ] **No implied endorsement:** no government logos, crests, the Canada wordmark or CRA branding; the tax
      collector is a generic grey box labelled TAX. No other firms' trademarks.
- [ ] **Professional designations used correctly:** follow FP Canada's guidelines for the CFP® marks (and IQPF's for
      Pl. Fin.) on the page around the figure; don't place designation marks inside the drawing.
- [ ] **Projections and returns:** if a figure shows growth, state the assumed rate, that it is hypothetical, and
      that returns are not guaranteed. Never show performance of a real product.
- [ ] **Insurance content:** keep it generic (needs, taxation, structures); product-specific material goes through
      the insurance compliance route (MGA / carrier), with licensing disclosure as required in each province.
- [ ] **Regulatory approval:** submit the built HTML, the stills and the post copy to the firm's compliance review
      (for a CIRO dealer this is the communications/advertising approval process; for insurance, the MGA or carrier).
      Record approval reference and date in the brief.
- [ ] **Record keeping:** keep the exact approved files (dist folder at the approved commit, git tag
      `pub/<slug>/<date>`) for the retention period your firm requires.
- [ ] **Accessibility:** the post copy describes what the figure shows (alt text); colour is never the only signal.
- [ ] **Language:** Quebec audiences need French versions (Charter of the French Language); plan a `fr` variant.

## House rules (fill in with your compliance team)
| Rule | Detail | Confirmed by / date |
|---|---|---|
| Approval route | _e.g. submit to compliance@... with the dist folder; turnaround 5 business days_ | |
| Required disclaimer wording | _paste the firm's approved disclaimer; fpPage({ firm }) can append it_ | |
| Firm name / logo use | | |
| Social platforms allowed | | |
| Archival period | | |

## Why the figures are a good fit for compliance
They show rules, not recommendations; every number has a source and a date; the build is deterministic (same commit,
same files); and the brief documents the reasoning, which is the record a reviewer wants.
