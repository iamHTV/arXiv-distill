# 2608.15191 — When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control (RAAC)

## Problem
- Reasoning stagnation (tình trạng suy luận đình trệ) ở Deep Research Agent (DRA): majority iterations contribute little/no improvement; agent lack awareness of trajectory (đã thu thập gì, discovery đã saturate chưa) → không adapt search strategy, không biết khi nào terminate. Prior work tập trung component-level (re-ranking, query reformulation, outline stage) — câu hỏi các component phối hợp thế nào trên long trajectory chưa được explore.

## Contribution
- First systematic analysis of DRAs based on intermediate behavior: intermediate recall R_t = |D_g ∩ D_{1:t}|/|D_g| và intermediate accuracy (spawn branch answer tại mỗi turn, không interfere main trajectory); document-type taxonomy (relevant/irrelevant × new/seen).
- 4 unsupervised trajectory signals + Retrieval-Aware Agent Controller (RAAC), agent-agnostic, action space {continue, intervene, stop}.

## Method
- Signals: (1) Criteria Coverage Cov_t = (1/|C|)ΣW(c,t), weight 0.5 partial / 1.0 full / 0 uncovered; (2) Document Novelty Nov_t = |D_t \ D_{1:t-1}|/|D_t|; (3) Successive Query Diversity Div_t = 1 − cos(e_t, e_{t-1}); (4) Original Question Similarity Sim_t = cos(e_t, e_x) — guardrail chống query drift.
- Controller: mỗi iteration tính 4 signals → action. Intervene gọi critical re-thinker (đánh giá why stagnating + generate substantially different creative query, append triplet vào history). Stop → generate final answer.
- Setup: 7 DRAs × 4 architectures (ReAct, GLM-4.7, GPT-oss-20b-high, Tongyi-DR, AgentCPM-Explore, WebWeaver, AgentCPM-Report; ReAct & WebWeaver backbone Claude Sonnet 4.5), 3 datasets (BROWSECOMP-PLUS, NEUCLIR, LEGALSEARCH — closed-source Thomson Reuters), retriever Qwen3-Embedding-4B (k=5), encoder cho signals cũng Qwen3-Embedding-4B; significance t-test (recall) + McNemar (accuracy), p<0.05.

## Key Findings
- Stagnation xác nhận: intermediate recall saturate sau vài iteration đầu trên cả 3 datasets/7 agents; over time agents retrieve fewer NEW docs, increasingly revisit SEEN ones; new relevant docs decline rồi biến mất → stagnation = limited exploration + khó escape local optimum của early relevant evidence.
- Search calls: −14 avg trên BROWSECOMP-PLUS (up to 44: Tongyi-DR 77.8→33.6), −4 NEUCLIR (Tongyi-DR 62.1→34.4, −45%), −5.5 LEGALSEARCH (−58% iterations). WebWeaver+RAAC −33% search calls.
- Accuracy: +up to 10%, +3% avg. Best overall: GLM-4.7+RAAC BrowseComp R 67.2† / Acc 51.3† (base 64.9/47.8); Tongyi-DR+RAAC R 48.4→59.0†, Acc 37.9→47.9†; WebWeaver R 60.9→62.6, Acc 35.7→39.1; CPM-Explore R 40.1→48.0† (#S 29.6→21.7); ReAct R 55.9→59.2†, Acc 32.0→34.9†, #S 50.3→36.8.
- Ngoại lệ CPM-Report: tự terminate quá sớm → RAAC tăng search calls (NeuCLIR 20.6→22.2, LegalSearch 18.2→21.6) và cải thiện显著 (R 44.5→48.7, 31.8→40.8†) — RAAC adaptive cả 2 chiều.
- RAAC overhead ~10% latency của agent reasoning+retrieval; nhỏ hơn 33% reduction search calls.
- Ablation: Cov giúp trên BROWSECOMP-PLUS (có human criteria) nhưng hại trên NEUCLIR/LEGALSEARCH (LLM-generated criteria chỉ useful khi không có human criteria); Nov là primary signal hiệu quả nhất (bỏ Nov → recall giảm). AUROC vs New-item Recall: Nov 0.81/0.74/0.71 (3 datasets), Cov 0.71/0.71/0.74, Div 0.64/0.52/0.46.
- Action analysis: Has-Stop group win 35% vs loss 18% (BrowseComp), 30% vs 15% (NeuCLIR), 41% vs 15% (LegalSearch); Intervene-Only 33% vs 18%, 30% vs 18%, 40% vs 24% — cả 2 action đều effective, stop không premature.

## Actionable Insights
- Monitor document novelty (fraction new docs per iteration) như early-warning stagnation — signal cao nhất correlation với productive iteration (AUROC 0.81); novelty ≈ 0 nghĩa là agent đang lặp, nên intervene hoặc stop.
- Critical re-thinker pattern: khi trajectory stale nhưng recoverable, inject 1 external nudge (đánh giá why stagnating + creative different query) thay vì để agent tự lặp — intervention win gấp ~2× loss.
- Coverage signal chỉ dùng khi có human-defined criteria; nếu criteria do LLM generate, bỏ Cov (hại trên 2/3 datasets) — đừng giả định multi-signal luôn tốt hơn.

## Assumptions & Limitations
- Prompt-based controller: hand-crafted prompt map signals → 3 discrete actions, fixed weights cho mọi query (không adaptive per-query); learned controller có thể better.
- Signals chưa toàn diện: chưa dùng document content, retrieval confidence, inter-document redundancy.
- Action set chỉ cover 2 failure modes (không stop đúng điểm + bị trap narrow search space); DRA evolve nhanh, failure mode mới có thể xuất hiện.
- LEGALSEARCH closed-source (Thomson Reuters); criteria cho NEUCLIR/LEGALSEARCH do LLM generate (không human-verified như BrowseComp).

## Metadata
- 2026 (2026-08-15), Heydar Soudani (Radboud University / Thomson Reuters Labs), Elizabeth Lingg, Faegheh Hasibi (Radboud), Navid Rekabsaz (Thomson Reuters Labs), cs.IR, https://arxiv.org/pdf/2608.15191
