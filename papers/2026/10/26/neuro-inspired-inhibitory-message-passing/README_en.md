# 2610.24718 — Neuro-Inspired Inhibitory Message Passing for Accurate and Token-Efficient Multi-Agent Reasoning

## Core Value (1 sentence)

Use a training-free communication router that forwards only the original evidence sentences each receiver lacks, cancels duplicate copies, and excludes senders' reasoning and answers — improving group accuracy by 39-77 percentage points and reducing tokens per run by 10-46%.

## Problem

In multi-agent systems, a group collectively holds all evidence needed to solve a task yet still reaches the wrong conclusion because shared evidence crowds out rare, decisive private evidence (hidden profile problem). Standard message passing delivers every sender's full message — including their reasoning and answers — to all receivers, increasing each agent's input load and biasing judgment through repetition (data incest). Limiting the number of senders keeps inboxes small but risks excluding agents holding decisive evidence.

## Contribution

1. Proposes inhibitory message passing, a training-free communication router with three rules: (1) forward original evidence sentences, not sender messages; (2) deliver each evidence sentence at most once per round per receiver; (3) deliver only if the receiver lacks it.
2. Router removes evidence the receiver already holds, requires no additional model calls and no training.
3. Evaluated on 3 benchmarks (HiddenBench, decoy puzzles, MuSiQue), 7 open models (4B-32B parameters) and 2 commercial models (GPT-6 Luna, Claude Haiku 5.5), groups up to 64 agents, 3 architectures (peer-to-peer, orchestrator-worker, hierarchical).

## Method

Each agent writes a message each round. The router builds an inbox for each receiver from sender messages using three rules:

1. **Evidence, not messages**: when a sender's message restates an evidence sentence the sender holds, the original sentence (not the message) travels, without the sender's reasoning or answer.
2. **Once per round**: however many senders restate the same evidence sentence, the receiver gets it once per round.
3. **Only if missing**: an evidence sentence already in the receiver's own evidence is not delivered.

The router matches rare words in messages against each agent's known evidence sentences (Appendix C.1), makes no model calls and needs no training. Key formula (Equation 2): n_iu = min(E_iu, θ_iu) where θ_iu = 1 if the receiver lacks sentence u, 0 if they hold it — cancellation grows one-for-one with arrivals, so an inbox never holds more than the sentences the receiver lacks, regardless of how many senders repeat them.

## KNOWLEDGE — Data & Concepts

- Group accuracy improved 39-77 percentage points across 3 benchmarks and both main models vs standard message passing.
- Tokens per run fell 10-46% vs standard message passing (counting all agents, including the decider).
- 7 open models from 4B to 32B parameters (Qwen3-4B/8B/14B/32B, Olmo-3-7B, Ministral-3-8B, Gemma-4-12B) and 2 commercial models (GPT-6 Luna, Claude Haiku 5.5).
- Groups up to 64 agents (HiddenBench).
- On HiddenBench, Qwen3-8B accuracy stayed steady at 80-86% from 4 to 64 agents, while standard message passing stayed low (23% at N=4, degraded to 8% at N=64).
- Group accuracy rose 63 and 59 percentage points in pre-registered commercial evaluations across group sizes.
- At N=32, cancellation shrank the decider's prompt by roughly four-fifths in orchestrator-worker teams and nearly half in hierarchical teams.
- Removing all router rules dropped accuracy to 42-53% (HiddenBench) and 7-24% (decoy puzzles), at 2.4-4.7x the router's tokens.

## INSIGHT — Mechanism & Why

[Shared evidence repetition] happens BECAUSE [every message carries both evidence and the sender's preferred answer, making shared evidence over-represented in each receiver's inbox]. This means [model judgment is biased toward consensus, rare decisive evidence is overlooked, the group reaches the wrong answer despite collectively holding all needed evidence].

[Removing evidence the receiver already has] happens BECAUSE [each evidence sentence needs to be delivered only once per receiver, regardless of how many senders restate it]. This means [inbox size does not grow with group size, every holder of private evidence remains reachable, accuracy stays stable as the group grows].

[Forwarding original evidence instead of sender restatements] happens BECAUSE [sender sentences carry their preferred answers, spreading shared mistakes]. This means [receivers weigh evidence without being influenced by others' conclusions, closing one route by which shared errors propagate].

## IDEA — Actionable Applications

1. Apply inhibitory message passing to multi-agent research/analysis groups: build a lightweight router forwarding only original evidence sentences each receiver lacks, excluding sender reasoning and answers. First step: log the evidence sentences each agent holds, match rare words in outgoing messages against known evidence to filter inboxes.
2. Apply to multi-agent market research: each agent gathers independent sources, the router forwards only missing evidence to the decider, avoiding repetition that skews conclusions. First step: format each agent's output as a list of sourced evidence sentences (source tags), have the router subtract sentences the decider already has.

## WISDOM — General Principle

- Principle: In multi-agent systems, communication design matters more than model size — bounding redundant input per receiver lets accuracy scale independently of group size.
- When to use: Multi-agent groups that need to combine distributed evidence to reach a scored decision (e.g., research, analysis, diagnosis).
- When NOT to use: Work requiring agents to exchange intermediate results not contained in original evidence (coding, planning, distributed computation) — excluding them may impede collaboration.
- Example outside original domain: In human team meetings, summarize only new information each member hasn't heard rather than recapping the full discussion — shorter meetings, less anchoring to early majority opinion.

## Assumptions & Limitations

- Required conditions: reliable provenance link between message and evidence it refers to; ability to distinguish repeated reports of one observation from independent observations of the same claim; errors would suppress useful evidence or let redundant input accumulate.
- Paper's acknowledged limitations: experiments focus on tasks combining distributed evidence for scored answers; router bounds repetition but distinct evidence a receiver must process can still grow with group size; router does not assess truth/credibility of forwarded evidence (a planted false sentence reduced accuracy); cannot withdraw evidence later corrected or outdated.
- Paper's unaddressed limitations: does not establish when excluding sender reasoning/answers impedes collaboration on tasks needing intermediate result exchange (code, planning); effectiveness on tasks without clear evidence to match (e.g., creative writing) unverified.

## Metadata

- Year: 2026
- Authors: Nima H. Siboni, Magdalena Springer, Vahid Rostami
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.24718
- Citation count: not available yet (new paper, Oct 2026)
