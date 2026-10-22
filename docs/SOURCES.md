# Sources register

Ideas and numbers come from versioned sources. Each source gets a folder `sources/vN-<slug>/` and a row here.
Figures cite the source version in their brief; ledger rows cite it in their Source column.

| Ver | Folder | What | Added | Scope | Trust | Notes |
|---|---|---|---|---|---|---|
| v0 | `sources/v0-cfp-crash-notes/` | **CFP crash notes** (HTML, the owner's CFP Canada exam study notes, built from Brian Gordon's *Exam Success* notes with handwritten corrections) + `notes.txt` (plain-text extraction for search) | 2026-10-22 | all six areas: process (cash, debt, home, RESP, law, economics, protection), tax, investments, retirement, insurance, estate; a number wall; a "what changed" list | high for structure and 2026 federal figures (checked Oct 1, 2026 against CRA, ESDC, CIPF, CDIC, Assuris); still re-check before publishing | exam framing ("pick the most basic principle") suits education; "Trap" boxes = misconceptions to build around; amber "notes outdated" flags already corrected |

## Ingesting a new source (v1, v2, ...)
1. **File it:** `sources/vN-<slug>/` with the original (PDF, HTML, saved article, repo link in a `LINK.md`) and, for
   long text, a plain-text extraction for grep. Note the author, date and URL.
2. **Register it:** add a row above (what, scope, trust, caveats). Trust: official (CRA, ESDC, legislation) >
   professional bodies (FP Canada, CIRO, IQPF) > reputable firms' tax guides > articles and blogs.
3. **Mine it:** for each new concept, add a catalog row (`docs/CONCEPT-CATALOG.md`) with the source version; for each
   existing concept it improves, add the version to its Source column.
4. **Numbers:** add or update ledger rows (`docs/FACT-LEDGER-2026.md`) and `FP_FACTS` together. If the source
   disagrees with the ledger: the more official and more recent wins; note the conflict in the ledger change log.
5. **Log it:** one line in `docs/DECISIONS.md` if the source changes direction (a new domain, a new audience, a
   provincial expansion), and bump `docs/ROADMAP.md`.

## Wanted next (suggestions)
- Pension income splitting, the RRIF/LIF "65 rule" and the pension credit at 65 (R9 is unsourced).
- Provincial probate fees beyond Ontario; Quebec specifics (notarial wills, provincial tax).
- A 2027 indexation update (brackets, OAS quarterly, CPP) when CRA and ESDC publish.
- Corporate planning depth: holdco structures, RDTOH, IPP rules, the capital dividend account in practice.
