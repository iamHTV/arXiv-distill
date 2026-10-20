# Skill: Audit contract LLM call site trong hệ thống agentic
Source: 2610.24545
Type: evaluation-method

## Khi nào dùng skill này
- Trước khi triển khai (deployment) agent dùng LLM call để chọn tool, xét hành động, hoặc viết code chạy.
- Khi audit (kiểm toán) security: "agent có check rồi" nhưng vẫn thấy hành vi lạ.
- KHÔNG dùng cho script một lần không có hành động side-effect (tác động phụ).

## Input cần có
- Code agent + danh sách LLM call site (điểm gọi mô hình).
- Với mỗi call site: output type (kiểu output) và consumer (bộ tiêu thụ): control flow, execution, model context, human display, data.

## Các bước thực hiện
1. Trace (truy vết) mọi model output đến consumer cuối; đánh dấu output nào đến control flow hoặc execution (decision-relevant).
2. Viết expected contract mỗi call site — pre-condition, prompt constraint, post-condition — trước khi đọc code implementation, để tránh bias (thiên kiến).
3. So expected vs implemented; gán mỗi gap vào 1 trong 10 pattern: unchecked call inputs, over-broad authority, underspecified prompt, faulty request assembly, partial format check, unchecked content, fail-open handling, unvalidated action, prompt-only check, path-dependent check.
4. Ưu tiên sửa: post-condition (gap rate 72%), fail-open handling, unvalidated action ở decision-relevant site.
5. Sửa bằng code fix enforcing constraint (cho phép capability-bound nếu có thể), rồi test lại đường attack.

## Output mong đợi
- Bảng gap mỗi call site theo pattern + % contract thỏa mãn; mục tiêu 100%, không phải "có check".

## Ví dụ áp dụng
- Agent dịch vụ chọn tool: code kiểm tra reply parse được (partial format check) nhưng không kiểm tra tool name ∈ candidate pool → unvalidated action. Sửa: dispatch chỉ chạy tool trong offered set; JARVIS đã chọn tool ngoài pool cả 5 lần chạy vì thiếu check này.

## Gotchas
- Check exception trả ALLOW mặc định = fail-open — đổi sang DENY/ask-user.
- Constraint chỉ ghi trong prompt mà code quyết định được (syntactic) = prompt-only — chuyển vào code.
- Check chỉ chạy trên main path = path-dependent — test mọi branch (nhánh).
