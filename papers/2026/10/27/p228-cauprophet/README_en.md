# 2610.32477 — CauProphet: Teaching Agents to Develop Causal Cognition like Humans

## Core Value (1 sentence)

CauProphet is an agent that develops and updates causal knowledge from experience, connecting Causal Cognition with Causal Belief to guide decisions — in financial research, it achieves 25.4% improvement over baseline in mean rank correlation with next-day returns, and improves prediction accuracy from 21.3% to 28.6% in dynamic real-world settings.

## Problem

Existing LLM agents mainly retrieve records or summaries, lacking the ability to form and refine causal understanding of the world. For long-horizon tasks, agents cannot build persistent causal understanding from experience to apply to new decisions — they only retrieve records or summaries, without structured causal knowledge to guide action.

## Contribution

1. **CauProphet**: An agent that develops and updates causal knowledge within Causal Cognition. For each task, CauProphet combines relevant knowledge from Causal Cognition with current evidence to construct a Causal Belief, a structured belief capturing causal factors and effects of possible actions.
2. **Causal Scout**: A tool comparing competing explanations and suggesting observations that can distinguish them, helping the agent investigate competing explanations.
3. **Continuous update**: Causal Belief and Causal Cognition are continuously updated as new observations emerge, allowing causal knowledge to persist beyond individual experiences.
4. **Financial research evaluation**: CauProphet outperforms all baselines in mean rank correlation with next-day returns, achieving 25.4% improvement over baseline agent; improves prediction accuracy from 21.3% to 28.6% in dynamic real-world settings.

## Method

CauProphet views each task as a partially observable Markov decision process (POMDP), where the agent relies on a belief about an environment it cannot fully observe.

**Main components:**

1. **Causal Cognition**: Organizes retained knowledge around explanations of how recurring factors influence one another, together with their conditions, time scales, evidence, and unresolved questions. Its graph connects these factors through proposed causal relationships.

2. **Causal Belief**: A structured belief capturing what influences the outcome and how possible actions could change it, guiding the agent's decisions. Formed by combining knowledge from Causal Cognition with current evidence.

3. **Causal Scout**: Compares alternative explanations and suggests observations that could distinguish them.

4. **Causal Toolbox**: Tools for data diagnosis, causal inference, hypothesis checking.

**Process:** Observe → Analyze → Build Causal Belief → Select Action → Update Causal Belief and Causal Cognition.

## KNOWLEDGE — Data & Concepts

- Base model: DeepSeek-V4-Pro (open-source, reproducibility, strong performance at low cost).
- Baselines: ReAct, OpenCode (open-source harness with over 200,000 GitHub stars).
- Financial research: Uses AlphaBench factor-search task asking agents to construct formulas ranking stocks by predicted next-day returns.
- Two six-period studies: price-and-volume research 2014–2016 and volume-only research 2017–2019.
- 25.4% improvement over baseline agent in mean rank correlation with next-day returns.
- Prediction accuracy improved from 21.3% to 28.6% in dynamic real-world settings.
- Each task starts in fresh context; agents with memory can retrieve earlier findings.

## INSIGHT — Mechanism & Why

[Agents can develop persistent causal understanding] occurs BECAUSE [Causal Cognition organizes knowledge around explanations of how factors influence one another, with conditions, time scales, evidence, and unresolved questions; its graph connects factors through proposed causal relationships]. This means [causal knowledge can be accumulated and reused across tasks, not limited to current context].

[Causal Belief guides decisions better] occurs BECAUSE [structured belief captures causal factors and effects of possible actions, formed from stored knowledge and current evidence]. This means [agents make decisions based on causal understanding, not just surface correlation].

[Causal Scout helps distinguish competing explanations] occurs BECAUSE [the tool compares alternative explanations and suggests observations that can distinguish them]. This means [agents can investigate and verify causal relationships instead of relying on correlation alone].

## IDEA — Actionable Applications

1. Build causal memory for financial analysis agents: Instead of only retrieving past trade summaries, build Causal Cognition containing causal relationships between market factors (price, volume, volatility) and their conditions. First step: create a causal database storing causal hypotheses and supporting evidence from prior analysis sessions.

2. Apply Causal Belief in business decision processes: Before important decisions, the agent should build a structured Causal Belief capturing what influences the outcome and how possible actions could change it. First step: design a Causal Belief template with fields: causal factors, expected impact, supporting evidence, conditions of application.

3. Use Causal Scout for hypothesis testing in scientific research: When multiple explanations exist for a phenomenon, use the tool to compare alternative explanations and suggest observations that can distinguish them. First step: list competing hypotheses, identify the most important observation to test each hypothesis.

## WISDOM — General Principle

- Principle: Intelligent agents not only need to remember experience, but need to form structured causal understanding to apply to new situations — causal knowledge persists beyond individual experiences.
- When to use: When building agents for long-horizon tasks requiring understanding of causality and causation (financial analysis, scientific research, complex decision processes).
- When NOT to use: Simple tasks that only need information retrieval, without needing causal understanding.
- Example outside original domain: In medical diagnosis, doctors not only need to remember symptoms of prior patients, but need to understand causal relationships between risk factors and disease to make appropriate treatment decisions for new patients with different conditions.

## Assumptions & Limitations

- Conditions that must hold: sufficient evidence to test causal relationships; base model has good prior knowledge when evidence is insufficient.
- Paper's acknowledged limitations: When evidence is insufficient to test causal relationships, CauProphet relies more on base model's prior knowledge; experiments cover a limited number of stages; longer studies in changing real-world settings needed.
- Limitations paper does NOT state: effectiveness on tasks without clear causal structure; cost of maintaining Causal Cognition at scale; generalizability across domains beyond finance and science.

## Metadata

- Year: 2026
- Authors: Kaiwen Wu, Chaochao Lu
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.32477
- Citation count: not yet (new paper, Oct 2026)