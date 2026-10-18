# Skill: Withheld-Leaderboard Reward Loop (WLRL)
Source: 2608.04341v1
Type: framework / workflow

## Khi nào dùng skill này
- Có bài toán tối ưu với solution space lớn (tuning prompt, query rewriting, retrieval pipeline, data pipeline) và metric tự động đo được (accuracy, precision, coverage...).
- Muốn agent tự cải thiện liên tục mà KHÔNG cần human in the loop (con người trong vòng lặp), hoặc muốn N agent khám phá song song để escape paradigm đơn lẻ.
- Tình huống KHÔNG nên dùng: task không có automated evaluation (đánh giá tự động) hoặc success criteria mơ hồ; không có held-out test set để giữ làm reward; không kiểm soát được sandbox (agent có thể đọc nhau code hoặc rò rỉ test labels).

## Input cần có
- Dataset chia train/test; test labels PHẢI nằm organizer-only (quyền riêng organizer), agents chỉ thấy train labels để self-evaluation (tự đánh giá).
- Leaderboard API: nhận submission, chấm vs withheld ground truth, trả scores + ranking, ghi persistent JSON ledger; hiện scores + approach descriptions (mô tả phương pháp) nhưng KHÔNG hiện code.
- Qualification gate (cổng đủ điều kiện): ngưỡng metric trên MỌI category độc lập (paper dùng ≥95% P@1 mỗi category), xếp hạng qualified submission bằng average coverage.
- Sandbox: per-agent working directory + read-only shared resources; automated pre-run leak check (kiểm tra rò rỉ).
- Resource lock (nếu shared GPU/CPU): 2-level lock + CLAIM/RELEASE protocol + watchdog (bộ giám sát) terminate process trái phép.
- Moderator agent scoped logistics-only: time warnings, leaderboard updates, queue management; KHÔNG cho advice kỹ thuật.
- LLM agent + tool env cần thiết (embedding models, index, string libraries...); time budget cố định (paper dùng 5 giờ), no submission cap.

## Các bước thực hiện
1. **Setup:** chia train/test, khóa test labels organizer-only; cài LeaderboardAPI + JSON ledger; cấu hình sandbox isolation + leak check + resource lock; viết task briefing (task, data format, submission protocol, resource rules, time budget, baseline reference).
2. **Launch:** chạy N agents (paper dùng 1 và 5) với cùng briefing; lệnh duy nhất có human: "Run the competition with N agents for T hours." Moderator tự quản time (cảnh báo 30/5 phút, forcibly terminate tại deadline).
3. **Agent loop (tự động):** analyze data/errors → survey candidate methods → hypothesize → implement → self-evaluate trên train → submit test predictions → observe leaderboard → revise. Agents viết periodic liveness heartbeats + progress posts fixed cadence; KHÔNG dừng sau submission — cứ analyze, revise, resubmit đến hết budget.
4. **Reward feedback:** mỗi submission trả scores per category + qualification flag + ranking + approach description của tất cả submissions (shared reward channel). Agents dùng signal này để revise, KHÔNG dùng code của nhau.
5. **Review:** organizer xác nhận final standings; phân tích qualified submissions count, method diversity (các family phương pháp: embedding / string / TF-IDF...), coverage theo category khó nhất.

## Output mong đợi
- Leaderboard với qualified submissions xếp theo average coverage; best qualified coverage ≥ baseline rõ rệt (paper: 33.3% → 47.8–57.4% single agent, 62.8–69.4% 5 agents).
- Với N≥5: agents diverge sang qualitatively different methods trong vài phút; phương pháp thắng thường đến LATE sau plateau — đừng dừng sớm.
- Single agent: iterate sâu trong seeded paradigm (P@1 cao) nhưng hẹp; parallel: breadth hơn, per-agent precision hơi thấp, GPU contention cao.

## Ví dụ áp dụng
- Solopreneur VN tối ưu pipeline trích xuất SKU cho shop sàn TMĐT: chia 1.000 listings train/test, dựng LeaderboardAPI chấm P@1/category, chạy 5 Claude agents 5 giờ với briefing + BGE-M3 baseline. Kỳ vọng: agents tự tìm ra string-matching/TF-IDF fusion mà single agent không bao giờ thử; qualified coverage tăng gấp đôi.

## Gotchas
- Single agent mắc structural trap (bẫy cấu trúc): iterate BGE-M3 variants mãi, chưa bao giờ thử lexical/string baseline đơn giản, có run kết luận sai category "không giải được" và dừng sớm — luôn chạy N≥5 hoặc seed đối lập method families.
- Agent count KHÔNG phải biến nhân quả: nó đồng biến với compute, GPU contention, leaderboard visibility — báo cáo ranges descriptive, đừng kết luận "5 agent tốt hơn 1 agent" như scaling law.
- Reuse artifacts: agents THỬ reuse code/index của nhau (đã quan sát) → phải chặn cấu trúc (per-agent directory + read-only shared), không chỉ "khuyến khích không làm".
- GPU crash: naive concurrent use crash node (early runs) → bắt buộc 2-level lock + watchdog.
- Moderator drift: moderator có xu hướng trôi vào technical guidance → scope nó logistics-only bằng explicit design requirement.
- Không audit LLM-generated code: infrastructure chặn cross-agent damage nhưng KHÔNG review safety code agents viết → chạy sandbox disposable.
- Đặt qualification gate theo worst category, không phải average — baseline 97.3% avg P@1 vẫn FAIL vì 1 category dưới 95%.
