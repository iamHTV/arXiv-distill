# Skill: Dats — Difficulty-Aware Topology Router (per-problem multi-agent topology selection)
Source: 2609.13890
Type: framework / routing-workflow

## When to use this skill
- A multi-agent system with ≥3 pipeline templates (single call, chain, mesh, hierarchical) and a budget constraint
- You need to fairly compare or deploy cost-aware routers (budget-matched protocol)
- Collaboration benefit varies with problem difficulty — easy problems don't need multi-agent; only hard problems justify paying 5–10× tokens

Do NOT use: only one topology exists; all problems are equally difficult; latency or worst-case cost is the main constraint (the protocol equalises only expected monetary spend).

## Input required
- Problem statements + cached outcomes (pass/fail) for EVERY topology in the catalogue on a representative benchmark (paper: 614 problems × 5 topologies × 4 backbones = 12,280 executions, ~$1,807)
- Cost table c_t (tokens/USD per problem per topology — measure once, reuse; stable within 3% across backbones)
- Budget B as a fraction of always-hierarchical (most expensive fixed topology) cost
- 39-feature extractor: lexical (5), structural (4), complexity (3), difficulty rating (1), TF-IDF SVD (16), algorithmic one-hot (10 categories, keyword vote)

## Steps
1. Cache outcomes: run the full grid (each problem × each topology), record pass/fail + token counts. Do NOT retrain agents — the predictor receives no gradients.
2. Extract the 39 features per problem (feature extraction <1ms/problem, linear in statement length).
3. Train the topology-graph GNN: shared trunk 39→d (affine+ReLU); node init h^0_t = ReLU(W_0[z ∥ e_t] + b_0) with e_t = (agent count, edge count, diameter, mean degree); message passing 2 rounds with tied W_self, W_nbr (mean over neighbors); per-node sigmoid readout. Loss = mean BCE over the 5 heads (targets are per-topology outcomes, NOT a single label). Adam lr 1e-3, early stopping, <30s CPU. 13.7K parameters.
4. Calibrate λ by bisection on a 3-fold split of the training fold: target B as a fraction of always-hierarchical cost, 0.5% tolerance or 60 iterations (paper: λ ≈ 0.052–0.065; 21.4 steps on average). Do NOT tune λ for accuracy — λ is a budget parameter.
5. Inference: predict ŝ_t(x) for the 5 topologies → τ*(x) = argmax_t [ŝ_t(x) − λĉ_t] with ĉ_t = c_t/max c → execute ONLY the selected topology. At λ=0.06, upgrading Single→HRM must buy ≥5.4 points of predicted success.
6. Verify realised spend out of fold (0.4pp tolerance) and print USD/problem + % of reference budget beside accuracy. Compare accuracies only within the matched group; report fixed topologies/oracle separately as frontier locators.

## Expected output
- Per-problem topology assignment + predicted success probabilities (ECE ≈ 0.027, Brier ≈ 0.172, mild under-confidence in the 0.4–0.7 band).
- Budget-matched accuracy: paper 77.69% pass@1 at 40% of always-hierarchical cost ($0.377/problem), +4.07 over always-HRM, +6.03 over direct classification, +9.12 over Random.
- Routing distribution: ~49% Single, ~13% HRM, 38% Chain/mid (suite-dependent: 80% of HumanEval+ → Single; 47% of APPS-Competition → HRM).
- Example: a 5-template coding agent at 40% HRM budget → Dats solves 477/614 vs 452 for always-HRM, saving 60% of spend.

## Example application
- Deploy a coding agent over 2 benchmark levels (easy: HumanEval+-like; hard: competition-like): cache 5 topologies × 100 problems each, train Dats, bisection λ to the 40% budget → easy problems 80% single call, hard graph/DP problems 49% HRM. Switch the budget to 60%: only re-run bisection on λ (NO retraining) — the predict-then-optimize factorisation makes the cost penalty a single recalibratable scalar.

## Gotchas
- Do NOT use direct five-way classification instead of predict-then-optimize (−6.03 points): the label "the topology that solved it" is ambiguous when several topologies succeed (38% of problems) and undefined when none succeed.
- Do NOT use a flat multi-label head (5 independent sigmoids) instead of the topology-graph GNN (−1.66 points): the topologies form a connectivity order — solvability inherits the order almost monotonically; the graph head knows that structure with FEWER parameters (13.7K).
- Do NOT compare routers with a shared λ (a "fair" comparison) — λ multiplies each method's own score scale → realised spend spreads 21.6pp and rankings reverse (RandomForest first under shared λ, Dats first once calibrated, by 3.42 points). Always calibrate and print realised spend.
- Do NOT fine-tune pretrained encoders (CodeBERT/GraphCodeBERT) for the representation — 125M parameters fine-tuned buys +0.49 points, NOT significant (p>0.35, seed SD 0.71). The 39 hand-crafted features suffice.
- Cross-backbone transfer is NOT significant (p=0.318): the routing policy transfers but the probability calibration shifts → recalibrate on a few hundred cached problems when switching backbones.
- LiveCodeBench-style contest problems: stylistically uniform statements defeat surface features (oracle gap of 20 points) — stronger features are needed for the contest regime.
- The protocol equalises expected spend, NOT latency/worst-case/variance — a method that meets the budget by occasionally choosing a very expensive topology is different from one that never does.
- The difficulty × category interaction is where the signal lives: a linear probe loses 3.75 points because it cannot express "hard graph problems need HRM while hard implementation problems do not".
