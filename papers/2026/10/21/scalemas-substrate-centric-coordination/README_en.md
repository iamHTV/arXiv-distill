# [2610.16120v1] Scaling Multi-Agent Intelligence with Substrate-Centric Coordination

## Core Value (1 sentence)
ScaleMAS is a task-agnostic agent substrate where asynchronous LLM agents self-coordinate through a shared datastore of linked messages via three operations (publish, search, visit), with bounded reads per agent regardless of group size, citation-based ranking, and persistence after producers leave — scaling to 128 agents at lower inference compute than agent-centric baselines.

## Problem
Existing LLM-based multi-agent systems scale poorly: reading burden grows with group size, useful information is diluted by shared work of unknown quality, and systems are fragile to failed agents. Agent-centric designs (fixed workflows, central coordinators, peer-to-peer messaging) wire coordination into agents, causing unbounded reads and single points of failure.

## Contribution
1. Build ScaleMAS, a task-agnostic agent substrate where asynchronous agents interact with a shared datastore of linked messages via three operations: publishing messages with optional references, searching by content (returns at most k), and visiting by address.
2. Citation-based ranking: messages start at weight 0, gain weight when cited (sm ← sm + α(1−sm)), decay each step (sm ← γsm); search ranks by citation weight plus normalized lexical relevance.
3. Evaluate on four agentic tasks (BrowseComp-Plus, FATE, SWE-bench Verified, Contradiction Audit) with two backbones (Qwen3.5-9B, Claude-5-Sonnet), comparing against Multi-Agent Debate, DeLM, AOrchestra, and parallel ReAct.

## Method
ScaleMAS comprises: (1) a datastore D, an append-only sequence of messages m = (u, a, r, R) recording completed work (sub-task, artifact, rationale, references); messages get sequential addresses, are never edited/deleted, forming a DAG of references; each message carries citation weight sm ∈ [0,1). (2) Three operations: publish appends a readable message; search(q) returns top-k ranked messages; visit(m₁,…,mⱼ) returns named messages by address. (3) Deterministic rules: publish requires all references exist and rationale names every reference; weight starts at 0, increases by α(1−sm) per citation, decays by γ each step; search score = sm + Rel(q,m)/max Rel; every read adds at most k bounded-length messages to context regardless of group size or datastore growth.

## KNOWLEDGE — Data & Concepts
- 4 tasks: BrowseComp-Plus (search-intensive), FATE (Lean 4 theorem proving), SWE-bench Verified (GitHub issue resolution), Contradiction Audit (contradiction detection in software docs, author-built)
- 2 backbones: Qwen3.5-9B, Claude-5-Sonnet
- 4 baselines: Parallel ReAct (no communication), Multi-Agent Debate (all-to-all messaging), DeLM (blackboard shared context), AOrchestra (coordinator-based delegation)
- Results (Qwen3.5-9B): BrowseComp-Plus 38.1% (1 agent) → 65.3% (16 agents); FATE-M 24.0% → 56.0%; Contradiction Audit x4 4.1% → 29.4%; SWE-bench Verified plateaus after 8 agents
- Claude-5-Sonnet: Contradiction Audit x8 10.6% (1 agent) → 57.5% (8 agents)
- Compute efficiency: BrowseComp-Plus ~20M tokens/example, 8 ScaleMAS agents 60.0% vs 16 DeLM agents 26.0%; SWE-bench Verified 4 ScaleMAS agents 80.0% with 15.3M tokens vs 8 ReAct 28.3M tokens
- Claude BrowseComp-Plus ~3.5M tokens/example: 8 ScaleMAS 79.8% vs 8 MAD 73.0% vs 4 ReAct 72.0%
- MAD tokens/example grow 5.6M (2 agents) → 48.5M (16 agents), accuracy flat 28–32%
- Scale to 128 agents (Qwen3.5-9B): FATE-M ScaleMAS plateaus below 60% at N=16, MAD peaks at N=32 then declines, DeLM lower at N=128 than N=8; Contradiction Audit x4 ScaleMAS reaches 50.9% at N=128, DeLM/MAD never exceed 7%
- Resilience: 1 permanently failing agent, 7 healthy ScaleMAS agents reach 19.4% (same as 7 healthy alone); DeLM drops below 1% with one failure; p=0.8 dropout: 8 ScaleMAS agents solve 22.0% of FATE-M vs 2.0% with 1 agent; AOrchestra loses >50% score at p=0.2 (coordinator loss)
- Ablation: removing citation weight, N=8: BrowseComp-Plus 60.0%→40.8%, Contradiction Audit x4 23.1%→9.7%; FATE-M N=8: 49.0% vs 42.0%, BM25 reads 2× tokens (5.7M vs 2.7M)
- Private substrate (partitioned by author): lowers accuracy 8.3 pts BrowseComp-Plus, 8.4 SWE-bench Verified
- No substrate (independent ReAct): Contradiction Audit 8.1% vs 6.6% (ScaleMAS)
- Peer citations: messages on correct answer's evidence chain rise from 29% (least-cited quintile) to 85% (most-cited); messages naming gold evidence get ~2× citations vs other documents
- Correct answers assembled across agents: share with peer-found gold evidence in citation chain grows 9% (2 agents) → 24% (8 agents)

