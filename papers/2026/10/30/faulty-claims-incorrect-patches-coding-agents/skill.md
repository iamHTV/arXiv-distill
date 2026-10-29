# Skill: cot-claim-audit (kiểm toán claim-level CoT của coding agent)
Source: 2610.32338
Type: evaluation-method / workflow

## Khi nào dùng skill này
- Review (kiểm tra) patch (bản vá) do coding agent (tác nhân viết code) tạo RA TRƯỚC KHI merge (gộp) — đặc biệt task phức tạp (SWE-bench Pro-like: patch hàng trăm dòng, nhiều defect (lỗi) tiềm ẩn).
- Build monitoring (giám sát) hoặc checkpoint (điểm kiểm tra) cho pipeline coding agent: verify claims (xác minh khẳng định) agent tin trước khi nó nộp patch.
- Post-hoc audit (kiểm toán sau sự kiện): patch pass tests nhưng behavior (hành vi) nghi ngờ sai — plausible patch (bản vá có vẻ đúng).
- KHÔNG nên dùng: model không expose native CoT (chain of thought — chuỗi suy nghĩ gốc) (closed model (model đóng) — suy giảm về framework thoughts, ít detail); không có access (quyền truy cập) repository tại base commit (commit gốc) + task statement + library docs để verify.

## Input cần có
- Trajectory (hành trình) của coding agent với native CoT per step (open-weight reasoning model (model reasoning trọng số mở): DeepSeek, Qwen...), hoặc recorded thoughts (suy nghĩ ghi lại) từ agent framework.
- Repository tại base commit của task (để verify claims về original implementation).
- Task statement (phát biểu task) nguyên bản.
- Library documentation access (tài liệu thư viện) cho claims về dependency/API.
- Validation test suite (bộ test kiểm chứng) + ability (khả năng) chạy execution probes (dò tìm thực thi) / targeted tests (test mục tiêu).

## Các bước thực hiện
1. **Extract claims (trích khẳng định):** với mỗi step CoT, trích reasoning units (đơn vị suy luận) — proposition (mệnh đề) nhỏ nhất tự judge (phán xét) đúng/sai — kèm verbatim quote (trích dẫn nguyên văn) từ CoT + files referenced. Classify type: O (original implementation — code/thư viện behavior/structure), G (implementation gap — code thiếu gì vs requirement), S (semantic constraint (ràng buộc ngữ nghĩa) — task yêu cầu gì), F (fix mechanism — cơ chế đề xuất có thỏa requirement không). Bỏ content không checkable (navigation, editing intention (ý định sửa), test status).
2. **Verify claims (xác minh):** mỗi unit judge supported / refuted (bị bác) / unresolved với evidence gather được: O → trace code behavior thực tế; G → compare implementation vs requirement; S → reconstruct requirement từ task statement, tìm input phân biệt; F → tìm counterexample (phản ví dụ) dưới điều kiện claim. Mỗi judgment kèm citation (trích dẫn nguồn evidence: file+line, doc excerpt). Refuted = faulty claim (khẳng định lỗi). Record quotes — quote không có trong CoT → discard judgment đó.
3. **Prioritize key faulty claims (khẳng định lỗi then chốt):** giữ LẠI chỉ faulty claims mà final patch vẫn build trên (check: patch có phụ thuộc claim không? later evidence (bằng chứng sau) đã sửa claim chưa?). Bỏ phần còn lại — 96.7% trajectory PASS vẫn chứa faulty claims (presence (sự hiện diện) là weak signal (tín hiệu yếu)); chỉ ~1/26 faulty claims là key. Expected yield (năng suất kỳ vọng): ~1 key claim/trajectory fail.
4. **Correct trước submission (nộp):** gửi correction message (tin nhắn sửa) cho agent ngay trước submission, nêu claim refuted + evidence citation + yêu cầu revise patch. Verify agent produce targeted fix (bản sửa trúng defect) — expect small focused edit: median 13 lines changed (vs median 101 original), ~17 steps thêm. Model mới follow correction đáng tin hơn (100% replays Flash/Qwen3.8 vs 77–87% model cũ).
5. **Anti-pattern scan (quét phản mẫu):** flag (đánh dấu) hedged claims (khẳng định mơ hồ: "Probably exact", "likely", "should be") và shortcut statements (câu tắt đường: "tests won't check", "only needs to pass validation") trong reasoning → queue patch cho human review (duyệt người) DÙ tests pass — đây là dấu hiệu agent narrow task (thu hẹp task) về phần được test.
6. **Targeted verification sau sửa:** chạy targeted tests cho behavior faulty claim đề cập + execution probes (gọi hàm thật với input phân biệt) — KHÔNG tin validation suite: 129/162 replays fix defect nhưng tests không hiện (tests không exercise behavior được sửa). Kiểm tra requirement scope (phạm vi): faulty S claims 2/3 là scope sai (overgeneralization (khái quát quá mức)/omission (bỏ sót)).

