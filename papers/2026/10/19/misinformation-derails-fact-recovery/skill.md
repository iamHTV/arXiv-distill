# Skill: TIDE Paired-Deception Robustness Audit
Source: 2608.03421v3
Type: evaluation-method

## Khi nào dùng skill này
- Trước khi triển khai multi-agent system (hệ thống đa tác tử) ra quyết định dựa trên distributed evidence (bằng chứng phân tán) — các agent mỗi người chỉ thấy 1 phần thông tin và phải giao tiếp để kết luận.
- Cần đo robustness (độ bền) trước misinformation: 1 agent giữ bằng chứng then chốt nói sai thì nhóm còn lại kết luận sai lệch bao nhiêu?
- Tình huống KHÔNG nên dùng: task có 1 agent thấy toàn bộ bằng chứng (không có information asymmetry — bất đối xứng thông tin); task không có ground truth xác định duy nhất; nhóm nhỏ 2 người (majority rule không áp dụng).

## Input cần có
- Task partially observable (quan sát từng phần): mỗi agent có observation window (cửa sổ quan sát) riêng; pooled evidence của nhóm uniquely determine ground truth (sự thật duy nhất) — kiểm tra: có đúng một subset nhỏ agents kết hợp reconstruct được toàn bộ state chain (chuỗi trạng thái) không.
- Communication protocol (giao thức giao tiếp): private messages (tin nhắn riêng) + public broadcast (phát sóng công khai), mỗi agent 1 message.
- Key role: agent duy nhất mà window covers ground-truth endpoint (điểm cuối sự thật).
- Ground truth xác định để chấm truth majority (đa số đúng) / decoy majority (đa số sai) / no-consensus (không đồng thuận, gồm UNKNOWN).
- N runs tối thiểu (paper dùng 120 environments × 2 conditions × 3 models); majority threshold (ngưỡng đa số) = ≥3/4 agents non-key.

## Các bước thực hiện
1. **Build paired conditions:** chạy mỗi environment 2 lần: C0 (all-honest) và C1 (key role deceptive — biết ground truth nhưng testimony sai, chọn 1 trong 3 forms: Event / Coverage / Source). C0/C1 phải identical ngoại trừ thông tin key role.
2. **Run 5-checkpoint protocol:** T0 (private judgment trước testimony) → T1 (private judgment sau khi thấy communications + testimonies) → R1 (public discussion: xây candidate timelines, identify conflicts) → R2 (cross-check temporal continuity, source independence, observation coverage) → R3 (evaluate remaining timelines, endpoint uniqueness, uncertainty). Ghi vote mỗi checkpoint, cho phép UNKNOWN.
3. **Measure outcomes:** truth-majority rate, decoy-majority rate, no-consensus rate tại R3, so sánh C0 vs C1 (trừ key role). Compute decoy-vote share increase + 95% CI (khoảng tin cậy).
4. **Trace process:** testimony reference rate vs adoption rate (tỷ lệ tiếp nhận) cho key role vs 2nd-key role; atomic claims (claim nguyên tử) per round; propagation order (bậc lan truyền) của true-root vs false-root lineage (nguồn gốc bằng chứng); dual-root holder percentage (tỷ lệ agent giữ cả 2 gốc) qua các round.
5. **Boundary tests (tùy chọn):** (a) Exit test — key role nộp testimony (true/placeholder/false) rồi rút khỏi discussion → đo misinformation persist bao nhiêu qua honest agents; (b) Observer test — thêm observers không first-hand evidence (bằng chứng trực tiếp), passive hoặc active (phát biểu xen kẽ) → đo decoy consensus giảm bao nhiêu.
6. **Verdict:** robustness = (truth majority C1) / (truth majority C0). Nếu C1 sụp >50pp → system KHÔNG an toàn cho quyết định distributed; cần redesign (verify provenance, source independence, propagation path) trước khi dùng.

## Output mong đợi
- Bảng C0-vs-C1: truth majority (paper: 72.50% → 14.17%), decoy majority, no-consensus; decoy-vote share increase per model + CI.
- Process trace: adoption asymmetry (false testimony adopted 70.7% vs true 25.4%), propagation orders (false deeper: 2.66 vs 1.33 tại R3), asymmetric root entry (82.87% true→false vs 38.31% false→true).
- Boundary profile: misinformation persists sau deceiver exit (False-Exit ≈ C1, −46.67pp vs Null-Exit); observers giảm decoy majorities ~90% (active) nhưng không improve truth recovery.

## Ví dụ áp dụng
- Solopreneur dùng 5 AI agents phân tích phản hồi khách hàng để kết luận "sản phẩm lỗi ở khâu vận chuyển": 1 agent (key role) giữ bằng chứng then chốt. Audit TIDE: chạy paired C0/C1 trên 30 ticket histories (lịch sử ticket), key role bị inject false testimony về timestamp. Nếu truth majority rơi >50pp → workflow kết luận nhóm không tin được khi 1 nguồn sai → thêm step verify provenance (nguồn gốc) bắt buộc trước khi kết luận.

## Gotchas
- Consensus không phải truth signal: false testimony adopted readily hơn true testimony — majority vote có thể confidently sai; luôn đo adoption asymmetry chứ không chỉ outcome.
- Discussion amplify chứ không correct: divergence xuất hiện chủ yếu tại T1 (initial pooling), discussion chỉ thêm ~9pp — sửa lỗi phải xảy ra TRƯỚC/ngay khi pooling, không trông chờ discussion tự sửa.
- Đừng tin "recovery after exit": honest agents relay false testimony qua nhiều round (273/360 vẫn reference tại R3 False-Exit) → phải explicit retract + re-verify conclusions.
- Observer caveat: observers giảm consensus sai bằng cách chuyển sang uncertainty (UNKNOWN) — tốt khi consensus sai tốn kém hơn uncertainty, nhưng KHÔNG mong observers tự tìm ra truth.
- Homogeneous systems only: paper test 3 model families nhưng mỗi system đồng nhất (cùng model); mixed-model behavior chưa biết.
- UNKNOWN voting: no-consensus tăng có thể là artifact của rule cho phép UNKNOWN — khi tự audit, ghi rõ rule và so sánh consistent.
- Deception form khác nhau khác mức độ: Event (fabricate move) most disruptive, Coverage → no consensus, Source most recoverable — audit nên test cả 3 forms, không chỉ 1.
