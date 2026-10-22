# Brief: RRSP vs TFSA (tax the seeds or tax the harvest)

| | |
|---|---|
| Catalog ID | R2 |
| Slug / folder | `figures/seeds-or-harvest/` |
| Domain / palette | Retirement / `ret` |
| Style | **everyday analogy** (proposed direction, `docs/VISUAL-DIRECTION.md`): a familiar scene, not an invented machine |
| Sources | v0 Retirement > RRSP vs TFSA table ("Compare them: ... If tax rate in = tax rate out, they tie"); v0 Tax > deductions |
| Facts re-checked on | no dated figures used: tax rates and growth are labelled examples |
| Status | prototype for owner review |

## 1. The idea in one sentence (9th-grade test)
"With a TFSA you pay tax on the seeds; with an RRSP you pay tax on the harvest. If the tax rate is the same both
times, you end up with exactly the same amount."

## 2. The rule, exact
- RRSP: contributions are deductible, so the whole pre-tax amount is invested (the tax refund is what makes that
  possible); growth is sheltered; withdrawals are taxed as income.
- TFSA: contributions come from after-tax money; growth is sheltered; withdrawals are tax-free.
- Same rate in and out -> same after-tax result: 10,000 x (1 - t) x G = 10,000 x G x (1 - t).

## 3. The analogy (why a garden)
Everyone knows seeds, planting, waiting and harvesting. "Pay tax on the seeds or on the harvest" is the line advisors
already use. Money as gold coins (each coin = $1,000, said once in plain words).

| Garden | Means |
|---|---|
| a sack of 10 gold-coin seeds, "$10,000" | money you earned, before tax |
| TFSA garden: 3 seeds go to the TAX basket first, 7 are planted | you invest after-tax money |
| RRSP garden: all 10 seeds are planted | the deduction: no tax going in |
| every seed grows into 3 coins in 20 years | growth (a made-up example), sheltered in both |
| TFSA harvest: every coin into your basket | tax-free withdrawals |
| RRSP harvest: the tax basket takes its share first | withdrawals are taxed |

## 4. Worked numbers (today's tax rate 30%, growth x3)
| Tax rate at harvest | TFSA keeps | RRSP keeps | Tax paid TFSA / RRSP |
|---|---|---|---|
| 20% (lower) | $21,000 | $24,000 | $3,000 / $6,000 |
| 30% (same) | $21,000 | $21,000 | $3,000 / $9,000 |
| 40% (higher) | $21,000 | $18,000 | $3,000 / $12,000 |
(Coins: TFSA 7 planted -> 21; RRSP 10 planted -> 30; harvest tax = round(30 x rate).)

## 5. Interaction
- Buttons: "Plant the seeds" -> "Wait 20 years" -> "Harvest"; "Tax rate at harvest" picker (20 / 30 / 40%);
  "Start over". Out of order: a short note ("Plant the seeds first").
- Stats: Years, TFSA: you keep, RRSP: you keep ("?" until harvest).
- One plain-English story line under the scene, changing with each step.
- "What it means" switch: labels that map each garden part to the real rule.

## 6. Language rules applied
Whole sentences, "you", dollars not units, the real term once, no jargon on the scene (signs say TFSA / RRSP and
"TAX THE SEEDS" / "TAX THE HARVEST").

## 7. Simplifications (disclaimer note)
Tax rates and growth are made-up examples; real returns vary and aren't guaranteed. The RRSP refund is shown as
planting the full amount. Contribution room and other rules not shown.
