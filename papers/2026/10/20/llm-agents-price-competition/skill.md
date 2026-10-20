# Skill: LLM Pricing Deployment Audit (đánh giá regime định giá của agent LLM)
Source: 2610.21711v1
Type: evaluation-method / framework

## Khi nào dùng skill này
- Bạn build hoặc dùng pricing agent (agent định giá) LLM cho e-commerce, marketplace, ad bidding, dynamic pricing (định giá động).
- Trước khi triển khai agent định giá ra thị trường thật — compliance check (kiểm tra tuân thủ) + consumer welfare (phúc lợi người tiêu dùng).
- KHÔNG nên dùng: agent không đặt giá (content, support agent); market không có feedback loop (vòng phản hồi) lặp lại.

## Input cần có
- Deployment spec 6 thành phần: H (history representation (biểu diễn lịch sử) + memory window (cửa sổ nhớ)), A (action space: continuous (liên tục) / grid (lưới)), O (output: point price (giá điểm) / probability distribution (phân phối xác suất)), Delta (update cadence (tần suất cập nhật)), M (persistent state (trạng thái lưu) / scratchpad), P (prompt framing (cách đặt lệnh)).
- Market model (mô hình thị trường): demand form (dạng cầu: logit / winner-takes-all (thắng nhận hết)), n firms, cost c, grid K, horizon T.
- Opponent ecology (hệ sinh thái đối thủ): standard learners (Exp3/UCB/PPO/FTRL...) vs LLM agents vs heuristic (quy tắc heuristic).
- Logging: price path per period (đường giá từng period), profit share (phần lợi nhuận), consumer share (phần consumer).

## Các bước thực hiện
1. Định benchmark: competitive region (vùng cạnh tranh = finite-grid Nash region) + joint-profit benchmark (benchmark lợi nhuận chung); compute price-elevation index Delta (0 = Nash, 1 = monopoly) on final-third window (½ cuối) của mỗi run.
2. Self-play (tự chơi) tối thiểu 2 deployment đối lập — (point + raw history + rival visible) vs (distribution + summary + interval 25) — mỗi loại 5-10 seeds. CẢNH BÁO: point+raw self-play Delta > 0.5 = high-price regime (chế độ giá cao).
3. Matchup vs standard learners (T=2,000, 10 seeds): đo share of cumulative industry profit (phần lợi nhuận tích lũy); D-S-style kỳ vọng 71-72% qua undercut (giá thấp hơn đối thủ 57-60% periods cuối), KHÔNG qua giá cao.
4. Protocol ablation: từ control, thay đổi information interface — hide rival price (ẩn giá đối thủ) + summary history (lịch sử tóm tắt) gây movement lớn nhất (0.97 → 0.56/0.53/0.31); đổi action representation alone (point→grid→distribution) KHÔNG đổi regime (1.01-1.05).
5. Gán nhãn regime descriptors (mô tả regime): high-price lock-in (giam giá cao), anchor-and-harvest (neo then thu hoạch — reset lên cao rồi hạ briefly), competitive undercutting (đấu giá thấp), Nash-like. Phát hiện anchor-and-harvest: tìm pattern price reset-up → brief undercut trong price path.
6. Welfare + audit logging: đo % consumer share per regime (15% P-R-1 vs 95% D-S); log model version, prompt, observation stream, memory state, price recommendation, sampling procedure (quy trình lấy mẫu), human overrides (ghi đè của người).

## Output mong đợi
- Regime map (bản đồ regime): deployment x opponent → regime label + elevation index + consumer share; khuyến nghị rõ deployment nào launch / redesign / block trước khi ra thị trường.

## Ví dụ áp dụng
- Marketplace VN, 2 sellers dùng agent class Gemini: deployment X (point + raw 100-period rival history, every period) self-play Delta_H = 0.88, consumer share 15% → redesign thành Y (distribution + per-price summary, interval 25) → self-play 0.05, consumer 95%; vs Exp3: X 63% / Y 71%. Launch Y, block X.

## Gotchas
- Single-run heterogeneous markets (n=1/run) = representative paths, KHÔNG phải treatment effects — replicate trước khi kết luận.
- Hiding rival price KHÔNG tự động pro-competitive (có lợi cạnh tranh): trong P-R-1-D-S-1 hidden, D-S-1 vẫn học threshold (ngưỡng) dưới anchor và lấy 71% profit.
- Trace (plans/insights) là behavioral artefact (sản phẩm quan sát hành vi), KHÔNG phải hidden computation: collusive outcome (outcome thông đồng) có thể KHÔNG thấy trong chain-of-thought (chuỗi suy nghĩ).
- High prices KHÔNG đi kèm cumulative-reward optimization (tối ưu phần thưởng tích lũy): PPO vẫn về Nash — đừng giả định "agent tối ưu long-run = collusion (thông đồng)".
- Surrogate (DBBS) không phải no-regret guarantee (bảo đảm hối tiếc bằng 0) — đừng dùng cho worst-case pricing (định giá xấu nhất).

## Dry run test
- Test case giả (marketplace 2 sellers, Gemini-class agent): Step 1 benchmark: K=21, c=0.10, ceiling 0.36, competitive region {0.100, 0.113, 0.126}. Step 2: X self-play 5 seeds mean Delta_H 0.88 (ceiling lock-in); Y mean 0.08. Step 3: vs Exp3 T=2,000 10 seeds: X 63%, Y 71% (Y giá thấp hơn 57-60% periods cuối). Step 4: ablation từ X: hide rival → 0.56; summary → 0.53; both → 0.31; grid-distribution-only → 1.03 (không đổi). Step 5: X = high-price lock-in; Y = Nash-like. Step 6: consumer share X 15% vs Y 95%; logging spec emitted. Output: regime map + "launch Y, block X" — có nghĩa, follow được → [SKILL VALID].
