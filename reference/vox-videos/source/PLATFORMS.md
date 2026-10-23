# Platforms: specs, search and metadata

Sources are in `RESEARCH-LOG.md`. Platforms don't publish their ranking weights, so these are the consistent
practices in the 2026 guides, labelled where only one vendor claims them. `tools/publish-pack.mjs` turns
`projects/<slug>/publish.json` into the files below.

## 1 · What every platform reads
Search on every platform now reads **what's said** (the transcript), **what's on screen** (OCR) and **the caption**.
So the topic keyword appears in (1) the first 3 s of the narration, (2) the first on-screen text, and (3) the first
50–80 characters of the caption. Say the plain-English term people search for ("salary vs dividend", "OAS
clawback", "estate freeze"), not only the technical one.

## 2 · Per platform
| Platform | Spec | Length | Caption / title | Notes |
|---|---|---|---|---|
| **YouTube (long)** | 1920×1080 H.264, 60 fps OK | 3–15 min | Title ≤ 60 characters with the keyword early; the outcome is clear and there's no bait. Description: disclosures first (2 lines), then a 2–3-sentence summary with the keyword, the chapters (`0:00` first, ≥ 3 chapters, each ≥ 10 s), the sources, the disclaimer, then hashtags (≤ 3) | Upload the **SRT captions** (accurate captions help search and Shorts completion). Thumbnail 1280×720 < 2 MB: one hero cut-out, ≤ 4 big words, matches the title's promise |
| **YouTube Shorts** | 1080×1920 | ≤ 60 s (we use 35–60) | Title = the keyword plus the hook (it's searchable) | Link to the long video (related video) |
| **TikTok** | 1080×1920 | 35–60 s | The caption's first 80 characters carry the keyword; 3–5 specific hashtags (#canadiantax #estateplanning …), none generic | Switch on the **AI-generated content** label. Trending sounds don't apply (our sound is code-made) |
| **Instagram Reels** | 1080×1920; keep text inside the centre 1080×1420 | 30–60 s | Keyword-rich first line; hashtags are for categories (3–5) | Originality matters: always post our own render, never a repost of another platform's watermarked file. "Trial reels" can test a hook with non-followers first |
| **LinkedIn** | 1080×1920 or 1080×1080, MP4 H.264 + AAC | 30–90 s | First 2 lines are the hook for advisors; no external link in the body (put it in the first comment); a real question at the end, not engagement bait | Upload the captions (most watch muted). Comments from credible professionals extend reach, so engage with replies within the first hour |

Burned-in captions: the shorts carry on-screen key words by design. For full burned captions, the kit renders from
`words.json` (a block `Captions` is on the improvement list; `IMPROVEMENTS.md`). Max 2 lines, 3–5 words a line, and
a highlight on the key word.

## 3 · `publish.json` (Stage 9)
```json
{
  "series": "The Receipt",
  "keyword": "capital dividend account",
  "titles": { "youtube": "…", "shorts": "…", "linkedin_hook": "…" },
  "summary": "2–3 sentences, the keyword in the first one",
  "audience": "families",
  "hashtags": ["#canadiantax", "#smallbusinesscanada", "#estateplanning"],
  "chapters": "auto",
  "related": ["slug-of-the-long-version"],
  "disclosures": []
}
```
`"chapters": "auto"` builds them from the beat map's scene starts in `PLAN.md` (explainers only).

## 4 · The sources block (always)
Generated from `claims.json`: "Sources (retrieved <date>):" then one line per **primary** source: the title, then
the URL. Then "Figures for <tax_year>, <jurisdictions>. Illustrative examples are invented."

## 5 · The standard disclosures and disclaimer (top of every description, and the end card for explainers)
```
Narration: AI-generated voice. Written and reviewed by {reviewer.by}{, reviewer.credentials}.
Education only. This is not tax, legal, investment or insurance advice for your situation.
```
And after the sources:
```
This video explains general rules as of {as_of}. Tax law changes, and how a rule applies depends on your facts.
Speak with your own accountant, lawyer or advisor before acting. Nothing here is a recommendation to buy or sell
any security or insurance product. {disclosures}
```
`{disclosures}`: any financial interest, sponsorship or affiliation, **specific**, and also on screen at the start
(COMPLIANCE.md §1). If there are none, leave it out. Don't write "I may have interests".

## 6 · Don't look template-made
YouTube's **inauthentic content** policy (renamed from "repetitious content" in July 2025) makes "content that looks
like it was made with a template with little to no variation", or that is "easily replicable at scale", ineligible
for monetisation. AI tools are allowed. The risk is sameness. One unverified 2026 report adds "AI personas giving
advice on sensitive topics". So:
- Rotate the series and pillars (AUDIENCE.md §3–4). Each video gets at least one new composition idea (a new
  scene, a new metaphor, a new chart). The kit's rule against the same transition twice in a row applies across
  videos too.
- Original research (the statute on screen, our own worked examples) and a **named human writer and reviewer** in
  every description.
- Never present the narrator as a persona giving personal advice. It's a narrator explaining the law.
- Consider Mo on camera or Mo's own voice for some pieces (NARRATION.md §4).

## 7 · Posting rhythm (start here; adjust from analytics)
- 2 shorts a week (each cut to TikTok, Reels and Shorts) + 1 LinkedIn advisor cut a week + 1 explainer every 2–3
  weeks.
- Seasonal: RRSP season (January–February), tax season (March–April), budget days, corporate year-end (often
  December), November (indexation; "what changes January 1"), each quarter's prescribed-rate change.
