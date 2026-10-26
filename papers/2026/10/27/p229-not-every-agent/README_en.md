# 2610.31743 — Not Every Agent Needs the Strongest Model: Unified Prompt–Model Optimization for Heterogeneous LLM-based Multi-Agent Systems

## Core Value (1 sentence)

Not every agent in a multi-agent LLM system needs the strongest model — UniMASO optimizes prompts and model assignments by role, achieving average score 70.40 (up from 69.79) while reducing token-weighted deployment cost by 85.2% compared to homogeneous DeepSeek-V4-Pro configuration.

## Problem

Prompt optimization in multi-agent LLM systems typically keeps model assignments fixed, ignoring differences in role requirements and their associated inference costs. This leads to using the strongest model for every agent, causing unnecessary deployment costs without significantly improving task quality.

## Contribution

1. **UniMASO**: A unified framework for heterogeneous Multi-Agent System Optimization through joint adaptation of prompts and model assignments.
2. **Multi-level feedback**: UniMASO evaluates candidate updates through local, downstream, and global feedback.
3. **Cost-aware Pareto search**: Retains useful quality–cost trade-offs.
4. **Topology-aware co-evolution**: Coordinates updates according to agent roles and dependencies.
5. **Cross-level trajectory memory**: Supplies historical successes and failures to guide subsequent optimization.
6. **Experimental results**: On 5 benchmarks and 5 execution topologies, UniMASO achieves competitive task performance at substantially lower deployment cost than strongest homogeneous configurations. Centralized execution: improves average score from 69.79 to 70.40 while reducing token-weighted deployment cost by 85.2% relative to DeepSeek-V4-Pro with MASPO.

## Method

UniMASO operates through key components:

1. **Multi-level feedback**: Evaluates candidate updates through local (single agent task), downstream (downstream task affected), and global (whole system) feedback.

2. **Cost-aware Pareto search**: Searches for cost-optimal updates, retaining useful quality–cost trade-offs instead of only optimizing quality.

3. **Topology-aware co-evolution**: Coordinates updates according to agent roles and dependencies in the communication topology.

4. **Cross-level trajectory memory**: Stores historical successes and failures to guide subsequent optimization.

**Process:** Evaluate candidates → Pareto search → Coordinate via topology → Update prompts and models → Store trajectory → Repeat.

## KNOWLEDGE — Data & Concepts

- 5 benchmarks, 5 execution topologies.
- Centralized execution average score: 69.79 (baseline) → 70.40 (UniMASO).
- Token-weighted deployment cost reduced by 85.2% compared to DeepSeek-V4-Pro with MASPO.
- Code: https://github.com/Achilles008/UniMASO_main
- Heterogeneous model assignment based on role requirements.

## INSIGHT — Mechanism & Why

[Not every agent needs the strongest model] occurs BECAUSE [different agent roles have different capability and inference cost requirements; assigning the strongest model to every agent causes unnecessary costs]. This means [heterogeneous model assignment by role can significantly reduce cost without losing quality].

[Joint prompt–model optimization] occurs BECAUSE [prompts and models interact — a good prompt can compensate for a weaker model, and a strong model can compensate for a weak prompt; separate optimization misses this interaction]. This means [joint prompt–model adaptation is more effective than optimizing each component separately].

[Cost-aware Pareto search] occurs BECAUSE [it is necessary to retain useful quality–cost trade-offs, not just find the highest quality point regardless of cost]. This means [developers should consider both quality and cost when designing multi-agent systems].

## IDEA — Actionable Applications

1. Role-based model assignment in multi-agent systems: Instead of using the strongest model for every agent, assign smaller models to agents that only handle formatting tasks and larger models to agents that need deep reasoning. First step: classify agents in the system by role and reasoning requirements, then assign appropriate models.

2. Joint prompt–model optimization: Instead of optimizing prompts separately then selecting models, search for optimal (prompt, model) pairs simultaneously for each role. First step: set up a search space containing prompt–model pairs and use Pareto search to find useful trade-offs.

3. Use trajectory memory to guide optimization: Store successes and failures from optimization history to inform subsequent rounds. First step: record results of each optimization round (prompt, model, score, cost) and use to filter out unpromising candidates.

## WISDOM — General Principle

- Principle: In multi-agent LLM systems, not every agent needs the strongest model; role-based model assignment and joint prompt–model optimization can significantly reduce cost without sacrificing quality.
- When to use: When building multi-agent systems with agents having different roles and where inference cost is a concern.
- When NOT to use: Systems with only one agent or where all agents need the same capability level.
- Example outside original domain: In a customer support team, agents handling FAQ queries can use smaller cheaper models, while agents handling complex complaints use larger models — reducing total operational cost without affecting service quality.

## Assumptions & Limitations

- Conditions that must hold: multi-agent system with agents having different roles; ability to measure inference cost of each model.
- Paper's acknowledged limitations: experiments on 5 benchmarks and 5 execution topologies; may not represent all real-world cases.
- Limitations paper does NOT state: effectiveness on dynamic topology multi-agent systems at scale; cost of maintaining cross-level trajectory memory.

## Metadata

- Year: 2026
- Authors: Mingxiu Cai, Haoyang Xian, Xinyu Ma, Yutong Wang, Zhenxi Song, Jing Li, Xuebo Liu
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.31743
- Citation count: not yet (new paper, Oct 2026)