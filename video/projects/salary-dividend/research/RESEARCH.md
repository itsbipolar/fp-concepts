# Why can a dividend feel cheaper than a salary?

Research attempt: **2026-10-23 UTC**. Scope: internal film development; Canadian federal + Ontario, **2026 taxation year**, with a 40-year-old Ontario resident who controls their Canadian private corporation. **Primary verification is blocked. No legal claim or rate in this dossier is marked verified.** The useful output is a bounded qualitative argument and a precise evidence backlog, not a numerical comparison.

## Actual access evidence

The managed-cloud runtime skill and its networking reference were read. The executor's `/etc/codex/network-policy.json` has restricted HTTP policy, package-manager destinations, no VPN, and no TCP grants. The current environment-status response reported `observations_current: true`, restricted mode, policy state `unknown`, no custom allowed hosts, and no official Canadian tax domains in its effective destination list. `unknown` does not establish that the policy is enforced; the request failures below establish the observed access problem.

Five ordinary HTTPS requests through inherited proxy settings, retaining TLS verification, were attempted at **2026-10-23T02:59:37 UTC**. Each failed before retrieving the official document with this exact error:

> `<urlopen error Tunnel connection failed: 403 Forbidden>`

| Requested official document | Publisher | Observed result |
| --- | --- | --- |
| [Income Tax Act, full text](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/FullText.html) | Justice Laws Website | Proxy CONNECT denied; no text retrieved |
| [CPP payroll contributions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp.html) | CRA | Proxy CONNECT denied; no text retrieved |
| [RRSP deduction limit](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/rrsp-deduction-limit.html) | CRA | Proxy CONNECT denied; no text retrieved |
| [Federal dividend tax credit](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40425-federal-dividend-tax-credit.html) | CRA | Proxy CONNECT denied; no text retrieved |
| [Corporation tax rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) | CRA | Proxy CONNECT denied; no text retrieved |

Machine-readable exact request URLs, timestamps and errors are in [access-checks.json](access-checks.json). Supporting primary passages, document effective dates and successful retrieval dates are all **null**, not copied from historical records. No proxy bypass, alternate host, archived fetching script or repeated retry was used. No secrets were inspected. No network setting was changed.

Concrete blocker: this execution session cannot currently retrieve the official sources required to substantiate either a quantified example or current qualitative legal claims. The draft can be prepared and rendered for creative review with its pending research status retained. Primary evidence remains a separate completion requirement; rendering cannot resolve it.

## Bounded scenario

Use 2026 throughout. Suggested illustrative person: age 40, Ontario resident all year, owns 100% of the voting shares and works in the business. The company is a CCPC earning active business income eligible for small-business treatment; assume no associated-company or passive-income complication. Compare reasonable salary for actual work with an ordinary **non-eligible taxable dividend**, paid in the same year. Exclude capital dividends, shareholder loans, eligible dividends and refundable corporate-tax complications from this film.

The shared comparison basis, if later quantified, is the **same incremental pre-remuneration company profit/cost budget**. Salary branch must fit gross salary **plus employer CPP and any other applicable employer costs** inside that budget. Dividend branch begins with the company tax attributable to the underlying profit; the remaining distribution then faces shareholder taxation with the applicable gross-up and credits. Comparing equal cash salary and dividend amounts at the owner's hand does not answer the same-company-cost question.

For the CPP/RRSP connection, assume ordinary pensionable employment, no other annual pensionable earnings and sufficient headroom below applicable annual ceilings; state that salary **can** add to the CPP earnings record and **can** create new RRSP room next year, subject to limits and adjustments. A salary payment above a ceiling does not necessarily create an additional benefit or more room. RRSP room is a tax-deferred saving permission, not money deposited into an RRSP.

## Proposed film wording — research pending

These are careful candidate statements, **not authoritative verified quotations**. Claim IDs link to [claims.json](claims.json).

