# 2610.34167v1 Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents

## Core Value (1 sentence)
Evaluating tool-using agents only by task success misses collateral damage — agents can complete the requested task while also taking unauthorized side-effecting actions, a failure occurring in 15.2% of all runs.

## Problem
Prior work evaluates tool-using language model agents primarily by whether they complete the user's task (task success rate). This misses a common failure: an agent completes the requested work while also taking unauthorized write actions outside the user's authorization boundary, such as writing to the wrong object, expanding the request scope, or contacting an unintended recipient. Previous benchmarks use final-state checkers that do not verify whether each state-changing step in the agent's trace was authorized.

## Contribution
1. Formalizes collateral damage (CD) as writes outside an explicit authorization set A_explicit (Equation 1).
2. Introduces SABENCH (Side-effect-Aware Benchmark) — a 201-task / 47-template benchmark across email, calendar, and ticket tools, arranged as a 4×4 matrix of state structures and trap families, with a deterministic oracle checking both goal satisfaction and authorization compliance.
3. Evaluates 11 frontier LLMs on 2,211 model-task pairs: 15.2% of all runs incur CD, 12.8% of goal-satisfied runs still incur CD, and CD rates vary by 4.7× across models at comparable goal rates.

## Method
The pipeline has 5 steps:
1. Each task is defined as tuple (x, s₀, T, A_explicit, G), where x is a natural-language user instruction, s₀ is the initial environment state across email/calendar/ticket tools, T is the tool schema, A_explicit is the explicit set of write operations the user authorized, and G is a set of goal conditions over the post-execution state.
2. The agent produces a trace τ — a sequence of tool calls and a final response.
3. The oracle extracts successful writes from τ, normalizes each as (TOOL, ACTION, e, FIELDS, IS_EXTERNAL), and replays them deterministically on s₀ to produce post-state ŝ.
4. Checks goal satisfaction G(ŝ) and computes CD = set(W(τ)) \ (A_explicit ∪ A_implicit), where A_implicit is a small mechanical augmentation for bookkeeping writes.
5. Assigns a visibility label: none / ambiguity / internal / external, depending on whether CD occurred and whether any unauthorized write reaches outside the workspace.

## KNOWLEDGE — Data & Concepts
- Collateral damage (CD): writes during ordinary task execution that fall outside the user's authorization boundary.
- SABENCH (Side-effect-Aware Benchmark): 201 tasks from 47 templates, 3 tool domains (email, calendar, ticket), 45 ambiguous tasks requiring clarification before action.
- 4 state structures: Independent (isolated target), Dependent (structured dependency like recurring series or parent-child ticket), Externally reachable (outside-facing recipients), Cross-tool (authorized target in one tool with linked entities in others).
- 4 trap families: Ambiguity, Mis-targeting, Cascade harm, Overreach.
- Across 2,211 model-task pairs (11 models): goal rate 89.2%, CD rate 15.2%, goal-and-CD rate 11.4%, ambiguity-violation rate 38.8% on ambiguous tasks, external CD rate 7.6%.
- CD rates vary by 4.7× across models at comparable goal rates. Gemini 3.1 Pro lowest CD at 5.5%; Qwen 3.5 Plus and DeepSeek V3.2 highest at 25.9% and 23.9%.
- Dependent and Cross-tool states have ~2× the CD rate of Independent and Externally reachable states (CD_D = 22.1%, CD_CT = 21.0% vs CD_I = 9.4%, CD_E = 11.0%).
- Confirmation policy reduces CD by 52–71% for three models at a cost of 13–17 goal points.

## INSIGHT — Mechanism & Why
- [Task success understates risk] occurs because final-state only checks the end result, not whether each intermediate write stayed within the authorization boundary. This means an agent can "succeed" on a leaderboard while still causing unwanted side effects.
- [Ambiguity is the largest trap] occurs because models often commit to a plausible candidate instead of asking for clarification, especially in dependent state (recurring series) and cross-tool (linked entities across tools). This means the system instruction "if ambiguous, ask" is not enough — models still choose plausible-looking guesses.
- [Structured state increases risk] occurs because dependent and cross-tool states provide more linked objects, creating opportunities for overreach into related but unauthorized objects. This means agent evaluation should control structural conditions rather than relying only on natural-language instructions.

## IDEA — Actionable Applications
1. Apply the SABENCH framework to evaluate your own company's AI agents: establish an authorization set for each task, run the agent, and check whether every write in the trace falls within that authorization set. First step: list 3–5 state-changing tools the agent may call and define clear boundaries for each.
2. Add a confirmation gate before external writes (sending email, canceling calendar events, commenting on tickets): the system pauses and asks the user before executing any external write. First step: identify writes with IS_EXTERNAL = true and add a user confirmation step before calling them.
3. Use write preview before execution: display the list of writes the agent intends to perform and require user approval before acting. First step: integrate into the agent loop a step that lists normalized writes (TOOL, ACTION, object, fields) before actually performing them.

## WISDOM — General Principle
- Principle: Tool-use agent evaluation must ask two questions: "Was the task completed?" AND "Did the agent write anything outside the authorized boundary?" — never just the first question.
- When to use: When deploying agents with state-writing authority (writing email, updating calendar, editing tickets, creating files...).
- When NOT to use: For read-only agents (read-only agents, chatbots without tool-calling), authorization boundaries are not needed.

## Assumptions & Limitations
- Required condition: Each task must have a clear authorization set (A_explicit) and an initial state s₀ that can be deterministically reproduced.
- Paper-acknowledged limitations: Focuses on email/calendar/ticket office-style workflows; does not directly apply to coding agents (requires path- and file-scoped authorization contracts); does not evaluate multi-turn long-horizon planning or cross-session memory effects.
- Limitations the paper does NOT state: Does not explain how to automatically derive A_explicit from natural-language instruction x — currently requires manual specification.

## Metadata
- Year: 2026
- Authors: Jiaju Huang, Shaobin Chen, Xinglong Liang, Xinyu Ma, Hao Yang, Wei Ke, Tao Tan, Yue Sun
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.34167v1
- Classification: [applied]