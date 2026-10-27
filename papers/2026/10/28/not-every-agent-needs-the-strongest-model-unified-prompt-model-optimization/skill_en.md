# Skill: unimaso-prompt-model-optimization
Source: 2610.31743v2
Type: optimization-method

## When to use this skill
- You have a multi-agent LLM system with different roles and want to optimize quality–cost trade-off.
- Want to assign models appropriate to each role's requirements instead of using the strongest model for every agent.
- Want to jointly optimize prompts and model assignments instead of optimizing prompts with fixed models.

## When NOT to use this skill
- The system has only a single agent.
- All agents have the same capability requirements (no need to differentiate models).

## Required inputs
- Multi-agent system as directed graph G = (V, E) with execution topology.
- Prompt space Pi for each agent vi and homogeneous model pool M = {m(1), ..., m(K)}.
- Validation dataset D = {(xj, yj)} for task quality evaluation.
- Model cost coefficients from provider pricing reference.

## Steps to perform
1. Model the N-agent system as directed graph: each agent vi has prompt pi ∈ Pi and model mi ∈ M, assignment zi = (pi, mi).
2. Generate candidates from execution traces: sample traces with inputs, contexts, outputs, feedback; propose candidates from current configuration.
3. Evaluate candidates at three granularities: local validity, lookahead utility, global alignment. Utility: Ui(p') = α·qloc_i(p') + β·qlook_i(p') + γ·qglob_i(p'), α + β + γ = 1.
4. Apply cost-aware beam search: expand candidate when Ui(p')·ηi(p')−λ > uref (λ = 0.2, uref = 0.5). Retain non-dominated quality–cost candidates.
5. Extend candidates to prompt–model pairs z'i = (p'i, m'i). Find best local update ¯zi = (¯pi, ¯mi).
6. Coordinate system by topology: create focal view for each logical agent, measure empirical support weighted by proposal concentration: Ai(m) = πi(m)(1 − H̄i). Solve configuration-level decision subject to feasibility and capability–cost balance.
7. Store optimization trajectory: ξt = (zt, at, qt, Ct, bt). Group into low-cost global successes, local successes–global failures, high-cost global successes. Category-balanced retrieval (Kmem = 2 per category).
8. Run 3 optimization rounds with search depths 3–2–2; evaluate selected configuration on full evaluation set.

## Expected output
- Optimal prompt–model configuration for each agent in the system.
- Task quality score and deployment cost (token-weighted).
- Model distribution by role (e.g., Qwen3.5-9B for structured/summarization, DeepSeek-V4-Flash for reasoning/verification).

## Example application
A company has a multi-agent customer support system with roles: Planner, Reasoner, Reviewer, Aggregator. Currently all agents use DeepSeek-V4-Pro (high cost). Apply UniMASO: jointly optimize prompts and model assignments. Result: Planner uses Qwen3.5-9B (43.5% structured/summarization), Reasoner uses DeepSeek-V4-Flash (45.5% reasoning/verification). Average score 70.40 (+0.61), cost reduced 85.2% (30.92M vs 208.28M).

## Gotchas
- Joint prompt–model optimization is more complex than sequential optimization (prompt first, model after).
- Need validation dataset to evaluate task quality.
- Meta-optimization cost can be significant — need to balance with deployment cost.
- Results depend on available model pool and execution topology.
- Trajectory memory needs proper storage and retrieval to reuse experience.