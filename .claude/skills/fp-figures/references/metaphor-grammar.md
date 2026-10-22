# Metaphor grammar: from a financial rule to a machine

> **Read `docs/VISUAL-DIRECTION.md` first.** The owner found an invented machine (Fig. 01) too hard to decode. The
> proposed style is an everyday scene people already know (Fig. 02's garden). Use this page to find the *shape* of a
> rule (a threshold, a schedule, a test), then pick a familiar scene with that shape from the analogy bank there.

The whole project rests on one move: **find the machine whose physics already behaves like the rule.** When the
match is right, the client doesn't need the label to get it; the label just names what they already saw.

## 1. Materials: what money is made of

Pick one material per figure and keep it.

| Material | Use for | Why |
|---|---|---|
| **Water** in pipes and tanks | continuous flows: income, cash flow, withdrawals, tax leaking each year | levels, overflow, taps and leaks read instantly |
| **Coins** (`fpCoinStack`, `FP_GOLD`) | discrete amounts: contributions, grants, credits, a $5,000 unit | countable; "20% match" = 1 coin per 5 |
| **Marbles** on a run | decision trees: tests, eligibility, "which rule applies" | a marble choosing a path is a flowchart you can watch |
| **Blocks / crates** | assets with an owner and a cost: shares, a cottage, a rental | can carry two numbers (ACB stamp, FMV stamp), change owner, get frozen |
| **Ice** | values fixed in time | estate freeze, locked-in, frozen YBE |
| **Paper slips** | documents and elections: T2057, beneficiary designation, will | the slip in a slot is what changes the route |

## 2. The ten archetypes

Most planning rules are one of these shapes. Start from the archetype, then specialise.

| # | Archetype | The physics | Rules it fits |
|---|---|---|---|
| A1 | **Tank and tap** | containers with an inlet, an outlet and a tap that takes a share at one end | RRSP vs TFSA vs non-registered, RRIF minimum drain, FHSA, RESP, RDSP |
| A2 | **Weir / overflow** | a level line; whatever spills over is skimmed at a rate | OAS clawback (15% over $95,323), GIS (50 cents per $1), BPA shrink, age amount |
| A3 | **Bracket tower** | stacked tanks, each with its own tap rate; fill from the bottom | marginal rates, "only the dollars above the line pay more", top-rate traps |
| A4 | **Marble sorter** | a run with gates; each gate is a yes/no test | superficial loss, attribution, HBP first-time test, principal residence, TOSI age tests, CCA outcomes, OAS residency |
| A5 | **Ratchet / calendar drum** | a counter with the real number of teeth; one tick per year or month | HBP 1/15 repay, LLP 1/10, spousal RRSP 3-year rule, 21-year trust rule, RESP 31/35 years, CPP start dial |
| A6 | **Press / converter** | a material goes in, is stamped or transformed, comes out changed | dividend gross-up and DTC, 50% capital gains inclusion, CSV to policy gain, LIRA to LIF |
| A7 | **Balance / scale** | two pans; the needle shows the gap | life-insurance needs analysis, cash-flow statement, GDS/TDS, net worth |
| A8 | **Freezer / splitter** | a block is frozen at today's value; new growth sprouts elsewhere, or a flow is split into two pipes | estate freeze, income splitting, pension sharing, prescribed-rate loan |
| A9 | **Vault with compartments** | separate safes, each with a cap | CDIC per category, CIPF per group, Assuris, seg-fund guarantees |
| A10 | **Toll bridge / gate** | at an event, everything crosses one bridge; some lanes bypass the toll | death (deemed disposition, spousal rollover lane, beneficiary designation chute past probate), emigration, change of use |

Two more shapes appear often: a **seesaw** (bond price vs yield, duration as arm length) and a **boomerang pipe**
(attribution: income returns to whoever gave the money).

## 3. The parts dictionary

| In the rule | In the machine |
|---|---|
| a registered account | a container with a nameplate and a glass (sheltered) or open (taxed) body |
| contribution room | a fill line or a dipstick; over-contribution = an overflow spout dripping a 1%/month penalty coin |
| a deduction | a valve that lowers the water before the tax tap (saves amount x marginal rate) |
| a credit | a refund chute after the tax tap (saves amount x 14%) |
| a threshold | a weir lip at the exact height |
| a rate | a tap's opening or a skimmer's share (show the fraction: 1 coin in 5) |
| a test | a gate on a marble run with the test as its sign |
| a deadline | a calendar drum or an hourglass with the real count |
| ownership | a nameplate, a key, a valve handle someone holds |
| the tax system | one neutral grey collection box labelled TAX (`FP_CRA`), never a government logo |
| a life event | a button that moves the machine (turn 65, retire, pass away, separate) |
| an election / form | a paper slip dropped into a slot that throws a switch |

## 4. The five metaphor tests (write the answers in the brief)

1. **Faithful:** is there any way to operate the machine that gives an answer the real rule would not? If yes, change
   the machine, not the rule.
2. **One idea:** can you name the figure's single lesson in one line? If it takes two, it is two figures.
3. **Numbers move things:** does each number in the rule drive a visible quantity (a height, a count, a speed)?
4. **The misconception breaks:** can the client try the wrong belief and watch it fail?
5. **Five seconds closed:** before any label or see-through, would a non-expert guess roughly what the machine does?

## 5. Worked translations (from the v0 source)

**OAS clawback (A2 weir).** Retirement income fills a tall glass column (one tank per source: CPP, RRIF, pension,
dividends at their grossed-up value). At $95,323 of net income a weir lip sits on the column; every dollar above it
spills over into a skimmer that takes 15% from the OAS coin stack until it is gone at $155,320. TFSA withdrawals
come in through a side pipe that **joins the spending jug below the column**, so they never raise the level. Buttons:
withdraw from RRIF, withdraw from TFSA, split pension income with spouse, defer OAS to 70. Stat: OAS kept per year.
Misconception broken: "all retirement withdrawals are the same."

**Dividend gross-up (A6 press).** A $10,000 cash-dividend coin stack enters a press stamped x1.38 and comes out
$13,800 tall; the bracket tap takes 33%; a credit chute returns 15.02% of the grossed-up amount. Stat: net tax
$2,481. Misconception: "the gross-up means I pay tax on money I didn't get" — the see-through shows the corporate tax
already paid upstream (integration) as the reason.

**Superficial loss (A4 sorter).** A loss marble rolls to a gate: "identical property bought 30 days either side and
held on day 30?" No: the marble drops into the ALLOWED tray. Yes, by you, spouse or your corporation: it is lifted
onto the new shares' ACB block. Yes, inside your RRSP/TFSA: it falls through a trapdoor and is gone. Calendar drum
shows the 61-day window.

**Estate freeze (A8 freezer).** An Opco crate grows (a green sprout on top, plus a growing FMV stamp). Press FREEZE:
the crate is encased in ice as preferred shares at today's value (voting prefs keep the parent's key), and new
common-share seedlings are planted for the children or a family trust; from then on, growth sprouts only from the
seedlings. Stat: tax at death on the frozen value vs on the unfrozen value.

**Deemed disposition at death (A10 toll bridge).** Assets on a conveyor reach the bridge when "Pass away" is pressed.
Spouse lane: rollover at ACB, no toll. Other lanes: FMV - ACB gain stamped and half of it taxed; the RRSP crate
collapses fully into income; assets with a named beneficiary drop down a chute past the probate booth. Stats: income
tax at death, Ontario EAT.

## 6. Anti-patterns
- A flat diagram on a plate (a flowchart drawn on a board) is not a machine: build it in 3D (upstream rule).
- Decorative money: coins that don't count anything. Every coin is a known amount.
- A machine for two rules at once (TFSA *and* FHSA *and* RRSP): pick the contrast that matters for the lesson.
- Showing a rule that changed after the source date without re-checking the ledger.
- People drawn as figures: the engine draws objects; use nameplates and tokens for parties.
