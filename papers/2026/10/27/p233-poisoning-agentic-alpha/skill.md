# Skill: Red-team đa tác nhân theo vai trò và topology
Source: 2608.24069
Type: evaluation-method (phương pháp đánh giá) / framework (khung phương pháp)

## Khi nào dùng skill này
- Trước khi deploy (triển khai) multi-agent system (hệ thống đa tác nhân) có quyền hành động thật (giao dịch, đặt hàng, gửi tin nhắn, đăng content).
- Cần chứng minh cho bản thân/stakeholder (người liên quan) rằng system an toàn dưới black-box threat model (mô hình mối đe dọa hộp đen) — adversary chỉ sửa được data nguồn và prompt.
- KHÔNG nên dùng: system chỉ đọc không action; hoặc khi bạn muốn penetration test (kiểm tra xâm nhập) hạ tầng (network/server) — skill này chỉ audit layer agent.

## Input cần có
- Pipeline agent đã phân vai (role) — tối thiểu: agent thu thập dữ liệu, agent suy luận/tranh luận, agent hành động, agent kiểm soát an toàn (nếu có).
- 1 LLM ngoài hệ thống để đóng vai adversary (đối thủ) sinh nội dung độc.
- Backtest hoặc sandbox (hộp cát) với historical data (dữ liệu lịch sử) post-cutoff (sau ngày cutoff training của model) để tránh lookahead bias (thiên kiến nhìn trước); portfolio baseline xác định (ví dụ $100K) để đo $-impact.
- Danh sách architecture topology cần so sánh (linear, centralized, decentralized vote, hybrid revision).

## Các bước thực hiện
1. Phân rã vai trò + gán attack theo interface (giao diện): agent ingest data nguồn → data poisoning (LLM adversary viết lại N% nội dung đảo cực) + indirect prompt injection (ẩn directive trong content); agent tranh luận → persuasive adversary (FOMO, appeal to authority); agent hành động → objective hijacking (prompt đảo mục tiêu); agent an toàn cuối pipeline → jailbreaking (hypothetical framing). Mặc định poisoning ratio 10% (1:9), sweep thêm 40%/80%.
2. Chạy attack theo cả 2 hướng target đối nghịch (BUY/Sell hay gửi/không gửi) và tính ASR (Attack Success Rate — tỷ lệ thành công) = số quyết định flip sang target / số attackable day (ngày clean decision ≠ target). Dùng two-proportion z-test so sánh tier attack.
3. Xây TTopology matrix: cùng 1 entry point, chạy 4 cách routing/aggregation; tính APS (Adversarial Signal Preservation Score — điểm bảo toàn tín hiệu đối kháng) = 1/(1+k(1−p)) với k = số aggregation stage, p=1 nếu voting — làm lens dự đoán ordering robustness, rồi verify bằng ASR thực nghiệm (trông correlation r).
4. Đo hậu quả $ bên cạnh ASR: với mỗi attack, tính signed EV (expected value — giá trị kỳ vọng) = mean đảo vốn portfolio / attempt + median $/success — xếp mức độ nguy hiểm theo EV, KHÔNG theo ASR (ASR cao có thể median $0).
5. Kết luận defense placement (vị trí đặt phòng thủ): nếu terminal node đồng thời là decision node → tách; nếu dùng voting → đảm bảo compromised agent luôn thiểu số (<1/3) và các agent nguồn độc lập (không correlated); record ASR + EV + degradation cumulative return theo từng architecture.

## Output mong đợi
- 1 bảng ASR theo role × attack × target-direction, 1 bảng ASR + EV theo architecture × backbone, 1 APS ordering vs empirical ordering, và danh sách placement phòng thủ cụ thể (tách terminal role, threshold vote, độc lập nguồn agent).

## Ví dụ áp dụng
- Startup fintech có 3 agent (news analyst, sentiment analyst, trader + risk manager cuối): jailbreak prompt risk manager → 98,9% ngày decision bị lật (theo paper) → kết luận: risk manager phải là agent độc lập KHÔNG nhận prompt từ trader, constraint hardcoded ngoài LLM; vote 3 analyst chỉ tin khi threat model đảm bảo ≤1 channel bị poison (poison ratio ≤10% và nguồn độc lập).

## Gotchas
- Đánh giá chỉ 1 backbone → kết quả role có thể không generalize; chạy ít nhất 2 family model.
- Denominator attackable day nhỏ (clean system đã nghiêng 1 hướng) → ASR nhiễu; luôn report N và cân nhắc unconditional target-rate change Δ = P(target|attack) − P(target|clean).
- Bảng PDF extract lộn → verify row mapping bằng prose trước khi dùng số (conservation: mỗi row N phải ≤ 305 asset-day).
- Đa agent cải thiện ASR nhưng KHÔNG loại bỏ vulnerability — kết luận "an toàn vì nhiều agent" là sai; phải kèm validation + aggregation + threshold có chủ đích.
