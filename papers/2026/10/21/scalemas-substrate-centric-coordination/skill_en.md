# Skill: scalemas-substrate-coordination

Source: 2610.16120v1
Type: framework / workflow

## When to use this skill
- When building multi-agent LLM systems that need to scale with agent count without increasing per-agent reading burden.
- When wanting to design agent coordination through a shared datastore (substrate) rather than wiring it into agent logic.
- When needing failure-tolerant agent systems (agent failures, agents leaving, new agents joining) without disrupting group operation.

## When NOT to use this skill
- When the task is simple and needs only 1–2 agents (no scaling needed).
- When lacking a queryable shared datastore or a search function for ranking messages.
- When agents must run synchronously and wait for each other (ScaleMAS is designed for asynchronous operation).

## Required inputs
- A shared linked-message datastore (append-only sequence of messages).
- Each message has 4 fields: sub-task (u), artifact (a), rationale (r), reference set (R).
- A search function (BM25 or equivalent) for ranking messages by content.
- Asynchronous agents, each accessing the datastore only through 3 operations: publish, search, visit.
- Threshold k (max messages returned per search) and citation weight parameters (α, γ).

## Steps to execute
1. Set up the message datastore: each message m = (u, a, r, R) records completed work, gets sequential address on write, never edited/deleted, forming a DAG via references.
2. Implement 3 operations: publish appends a readable message; search returns top-k ranked messages; visit returns named messages by address.
3. Apply deterministic rules: publish requires all references exist and rationale names every reference; weight starts at 0, increases by α(1−sm) per citation, decays by γ each step; search ranks by score = citation weight + normalized lexical relevance.
4. Bound each read: every read adds at most k bounded-length messages to context regardless of group size or datastore growth.
5. Run agents asynchronously: each agent is a normal LLM agent with task tools plus 3 extra operations; no agent holds a role, messages another agent, or assigns work to others.
6. Handle failures: messages outlive their producers, newcomers read the datastore and catch up via search, failing agents publish nothing.

## Expected output
- A scalable multi-agent LLM system with bounded per-agent reads.
- Performance report: accuracy by group size, inference cost (tokens/example), agent turn count.
- Failure tolerance: group continues operating when agents fail or leave.

## Example application
A group of 16 LLM agents performs deep research on a large document corpus. Each agent publishes findings to the shared datastore via publish, searches others' information via search (max 10 messages per read), and visits details via visit. Messages cited by many other agents rank higher in search. When one agent fails, others continue working on published messages. Results: on BrowseComp-Plus, 16 ScaleMAS agents reach 65.3% vs 38.1% with 1 agent; at matched ~20M tokens/example, 8 ScaleMAS agents reach 60.0% vs 16 DeLM agents reaching 26.0%.

## Gotchas
- No real setup/maintenance cost data for shared datastore.
- No search latency measured at very large datastore scale.
- No direct comparison with production agent orchestration systems.
- SWE-bench Verified plateaus after 8 agents (LLM capability limit).