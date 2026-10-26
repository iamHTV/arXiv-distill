# 2610.31709 — Mining the Design Space of Multi-Agent Workflows

## Core Value (1 sentence)

Designing multi-agent LLM workflows should not start with Star fan-out (independent workers solving then one-shot aggregation), but should use SharedMemory (persistent shared document) instead of Debate (multi-round conversation), and write specific prompt templates with named placeholders — gains comparable to choosing communication structure.

## Problem

Designing LLM-based multi-agent systems (MAS) still relies on trial and error and informal "folk wisdom." Manual studies test only a few fixed communication structures (topologies), while automated optimizers discard intermediate search trajectories after selecting a task-specific workflow — losing the intermediate comparisons needed to explain why one design succeeds and another fails.

## Contribution

1. A two-phase pipeline to mine reproducible multi-agent workflow design principles from workflow code and execution traces.
2. Repurposes AFlow's MCTS optimizer across 6 composable operators and 26 deterministically verified Enigmata tasks, retaining all intermediate rounds to build a corpus of 28,568 executable workflows.
3. A sandboxed AutoResearch loop mines orchestration code and prompt templates under an L0-penalized validation objective, then tests candidate principles on held-out searches.
4. Extracts 3 design principles at 3 granularities: Star-first hurts accuracy, SharedMemory outperforms Debate, and prompt specificity has gains comparable to communication-structure selection.

## Method

Two-phase pipeline:

**Phase 1 (Sampling):** Repurposes AFlow MCTS to search workflows over N = 20 rounds, K = 5 independent runs per condition. Each workflow W is represented as an executable Python class in graph.py accompanied by hard text prompt templates in prompt.py (no soft prompts or gradient updates). Samples parents from top-k (k = 4) evaluated workflows using a mixed uniform/softmax distribution (λ = 0.2 uniform weight, temperature α = 0.4).

**Phase 2 (Analysis):** Uses AutoResearch in a sandbox to mine features from graph.py and prompt.py, fits a regressor from features φ(W) and task descriptors ψ(T) to score m, scores candidates on held-out validation via objective F = R² − λ||φ||₀ (penalizing active feature count).

## KNOWLEDGE — Data & Concepts

- Corpus: 28,568 executable workflows across 26 Enigmata tasks (deterministically verified reasoning tasks), 1,701 completed MCTS search traces out of 1,740 grid cells.
- 6 operators: Sequential (47.2%), Star (44.5%), Debate (22.3%), SharedMemory (20.8%), DebateWithModerator (11.8%), StarWithCoordinator (8.8%).
- R² graph.py-only = 0.521; jointly mining prompt.py lifts R² to 0.638 (27 features).
- Cost: ~$0.0064 per task instance, ~$4,454 total compute.
- Model backbones: GPT-5.4 as MCTS optimizer; {GPT-5.4-mini, GPT-5.4-nano} as worker and aggregator.

## INSIGHT — Mechanism & Why

[Star-first hurts accuracy] occurs BECAUSE [independent workers without lateral communication propagate errors, and the aggregator must reconcile without peer verification]. This means [independent fan-out at entry increases error without error-correction between branches].

[SharedMemory outperforms Debate] occurs BECAUSE [persistent state in a shared document (blackboard) avoids information loss compared to multi-round conversational dialogue]. This means [agents writing sequentially to one shared document retain context better than each agent reading all peer proposals then revising].

[Prompt specificity and placeholder-based context routing matter as much as communication-structure selection] occurs BECAUSE [sub-topological structure in prompt.py explains additional workflow variance that macro-topology in graph.py alone cannot capture (R² rises from 0.521 to 0.638)].

## IDEA — Actionable Applications

1. Don't start multi-agent workflows with Star fan-out: Instead of having agents work independently then aggregating once, start with Sequential (sequential agents) or SharedMemory. First step: design entry point as a sequential coordinator rather than independent fanning-out to multiple workers.

2. Use SharedMemory instead of Debate for complex reasoning tasks: Instead of having agents read all peer proposals then revise over multiple rounds, create a persistent shared document (blackboard) that agents read and append to sequentially. First step: build a shared document that agents update sequentially rather than multi-round chat.

3. Write specific prompt templates with named placeholders: Instead of generic prompts, write detailed prompt templates with named placeholders like {problem}, {worker_outputs} to route context. First step: review current prompt templates, add named placeholders and higher specificity for each agent role.

## WISDOM — General Principle

- Principle: Multi-agent workflow design should start with persistent shared state, not independent fan-out; prompt structure matters as much as communication structure.
- When to use: When building multi-agent systems for complex reasoning tasks requiring coordination between agents.
- When NOT to use: Simple tasks that don't require coordination (single-agent suffices).
- Example outside original domain: In a content team, working on a shared Google Doc (shared memory) is more effective than each member writing separate drafts then the lead merging once.

## Assumptions & Limitations

- Conditions that must hold: deterministically verified reasoning tasks without external tools (tool-free); single model family (GPT-5.4 as optimizer, mini/nano as workers).
- Paper's acknowledged limitations: focuses on abstract reasoning tasks from Enigmata, single model family, controlled setup removes grading noise and API variance but limits real-world applicability.
- Limitations paper does NOT state: effectiveness on tool-using tasks, real-world tasks beyond abstract reasoning, cost of human evaluation at scale.

## Metadata

- Year: 2026
- Authors: Xavier Cadet, Junyan Cheng, Peter Chin, Kyle Richardson
- arXiv category: cs.SE
- PDF link: https://arxiv.org/pdf/2610.31709
- Citation count: not yet (new paper, Oct 2026)