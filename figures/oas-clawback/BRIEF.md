# Brief: OAS clawback (the overflow line)

| | |
|---|---|
| Catalog ID | R1 |
| Slug / folder | `figures/oas-clawback/` |
| Domain / palette | Retirement / `ret` |
| Archetype | A2 weir / overflow |
| Sources | v0 Retirement > "OAS, GIS and the Allowance" (clawback, 2026 thresholds); v0 Retirement > RRIF minimums; v0 Tax > dividends (gross-up); v0 Tax > "From income to tax payable" (net income) |
| Facts re-checked on | not yet: re-check against Canada.ca (OAS recovery tax 2026 income) before publishing |
| Status | verified (see log) |

## 1. The rule, plain
Once your net income passes $95,323 (2026), the government takes back 15 cents of your Old Age Security for every
dollar above that line, until all of it is gone. Withdrawals from a TFSA aren't income, so they never push you over.

## 2. The rule, exact
- OAS recovery tax ("clawback") = 15% x (net income - $95,323), for 2026 income. [`ret.oasClawThreshold`, `ret.oasClawRate`]
- It stops when the whole OAS is recovered: at $155,320 for ages 65–74 ($161,320 at 75+). [`ret.oasGone6574`]
- So the OAS amount the figure uses is the amount fully recovered at that point:
  (155,320 - 95,323) x 15% = **$8,999.55 a year** (about $750 a month). The v0 monthly maximum is $762.50
  (Oct–Dec 2026, indexed quarterly), so this is a close, internally consistent simplification.
- **Net income counts:** OAS itself, CPP, RRIF withdrawals (minimum and extra), eligible dividends at their
  **grossed-up** value (x 1.38). [`tax.eligGrossUp`] (v0 Tax, "Total income ... grossed-up dividends ... OAS/CPP ... RRSP withdrawals")
- **Doesn't count:** TFSA withdrawals (v0 Retirement, RRSP vs TFSA table: "Tax-free; no effect on OAS or GIS").
- RRIF minimum at 68: 1 / (90 - 68) x Jan 1 value. [`ret.rrifMinUnder71`]

## 3. The misconception
"A dollar out of my RRIF and a dollar out of my TFSA are the same dollar." The client takes the same $30,000 both
ways and sees the clawback stat jump from $0 to $3,941 on one path and stay at $0 on the other. Second, quieter
lesson in the see-through: $20,000 of dividends sits in the column as $27,600.

## 4. Mapping: rule -> machine
| Rule component | Machine part | Moves when / how | FP_FACTS |
|---|---|---|---|
| Net income | tall glass NET INCOME column; water height on a fixed $1,500/unit scale | rises when RRIF money is pumped in | |
| What counts | coloured layers of water (see-through): OAS, CPP, RRIF minimum, dividends, gross-up, RRIF extra | layers stack in that order | `tax.eligGrossUp` |
| $95,323 threshold | the weir crest: an orange line and the spout's height on the column | fixed | `ret.oasClawThreshold` |
| Income above the line | water spilling out of the spout into the OVERFLOW tube, on the same scale | fills as income passes the line | |
| 15% recovery | a gauge on the tube (float -> rod -> needle) and gold OAS coins hopping to the grey TAX plinth: 1 coin ($500) per $3,333 of overflow | as overflow rises | `ret.oasClawRate` |
| OAS fully gone | red ring on the tube at $59,997 of overflow ($155,320 income); last coin leaves | | `ret.oasGone6574` |
| RRIF | glass RRIF jar with a pump and a pipe into the column top | level drops $10k per press | `ret.rrifMinUnder71` |
| TFSA | sealed glass TFSA jar with a tap into a CASH pail, no pipe to the column | level drops $10k per press | |
| The tax system | grey TAX plinth (`FP_CRA`), no government branding | receives coins | |

## 5. Persona and worked numbers
Fictional: a single retiree, 68. CPP $15,000/yr; RRIF worth $880,000 on Jan 1 (minimum 1/22 = $40,000);
$20,000 of eligible dividends from a non-registered portfolio (grossed up to $27,600); OAS $8,999.55; TFSA $60,000.

Base net income = 8,999.55 + 15,000 + 40,000 + 27,600 = **$91,599.55** (just under the line).

