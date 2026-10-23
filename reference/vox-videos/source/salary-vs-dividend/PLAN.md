# Salary or dividend: where the tax hides — plan (2026-10-22)

Composition `SalaryVsDividend` · 1080×1920 · 60 fps · 44.56 s · synced to a voice-over

## Brief
- What it says (one sentence): taking $10,000 of company profit as a salary or a dividend leaves almost the same cash at
  Ontario's top rate, on purpose; the real difference is what a salary gets you (RRSP room, a CPP pension).
- Where it will be used / output: vertical short (Shorts, Reels, TikTok, LinkedIn); MP4.
- Images available: none needed. Everything is drawn in code (cash, ledger card, bars, stamps).

## Beat map (STYLE.md §2) — one row per scene (v2)
| Time (s) | Scene | What happens on which beat | Sound |
|---|---|---|---|
| 0.0–7.8 | Hook | cash lands on the company building at frame 0; $10,000 counts; SALARY / DIVIDEND tubes grow on their words; scissors over the dividend tube on "taxed"; slow push-in | paper-land, count, click |
| 7.8–16.5 | Salary | the cash rides the tube to the owner; NO COMPANY TAX stamp; the scissors cut the pile, the tax part flies off; ONTARIO TOP RATE; YOU KEEP $4,647; pan with the cash | tear, cash, stamp, click, count |
| 16.5–26.0 | Dividend | cash into the cash register; it rings and a strip drops in (COMPANY TAX); the rest rides to the owner; TAX BREAK coupon; scissors; YOU KEEP $4,539 | tear, ding, cash, flip, click, count |
| 26.0–30.2 | Almost the same | the piles drop onto a balance scale that wobbles and settles almost level; ON PURPOSE | tear, cash ×2, stamp |
| 30.2–39.5 | What a salary gets you | piggy bank + coins (RRSP ROOM), rocking chair (CPP PENSION); ghosts on the dividend side, struck; NEITHER | tear, paper-land ×2, chip ×3, strike ×2 |
| 39.5–47.0 | Kicker | iceberg; FEELS… CHEAPER slams; the camera sinks below the waterline: COMPANY TAX ALREADY PAID; DISCLAIMER card holds | tear, stamp + impact, stamp |

## Images (IMAGES.md)
| File | What | Source (user / generated / code) | Status |
|---|---|---|---|
| building, cash, owner, scissors, register, scale, piggy, chair, iceberg (.png) | halftone cut-outs in public/graphics/salary-vs-dividend/ | generated with Higgsfield nano_banana_pro (green key, cutout.py), 2026-10-22; originals in img-originals/ | done |

## Versions
| Version | Date | What changed | User's notes |
|---|---|---|---|
| v1 | 2026-10-22 | first build: code-drawn ledger cards and bars (frozen: SalaryVsDividendV1, renders/SalaryVsDividend/v1/) | "mostly line items and graphs"; "The Ledger" on the end card should be a disclaimer |
| v2 | 2026-10-22 | rebuilt as a collage: 9 generated cut-outs acting it out, tubes, scissors, register, scale, iceberg; camera moves; DISCLAIMER end card; 47.0 s (2.9 s hold on the disclaimer) | see v3 |
| v3 | 2026-10-22 | calmer wobble on the building, owner, register and scale (boil 0.3); the company's tax is now an 11.2% corner torn off at the register and kept through the ride and the tax break, then the owner's cut leaves 45.4% (true shares); coupon moved so the cut corner shows; disclaimer without "sources in the description" | Mo: some icons too wobbly; smaller cut for the company's tax; no "sources in the description" |

## FP brief (fp-video Stage 0–1)
- Series · pillar · audience: The Ledger · 1 (the owner's money) · families (owner-managers)
- Summit catalogue id and dossier: CORP-04 · reference/summit/docs/catalogue/dossiers/corporate-succession.md#CORP-04
- Angle (the question a real person asks): "How should I pay myself from my company: salary or dividends?"
- Why now: year-end pay decisions; the numbers use the rules in force for 2027.

## Compliance (COMPLIANCE.md §7; answer each one)
1. Names a security, fund, carrier or product? No.
2. Could a viewer take it as tailored advice? Which line, and how is it made general? No recommendation is made; it compares two routes for an illustrative $10,000 at the top bracket and says what each one gets you. The close says "Education only, not advice" and "example before CPP and payroll costs".
3. A financial or other interest to disclose? Where is it placed? None.
4. Proposed (not enacted) measures, and are they labelled? None used in the video. The 2027 Ontario dividend credit and small-business rate are enacted (Bill 97, Royal Assent April 24, 2026). The proposed 2027 CPP base-rate cut is not used (backup notes it).
5. A GATE or DECLINE topic shown as a number? No. Everything is COMPUTE (statute and CRA/Ontario published rates).
6. Quebec: handled / flagged / excluded on screen? Excluded: the stamp reads EXAMPLE · ONTARIO and sources say Ontario; the description and backup say Quebec isn't covered.
7. Firm pre-approval (always required; Stage 9b, recorded in publish.json → firm_approval): see publish.json

## QA (QA.md; tick each one, or write why it doesn't apply)
- [x] every figure on screen matches claims.json (checked on the stills sheet): $10,000, $0, $4,647, $4,539
- [x] each figure shows its year, and its province where it's provincial: "EXAMPLE · ONTARIO", "ONTARIO TOP RATE", source line "2027 rules"
- [x] CRA positions labelled; GATE shows factors; UNSETTLED is stamped; PROPOSED is dated: none apply
- [x] receipt text is verbatim from the claim's quote: no receipts on screen (plain-words rule, Mo 2026-10-22); the quotes are in the Excel backup
- [x] the worked example states its basis and is stamped ILLUSTRATIVE: EXAMPLE stamp; top bracket; "example before CPP and payroll costs" on the close
- [x] Quebec handled or flagged: Ontario only (see Compliance 6)
- [x] education only; no product, ticker or performance figure
- [x] disclosures (if any) are on screen in the first seconds: none needed; AI narration is disclosed in the publish pack
- [x] the hook lands in the first second with the keyword; the question by 5 s / 30 s: cash at frame 0, "salary or a dividend?" at 3.8–4.5 s
- [x] beats chain with but/so; at least one receipt beat; a source line on figure beats: receipt beats replaced by plain source lines (ELI5 rule)
- [x] new in this video vs the last one in the series: first video of the series
- [x] vertical text inside the safe area: content y 250–1670; the eyebrow (y 190) and the source line sit outside the Reels centre box, which the kit's layout accepts
- [x] the voice ↔ script check passes (fp-check): 87%, the rest is digits vs spelled numbers; RRSP/CPP heard correctly; a repeated sentence was cut
- [x] the reviewer signed claims.json → review: Mo, in chat, 2026-10-22
