# Skill: Replace backbone with diffusion for deep research (DiffResearch 3 stages)
Source: 2610.28909
Type: framework

## When to use this skill
- A deep research / long-report writing system currently uses autoregressive LLMs and is slow in planning and writing stages.
- Need to reduce end-to-end latency without changing the agent scaffold, retrieval code, prompts, or evaluation.
- Do NOT use when the main problem is source accuracy, or when the final output must be exactly correct word-by-word.

## Input needed
- Existing agent scaffold (intent classification, query reformulation, planning, retrieval, writing).
- A diffusion LLM runnable via Hugging Face runtime (e.g. diffusiongemma, LLaDA, Dream, Mercury).
- A comparable AR model to use as baseline.
- An evaluation benchmark and scoring rubric (e.g. RACE).

## Steps
1. Keep the agent scaffold, retrieval code, prompts, and evaluation unchanged; only swap the text-generation backbone between diffusion LLM and AR model for a controlled comparison.
2. Implement the 5 core stages: intent classification, query reformulation, planning, retrieval (using Semantic Scholar / Serper API, deterministic, no LLM in the loop), and writing; add optional judging.
3. Run full mode (dFull): diffusion generates the full report to completion, parse JSON, evaluate RACE.
4. Run fast decomposition mode (dFast): read intermediate denoising states of the diffusion model, extract the subquery list early when a valid JSON object appears, dispatch retrieval before generation finishes.
5. Measure latency and RACE quality for all three configurations (dFull, dFast, AR), compare on the same task set.

## Expected output
- Deep research system on diffusion backbone runs roughly 6× faster end-to-end than AR, with RACE quality unchanged (dFast 0.3969 vs AR 0.3904 on 0–1 scale).
- dFast provides 1.99× median speedup for the query decomposition step without losing report quality.

## Example application
- An internal research report writing agent using 3 search tools: replace the AR backbone with a diffusion LLM, keep the 5 stages, measure latency on 100 tasks → reduce from ~71s to ~12s end-to-end, RACE stays the same.

## Gotchas
- Must measure on similar hardware (H200 pod) and the same retrieval backend for results to be comparable.
- dFast does not help reduce end-to-end latency if retrieval is rate-limited and decomposition is only a small fraction of total time.
- Only one backbone pair was tested, not a broad sweep across model families and sizes.
- Source-grounded audit showed only 28% of claims fully supported — reducing latency does not solve retrieval quality problems.