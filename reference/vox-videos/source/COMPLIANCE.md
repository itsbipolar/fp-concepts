# Compliance: what this channel can and can't say

This is not legal advice, and **Mo's firm's compliance policy outranks this page**.

**Decided by Mo (2026-10-22):** this is his **personal brand** (LinkedIn, and YouTube under a version of his name).
**Every video goes to his firm for approval before posting** (`kit.config.json → brand.firm_preapproval: true`;
fp-video Stage 9b). He **can't give investment advice**, but he can speak to investments as they relate to planning
(§1a). When the firm's feedback reveals a standing rule ("never name a fund company", "use this disclaimer"),
record it in §8 below so it's applied before submission next time.

## 1a · Investments, as they relate to planning (what Mo can and can't say)
| OK (planning mechanics, general) | Not OK (investment advice) |
|---|---|
| How a type of income is taxed (interest vs dividends vs capital gains; in a TFSA, an RRSP, a corporation) | Which security, fund, ETF or stock to buy, hold or sell |
| Asset location as a concept ("where a type of investment sits changes the tax") | "Put your bonds in your RRSP" to the viewer; any allocation for the viewer |
| How the passive-income grind works and which income types count | Recommending a corporate-class fund, a product or a strategy to beat the grind |
| What a segregated fund *is* and how it's treated at death (the structure) | That a seg fund or any product is *suitable* for the viewer |
| Return of capital, ACB, superficial losses, tax-loss harvesting *rules* | Market calls, forecasts, performance claims, "now is a good time to…" |
| Risk *concepts* in a plan (sequence risk, concentration in the family company) | Telling the viewer how much risk to take |
Use product *categories*, never products or issuers. Any illustrative return is labelled ("an assumed 5% a year,
for illustration"), preferably from the FP Canada/IQPF Projection Assumption Guidelines with its year, and never
presented as expected performance.

## 1 · Securities law: CSA/CIRO Staff Notice 31-369 (December 11, 2025)
Read from the notice itself (primary text, retrieved October 22, 2026):
- **"Advice" includes offering an opinion about the merits of investing in a business or its securities, or a
  recommendation**. Emojis and promotional phrases "such as 'not to be missed' and 'golden opportunity' could be
  perceived as investment recommendations." Purely factual information ("how securities markets work, investing
  basics") is not advice.
- Advice given **for a business purpose** needs registration. The factors include acting like a registrant,
  repetition, expected compensation in any form, and soliciting. **A disclaimer does not avoid registration**: "the
  registration requirement cannot be avoided by simply making a disclaimer asserting you are not providing advice."
- **The general advice exemption** (NI 31-103 s. 8.25): advice that is *not tailored to the needs of an individual*
  doesn't need registration, but **any financial or other interest in a security mentioned must be disclosed**.
- **Disclosure must be clear and conspicuous**, and specific (the security, the nature of the compensation, the
  payer, the recipient). It must sit where the audience connects it to the content, "typically … at the beginning",
  and not at the end of a long video or behind "Show more". "I may have a financial interest in some of the
  securities that I mention" is not enough.
- **Misrepresentation** includes statements you "reasonably ought to know are untrue or misleading", even
  unintentionally. Judge the impression a reasonable viewer takes away.
- The scenarios: answering followers' **personalised questions in comments or DMs** and then advising for a fee
  turns general content into registrable advice (the "Flora" scenario). Sponsorship hidden behind "Show more" was
  sanctioned (*Re Floreani*, 2025 ABASC 41).
- **AI**: whoever uses AI "to provide advice … may be held responsible for what the AI does as if they themselves had
  done it directly."

**What this means for us:**
1. We explain **planning mechanics and the law** (tax, estates, insurance structure, retirement rules). That's
   factual and educational. We **don't** recommend securities, funds, ETFs, stocks, crypto, or a carrier's product.
2. No tickers, no "buy", "sell" or "load up", no price predictions, no performance promises.
3. **No tailored answers.** Comments get general replies plus "speak with your own advisor or accountant about your
   situation". Never "in your case, do X". DMs asking for personal advice get the same template
   (`templates/fp/replies.md`).
4. If Mo or a guest holds a position in, or is paid by, anything named, the disclosure goes **on screen in the
   first seconds** and at the top of the description.
5. Sponsorships and affiliate links: **none without the user's explicit decision**. If one is added, it's disclosed
   specifically, on screen, at the start.

## 2 · Insurance (where a video touches insurance products)
Explain the structure (who owns, who pays, who's the beneficiary; the CDA credit; the policy's ACB; the 148(8)
rollover) as law. **Never** compare named carriers' products, quote premiums or illustrated values, or imply a
product is suitable for the viewer. Illustrations are "illustrative, not a quote". Provincial insurance councils
(and FSRA in Ontario, the AMF in Quebec) regulate licensed agents' advertising. If Mo is licensed, his licence
rules apply.

## 3 · Titles and designations
- **CFP® marks** (FP Canada CFP® Marks Usage Guide v1.2, May 2022): use them only as adjectives ("CFP® professional",
  never "a CFP" or "CFPs"). Use ® on the first mention on each page or screen. **Never use them in a channel name,
  handle, domain or email address.** Never use them alone in promotion. Never imply FP Canada's or FPSB's
  endorsement.
- **Don't use "FP Canada"** (FP Canada's brand) or anything that implies affiliation with the body in the public
  brand, the channel name or the handles. The repository's name is internal only.
