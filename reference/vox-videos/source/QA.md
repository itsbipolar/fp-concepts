# QA: before anything is exported (Stage 8)

`node tools/fp-check.mjs <slug>` covers what a script can check. This list is for what a person (or Claude, looking at
the stills sheet) has to judge. Tick it in `projects/<slug>/PLAN.md → QA`.

## Numbers and law
- [ ] Every figure on screen and in the narration has a claim (the tool checked the narration; **you check the
      screen** against `claims.json` on the stills sheet)
- [ ] Each figure shows its year, and the province where it's provincial
- [ ] CRA positions are labelled as positions; GATE topics show factors, not a number; UNSETTLED is stamped
- [ ] Proposed measures are labelled PROPOSED with the date
- [ ] Any money cut or split on screen is its **true share** from `claims.json`; no statute text or section number on screen (ELI5)
- [ ] The worked example states its basis (after-tax / pre-tax, today's dollars) and is labelled ILLUSTRATIVE
- [ ] Quebec is either handled or flagged ("Quebec differs; not covered here")
- [ ] Nothing contradicts the Summit traps list (VERIFICATION.md §5)

## Compliance
- [ ] Education only: no line reads as advice to one viewer
- [ ] No product, security, carrier, ticker or performance figure (or the user approved it in writing in PLAN.md)
- [ ] Disclosures, if any, are on screen in the first seconds
- [ ] CFP® marks used correctly or not at all; no "FP Canada" in the brand
- [ ] The AI narration disclosure is in the publish pack

## Craft (on top of the kit's CHECKLIST.md)
- [ ] The hook lands in the first second: visual + spoken + on-screen text, with the keyword
- [ ] The question is stated by 5 s (short) or 30 s (explainer)
- [ ] Every beat chains with "but" or "so"; no "and then" sections
- [ ] Every beat has an object acting it out (collage acting); a source line on every figure beat; ends on the Disclaimer card
- [ ] The kicker is set up by a pause and is repeatable
- [ ] New in this video vs the last in the series: _____ (PLATFORMS.md §6)
- [ ] Vertical: text sits inside the safe area (Reels' centre 1080×1420)

## Sign-off
- [ ] The script ↔ transcript check passes (no mispronounced acronyms or wrong numbers in `words.json`)
- [ ] `claims.json → review` is filled in **by the reviewer** (Claude never fills it in)
- [ ] The firm's pre-approval, if required (`kit.config.json → brand.firm_preapproval`), is recorded in PLAN.md