| State (URL params) | Cash taken | Net income | Clawback | OAS coins left / at TAX |
|---|---|---|---|---|
| (start) | $0 | $91,600 | $0 | 18 / 0 |
| `rrif=10000` | $10,000 | $101,600 | $941 (= 6,276.55 x 15%) | 16 / 2 |
| `rrif=30000` | $30,000 | $121,600 | $3,941 | 10 / 8 |
| `tfsa=30000` | $30,000 | $91,600 | $0 | 18 / 0 |
| `rrif=70000` | $70,000 | $161,600 | $9,000 (all of it) | 0 / 18 |

Coins: 18 x $500; coins at TAX = round(clawback / 500).

## 6. Interaction
- **Buttons:** "Take $10k from RRIF", "Take $10k from TFSA", "Start over". (Clicking the jars does the same.)
- **Out of order / limits:** TFSA empty -> "The TFSA is empty"; RRIF extra capped at $80,000 -> "That's enough for one year".
  First RRIF press that crosses the line -> "Over the line: 15 cents of OAS per dollar". TFSA press -> "TFSA
  withdrawals aren't income: the column doesn't move".
- **Stats:** CASH TAKEN, NET INCOME, OAS CLAWBACK.
- **URL params:** `rrif`, `tfsa` (dollars of extra withdrawal).

## 7. See-through and labels
- See-through turns the uniform "income water" into its source layers and shows the float, rod and gauge pinion in
  the overflow tube.
- Surface labels: RRIF, TFSA, CASH, NET INCOME, $95,323 LINE, OVERFLOW, OAS, TAX.
- Inside labels: OAS (COUNTS TOO), CPP, RRIF MINIMUM, DIVIDENDS, GROSS-UP 38%, RRIF EXTRA, FLOAT, OAS GONE $155,320.

## 8. Five metaphor tests
1. **Faithful:** the column only takes counted income; the TFSA has no pipe to it; coins leave only from the
   overflow at 15%; nothing leaves past the OAS amount. No operation gives a wrong clawback.
2. **One idea:** "income above $95,323 costs you 15% of your OAS; TFSA money doesn't count."
3. **Numbers move things:** threshold = crest height; overflow = tube height; clawback = coins moved and gauge angle.
4. **Misconception breaks:** same $30k, two buttons, two outcomes.
5. **Five seconds closed:** a full column, a spout, a tube filling, coins leaving: "going over the line costs me coins."

## 9. Simplifications (in `fpPage({ note })`)
Federal OAS recovery tax only, ages 65–74, 2026 income; OAS shown as about $9,000 a year; income tax on the
withdrawals and the dividend tax credit not shown; fictional persona.

## 10. Verification log
| Round | What was checked | Found / fixed |
|---|---|---|
| 1 | default view, closed + see-through | tube and RRIF hidden behind the column; solid column cap hid the water -> re-laid along the view diagonal (RRIF, TFSA left; column; tube, OAS, TAX right), cap made an open frame |
| 2 | labels, closed + see-through | every pill fell into the left column with leaders across the machine -> right-hand parts now get a row of pills under the board (`oaRowTags`); spill stream added while pouring |
| 3 | 7 angles x closed/see-through, phone, press run (RRIF, RRIF, TFSA) | all coherent; band labels pointed at hidden walls from behind -> anchored on the facing wall; row kept clear of the zoom chip |
| numbers | `shoot.py errors` at every persona state | start $91,600 / $0 · rrif=10000 $101,600 / $941 · rrif=30000 $121,600 / $3,941 · tfsa=30000 $91,600 / $0 · rrif=70000 $161,600 / $9,000 · press run ends $111,600 / $2,441, 5 coins: all match the hand calculation |

Exports in `dist/`: `1-start`, `2-rrif-30k`, `3-tfsa-30k`, `4-inside` (feed, square, wide each), `spin.mp4`, `spin.gif`.
Known polish item: in the 4:5 feed still the machine sits high with empty space below; a portrait-specific framing would fill it.

## 11. Compliance pass
Pending: owner's house rules (docs/COMPLIANCE.md). Self-check: no advice wording, no logos, fictional persona,
dated figures, disclaimer present.

## 12. Post copy (draft)
- Hook: "Same $30,000. One withdrawal costs you $3,941 of OAS. The other costs nothing."
- Rule: "Above $95,323 of net income (2026), 15 cents of OAS goes back for every dollar. TFSA withdrawals don't count."
- Alt text: "Hand-drawn machine: a glass column of retirement income with a spout at $95,323; water spilling into an
  overflow tube moves gold OAS coins to a grey tax plinth, while a TFSA jar pours into a cash pail without touching
  the column."