- **Title protection**: in Ontario (FSRA) and Saskatchewan, "financial planner" and "financial advisor" are
  protected titles. Only credentialed people may hold them out. (This was written from background knowledge, not
  re-read for this page: check fsrao.ca and fcaa.gov.sk.ca before the first video that names a title.) Show Mo's titles exactly as his credentials allow
  (`kit.config.json → brand.reviewer.credentials`). Never invent or upgrade one.

## 4 · AI disclosure and platform rules
- The narration is a **generated voice**. The description says so in the first lines: "Narration: AI-generated voice.
  Written and reviewed by <reviewer>."
- **TikTok**: switch on the AI-generated content label (its policy covers AI voiceovers). **YouTube**: turn on
  "altered or synthetic content" when the content is realistic (a realistic synthetic voice presented as a real
  person, or realistic scenes). Our animated collage plus a disclosed narrator generally isn't realistic, but **turn it
  on anyway** if the voice could be taken for a real, named person. **Meta**: use the AI info label where offered.
- Never clone or imitate a real, recognisable person's voice. Never generate a real person's face (the kit's rule).

## 5 · Honesty rules that are ours
- No invented testimonials, client stories, reviews, comments or screenshots. Invented families are labelled.
- No fear-selling ("CRA is coming for you"), no scarcity ("before it's too late"), no "secret" or "loophole" framing
  of legal planning. Name the rule and the section instead. "Loophole" misdescribes legislated planning, and it
  invites GAAR-flavoured misunderstanding.
- Name what we don't cover: "this skips the AMT and provincial surtaxes" when it matters.
- Every video carries the **standard disclaimer** (PLATFORMS.md §5). **The disclaimer doesn't make advice into
  education. The content has to be education.**

## 6 · What `tools/fp-check.mjs --stage script` scans (the script, on-screen text and captions)
- **Errors**: tickers (`$ABC`, "TSX: ABC"), "buy now", "you should buy/sell", "guaranteed return", "risk-free",
  "can't lose", "golden opportunity", "not to be missed", "act now", "before it's too late", "secret", "loophole",
  "CRA requires" (use "CRA's position"), "CFPs" and "a CFP" (marks as nouns), and "FP Canada" in a brand field.
- **Warnings** (a person decides): "you should", "you need to", "you must" (make it general: "an owner might
  consider asking…"), "best" plus a product word, a named carrier, bank or fund company, rocket or money-bag emojis,
  a performance figure (% returns), "always" or "never" applied to planning.

## 7 · The questions answered in PLAN.md → Compliance (Stage 5)
1. Does it name a security, fund, carrier or product? (If yes: why, and is it purely factual?)
2. Could a viewer take it as advice tailored to them? Which line, and how do we make it general?
3. Any financial or other interest to disclose? Where is it placed?
4. Any proposed (not enacted) measure? Is it labelled?
5. Any GATE or DECLINE topic presented as a number? (Fix it.)
6. Quebec: is it covered, flagged as different, or excluded on screen?
7. Firm pre-approval (always required): submitted on (date), approved on (date), reference, conditions.

## 8 · Standing rules from Mo's firm (add as compliance gives feedback)
| Date | Rule | Applies to |
|---|---|---|
| 2026-10-22 | Every video goes to the firm with an Excel backup: one sheet with every figure, its source and verbatim quote, and the worked numbers as live formulas (`tools/fp-workbook.py`, in the publish pack) | every video |
