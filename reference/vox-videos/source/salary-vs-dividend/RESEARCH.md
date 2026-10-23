# Salary vs dividend: research (CORP-04)

Researched 2026-10-22. Ontario + federal, 2026 tax year. Series: The Ledger (vertical short). Audience: owner-managers (families).

## The angle (Mo, 2026-10-22: no rate-cut storyline; keep it to salary vs dividend)
$10,000 of extra profit, two ways out. At Ontario's top rate, salary keeps $4,647 and a dividend keeps $4,539 under the rules
in force for 2027. The two are close by design (integration), so the real difference is what a salary buys (RRSP room, a CPP
pension). Kicker: a dividend only feels cheaper because its first tax bill is paid inside the company, where you don't see it.
The full ledger is in claims.json; the worked numbers are live formulas in salary-vs-dividend-backup.xlsx.

The rate change (Ontario's small-business rate cut on July 1, 2026, and the lower dividend credit from 2027) is used only as
the current law behind the numbers. It isn't narrated.

## Sources (primary, read 2026-10-22)
| Point | Source | Status | Tier · behaviour |
|---|---|---|---|
| Federal 2026 brackets; 33% over $258,482 | CRA, *Current year tax rates and income brackets (2026)* (page 2026-06-25); T4127 July 2026 Table 8.1 | verified | T1 · COMPUTE |
| Ontario 2026 brackets; 13.16% over $220,000 | same pages | verified | T1 · COMPUTE |
| Ontario surtax 2026: 20% over $5,818, 36% over $7,446 | T4127 July 2026 Table 8.2 (values as numbers, not prose) | verified (table) | T1 · COMPUTE |
| Surtax computed before the Ontario dividend credit | CRA Form ON428 **2025** e-text, lines 63–71 | 2026 form not published yet → re-check | T1 · COMPUTE |
| Gross-up 15% (non-eligible, years after 2018) | ITA s. 82(1)(b)(i), Justice Laws (current to 2026-09-30) | verified | T1 |
| Federal credit 9/13 of the gross-up | ITA s. 121(a) | verified | T1 |
| Federal small-business rate 9%; $500,000 business limit | CRA *Corporation tax rates* (page 2026-10-21); ITA 125(1.1), 125(2) | verified | T1 |
| Ontario lower rate 3.2% → 2.2% from July 1, 2026, prorated for straddling years | CRA *Corporation tax rates* footnote; ontario.ca *Corporate Income Tax* (updated 2026-04-27); Ontario Budget 2026 annex (2026-03-26) | verified | T1 |
| Ontario non-eligible credit 2.9863% → 1.9863% from January 1, 2027 | Ontario Budget 2026 annex; Bill 97, *Plan to Protect Ontario Act (Budget Measures), 2026*, Royal Assent 2026-04-24 (S.O. 2026, c. 2), Sched. 15: 15.2283% of the 82(1)(b)(i) amount (= 1.9863% of the grossed-up dividend) for taxation years ending after Dec 31, 2026 | **enacted** | T1 |
| RRSP room = lesser of 18% of prior-year earned income and the dollar limit | ITA s. 146(1) "RRSP deduction limit" | verified | T1 |
| 2026 RRSP dollar limit $33,810 | CRA *MP, DB, RRSP, DPSP, ALDA, TFSA limits, YMPE and YAMPE* (page 2025-12-01) | verified | T1 |

## Open (before the script is final)
1. "Earned income" excludes dividends: quote ITA 146(1) "earned income" (salary is in, dividends aren't listed).
2. CPP: salary is pensionable earnings, dividends aren't: quote the CPP Act / CRA payroll page.
3. Read Bill 97 Schedule 15's operative text (not just the explanatory note), and the Taxation Act, 2007 s. 19.1.
4. Quebec differs (QPP, its own rates and credits): say "Ontario only" on screen.
5. Integration as a policy aim: quote Finance's 2017 *Tax Planning Using Private Corporations* paper.

## Summit behaviour
COMPUTE throughout (statute and regulation). Summit's 2026 pack is empty by design, so no `pack_ref` cross-check. Summit's
CORP-04 is a full sweep (best salary across a range); this video does one marginal slice, not the sweep.
