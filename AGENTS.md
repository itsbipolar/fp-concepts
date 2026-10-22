# FP Concepts

This repository explores visual, interactive education for Canadian financial planning.

## Current work

Current review: `explorations/style-frames/README.md`. Three still images test art directions for company ownership before another interactive lesson. No direction is approved yet.

The owner has rejected numerical charts, the garden analogy, money-only typography, a literal miniature streetscape, and ungrounded abstract visual studies. Use recognisable, stylised subjects with personality; show financial relationships through behaviour. Do not assume the older Colorfigures or physical-machine requirements apply to new independent explorations.

## Design guidance

The repository-local Codex skill `.agents/skills/frontend-design/SKILL.md` provides audited presentation/design guidance. Its upstream commit and Apache-2.0 license are recorded alongside it. Read when building or redesigning a visual interface. User preferences and explicit task requirements take precedence.

For existing Colorfigures figures, read their existing briefs and pipeline instructions before changes. For new explorations, use the medium that serves the idea. Keep facts, educational scope, and asset provenance clear.

## Persistence and review

Use the existing checkout. Do not create a worktree unless requested. The working branch is `codex`. The user has authorized work on that branch and GitHub. Save completed review artifacts in Git so cloud environment restarts cannot erase them. Supply GitHub view/download links for review artifacts; internal `/workspace` links alone previously failed for the user.

Style-frame package: `python3 explorations/style-frames/package_review.py` rebuilds the embedded HTML and ZIP. The user can open the extracted HTML without a server.