## INSIGHT — Mechanism & Why
[ScaleMAS scales better than agent-centric baselines] BECAUSE [each read returns at most k messages ranked by citation weight and lexical relevance, so agent reading stays bounded regardless of group size; messages persist after producers leave, so the group continues when individual agents fail]. This means [coordination should be designed into the shared substrate, not wired into agent logic].
[Peer citation weights automatically curate the datastore] BECAUSE [weight accumulates only when others build on a message, so search surfaces what the group has actually relied on; signal strengthens as datastore grows]. This means [quality is earned through reuse, not centralized judgment].
[Correct answers are assembled across agents] BECAUSE [agents increasingly answer by combining evidence others found; more correct answers rest on peer-found evidence as group grows]. This means [division of labor emerges without explicit task assignment].
[One failing agent doesn't break the group] BECAUSE [ScaleMAS assigns no jobs to agents and requires no agent to finish; a failing agent publishes nothing, healthy agents keep building on each other's messages]. This means [flexible membership — newcomers read the datastore and catch up via search; leavers take nothing with them].

## IDEA — Actionable Applications
1. Apply [substrate-centric coordination] to [building scalable multi-agent LLM systems]: first step is to set up a shared linked-message datastore, have agents interact only via publish/search/visit, and bound each read to k messages.
2. Apply [peer citation weighting] to [ranking shared information without central judgment]: first step is to track which messages other agents cite and use citation count as a quality signal for search ranking.
3. Apply [failure-tolerant agent membership] to [designing continuously operating agent systems]: first step is to make messages outlive their producers, not assign fixed jobs to agents, so newcomers can join and leavers don't disrupt.

## WISDOM — General Principles
1. Principle: Multi-agent coordination should be designed into the shared substrate (bounded reads, search, persistent messages) rather than wired into agent logic. Apply when: building multi-agent systems that need to scale with agent count. Do not apply when: task is simple and needs only 1–2 agents.
2. Principle: Quality signals can be earned through reuse (citations) rather than centralized evaluation. Apply when: needing to rank shared information in large open systems. Do not apply when: there's no mechanism to track information reuse.

## Assumptions & Limitations
- Conditions that must hold: agents can run asynchronously, shared datastore is queryable, search function (BM25 or equivalent) available for ranking.
- Limitations acknowledged by paper: ScaleMAS is harness-agnostic (runs on standard ReAct loop), evaluation limited to 4 chosen benchmarks; SWE-bench Verified plateaus after 8 agents (LLM capability limit).
- Limitations paper does NOT mention: no real setup/maintenance cost of shared datastore; no search latency measured at very large datastore scale; no direct comparison with production agent orchestration systems.

## Metadata
- Year: 2026
- Authors: Zhenting Qi, Zhuokai Zhao, Rulin Shao, Kerem Oktar, Zhiyuan Yao, Himabindu Lakkaraju, Wen-tau Yih, Ansong Ni, Bhargavi Paranjape, Yilun Du (FAIR at Meta, Meta AI, Harvard, Kempner Institute)
- arXiv Category: cs.CL
- PDF Link: https://arxiv.org/pdf/2610.16120
- arXiv ID: 2610.16120v1
- Label: [applied]
- Citation count: [not found]