# Financial scope and source notes

This is a **qualitative visual prototype**, not a salary/dividend tax calculator. The orange note and paper sizes encode no amounts. No tax winner, equal-company-cost result, CPP pension amount or RRSP dollar amount is claimed.

## Supplied source material

The repository's [v0 study notes](../../sources/v0-cfp-crash-notes/notes.txt) support the mechanisms used here:

- Lines 218–226: taxable dividends, gross-up and dividend tax credits.
- Lines 540–552: employee/employer CPP, pensionable earnings and limits; investment income does not generate contributions.
- Lines 615–626: RRSP room from prior-year earned income, unused room carried forward; employment income included and dividends excluded.

These are supplied educational notes, not an independently verified current primary source. The prototype does not reproduce the rates or dollar limits from them. Reasonable salary deductibility and non-deductibility of dividends are presented as general tax treatment; their authoritative rule references must be checked before expanding this into a quantified published lesson.

## Live verification remains pending

Official Canadian financial sites were denied by this environment's network proxy. The running policy contained package-manager hosts and no Canada.ca/Ontario.ca entries. A draft adding `canada.ca`, `www.canada.ca`, `ontario.ca` and `www.ontario.ca` was saved. Saving a draft does not apply it; review/save/publish through environment settings is required. Do not claim the links below were fetched successfully during this build.

Primary-source starting points for the next quantitative pass:

- [CRA CPP contributions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp.html)
- [CRA RRSP deduction limit](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/rrsp-deduction-limit.html)
- [CRA dividend tax credit](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40425-federal-dividend-tax-credit.html)
- [Ontario personal income tax](https://www.ontario.ca/page/personal-income-tax)

## Before adding amounts

Choose the year and jurisdiction; verify company rates and eligibility, reasonable remuneration, CPP earnings bands/exemptions, personal brackets and credits, dividend gross-up/credits, any surtax/health premium, and RRSP timing/limits. State a common company-cost or pre-compensation-profit basis. Calculate salary plus employer contributions and dividend after corporate tax from that basis; independently verify representative and boundary cases. Pension entitlement needs a contribution history and benefit model, not a direct conversion of premiums into a savings bag.
