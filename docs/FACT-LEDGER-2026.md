# Fact ledger: 2026

Every rule number a figure uses lives here, with its source, and is mirrored in `FP_FACTS` in
`.claude/skills/fp-figures/assets/fp-kit.js`. **Change both together.** A figure never hard-codes a rule number.

- **Source key:** `v0` = CFP crash notes (`sources/v0-cfp-crash-notes/`), whose 2026 figures were "checked against
  CRA, ESDC, CIPF, CDIC and Assuris on Oct 1, 2026". Later sources get `v1`, `v2`... (see `docs/SOURCES.md`).
- **Indexing:** `Y` = indexed yearly (Jan), `Q` = quarterly, `J` = each July (benefit year), `—` = fixed until changed by law.
- **Before publishing** any figure: re-check every row it uses against the official source (CRA, ESDC, etc.) and
  write the date in its brief. A row marked **verify** has a known caveat.
- Federal figures only unless stated. Provincial tax and Quebec rules are out of scope until a source covers them.

## Tax
| Fact | Value | Idx | FP_FACTS key | Source |
|---|---|---|---|---|
| Federal brackets 2026 | 14% to $58,523 · 20.5% to $117,045 · 26% to $181,440 · 29% to $258,482 · 33% above | Y | `tax.brackets` | v0 Tax |
| Lowest rate (credit rate) | 14% (was 15%; notes outdated) | — | `tax.lowestRate` | v0 Tax |
| Basic personal amount | $16,452, shrinking to $14,829 between $181,440 and $258,482 | Y | `tax.bpa`, `tax.bpaMin` | v0 Tax |
| Age amount (65+) | $9,208, reduced by 15% of net income over about $46,000 | Y | `tax.ageAmount` | v0 Tax (threshold approx: **verify**) |
| Pension amount | $2,000 | — | `tax.pensionAmount` | v0 Tax |
| Capital gains inclusion | 50% (the proposed 2/3 rate was cancelled March 2025) | — | `tax.cgInclusion` | v0 Tax |
| Eligible dividends | gross-up 38%, federal DTC 15.02% of grossed-up | — | `tax.eligGrossUp`, `tax.eligDTC` | v0 Tax |
| Non-eligible dividends | gross-up 15%, federal DTC 9.03% of grossed-up | — | `tax.nonEligGrossUp`, `tax.nonEligDTC` | v0 Tax |
| Worked example | $10,000 eligible -> $13,800 x 33% = $4,554 - $2,073 DTC = **$2,481** | | | v0 Tax |
| LCGE (QSBC shares) | $1,275,000 | Y | `tax.lcge` | v0 Tax |
| Small business deduction limit | $500,000 | — | `tax.sbdLimit` | v0 Tax |
| AMT | exemption $181,440, rate 20.5%, carry-forward 7 years; 100% of gains, 30% of LCGE and donated-securities gains | Y | `tax.amtExemption`, `tax.amtRate`, `tax.amtCarryYears` | v0 Tax |
| Prescribed rate | 3% (Q4 2026), interest paid by Jan 30 each year | Q | `tax.prescribedRate` | v0 Tax |
| TFSA | $7,000 for 2026; $109,000 cumulative if 18+ in 2009; 1%/month over-contribution | Y | `tax.tfsaAnnual`, `tax.tfsaCumulative` | v0 Tax |
| Donation credit | 14% first $200 · 29% above · 33% on the part above $258,482; up to 75% of NI (100% year of death and prior) | Y | `tax.donation` | v0 Tax |
| Listed securities donated | 0% capital-gain inclusion (30% for AMT) | — | | v0 Tax |
| Superficial loss window | 30 days before and after; still held on day 30 | — | | v0 Tax |
| TOSI | <18 top rate; 18–24 reasonable return / safe harbour; 25+ exclusions: 20 hrs/wk, 10% shares, owner spouse 65 | — | | v0 Tax |
| Instalments | net tax owing > $3,000 this year and either of 2 prior years | — | `tax.instalmentThreshold` | v0 Tax |
| Principal residence | exempt = (1 + years designated) / years owned x gain; one designation per family unit per year | — | | v0 Tax |

