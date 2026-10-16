# 2608.15191 — When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control (RAAC)

## Problem
- Reasoning stagnation in Deep Research Agents (DRAs): the majority of iterations contribute little or no improvement to final performance, and agents lack awareness of their trajectories (what has been collected, whether information discovery has saturated), so they cannot adapt search strategies or determine when to terminate. Prior work focused on component-level improvements (re-ranking, query reformulation, extra outline/report stages); how components interact over long trajectories was unexplored.

## Contribution
- First systematic analysis of DRAs based on intermediate behavior: intermediate recall R_t = |D_g ∩ D_{1:t}|/|D_g| and intermediate accuracy (spawning a branch answer at each turn without interfering with the main trajectory); a 4-type document taxonomy (relevant/irrelevant × new/seen).
- Four unsupervised trajectory signals + a Retrieval-Aware Agent Controller (RAAC), agent-agnostic, with action space {continue, intervene, stop}.

## Method
- Signals: (1) Criteria Coverage Cov_t = (1/|C|)ΣW(c,t), weights 0.5 partial / 1.0 full / 0 uncovered; (2) Document Novelty Nov_t = |D_t \ D_{1:t-1}|/|D_t|; (3) Successive Query Diversity Div_t = 1 − cos(e_t, e_{t-1}); (4) Original Question Similarity Sim_t = cos(e_t, e_x) — a guardrail against query drift.
- Controller: at each iteration it computes the four signals and picks an action. Intervene invokes a critical re-thinker (assesses why the trajectory is stagnating + generates a substantially different, potentially creative query; the triplet is appended to history). Stop triggers final answer generation.
- Setup: 7 DRAs × 4 architectures (ReAct, GLM-4.7, GPT-oss-20b-high, Tongyi-DR, AgentCPM-Explore, WebWeaver, AgentCPM-Report; ReAct and WebWeaver use Claude Sonnet 4.5 backbone), 3 datasets (BROWSECOMP-PLUS, NEUCLIR, LEGALSEARCH — closed-source, Thomson Reuters), retriever Qwen3-Embedding-4B (k=5); the same encoder for signals; significance via t-test (recall) and McNemar test (accuracy), p<0.05.

## Key Findings
- Stagnation confirmed: intermediate recall saturates after the first few iterations across all datasets and agents; over time agents retrieve fewer NEW documents and increasingly revisit SEEN ones; new relevant documents decline and eventually disappear — stagnation stems from limited exploration and difficulty escaping the local optimum defined by early relevant evidence.
- Search calls: −14 on average on BROWSECOMP-PLUS (up to 44: Tongyi-DR 77.8→33.6), −4 on NEUCLIR (Tongyi-DR 62.1→34.4, −45%), −5.5 on LEGALSEARCH (−58% of iterations). WebWeaver+RAAC −33% search calls.
- Accuracy: +up to 10%, +3% average. Best overall: GLM-4.7+RAAC BrowseComp recall 67.2† / accuracy 51.3† (base 64.9/47.8); Tongyi-DR+RAAC recall 48.4→59.0†, accuracy 37.9→47.9†; WebWeaver 60.9→62.6 / 35.7→39.1; CPM-Explore 40.1→48.0† (#S 29.6→21.7); ReAct 55.9→59.2† / 32.0→34.9†, #S 50.3→36.8.
- Exception CPM-Report: it inherently terminates too early, so RAAC INCREASES its search calls (NEuCLIR 20.6→22.2, LEGALSEARCH 18.2→21.6) with significant gains (recall 44.5→48.7, 31.8→40.8†) — RAAC adapts in both directions.
- RAAC overhead ≈10% of the agent's reasoning+retrieval latency, small vs the average 33% reduction in search calls.
- Ablation: Criteria Coverage helps on BROWSECOMP-PLUS (human-provided criteria) but hurts on NEUCLIR/LEGALSEARCH (LLM-generated criteria are useful only when human criteria are unavailable); Document Novelty is the most effective primary signal (removing it reduces recall). AUROC vs New-item Recall: Nov 0.81/0.74/0.71 across the three datasets, Cov 0.71/0.71/0.74, Div 0.64/0.52/0.46.
- Action analysis: Has-Stop group win 35% vs loss 18% (BrowseComp), 30% vs 15% (NEuCLIR), 41% vs 15% (LEGALSEARCH); Intervene-Only 33% vs 18%, 30% vs 18%, 40% vs 24% — both actions are effective; stopping does not prematurely terminate productive iterations.

## Actionable Insights
- Monitor document novelty (fraction of new documents per iteration) as an early-warning stagnation signal — it has the highest correlation with productive iterations (AUROC 0.81); novelty ≈ 0 means the agent is looping, so intervene or stop.
- Critical re-thinker pattern: when a trajectory is stale but recoverable, inject one external nudge (assess why it is stagnating + a creative, different query) instead of letting the agent loop — intervention wins ~2× more often than it loses.
- Use a coverage signal only when human-defined criteria exist; if criteria are LLM-generated, drop Cov (it hurt on 2 of 3 datasets) — don't assume multi-signal is always better.

## Assumptions & Limitations
- Prompt-based controller: a hand-crafted prompt maps signals to 3 discrete actions with fixed weights across queries (not per-query adaptive); a learned controller could do better.
- Signal comprehensiveness: document content, retrieval confidence, and inter-document redundancy are not used.
- Action set covers only the two observed failure modes (failing to stop at the optimal point; trapped in a narrow search space); DRAs evolve fast and new failure modes may appear.
- LEGALSEARCH is closed-source (Thomson Reuters); criteria for NEUCLIR/LEGALSEARCH are LLM-generated (not human-verified like BrowseComp's).

## Metadata
- 2026 (2026-08-15), Heydar Soudani (Radboud University / Thomson Reuters Labs), Elizabeth Lingg, Faegheh Hasibi (Radboud University), Navid Rekabsaz (Thomson Reuters Labs), cs.IR, https://arxiv.org/pdf/2608.15191
