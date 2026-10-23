# Format: the Vox structure, adapted to planning mechanics

The pattern below is consistent across the analyses of Vox-style explainers in the research log. Its sources are
secondary (tutorials, case studies, a Frontiers mini-review on explainer structure), so the rules are a starting
shape, and our retention curves refine them.

## 1 · The spine (every cut)
1. **Cold open on a concrete thing** (0–3 s short / 0–15 s long): an object, a document, a number, a family, and no
   preamble. The visual hook, the spoken hook and the on-screen text all land in the first second (frame 0 is never
   empty: the kit's rule).
2. **The question in one sentence** (by 3–5 s short / 15–30 s long): the promise. "Why does the same $1 cost this
   family twice when they die?"
3. **Context in short pulses**, each one *after* something has made the viewer want it. History and definitions
   stay a minority of the runtime.
4. **Chain with "but" and "so", never "and then".** Every beat answers the last one and raises the next ("The
   company pays the tax, **but** the money's still inside, **so** to get it out…").
5. **Plain words, ELI5** (Mo, 2026-10-22): the video explains a complex idea simply. No statute names, section
   numbers, form lines or Summit terms are spoken or shown. Say what the rule *does* ("the company can deduct a salary"),
   not where it lives. The technical proof (sections, quotes, formulas, every cost the example skips) goes in the Excel
   backup and the description's sources. When a beat states a rule, the on-screen proof is a small plain tag
   ("SOURCE: CRA", "SOURCE: GOVERNMENT OF ONTARIO"), never the legal text.
6. **The worked number**: one illustrative case, **acted out by objects** (Mo, 2026-10-22: the reference is
   SalaryVsDividend v3): the money is a cut-out cut to its true share at each step, it travels between the people and
   places involved, and the hero number counts up beside it. A ledger card or bars only as a short payoff.
7. **The turn**: what planning changes (a freeze, a CDA payout, an insurance structure, a timing choice), framed as
   what owners and advisors look at, not as "do this".
8. **Zoom out, then the kicker**: the bigger idea in one line, then a reversal people repeat, set up by a pause.
9. **The close** (1–3 s): a finished still headed **"DISCLAIMER"** (Mo, 2026-10-22: no series name or logo on it), then
   the note: what the example leaves out, "Education only, not advice". Don't say "sources in the description" on it (Mo, 2026-10-22). No "smash that like button".

## 2 · Cuts and timing
| Cut | Format | Length | Words | Beats | Notes |
|---|---|---|---|---|---|
| Short (Shorts, TikTok, Reels) | 1080×1920 | 35–60 s (21–34 s for a single fact) | 90–150 | 6–10 | One mechanic only. Captions burned in (most watch muted). Keyword in the first 3 s of audio and in the first on-screen text. |
| LinkedIn | 1080×1920 or 1080×1080 | 30–90 s | 75–220 | 6–14 | Captions on. No link in the post: it goes in the first comment. Pitched to advisors. |
| Explainer (YouTube) | 1920×1080 | 3–8 min | 450–1,200 at ~150 wpm | chapters every 45–90 s | Chapters, captions file, a sources card at each act. |
| Deep dive | 1920×1080 | 8–15 min | to ~2,000 | acts | Only for a Two Deaths or Family File topic that earns it. |

Something visibly changes every 0.5–1.2 s (the kit's rule). Visual change every ~1.5–2 s is the short-form norm in
the research. Our kit is already faster.

**Retention targets** (from vendor benchmarks, so directional): hold at least 60–70% at 3 s on shorts, and aim for a
50%+ completion rate on a 45-s short. On YouTube long-form, watch the 30-s drop and the first chapter change. Replace
these with our own medians in `analytics/` after the first 10 videos.

## 3 · The visual grammar (built on the kit's STYLE.md; these are new FP-specific blocks)
The default is **collage acting** (STYLE.md "The reference piece"; RECIPES.md "Collage acting"): a cast of cut-outs
(the company as a building, the owner seen from behind, the CRA's cut as scissors, a credit as a coupon, a pension as a
rocking chair, savings as a piggy bank) performing each spoken idea, with the money cut to its true share.

| Block | What | Build it from |
|---|---|---|
| **Money flow** | cash rides a tube between the company, the person, the government; each tax is a cut of its true share; a credit lands as a coupon | `MoneyCut` + `Tube` + `Snip` + `Coupon` + `CountUp` |
| **The comparison** | two outcomes on a balance scale that wobbles and settles to its true tilt; or two piles side by side | `Cutout` (library/scale.png) + `MoneyCut` + `kick` |
| **What you get** | the benefits as objects landing in a column (piggy bank, rocking chair…); the other side gets faded ghosts, struck | `Cutout` + `RiseWord` + `Strike` + `Stamp` |
| **The reveal** (kicker) | a visual metaphor with one camera move: sink below the waterline, open the building | dark page + layer translate + `DarkStamp` |
| **Disclaimer card** | the close of every video: DISCLAIMER + the note, held ≥ 2.5 s | `Disclaimer` |
| **Receipt** | only when the viewer needs to see a document to believe it, and then in plain words: the government's own one-line summary (from the claim's `quote`), never a statute or section number | `TornPaper` + `TypeOn` + `Highlight` |
| **Ledger card** | payoff only (≤ 3 s): rows that stack (income → tax → net), the total counting up | `PanelStack` / `Tag` rows + `MoneyCounter` (RECIPES.md) |
| **Tier badge** | a small stamp: STATUTE / CRA POSITION / COURT DECIDES / UNSETTLED | `Stamp`; red only for UNSETTLED |
| **Family map** | people, companies and the trust as cut-outs joined by dotted ownership paths with % labels | `PersonIcon` / `Cutout` + `DottedPath` (no faces) |
| **Two-deaths timeline** | a horizontal line, two stamps (first and second death), money flowing as green cut-outs | `LineChart` or a local timeline + `Stamp` + money green |
| **Factor checklist** | GATE topics: the factors tick in, and the verdict box stays empty with "a court decides" | `TypeOn` + `Strike`/`MarkerCircle` |
| **Source line** | the `SourceLine` on every beat with a figure, in plain words ("Source: CRA, 2026" · "Source: Government of Ontario"); the section numbers live in the Excel backup | kit |
| **Illustrative stamp** | "ILLUSTRATIVE FAMILY" on any invented household, every time it appears | stamp |

Use **power moments** (STYLE.md §8, at most 2) for the hook number and the kicker.

## 4 · Hooks that fit this channel (fill them with a specific fact)
- **The double-take number**: "This family pays tax on the same dollar twice. Here's the line in the Act that does
  it."
- **The meeting phrase**: "Your accountant said 'capital dividend account'. Here's what it actually is."
- **The reversal**: "Paying yourself a salary can leave you with *less* tax than dividends. Here's when."
- **The date**: "On <date>, the rule for <X> changed. Here's who it hits."
- **The honest one**: "Nobody can give you one number for this. Here's why."
Avoid "secret", "loophole", "they don't want you to know", fear and urgency (COMPLIANCE.md §5).

## 5 · Repurposing one explainer
One horizontal explainer → (a) 3–5 vertical shorts, each one mechanic with its own hook (re-laid out, not cropped:
build each as its own vertical composition reusing the scenes); (b) a LinkedIn cut for advisors (30–90 s); (c) a
carousel (social skill, `carousel-frameworks.md`) from the key frames (the cast at each step, with the counter). Every derivative has its own claims subset
(they share the parent's `claims.json` through `"parent": "<slug>"` in its own ledger).
