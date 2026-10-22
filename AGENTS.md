# FP Concepts

This repository explores visual, interactive education for Canadian financial planning.

## Fresh chat startup

Read `docs/PROJECT-STATE.md` for the compact handoff. For a new or extended lesson, use the project skill `.agents/skills/fp-visual-build/SKILL.md`; it routes you to the relevant workflow, style references and templates. Read only the task's required material, not the full history, source library or generated embedded HTML. New sessions need this repository on `codex`; chat memory alone is not the handoff.

## Current work

**Selected direction: Within reach.** The owner endorsed its visual design and drawing style after reviewing the first ownership interaction. Latest build: `explorations/salary-or-dividend/README.md`, a qualitative connected-effects lesson; original ownership prototype: `explorations/within-reach/README.md`. The style-frame archive remains at `explorations/style-frames/README.md`; keep **The colossus** and **Separate bodies** intact as alternatives for future use. Visual approval does not imply approval of a finished financial lesson.

The owner has rejected chart-led explanations, the garden analogy, money-only typography, a literal miniature streetscape, and ungrounded abstract visual studies. Use recognisable, stylised subjects with personality; show financial relationships through behaviour. Quantification is welcome when it explains what changes in the illustration. Do not assume the older Colorfigures or physical-machine requirements apply to new independent explorations.

**One decision, several connected consequences.** Read `docs/INTERACTION-PRINCIPLES.md` before designing a financial lesson. An action can reveal immediate cash effects, related tax/cost changes, and later rights or benefits in the same scene. The assistant is responsible for researching these effects and inventing their visual treatment; do not ask the owner to supply metaphors. Salary/dividend is now the first build testing that workflow. Numerical tax modeling remains pending verified official sources; do not invent rates to fill that gap.

## Design guidance

`docs/STYLE-SYSTEM.md` fixes the drawing, texture, figure, palette and composition rules. `design/within-reach/` holds reusable colour tokens and a manifest of protected image references. View the actual master and relevant approved components before artwork work. Reuse components where possible; use `docs/templates/IMAGE-PROMPT.md` and real image references for new subjects. Save exact new prompts/provenance. Existing prompts were not recovered, and fresh generation is not pixel-deterministic.

The repository-local Codex skill `.agents/skills/frontend-design/SKILL.md` provides audited presentation/design guidance. Its upstream commit and Apache-2.0 license are recorded alongside it. Read when building or redesigning a visual interface. User preferences and explicit task requirements take precedence.

For existing Colorfigures figures, read their existing briefs and pipeline instructions before changes. For new explorations, use the medium that serves the idea. Keep facts, educational scope, and asset provenance clear.

## Model and context budget

Follow `docs/BUILD-WORKFLOW.md`. The user authorizes explicit model routing: prefer `gpt-6.1-sol` medium for routine building and coordination; reserve `gpt-6-astra` high/ultra for a concrete difficult causal/visual/correctness problem; optionally use `gpt-6-luna` for simple bounded support. Use tools for deterministic work. Do not spawn agents for work that solo execution handles efficiently.

When delegating and supported, select model/effort explicitly and use `fork_turns: "none"` with `docs/templates/AGENT-TASK.md`. Avoid copying the full conversation or unintentionally inheriting Ultra. Assign distinct files and concise return evidence. Main-chat model selection remains an app/user setting; repository guidance cannot change it. Disclose unavailable models and substitutions. Never invent usage or savings figures.

## Persistence and review

Use the existing checkout. Do not create a worktree unless requested. The working branch is `codex`. The user has authorized work on that branch and GitHub. Save completed review artifacts in Git so cloud environment restarts cannot erase them. Supply GitHub view/download links for review artifacts; internal `/workspace` links alone previously failed for the user.

Style-frame package: `python3 explorations/style-frames/package_review.py` rebuilds the embedded HTML and ZIP. The user can open the extracted HTML without a server.

Ownership package: `python3 explorations/within-reach/package_review.py`. Workflow/reference check: `python3 scripts/check_visual_system.py`. Run only checks relevant to the change. Update the lesson brief and `docs/PROJECT-STATE.md` before handing off.

Latest lesson package/checks: `python3 explorations/salary-or-dividend/package_review.py` and `python3 explorations/salary-or-dividend/verify.py`.
