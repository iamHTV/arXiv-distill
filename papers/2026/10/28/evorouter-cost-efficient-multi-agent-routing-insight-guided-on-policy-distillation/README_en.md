# [2610.35690] EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation

## Problem
- Current LLM routers (components selecting models/configurations for queries) optimize either single-model choice or MAS (multi-agent system) configuration piecemeal. Prior work has not solved joint configuration (model assignment, collaboration mode, agent count, interaction rounds, skills/subtasks) because: (i) the configuration space explodes combinatorially, making exhaustive evaluation infeasible, and a single execution trajectory reveals only the outcome under one specific configuration — insufficient evidence to tell which planning decisions are necessary, redundant, or suboptimal; (ii) RL (reinforcement learning) reward signals come only from final success and cost — sparse feedback that cannot indicate which coupled planning decisions were effective or wasteful.

## Contribution
- Insight-guided self-improvement loop: an LLM-based expert periodically synthesizes performance–cost feedback from trajectories across tasks into reusable conditional routing insights about capability requirements, returns from resource scaling, and interactions among configuration choices.
- Insight-conditioned on-policy distillation (OPD): a privileged teacher combines evolving insights with current execution feedback to provide dense token-level supervision on the student router's own planning trajectories.
- Cost-aware RL: reward R(τ)=R_perf−λ_C·R_cost with R_cost = log2(1+C(τ)/B(q)) normalized against a per-task reference budget; joint loss L_θ = L_RL + λ_D·L_OPD + β·L_KL (KL penalty against policy drift).
- Three foundational empirical insights: (1) Where to scale — scaling benefits are task-dependent (switching mβ+IO→mα+FullConnected: Multimodal +13.1pp but QA −5.0pp); (2) How much — returns are non-monotonic in rounds/agent counts with configuration-dependent saturation points; (3) What to combine — model-composition rankings reverse across collaboration modes (all-mβ wins under FullConnected; all-mα wins under Debate while cutting MAS FLOPs 79.8%).

## Method (core summary)
- Router emits a structured configuration plan P = {c, r, {(u_j, m_j, s_j, p_j)}} in a <plan> tag (after reasoning in <analysis>); a deterministic executor instantiates the MAS; outcomes return as observations; the router answers in <answer>, forming a two-stage trajectory.
- Stage 1: SFT (supervised fine-tuning) cold-start on demonstration trajectories filtered for valid format and correct answers; prompt contexts and environment feedback are masked; yields a frozen reference policy π_ref.
- Stage 2 evolution loop: sample G rollouts per task with group-relative advantages (GRPO-style); the insight distillation expert F updates in three steps: (i) rule induction — comparing intra-category trajectories across success/failure and cost spectra, (ii) precondition refinement — resolving conflicts by tightening boundaries (task difficulty, domain), (iii) capacity pruning — merging redundant rules under a capacity ceiling to curb context inflation. I_{k+1}=F(I_k,B_k).
- OPD: a frozen teacher receives privileged information z=(I, P_i, o_i, s(τ_i)) — insight pool, plan, outcome, verifier score — sharing context/prefix with the student; loss DKL(p^S || sg(p^T)) weighted by an insight reward. Deployment needs no privileged feedback at inference.

