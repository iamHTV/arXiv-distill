# Skill: RAAC — Retrieval-Aware Agent Controller (chống stagnation DRA)
Source: 2608.15191
Type: evaluation-method / control-loop framework

## Khi nào dùng skill này
- Deep research / RAG agent chạy nhiều iteration search mà recall đã saturate — nghi ngờ "reasoning stagnation" (agent lặp, không biết dừng)
- Cần giảm search calls/cost mà không giảm (hoặc muốn cải thiện) recall/accuracy
- Agent là black-box hoặc bất kỳ architecture nào (RAAC agent-agnostic, hoạt động ngoài policy của agent)

Tình huống KHÔNG nên dùng: trajectory ngắn (1–3 search) — overhead controller (~10% latency) không đáng; query đơn giản factoid không cần multi-hop; không có criteria nào (human hoặc LLM-generate) để tính coverage.

## Input cần có
- Trajectory agent: history H_t = (thought, action/query, observation/docs) mỗi turn; top-k docs mỗi search (paper dùng k=5)
- Encoder cho embeddings (paper dùng Qwen3-Embedding-4B)
- Criteria list C cho query (human-provided như BROWSECOMP-PLUS, hoặc LLM-generate — nhưng chỉ dùng signal Cov khi có human criteria)
- Một LLM cho critical re-thinker + controller (paper dùng Claude Sonnet 4.5)

## Các bước thực hiện
1. Cuối mỗi iteration t, tính 4 signals: Nov_t = |D_t \ D_{1:t-1}|/|D_t| (fraction docs chưa từng thấy); Cov_t = (1/|C|)ΣW(c,t) với W = 1.0 fully covered / 0.5 partial / 0 uncovered; Div_t = 1 − cos(e_t, e_{t−1}) (query kế nhau khác nhau bao nhiêu); Sim_t = cos(e_t, e_x) (query còn gần topic gốc không — guardrail).
2. Controller (prompt-based) map signals → action ∈ {continue, intervene, stop}. Rule of thumb từ paper: Nov ≈ 0 nhiều iteration liên tiếp + Cov cao → stop; Nov ≈ 0 nhưng Cov thấp + Div thấp (query lặp) → intervene; Sim giảm mạnh → intervene (đang drift).
3. Intervene: gọi critical re-thinker với H_t → output (critical reasoning thought τ' + substantially different creative query q'); retrieve docs D'; append triplet (τ', q', D') vào history — KHÔNG restart trajectory.
4. Stop: generate intermediate/final answer từ H_t (same spawn-answer pattern: τ'_T, r_T ~ π(·|f(H_t))).
5. Track win/tie/loss theo gold docs: win = RAAC retrieves more gold docs; target win ≈ 2× loss (paper: 33–41% win vs 15–18% loss). Nếu loss > win → kiểm lại threshold signal.
6. (Optional) Ablation check: nếu không có human criteria, chạy KHÔNG có Cov (paper: Cov hại trên NEUCLIR/LEGALSEARCH khi criteria do LLM generate).

## Output mong đợi
- Search calls giảm ~14 avg (paper: up to 44, −33% to −58% tùy agent/dataset) với recall/accuracy tăng hoặc持平 (accuracy +up to 10%, +3% avg); overhead controller ~10% latency agent.

## Ví dụ áp dụng
- BrowseComp-Plus query: agent gốc trả lời iteration 23 nhưng answer đã có từ iteration 8. RAAC: intervene sớm → relevant doc iteration 4 → stop iteration 8. Tongyi-DR: 77.8→33.6 search calls (−44) với recall 48.4→59.0.

## Gotchas
- Nov là primary signal quan trọng nhất (AUROC 0.81 vs New-item Recall) — đừng bỏ; Div correlation thấp nhất (0.46–0.64), không dựa vào Div một mình.
- Cov chỉ dùng với human criteria; LLM-generated criteria làm Cov hại performance trên 2/3 datasets.
- Controller prompt-based fixed weights — không adaptive per query; với domain đặc thù, tune threshold hoặc học learned controller (future work của paper).
- Dùng Sim làm guardrail: novelty cao mà Sim thấp = đang drift off-topic, đừng reward novelty đơn thuần.
- CPM-Report-style agent (terminate quá sớm) cần ngược lại: RAAC sẽ TĂNG search calls — đừng hiểu nhầm tăng calls là lỗi.
- Overhead ~10% latency chỉ đúng khi controller output ngắn; nếu critical re-thinker output dài, overhead tăng.
