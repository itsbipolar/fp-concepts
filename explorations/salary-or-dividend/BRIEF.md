# Salary or dividend: what follows the payment

Status: qualitative interaction prototype. Style: Within reach v1. Branch: codex.

## Decision and discovery

The learner chooses salary or a non-eligible taxable dividend. One choice reveals company and personal tax treatment, whether the payment adds CPP pensionable earnings, and whether it can create next-year RRSP room. The misconception is that choosing a payment route changes only cash in today's pocket.

Assume a working controlling shareholder age 40, pensionable salary below the annual CPP earnings ceiling, no other earned income and no employer pension plan. Existing CPP history and unused RRSP room persist. This is not an equal-company-cost comparison and makes no net-cash recommendation.

## Scope and source boundary

The planned numerical example was blocked: the environment denied access to official Canadian/Ontario financial sources. Network additions were saved as a draft; that is not proof of applied access. The usable build therefore teaches mechanisms without tax rates, contribution amounts or estimated future benefits. See `SOURCES.md`. Quantification remains pending primary-source verification and an independently checked financial model; never fill the gap with invented rates.

## Causal and visual plan

| Choice | Now | CPP record | Next year's RRSP room |
| --- | --- | --- | --- |
| Salary | Reasonable expense for company; personal employment income tax; employer and employee CPP | Contributions travel from both parties; an earnings mark is added, with earlier marks retained | A new empty paper flap unfolds beside existing room; room is capacity, not money |
| Dividend | Distribution of after-tax profit; personal gross-up and dividend-credit rules | No contribution from this payment; existing record remains unchanged | Existing room remains; no new flap is earned by this dividend |

The original company, owner and orange payment carry the Today scene. One new older version of the same character holds a paper earnings record in Later. His identity, figure proportions and tactile material connect the time periods. The paper record explains CPP history directly. A separate next-year paper fold represents RRSP capacity, with nearby plain labels.

Alternatives considered: a pension money bag would conflate entitlement and cash; separate comparison cards would lose the shared causal scene. The chosen scene uses a moving payment, stamped earnings record and unfolding capacity instead.

Colour anchors and texture follow `../../docs/STYLE-SYSTEM.md`. Quiet system sans type, art dominant, sparse nearby labels; no quantity is encoded by paper size or note count. Phone reflows Later below Today. Exact new prompt and reference hashes are in `provenance/`; original reference assets remain intact.

## Implementation and review

`model.js` contains qualitative financial states; `app.js` handles sequence and input. Every choice replaces the preceding hypothetical scenario. Payment replay does not create additional entitlements. Switching, pause, replay and reset cancel obsolete timers/animations. Reduced motion goes directly to the same final state. Accessible detail buttons explain each subject; the current sentence announces progress.

Validation evidence, review screenshots and package instructions are recorded in `README.md` after the final build. Current source-verification blocker must travel with the deliverable. No compliance-approved or numerically validated lesson is claimed.

## Work budget

One fresh Sol medium frontend worker; earlier Sol high source-check worker was interrupted by the account limit. One reference-based image-generation call. Root integrated qualitative states, source scope, packaging and browser checks. Token/cost totals are unavailable; no savings percentage is claimed.