## Key Findings
- 21 datasets (19 in-domain across 5 domains: math MATH/GSM8K/OmniMATH-2/Apex, commonsense ARC-Challenge/StrategyQA/SocialIQA, knowledge MMLU-Pro/GPQA-Diamond/SuperGPQA, retrieval NQ/TriviaQA/HotpotQA/2WikiMultiHopQA/PopQA/MuSiQue, multimodal ChartQAPro/MMMU/MMMU-Pro) + 2 out-of-domain (code LiveCodeBench, reasoning BBH-LD). LLM pool: Qwen3.5-35B-A3B/122B-A10B/397B-A17B, DeepSeek-V4-Flash, GLM-5; modes: IO, CoT, Reflection, Chain, FullConnected, Debate.
- In-domain average accuracy: EvoRouter-4B 68.69%, EvoRouter-8B 71.23%; out-of-domain sample-weighted 74.67–78.93%, surpassing the strongest baseline by 7.74–12.00 percentage points (pp).
- EvoRouter-4B: +7.23pp accuracy over strongest baseline RCR-Router while cutting mean MAS cost 50.95% (to 15.28k FLOPs units); total inference including router overhead 18.94k units — 76.5% below MasRouter, 39.2% below RCR-Router.
- Ablations (Table 3, EvoRouter-4B): full 68.69%/74.67% (in/out) at cost 15280.79/25952.47; w/o Insights 64.54/70.93; w/o OPD 63.23/69.87; w/o RL+OPD 59.77/63.20; w/o SFT+RL+OPD 53.23/52.80 at cost 25472/19795. OPD without Insights gives only +1.31/+1.06pp over RL, while insight-guided OPD reaches +5.46/+4.80pp — insights are the core value-add.
- Evolution dynamics (LLaMa-8B): early updates +2.62pp success with −16.4% compute; later +1.35pp with −7.4% cost.
- Sensitivity λ_C∈{0,0.025,0.05,0.1,0.2}: higher λ_C steers the policy to lower-cost configurations, shifting the per-question compute distribution toward low-budget regimes and suppressing the expensive upper tail — predictable workload expenditure.
- Unseen-resource generalization: +3.85pp in-domain / +7.47pp out-of-domain vs MasRouter with MAS compute −6.7%/−18.5%; beats the strongest out-of-domain baseline by 5.9pp with <½ its compute.

## Actionable Insights
1. MAS configuration is a JOINT decision — do not optimize components separately: model-composition effectiveness reverses across collaboration modes. Example: before locking a content-agent pipeline, A/B test 2–3 configurations (small model + Debate vs large model + FullConnected) on the same 20 tasks, measuring both accuracy and FLOPs/cost — pick the winner per task type, not the intuition "bigger model is always better".
2. Default a rounds/agents cap, then expand on verifier failure: scaling has configuration-dependent saturation points (Insight 2). Example: a QA agent uses max 3 rounds; only allow round 4 when the verifier fails, and log per-round success rate to find your workflow's own saturation point.
3. Distill conditional insights, not isolated outcomes: weekly, an LLM expert reviews execution logs to induce rules of the form "IF task_type=X AND difficulty=high THEN model=mβ+FullConnected", each rule carrying applicability conditions; merge duplicates, keep a ~20-rule ceiling. Example: from 100 support tickets, derive "refund request → Debate with 2 small agents" instead of "always use the big model".

## Assumptions & Limitations
- Conditions for the method to work: a deterministic executor that parses configuration plans; reliable per-task verifiers (code sandbox tests, QA exact match); a strong frozen teacher and bootstrap router available for training; cost measured in relative FLOPs units (Appendix B).
- Paper-stated: framework designed for cloud-based agent services; edge environments (resource-constrained, device heterogeneity, inter-agent communication overhead) left to future work.
- Not stated but observed: Table 2 per-cell extraction from the PDF was mangled — only prose-verified figures plus the clean Table 3 were used; FLOPs cost ≠ real API dollars (model prices differ); training cost (teacher + bootstrap + RL) is excluded from the 50.95% inference-saving figure; insight quality depends on the expert LLM — a new failure surface; unseen-resource generalization was tested in only one setup.

## Metadata
- Year: 2026 (Oct 26, 2026). Authors: Yitao Xiao, Shaoyong Guo (BUPT), Sitao Xie (Fudan), Xu Zhang, Yan Sun, Ye Cheng, Ziyue Zhu (BUPT), Guo Tong, Haoran Luo (NTU). Categories: cs.AI, cs.MA. Link: https://arxiv.org/abs/2610.35690. Code: https://github.com/CenYangtze/EvoRouter. Citation count: [NOT FOUND — API rate-limited].