- `{c:salary-deductible}` “A reasonable salary for your work can reduce the company's taxable income.”
- `{c:dividend-after-corporate-tax}` “A dividend comes from profit after company tax.” Use only for the stated ordinary active-income scenario. Visually retain the company tax payment when the dividend reaches the owner.
- `{c:dividend-credit}` “You then pay personal tax, with a dividend tax credit.” Do not imply zero personal tax or exact reimbursement of company tax.
- `{c:salary-cpp}` “Salary can add to your CPP earnings record.” Show a record entry connected to the older owner; do not show a pension dollar balance or guaranteed pension increase.
- `{c:salary-rrsp-next-year}` “And create new RRSP room for next year.” The 2026 salary may generate room in **2027**, governed by that year's limit and adjustments. This is a timing statement, not reuse of the old 2027 tax example.
- `{c:dividends-no-new-earnings}` “Dividends don't create those new earnings or new room.” Keep **new** in both the wording and visual logic. Existing unused RRSP room and prior CPP records remain visible.
- `{c:no-winner}` “Compare the same company cost—and the consequences beyond today's cash.” This is the closing comparison method; it asserts no winner.

A particularly defensible **12–15 second representative passage** is the company/personal-tax reveal: owner receives the dividend while the scene opens backward to reveal the company tax already paid, then a personal-tax slip appears beside the owner and a smaller labelled `dividend tax credit` tab engages that bill. Candidate caption rhythm: “A dividend reaches you after company tax.” → “Then comes your personal tax—with a dividend tax credit.” No amounts, widths, money counts, percentages, scales or timing ratios should encode a tax rate. Treat this passage as a research-pending internal creative draft while official access is blocked.

The CPP/RRSP consequence can follow in the full film, using a salary-specific record line and a next-year room outline. It is less suitable as the lone demonstration because it does not answer why the dividend can *feel* cheaper. Avoid the categorical sentence “A dividend only feels cheaper because…”: differences in payroll contributions, rates, income, timing and circumstances can produce real cash differences as well as a visibility effect.

## Evidence classification and remaining work

The ledger records **pending-primary-verification** for the proposed rules. Law pointers are research targets: ITA business-income computation and salary reasonableness (including s.67); ordinary dividends/gross-up and credit (ss.82 and 121); RRSP earned income and deduction limit (s.146). These references were not opened successfully. CRA pages are intended administrative explanations, not legislation. No case-specific interpretation has been resolved.

The supplied educational notes remain secondary support only. `sources/v0-cfp-crash-notes/notes.txt` describes “DTC as fraction of gross-up” in its dividend section, “Earnings only … not investment income” in CPP, “Earned income includes Employment” and “Excludes Interest, dividends” in RRSP, plus “unused room carried forward.” They motivate the candidate relationships; they do not verify current law. No numerical value from those notes is used here.

The historical `reference/vox-videos/source/salary-vs-dividend/RESEARCH.md` calls its scope 2026 while its worked comparison expressly uses 2027 rules. It also describes a mid-2026 Ontario corporate rate change and a 2027 dividend-credit change. Those are **unverified historical claims**, not current inputs. Do not silently carry over its rates, dollar outputs, “verified” labels, dates, quotes or omitted-payroll assumptions. A 2026 corporate year that straddles a rate change may require proration if that change is independently substantiated. The applicable corporate fiscal period must be specified before a number is computed.

Before quantification, independently retrieve and quote: federal/Ontario company rules and fiscal-period rates; 2026 personal brackets, credits, gross-up, Ontario surtax and health premium; **both employee and employer CPP including both earnings bands, exemption, rates and maxima**; controlling-shareholder EI exclusion (proposed 100% voting control; obtain authoritative rule rather than assuming owner status alone settles it); applicable Ontario EHT/WSIB or explicit supported exclusions; RRSP definition, timing, adjustments and applicable next-year cap. Related corporations and company payroll can affect provincial employer costs. No claim that provincial costs are universally zero is supported here.

A full numerical model must solve salary plus employer costs from the common company budget, apply personal income tax and employee contributions, and independently compare dividend after company and shareholder tax. It must state whether it measures incremental cash versus total annual cash and include other income because thresholds matter. Retained earnings, source deductions and final tax are distinct. Show no numeric winner until those inputs, independent calculation/boundary checks and the live review workbook required by `docs/VIDEO-EVIDENCE.md` exist.

No financial arithmetic is used in this dossier. There is no workbook or calculation result to validate, and no sourced rate was substituted with a remembered figure.
