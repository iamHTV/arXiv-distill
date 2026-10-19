# Skill: tool-recommendation-multi-step-agents
Source: 2610.23707v1
Type: framework

## When to use this skill
- An agent system with many tools (large, daily-changing catalog) where the agent cannot receive all tool definitions on every request.
- Want to reduce billed cost and input tokens for multi-step agent tasks without lowering task completion rate.
- A gateway exists between agent and tools that can execute calls under the end user's own credentials and check authorization.

## When NOT to use this skill
- Small, stable catalog (under 25-28 tools) → a static list is cheaper.
- Agent searches too often (more than 0.63 times per tool call) → each search costs a turn; recommendation won't save money.

## Required inputs
- An Arcade gateway (or equivalent) between agent and tool catalog.
- Tool definitions (name, description, argument documentation) to index.
- Two ranking models: a hybrid retrieval model (BM25 + dense) and a cross-encoder reranker (or equivalent).
- A system to record user consent per service/tool.
- An agent client able to call the three fixed tools: SelectTools, UseTool, ListApps.

## Steps
1. Set up a recommendation gateway between agent and catalog; the agent receives no catalog directly, only three fixed tools via MCP.
2. Index each tool (name, description, argument documentation) into a search index combining lexical (BM25) and dense retrieval.
3. When the agent describes a task, SelectTools retrieves candidates for each task description via BM25+dense fusion, then a cross-encoder re-ranks top candidates (when top candidates score close together).
4. Return definitions of the top 5 tools per task description; the agent selects and calls a tool via UseTool under the end user's own authorization.
5. Authorize twice per call: user consented to the tool's service, and the tool lies within the gateway's eligible scope.
6. Evaluate quality with Completeness@10 (fraction of queries with every needed tool in top-10), not just Recall@10, because missing one tool in a chain fails the task.
7. Measure end-to-end session cost (total bill, not just input tokens) vs a 100-tool static list; if the agent searches more than 0.63 times per tool call, use a static list instead.

## Expected output
- The agent gets every tool it needs from a large catalog, billed cost reduced (13.6% overall across 14 runs), task completion rate unchanged.

## Example application
- A solopreneur's customer support agent combining Slack, HubSpot, Gmail: instead of granting 100 static tools per request, install a recommendation gateway; the agent calls SelectTools when it needs a tool from an app, gets definitions of the top 5 tools, runs via UseTool, cutting session cost by ~20%.

## Gotchas
- Do not compare absolute scores across ranking systems run in different harnesses; only compare lift over each harness's own BM25.
- Do not report cost only via input tokens; prompt caching makes cached tokens billed at ~1/10 the full rate; report in dollars.
- Completeness@10 is a stricter metric than Recall@10; missing one tool in a multi-step chain fails the task.
- Each search adds a turn re-sending the whole conversation; 3+ searches can use more input than a static list.
- The system is only available through Arcade; session results cannot be reproduced outside Arcade.

## Self-check
- Can someone who has not read the original paper follow these 7 steps? [YES] — each step is a concrete action.
- Which step is most vague? Steps 2-3 (BM25+dense indexing and cross-encoder re-ranking) need implementation-specific details.
- Is the Input section sufficient? [YES] — gateway, catalog, 2 ranking models, consent system, agent client are all covered.

## Dry run (hypothetical scenario)
- Scenario: A solopreneur's sales support agent uses 200 tools on Slack, HubSpot, Gmail; the catalog changes weekly as new integrations are added.
- Run the skill: (1) Install a recommendation gateway between agent and the 200 tools; (2) index name+description+parameters of each tool; (3) agent calls SelectTools when it needs to perform a task (e.g., "find a lead in HubSpot then send email"); (4) gets definitions of the top 5 tools, calls UseTool under the user's authorization; (5) checks consent and eligible scope before executing; (6) evaluates Completeness@10 on 50 real tasks; (7) measures total bill vs a 100-tool static list; if search rate <0.63 searches per tool call, keep recommendation.

## Verdict: [SKILL VALID]