## Output mong đợi
- Bảng verdict per claim: claim quote, type O/G/S/F, verdict supported/refuted/unresolved, evidence citation.
- Danh sách key faulty claims + correction messages đã gửi + revised patch (có targeted fix, median ~13 lines).
- Flag list anti-patterns (hedged/shortcut statements) cần human review.
- Số thực tế đã verify: correction fix linked defect 89.0% (162/182); pass more tests 18.7%; resolve thêm 11.5% (đơn claim) — 40.4%/21.3% khi sửa tất cả key claims cùng message (multi-claim trajectories); resolution 53.0%→58.5% (4 models trung bình).

## Ví dụ áp dụng
- Agent sửa bug checkout shop: CoT claim O "cart.total() đã áp dụng discount" → Bước 2 đọc cart.py: total() KHÔNG có discount logic → refuted, citation cart.py L40-58. Bước 3: patch mới tính fee gọi total() → patch build trên claim → KEY. Bước 4: correction "total() không áp discount — fee phải cộng discount tường minh" → agent revise 13 lines, targeted fix có. Bước 5: scan thấy "probably tax module handles rounding" → flag review. Bước 6: targeted test discount-fee pass + probe legacy cart. Merge an toàn.

## Gotchas
- Faulty-claim COUNT là weak indicator: unresolved trajectory có nhiều faulty claims chủ yếu vì nhiều claims hơn (1.97× faulty nhưng 1.62× units); error rate chỉ cao 0.9–2.1 điểm phần trăm; 96.7% resolved trajectory vẫn có faulty claims. Đừng kết luận "nhiều faulty claim = agent hỏng".
- Verification phải check BEHAVIOR không phải identifier: 53.3% lỗi là misstatement (phát biểu sai behavior), chỉ 11.3% misreference (tham chiếu sai object) — mọi object claim đều tồn tại, claim nhìn plausible (có vẻ đúng); chỉ trace code mới phát hiện.
- Error rate 9.6% là LOWER BOUND (cận dưới): assessment precision 86.3%, recall unchecked — thực tế có thể cao hơn; assessment agent chôn mỗi key claim trong ~26 faulty claims khác → bước 3 (prioritize) là bắt buộc, đừng report tất cả faulty claims cho agent (gây noise (nhiễu)).
- Correction không đảm bảo resolve: defect fix 89% nhưng resolve chỉ 11.5% — defect khác còn hoặc tests miss behavior đã sửa. Multi-claim trajectories: sửa hết key claims cùng một message (40.4% pass more tests, 21.3% resolve) tốt hơn sửa rời rạc (8.8% resolve).
- Closed-model hạn chế: commercial models hide native CoT → skill suy giảm chất lượng (framework thoughts ngắn, ít claim). Khi đó kết hợp với step-level monitoring (repeated actions, untested fixes) thay thế.
- ~1/3 failing patches KHÔNG có faulty claim trong reasoning (defect sinh lúc editing: hunk header sai lines, move function quên add) → claim audit không thay thế code review; bổ sung consistency check reasoning-vs-edits (trace mỗi hunk về claim motivating nó).
