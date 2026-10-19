# [2610.23707v1] Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs

## Core value (1 sentence)
Give a multi-step agent the full tool catalog (~8,200 tools) through a fixed three-tool interface (SelectTools, UseTool, ListApps) running at the gateway, reducing input tokens and billed cost versus a curated static list, without fine-tuning on each organization's tools.

## Problem
Prior work failed to solve that an agent can invoke only the tools whose definitions it has been given, while the tools it may need are too many to list in full on every request (~8,200 tools, >1.76M tokens total, exceeding any model's context window), and a curated short list limits the agent to only the tasks the list anticipates.

## Contribution
- Tool Recommendation, a deployed system at Arcade: the agent receives three fixed tools via MCP instead of a tool list; SelectTools returns the definitions of the tools a task needs; UseTool runs a tool under the end user's own authorization; ListApps tells which applications are reachable.
- Evaluation of recommendation quality on ToolRet (7,961 queries over 44,453 tools) and end-to-end session cost on two agent clients (Codex, Claude Code), reporting both Recall@10 and Completeness@10 (the fraction of queries with every needed tool in the top ten).
- Comparison against BM25 and published systems with 6-9 times as many parameters (7.2B-10.4B vs. Tool Recommendation's 1.2B).

## Method
Two-stage architecture: stage 1 retrieves candidate tools for each task description by fusing lexical (BM25) and dense retrieval; stage 2 re-ranks leading candidates with a cross-encoder that reads task and tool together, whenever top candidates score close together (more than 99.9% of production requests). Both models are fine-tuned by Arcade on examples of tasks and the tools that accomplish them. The system runs at the gateway between agent and tools; every call executes under the end user's own credentials and is authorized twice: the user must have consented to the tool's service, and the tool must lie within the gateway's eligible scope. The fixed three-tool interface (SelectTools, UseTool, ListApps) totals 993 tokens, about 1,800 times fewer than the catalog.

## KNOWLEDGE — Data & figures
- ~8,200 tools (8,252 as of 2026-09-14) in Arcade's public catalog, definitions totaling ~1.76M tokens.
- ToolRet: 7,961 queries over 44,453 tools in three categories (web APIs, code functions, customized applications).
- Completeness@10: Tool Recommendation 45.2% vs BM25 28.8% (+57% relative), BM25 is a lexical ranking that commercial tool search offers.
- Recall@10: 55.2 vs 37.0 for BM25 (1.49x, 95% CI 1.35-1.78).
- First recommendation covered every tool the workflow required in 304/327 Codex sessions (93%).
- Input tokens: -17.2% with Codex, -39.6% with Claude Code; median Codex session used 19.0% less input.
- Total bill: -13.6% overall (95% CI 7.4%-18.4%, p=0.006); every one of 14 runs cheaper; by client: Codex -5.5%, Claude Code -21.8%.
- Task completion: 276/327 Codex with recommendation vs 273/327 static list (McNemar p=0.80); 74/81 Claude Code vs 76/81.
- Ranking service latency: 131 ms median / 292 ms p95; reranking 62 ms/195 ms; SelectTools ~1.4 s end-to-end.
- Model size: 1.2B parameters vs published baselines 7.2B-10.4B (up to 9x).
- Median Arcade gateway created with 30 tools, under 0.4% of the full catalog.
- Cost model: typical session has 3 user messages, each answered with 8 tool calls, search rate 0.12 searches per tool call over 30 days of production use during the system's free research preview.
- Static list cheaper only below ~25-28 tools, or when the agent searches more than ~0.63 times per tool call (5x the observed rate).
- Prompt cache: with Codex, 85% of input with recommendation and 87% with static list served from cache.

## INSIGHT — Mechanism & why
[Completeness@10 matters more than Recall@10] BECAUSE [an agent missing one tool in a chain fails the task, even if Recall@10 is high]. This means [tool ranking should be judged by whether it returns the complete set of tools a task needs, not just the fraction of correct tools].
[Each search adds a turn that re-sends the conversation] BECAUSE [one lone search pays for itself, three searches do not]. This means [search frequency determines whether recommendation is cheaper than a static list; threshold ~0.63 searches per tool call].
[Input token reduction does not predict the bill well] BECAUSE [prompt caching dominates the bill, cached tokens billed at about one-tenth the full rate]. This means [cost should be reported in dollars, with the client's caching behavior stated].
[Static list is cheaper for small catalogs (<25-28 tools) and short lookups] BECAUSE [each search costs a turn a short list doesn't need]. This means [use a static list for small, stable tool sets; use recommendation for large, daily-changing catalogs].

## IDEA — What to apply
Apply the fixed three-tool interface (SelectTools, UseTool, ListApps) to a solopreneur's agent system with many tools: step 1 is to set up a recommendation gateway before the agent, so the agent receives only 3 tools instead of the full list.
Use Completeness@10 instead of Recall@10 to evaluate a tool-finding system: step 1 is to define "every tool each task needs" and measure the fraction of tasks with all needed tools in the top-k.

## WISDOM — General principle
Principle: Give an agent the full catalog through a small fixed interface is cheaper than a curated short list, when the catalog is large and changes daily. DO NOT apply when the catalog is small (under 25-28 tools) and stable, or when the agent searches too often (more than 0.63 times per tool call).

## Assumptions & Limitations
- Conditions for validity: system runs via Arcade gateway, tools served by an Arcade gateway, catalog can change daily.
- Limitations acknowledged by the paper: only available through Arcade, others cannot reproduce session results outside Arcade; ToolRet measures ranking, not agent behavior; static prose documentation cannot express multi-turn context, authorization state, or tools depending on an earlier call's output; published baselines' absolute scores not directly comparable (run in other harnesses); session-cost evaluation limited in scope (two clients, 30-34 seeded workflows, vs 100-tool static list, at list prices).
- Limitations the paper does NOT mention: operational cost of the ranking service at scale; impact of the agent re-reading stored results; extra cost from consecutive searches.

## Metadata
- Year: 2026
- Authors: Sam Partee, River Stevens, Thierry Damiba, Valerie Fanelle (Arcade.dev)
- arXiv category: cs.LG
- PDF link: https://arxiv.org/pdf/2610.23707v1
- arXiv ID: 2610.23707v1
- Label: [applied]
- Skill: tool-recommendation-multi-step-agents | Test: [SKILL VALID]
