# 2609.30541 — AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework

## Problem
- Karpathy's AutoResearch (an LLM that edits a training script and keeps changes improving a held-out metric) was only tested on single-GPU, 5-minute runs with one scalar metric. Prior work never answered: does the paradigm survive when iterations cost hours of multi-GPU compute, evaluation is multi-criteria, and campaigns exceed a single context window?

## Contribution
- Taxonomy of 5 production-scale failure modes: infrastructure fragility, agent memory decay, search-direction stagnation, iteration-cost asymmetry, metric fixation
- A three-principle scaffold (prevent–persist–redirect) instantiated as a 3-agent extension (Researcher, Code Fixer, Criticizer)
- A cost-dependence principle: the weight on each principle should scale with iteration cost

## Method
- System A: 128-dim purchase-optimized retrieval embeddings for 98% of the book catalog, multi-GPU, 9–19h iterations, agent rewrites the entire train.py, 60+ iterations across 6 runs. System B: hierarchical Semantic IDs via RQ-VAE for generative retrieval, 1 GPU, 6–52 min iterations, agent edits hyperparameters/architecture, 150+ iterations across 15 runs. Per-iteration cost differs ~760×.
- Code Fixer (claude-opus-4-6) rewrites the proposed script pre-execution, catching semantic bugs (GPU underutilization, DDP misconfiguration, OOM precursors). Criticizer (Opus) fires only on stagnation (relative-gain threshold 8%, window of 5 iterations) and emits a 2–5 sentence strategic directive, cleared on next Keep. program.md persists to S3 cross-job storage. Context: sliding window with recent iteration summaries verbatim; best train.py always in full.

## Key Findings
- 220+ experiments over 12 weeks. System A peak 6.90% Recall@6 (iter-12) = 1.82× over hand-tuned baseline 3.79%, 2.45× over deployed baseline 2.82%; across-date mean still 1.63×. System B weighted coherence 0.735 = 2.1× over baseline 0.348 (random 0.26).
- Code Fixer caught 14 latent bugs on first deployment (3 DDP/multi-GPU, 4 OOM precursors, 3 recomputation, 2 dataloader/sampler, 2 eval-loop); the DDP wrapper bug alone would have wasted 10+ hours on an 8-GPU job.
- Criticizer directive "input representation problem" drove 5.48%→5.98% in 3 iterations. Agent autonomously designed a text-only fallback: 5.8× catalog coverage scale-up.

## Actionable Insights
- Gate expensive actions pre-execution: a semantic review step before running costly jobs catches one DDP bug = tens of GPU-hours saved — for any automation workflow, validate the plan before executing anything expensive.
- Intervene only on stagnation: a critic firing every iteration creates noise; firing on plateau (8%/5 iterations) produces paradigm shifts — apply to content pipelines: trigger strategic review only when KPIs flatline for 5 cycles.
- Failure memory must be durable: log negative results to cross-job storage from day one — the agent still re-tested 100-epoch training 6 times despite explicit prohibition in program.md.

## Assumptions & Limitations
- Observational ablation (natural campaign transitions, no controlled A/B); single domain (book recommendation), single organization.
- Offline metrics (Recall@6, weighted coherence) not validated against customer outcomes; online pilots underway.
- Not stated: Criticizer thresholds (8%, 5) chosen empirically — may fail in other domains; metric fixation is NOT solved (the agent never questions the metric).

## Metadata
- 2026, Aparajith Chandran, Juwon Kim, Saurav Jha, Pablo Castells, Florian Hottier (Amazon Books Core Recs Science), cs.LG/cs.IR, ICDM 2026, https://arxiv.org/pdf/2609.30541
