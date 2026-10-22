# FP Concepts

This repository explores visual, interactive education for Canadian financial planning.

## Current work

**Selected direction: Within reach.** The owner endorsed its visual design and drawing style after reviewing the first ownership interaction. Active work: `explorations/within-reach/README.md`. The style-frame archive remains at `explorations/style-frames/README.md`; keep **The colossus** and **Separate bodies** intact as alternatives for future use. Visual approval does not imply approval of a finished financial lesson.

The owner has rejected chart-led explanations, the garden analogy, money-only typography, a literal miniature streetscape, and ungrounded abstract visual studies. Use recognisable, stylised subjects with personality; show financial relationships through behaviour. Quantification is welcome when it explains what changes in the illustration. Do not assume the older Colorfigures or physical-machine requirements apply to new independent explorations.

**One decision, several connected consequences.** Read `docs/INTERACTION-PRINCIPLES.md` before designing a financial lesson. An action can reveal immediate cash effects, related tax/cost changes, and later rights or benefits in the same scene. The assistant is responsible for researching these effects and inventing their visual treatment; do not ask the owner to supply metaphors. The salary/dividend/CPP example explains this ambition; it is not a prescribed visual or a request to implement a calculator.

## Design guidance

The repository-local Codex skill `.agents/skills/frontend-design/SKILL.md` provides audited presentation/design guidance. Its upstream commit and Apache-2.0 license are recorded alongside it. Read when building or redesigning a visual interface. User preferences and explicit task requirements take precedence.

For existing Colorfigures figures, read their existing briefs and pipeline instructions before changes. For new explorations, use the medium that serves the idea. Keep facts, educational scope, and asset provenance clear.

## Persistence and review

Use the existing checkout. Do not create a worktree unless requested. The working branch is `codex`. The user has authorized work on that branch and GitHub. Save completed review artifacts in Git so cloud environment restarts cannot erase them. Supply GitHub view/download links for review artifacts; internal `/workspace` links alone previously failed for the user.

Style-frame package: `python3 explorations/style-frames/package_review.py` rebuilds the embedded HTML and ZIP. The user can open the extracted HTML without a server.
