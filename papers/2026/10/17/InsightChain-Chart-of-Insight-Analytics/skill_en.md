# Skill: insightchain-four-stage-visualization
Source: 2609.06438v1
Type: framework

## When to use this skill
- Building LLM-driven data visualization systems for open-ended insight discovery.
- Data is a single tabular dataset without a predefined analytical question or visualization intent.
- Need to evaluate both the analytical trajectory and the final visualization, not just final output metrics.

## When NOT to use this skill
- Visualization queries with a user-specified intent already available.
- No need to evaluate intermediate analytical process.
- No sandbox available to execute Python code safely.

## Input needed
- Single tabular dataset D with column names, dtypes, summary statistics, and a five-row sample.
- LLM capable of generating Python code (DSPy chain-of-thought module).
- Sandboxed executor to run Python code safely.
- LLM-as-judge to score five quality dimensions (EXPLORATION BREADTH, FOCUS RELEVANCE, HYPOTHESIS RIGOR, INSIGHT COMMUNICATION, VISUAL QUALITY).

## Steps to execute
1. Build a four-stage pipeline (Explore–Focus–Test–Present) emulating expert analytical workflows.
2. At each stage, the predictor produces structured output containing executable Python code.
3. Execute the Python code in a sandboxed executor with retry budget B = 2; if there is an error, feed the error trace back to the predictor for regeneration (self-correcting execution loop).
4. Collect records of each completed stage into running context C<t; condition downstream stages on prior outputs and execution traces.
5. Evaluate using Insight Progression Metric (IPM): sum over d in D of wd · ϕd(c), with five dimensions (EXPLORATION BREADTH 0.20, FOCUS RELEVANCE 0.25, HYPOTHESIS RIGOR 0.20, INSIGHT COMMUNICATION 0.25, VISUAL QUALITY 0.10), ϕd ∈ [1, 10] scored by LLM-as-judge.
6. Optimize per-stage prompts using VG-COPRO: COPRO outer loop for per-predictor optimization, OPRO proposer for inner loop, plus three modifications: per-dimension diagnostic critique, leave-one-domain-out (LODO) objective, vision-aware compile signal.

## Expected output
- Visualization pipeline outperforming single-shot baselines (Single-shot 4-prompt and LIDA) across task models (Gemini 3 Flash, GPT-4.1).
- VG-COPRO improves IPM in both in-domain and cross-domain settings: Gemini 3 Flash IPM 7.24 → 8.56 (+1.31); GPT-4.1 IPM 7.90 → 8.54 (+1.16).

## Application example
- Sales data analysis system: given a transaction table, the pipeline explores sales distributions (Explore), focuses on hypothesis about best-selling products (Focus), tests hypothesis with statistical validation (Test), and communicates findings in a final figure (Present).

## Gotchas
- IPM construct validity: full five-dimensional human ratings limited to the 100-chain pilot.
- 91.9% of datasets from real public sources, with small synthetic-template fallback for underrepresented domains.
- Existing APO methods fail to yield consistent gains; only VG-COPRO improves performance consistently.
