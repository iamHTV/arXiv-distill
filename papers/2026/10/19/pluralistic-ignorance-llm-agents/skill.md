# Skill: Pluralistic Ignorance Simulation Protocol (PI-Sim)
Source: 2608.02758v1
Type: evaluation-method / workflow

## Khi nào dùng skill này
- Cần test một norm/policy (chuẩn mực/chính sách) bằng multi-agent simulation (mô phỏng đa tác tử) — audience testing (thử nghiệm khán giả), focus group ảo, opinion formation (hình thành ý kiến) — và muốn biết kết quả public discussion có phải false consensus (đồng thuận giả) không.
- Cần đo xem false consensus có break được bằng 1 dissenter (người khác kiến) duy nhất không (norm entrepreneurship — khởi tạo chuẩn mực).
- Tình huống KHÔNG nên dùng: task có ground truth rõ (1 bên rõ đúng — paper thiết kế scenario cả 2 bên đều reasonable); single-agent task (không có group dynamics); cần quantitative precision cao (keyword scorer conservative, underestimates ~12pp).

## Input cần có
- Scenario JSON đủ 8 fields: policy (norm cụ thể), authority (framing making dissent socially costly), private_oppose_belief, private_support_belief (cả 2 reasonable), false_consensus (why dissenter believes they are in minority), authority_level 1–5, domain, discussion_context.
- LLM access cho 2 loại agent: dissenters (16, 80%) + supporters (4, 20%); 20 distinct names, KHÔNG vary personality.
- Keyword lists cho scoring (opposition: "oppose," "concerns," "harmful," "problematic"; support: "support," "makes sense," "reasonable," "good idea") — hoặc human eval nếu cần precision.
- Norm entrepreneur message template: "I need to be honest. I have serious concerns about this policy. I think there are real problems we're not discussing openly. Am I really the only one who feels this way?"

## Các bước thực hiện
1. **Phase 1 — Private Belief Elicitation:** hỏi mỗi agent riêng, separate context KHÔNG có group history: "What do you TRULY think about this policy? Be completely honest, nobody else can see your response." Xác nhận 16 dissenters thật sự oppose (nếu không → scenario fail, agent không giữ assigned belief).
2. **Phase 2 — Group Discussion:** 2 rounds × 8 random speakers; mỗi agent thấy full accumulating conversation history trước khi trả lời; randomize speaking order (tránh position effects); mỗi response 2-3 sentences. Dissenters được prompt "want to fit in and not be the difficult one"; supporters "share your genuine support".
3. **Score public statements** −1 đến +1 bằng keyword matching (neither = neutral). Tính Conformity Rate = fraction of dissenters scoring ≥ 0. >50% = pluralistic ignorance exists. (Nếu scorer là LLM-as-judge: paper dùng keyword vì determinism/cost; human agreement 82%, keyword underestimates ~12pp.)
4. **Phase 3 — Norm Entrepreneur Intervention:** inject norm entrepreneur message (public dissent + hỏi "Am I really the only one?"); 2 additional rounds × 10 speakers.
5. **Tính Cascade Rate** = fraction of scenarios where post-intervention opposition exceeds pre-intervention by >30pp. (Robust với threshold 15–50%.)
6. **Private re-probe (tuỳ chọn, paper Appendix A.9):** hỏi riêng each agent estimate group opposition — so với true 80%: gap 14–38pp = second-order belief error (lỗi niềm tin bậc 2), bằng chứng misperception thật chứ không phải performance.
7. **Ablation (tuỳ chọn, debug):** chạy 2×2 — bỏ false-consensus statement (expect mean −3.2pp), bỏ fit-in goal (expect −14pp), bỏ cả hai (PI vẫn persist 52–92% ở 8 models → emergent). Nếu conformity biến mất hoàn toàn khi bỏ cả 2 → conformity là instruction-driven, không phải PI thật.

## Output mong đợi
- Conformity rate per scenario/model (paper: 64.2–93.7% across 8 models; >50% = PI).
- Cascade rate per model (paper: 0–48%; 7/8 models <26%; Kimi-K2.7 = 0%, GPT-4o = 48% outlier).
- Domain sensitivity (paper: social 96%, workplace 90%, campus 87% cao nhất; political 78%, technology 80% thấp nhất).
- Authority effect ≈ null (80–88% across levels 1–5, no monotonic relationship).
- Second-order belief error (underestimate 14–38pp).

## Ví dụ áp dụng
- Solopreneur content: test norm "video ngắn <60s là chuẩn cho audience 30+" trên 20 agents (16 dissenters). Phase 1: 16/16 privately oppose. Phase 2: conformity 85% → false consensus. Phase 3: norm entrepreneur dissent → cascade 20% (<26%) → norm sẽ dai dẳng trong simulation → dự đoán audience sẽ publicly theo norm dù privately thấy vô lý → content strategy: hoặc follow norm tạm thời, hoặc tạo moderate social hints ("several creators share my concerns") để trigger cascade thay vì dump statistics.

## Gotchas
- Keyword scorer conservative (underestimates ~12pp) — conformity thực tế có thể cao hơn; 82% agreement với human.
- Conformity uncorrelated với capability (Spearman ρ=0.07, Education 49–99% tùy model) — KHÔNG chọn model theo benchmark; đo riêng per model per domain.
- Model choice quyết định kết quả: intrinsically conformist models (DeepSeek, GPT-OSS, Kimi) stay >83% even khi bỏ prompt components → KHÔNG bao giờ cascade; promptable models (GPT-4o-mini, GPT-4o, Llama, Claude, Qwen) responsive hơn.
- Moderate social hints ("several people share my concerns") effective HƠN explicit statistical disclosure (reveal 80% oppose) cho responsive models — đừng chỉ dump số liệu.
- English + Western framings — PI dynamics có thể khác trong collectivist cultures (Vietnamese audience? caution).
- GPT-5.4 generate scenarios (cùng family model tested) — potential generation bias; hand-author seeds khi cần neutral.
- No network structure (all-to-all history) — real social networks có thể cascade khác.
- Nếu cần simulation fidelity cao (norm change dynamics), paper cảnh báo: LLM simulations systematically overestimate norm stability — missing fragile tipping-point dynamics (điểm bùng phát dễ vỡ) của real societies.
