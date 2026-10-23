# Narration: the voice and the script it reads

## 1 · The persona
**The calm, exact explainer**: a documentary narrator who knows the Act and doesn't need to prove it. Warm, measured
and slightly wry. Confident on statute, careful on CRA positions, honest about what's unsettled. The research
consensus for explainers is a "friendly expert": clear articulation, mild inflection, steady pace, and enough warmth
to feel guided rather than automated.

| Dimension | Do | Don't |
|---|---|---|
| Pace | ~150 wpm for explainers (140–160); ~130–140 wpm on dense steps (a calc, a statute line) | race (180+ wpm is tiring); drag (120 wpm except on the receipt) |
| Pauses | a beat before the kicker; a short breath after each figure | dead air over 0.3 s between scenes (tighten-voice) |
| Register | "the company", "your estate", "an owner might" | "guys", hype, "insane", "crazy", fear words |
| Certainty | "the Act says", "CRA's position is", "a court decides" (the tier, spoken) | "everyone knows", "always", "never" about planning |
| Person | second person for families ("your company pays…"); "your client" for advisors | first-person anecdotes Mo didn't give |

## 2 · Writing for the ear (on top of the kit's VOICE.md §3)
- **One continuous paragraph** (the kit's rule), chained with *but* and *so* (FORMAT.md §1).
- **One idea per sentence**, sayable in one breath (about 12–20 words). A figure gets its own short sentence.
- **Numbers the way they're said**: the spoken text spells them ("two hundred and fifty thousand dollars", "twenty
  twenty-six", "fifty per cent"), and the screen shows the figure ($250,000 · 2026 · 50%). Both are tagged with the
  same claim.
- **Acronyms**: spell out the first use and pick one form ("the capital dividend account, the C-D-A"). TTS
  pronunciation cheat-sheet: `R-R-S-P`, `T-F-S-A`, `R-R-I-F` ("riff" is common; pick one and keep it), `C-P-P`,
  `O-A-S`, `R-D-T-O-H` (say "refundable dividend tax on hand" instead), `C-C-P-C`, `I-P-P`, `T-O-S-I` ("toe-see" is
  common among practitioners), `L-C-G-E`, `G-R-I-P` ("grip"), `Q-S-B-C`. Section numbers: "section eighty-four point
  one", "one-sixty-four six" for 164(6).
- **Never say section numbers, statute or case names** (Mo, 2026-10-22: ELI5). Say what the rule does. The citations are in the Excel backup.
- No parentheses, no slashes, no "e.g." in the spoken text (TTS reads them badly).

## 3 · The generated voice (kit.config.json → voiceGeneration)
- The locked setup: Higgsfield `seed_audio`, preset **Benji**, WAV at 48 kHz, `speech_rate: 25` (brisk
  documentary). For an **explainer**, try `speech_rate` 10–20 (closer to 150 wpm). Measure the words per minute
  of the result (`word count ÷ minutes` from `words.json`), and record the rate that worked in
  `kit.config.json → voiceGeneration.notes`.
- Generate **per paragraph** for long pieces (the kit's VOICE.md has the join command), so one fix doesn't re-voice
  everything.
- After generating, the **pronunciation pass**: transcribe (new-graphic does it) and compare `words.json` against
  `voice.txt`. Mismatched acronyms or numbers mean a re-take of that sentence, re-spelled phonetically in
  `voice.txt` only (the screen text stays correct). `tools/fp-check.mjs` reports the mismatches.
- Loudness: the kit's mix targets apply. Report measured LUFS and say "measured, I can't listen".
- **Disclose** the AI voice (COMPLIANCE.md §4). Never clone a real person's voice. Mo's own cloned voice only with his
  explicit go-ahead.

## 4 · Mo's own voice (optional, stronger for trust)
A recorded take (case A in the kit's VOICE.md) beats any generated voice for audience A's trust, and for YouTube's
"authentic content" signal. If Mo records: one quiet room, a phone at 20 cm, two takes, and the kit tightens the
pauses only. A hybrid also works: Mo's voice on the hook and the kicker, the generated voice on the mechanics (and
disclosed).
