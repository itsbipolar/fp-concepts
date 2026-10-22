# Bounded agent task

Fill this packet with concrete facts, usually about 300–600 words. Send it to a fresh agent with `fork_turns: "none"`; do not paste the conversation history. See [routing guidance](../BUILD-WORKFLOW.md#model-and-context-budget).

## Assignment and dispatch

- Task name: `<unique short name>`
- Outcome: `<one concrete, reviewable result and why it matters>`
- Model / effort: `<Sol medium by default; justify any exception>`
- Execution mode: `<solo executor or one specifically bounded review>`

## Context to read

- Repository / branch: `<absolute checkout path>` / `codex`; use the existing checkout.
- Read `AGENTS.md`, `docs/INTERACTION-PRINCIPLES.md`, and `<only relevant instructions, brief, source ledger, style/reference paths>`.
- Current state: `<implemented behaviour, accepted decisions, and relevant constraints>`.
- Financial assumptions: `<jurisdiction, year, shared comparison basis, timing, verified sources; mark unknowns>`.
- Visual meaning: `<decision, material consequences, selected mechanism and approved references to view>`.

## Ownership and boundaries

- You may edit: `<exact files or directories>`.
- Shared work / dependencies: `<other owners and required interface or artifact>`.
- Do not edit: `<explicit exclusions>`.
- Non-goals: `<features, redesigns, financial claims or polish outside this task>`.
- Authority: `<applicable user authorization for implementation, commit, push or packaging; do not infer authority to message others>`.
- Delegation: `<none by default; if authorized, specify one bounded role and model>`.

## Work and acceptance

1. `<specific implementation or review task>`.
2. `<required source/calculation check or rendered reference inspection>`.
3. `<targeted tests, screenshot states/sizes, accessibility or packaging checks>`.

Done means `<observable behaviour, required artifacts, and checks that establish success>`. For visual work, inspect the resulting screenshots; for quantitative work, verify rules and calculations independently of animation. Preserve existing approved work and other agents' changes.

## Escalation and return

Resolve routine choices within scope. Escalate only a concrete blocker: state the disputed causal/visual/correctness decision, evidence, attempts and smallest question that needs Astra. Do not reopen settled decisions or ask for repeated permission already covered by the assignment. If a requested model is unavailable, disclose the substitute or blocker.

Return a concise result: changed file paths, behaviour delivered, checks and evidence, remaining limits, and next action. Include elapsed time, tool/agent/image-generation counts if available, and runtime-reported tokens only if available. Do not invent cost or savings figures. Do not commit or push unless explicitly included in the authority above.
