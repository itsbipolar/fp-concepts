# Financial illustration build workflow

Build a reproducible lesson in the approved **Within reach** language: one learner decision, several connected consequences, and one coherent scene. The assistant researches the mechanism and invents its visual treatment. Follow [interaction principles](INTERACTION-PRINCIPLES.md) and [style system](STYLE-SYSTEM.md); preserve the existing ownership prototype and archived alternatives.

## 1. Brief and causal map

Start from [the lesson brief](templates/LESSON-BRIEF.md) and update [project state](PROJECT-STATE.md). Define the decision, misconception, audience, jurisdiction, year, comparison basis and intended deliverable. Map material consequences by cause, party, timing, kind of value or right, conditions and source. Check current primary financial sources before quantifying; record assumptions and calculation inputs so another run can reproduce the states. Separate cash, liabilities, contribution room, eligibility and future entitlement.

Explore a few candidate visual mechanisms internally. Select one that makes the causal relationship legible, then storyboard the choice, causal sequence, settled state, alternative and reset. Locate future effects visibly in the future. Record what each subject's behaviour means and what simplifications could mislead. Routine creative choices remain within the user's existing authorization.

## 2. Lock the reference and meaning

View the actual approved style references before implementation; filenames and prose are insufficient. Record the chosen reference paths, visual vocabulary, scene composition and storyboard in the brief. Lock financial meaning and comparison assumptions before polishing movement. Any new image generation needs a specific missing asset, reference and acceptance criterion; reuse approved assets where suitable. Record prompts, inputs, outputs and provenance.

## 3. Implement a small complete lesson

Use [the visual build skill](../.agents/skills/fp-visual-build/SKILL.md) and the repository's frontend guidance when building. Keep financial state calculations separate from animation. Switching or replaying must produce a coherent state without duplicating cash or erasing existing rights. Keep labels near their subjects and distinguish symbolic decoration from measured quantities. Include keyboard and touch operation, reduced motion, reset and a concise textual state description.

## 4. Verify the claims and the scene

Check sourced rules and representative calculations independently of animation, including relevant boundaries. Run the checks appropriate to the changed code. Capture and inspect screenshots at phone and desktop sizes, including the settled alternative states. Check causality, timing, visual hierarchy, style fidelity and readable labels; exercise choice switching, replay, reset and accessibility behaviours. Review the actual rendered result, not only code or screenshot creation success. Use one independent reviewer only when complexity or an unresolved correctness risk warrants it; give that reviewer a specific question. Fix findings and repeat affected checks.

## 5. Commit and hand off

Update the brief and project state with decisions, sources, validation evidence, known limits and the next concrete step. Save approved-scope review artifacts in Git on the existing `codex` branch; do not create another checkout unless requested. Follow the task's authorization for commit/push. Package a self-contained review when appropriate and provide GitHub view/download links. State what the lesson actually demonstrates and what remains symbolic or unimplemented.

## Model and context budget

These are routing recommendations and tool dispatch settings, not installed application configuration. The user/app selects the main conversation model; a spawned agent does not change it. Model availability can change. If the requested model is unavailable, report that fact and use the closest suitable available model with disclosure, or report the blocker if none can do the job.

| Work | Default routing |
| --- | --- |
| Routine orchestration, scoped implementation, ordinary review | `gpt-6.1-sol`, medium effort |
| Unresolved causal or visual architecture; difficult financial correctness | `gpt-6-astra`, high; ultra only when the concrete difficulty warrants it |
| Small mechanical documentation or inventory with explicit inputs | Optional `gpt-6-luna`, low/medium |
| Search, conversion, packaging, arithmetic and repeatable checks | Shell/tools before another agent |

Default to solo execution. If delegation pays for itself, use one bounded executor; add one independent reviewer only for a distinct need. Do not fan out the same task or multiply reviews. Preserve Astra capacity for hard story and visual decisions; escalation must name the blocker, evidence, attempted approaches and the decision needed. Return the answer to the executor as a short decision record.

Use [the agent task packet](templates/AGENT-TASK.md), about 300–600 words when needed: paths and relevant facts, not conversation history. With a tool supporting these fields, dispatch explicitly, for example `spawn_agent({task_name: "lesson_executor", model: "gpt-6.1-sol", reasoning_effort: "medium", fork_turns: "none", message: "<bounded task packet>"})`. Full-history forks inherit the parent's model and effort and cannot override them; they can unintentionally carry Ultra into routine work. Fresh agents need all essential constraints in the packet and must read the named repository instructions.

Record elapsed time, tool calls, agent count and image-generation count in the handoff when available; report token usage only when supplied by the runtime. No verified model pricing or comparative benchmark is established here. Do not invent token totals, costs or savings percentages. Compare observed runs with equivalent scope before claiming an improvement.