## Retirement
| Fact | Value | Idx | FP_FACTS key | Source |
|---|---|---|---|---|
| RRSP dollar limit | $33,810 (2026); 18% of last year's earned income; $2,000 buffer | Y | `ret.rrspLimit`, `ret.rrspPct`, `ret.rrspBuffer` | v0 Ret |
| Money purchase / DB / DPSP | $35,390 · $3,932.22 per year of service · $17,695 | Y | `ret.mpLimit`, `ret.dbMaxPerYear`, `ret.dpspMax` | v0 Ret |
| CPP earnings | YBE $3,500 · YMPE $74,600 · YAMPE $85,000; 5.95% each (11.9% self-employed); CPP2 4% | Y | `ret.ybe`, `ret.ympe`, `ret.yampe`, `ret.cppRate`, `ret.cpp2Rate` | v0 Ret |
| CPP max retirement at 65 | $1,507.65/month | Y | `ret.cppMax65` | v0 Ret |
| CPP start age | 60–70; -0.6%/month before 65 (-36% at 60), +0.7%/month after (+42% at 70); permanent | — | `ret.cppEarlyPerMonth`, `ret.cppLatePerMonth` | v0 Ret |
| CPP death benefit | $2,500 lump sum | — | `ret.cppDeathBenefit` | v0 Ret |
| OAS clawback | 15% of net income over $95,323 (2026 income); gone at $155,320 (65–74) / $161,320 (75+) | Y | `ret.oasClawThreshold`, `ret.oasClawRate`, `ret.oasGone6574`, `ret.oasGone75` | v0 Ret |
| OAS maximum | $762.50/month (65–74), $838.75 (75+), Oct–Dec 2026 | Q | `ret.oasMax6574`, `ret.oasMax75` | v0 Ret |
| OAS deferral | +0.6%/month to 70 (max +36%) | — | `ret.oasDeferPerMonth` | v0 Ret |
| OAS residence | 10 years minimum, 40 for full, 20 to be paid abroad | — | `ret.oasMinYears`, `ret.oasFullYears` | v0 Ret |
| GIS single | max $1,138.90/month, income under $23,112; drops ~50 cents per $1 of other income | Q | `ret.gisSingleMax`, `ret.gisSingleIncomeCap`, `ret.gisReductionPerDollar` | v0 Ret |
| RRIF minimum | under 71: 1 / (90 - age) x Jan 1 FMV; 71: 5.28% · 75: 5.82% · 80: 6.82% · 85: 8.51% · 90: 11.92% · 95+: 20% | — | `ret.rrifMinUnder71`, `ret.rrifTable` | v0 Ret |
| Spousal RRSP | withdrawal before Jan 1 of the 3rd calendar year after the contribution year taxed to contributor | — | `ret.spousalAttributionYears` | v0 Ret |
| RRSP lump-sum withholding | 10% to $5,000 · 20% to $15,000 · 30% above (outside Quebec) | — | `ret.withholding` | v0 Ret |
| OAS clawback check (worked) | net income $120,000: (120,000 - 95,323) x 15% = **$3,701.55** clawed back for the year | | | derived from v0 |

## Home, education, protection
| Fact | Value | Idx | FP_FACTS key | Source |
|---|---|---|---|---|
| HBP | $60,000 per person, own RRSP only; repay 1/15 a year from year 2 (year 5 for 2022–25 withdrawals) | — | `home.hbpMax`, `home.hbpRepayYears` | v0 Process |
| FHSA | $8,000/yr, $40,000 lifetime, carry-forward max $8,000; close by year 15 or age 71 | — | `home.fhsa*` | v0 Process |
| GDS / TDS | guidelines 32% / 40%; CMHC limits 39% / 44%; 3% of any LOC limit counts in TDS | — | `home.gds*`, `home.tds*`, `home.locInTds` | v0 Process |
| Stress test | higher of 5.25% or contract + 2% | — | `home.stressFloor`, `home.stressAdd` | v0 Process |
| Minimum down payment | 5% on first $500k · 10% to $1.5M · 20% at $1.5M+; insured cap $1.5M | — | `home.downTiers`, `home.insuredCap` | v0 Process |
| RESP | $50,000 lifetime; CESG 20% on $2,500 = $500/yr ($1,000 with catch-up), $7,200 lifetime; 31 yrs contributions, 35 to close; AIP not rolled = +20% | J (A-CESG) | `resp.*` | v0 Process |
| CDIC | $100,000 per person, per member, per category | — | `protect.cdic` | v0 Process |
| CIPF | $1M per dealer for each account group | — | `protect.cipf` | v0 Process |
| Assuris | greater of 90% or $1M death benefit | — | `protect.assurisDeath` | v0 Process |

## Estate
| Fact | Value | Idx | FP_FACTS key | Source |
|---|---|---|---|---|
| Ontario estate administration tax | $15 per $1,000 over $50,000; nothing on the first $50,000 | — | `est.ontarioEatPer1000`, `est.ontarioEatFreeFirst` | v0 Est |
| Trust deemed disposition | every 21 years | — | `est.trustDeemedYears` | v0 Est |
| Graduated rate estate | up to 36 months | — | `est.greMonths` | v0 Est |
| U.S. estate tax | exemption US$15M (2026), unified credit $5,945,800 x (U.S. assets / world estate), top rate 40%, Form 706-NA over US$60,000 U.S. assets | Y | `est.usExemption`, `est.usUnifiedCredit`, `est.usTopRate`, `est.us706Threshold` | v0 Est |
| U.S. worked example | US$1M Florida condo, US$20M world estate: credit $297,290, tax on $1M $345,800 -> $48,510 before the Canadian FTC | | | v0 Est |

## Change log
| Date | Change | By |
|---|---|---|
| 2026-10-22 | Ledger created from v0 (figures checked Oct 1, 2026) | project setup |
