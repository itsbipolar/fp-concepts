# The illustrative families (a recurring cast)

Worked examples need a family. Reusing a small cast of **invented** households across videos builds familiarity
("the MacGregors are back, now at the second death"), and it keeps us honest: no real client ever appears. The cast
comes from Summit AI's golden households (`reference/summit/docs/GOLDEN-HOUSEHOLDS.md`), so a video's worked
example can later be cross-checked against Summit's own expected values for the same family.

## Rules
1. **Always labelled**: the ILLUSTRATIVE FAMILY stamp on screen every time they appear, and "an illustrative family"
   in the narration the first time.
2. **Invented, and never composited from a real client**, even loosely. No real addresses (a town name is fine:
   Oakville, Muskoka).
3. **No faces** (the kit's rule): silhouettes, objects (the cottage, the company sign, the policy), or `PersonIcon`.
4. **The numbers are ours, per video**: round illustrative inputs in `claims.json` (`illustrative: true`), worked
   for the video's tax year. Summit's own figures for the family are its test expectations, not facts. Don't
   quote them.
5. Keep a family's facts consistent across videos: `ideas/cast.json` records what each video established (ages,
   holdings, structure). Check it before reusing a family. A change needs a reason ("ten years later").

## Casting by topic
| Topic | Family (Summit GH) | Why |
|---|---|---|
| Owner-manager pay, the passive grind, the CDA, freezes, the 21-year rule, double tax at death | **The MacGregors** (GH01; family group GH20): Ontario, Holdco 60/40, a family trust (settled 2008), the cottage, a triplex | The full owner-manager story in one family |
| Associated companies, the shared business limit, 55(2) | the two-company owner-manager (GH33) | |
| Professional corporations: physicians | **The Patels** (GH06): an Ontario physician PC, spouse with non-voting shares, an IPP | IPPs, TOSI and the PC rules |
| Law and accounting partners | **The Okafors** (GH02–04): a law partner through a PC; the accounting partner (GH05) | SPI/SCI, partnership draws, the business limit |
| Retirement decumulation, OAS recovery, RRIF/LIF, DB pensions | the retired couple (GH10) · **the Lefebvres** (GH22): snowbirds with accounts at four institutions | Meltdown, splitting, residency days |
| US connections | **The Chen-Walkers** (GH19): a US-citizen spouse, a TFSA, an IRA, a Florida condo | US estate tax, US persons, situs |
| Older wealth, giving, the estate bond, cascades | **The Rossis** (GH24) · **Mrs Hughes** (GH23): a widow, 78, with GICs and charitable intent · the philanthropic couple (GH26) | Insured annuity, gifts in kind, DAFs, CRTs |
| Insurance as a corporate tool | the insurance-heavy Holdco (GH25): joint last-to-die, an IFA | The CDA credit, the IFA, ownership |
| Family events | separation (GH28) · the cottage with three children (GH30) · the blended family (GH31) · the disability/Henson trust family (GH27) · the trust family paying tuition (GH13) | |
| Business sale, first death | the year of a sale (GH17) · the year of the first death (GH18) | Liquidity events, terminal returns |
| Quebec | **The Tremblays** (GH08) · the Quebec couple (GH09) | Quebec is its own jurisdiction: flag, or cover properly |
| The baseline "regular" family (for contrast) | the salaried Ontario couple (GH32, "the Harts") · the young single-income family (GH16) · the single professional (GH34) | "Here's what changes when there's a company" |

`ideas/cast.json` starts empty. Add `{ "family": "MacGregor", "video": "<slug>", "established": { … } }` after each
video that uses one.
