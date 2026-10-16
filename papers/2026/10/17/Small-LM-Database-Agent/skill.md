# Skill: Agent Failure Ledger Taxonomy (phân loại failure agent qua ledger)
Source: 2609.21341
Type: evaluation-method / debugging-workflow

## Khi nào dùng skill này
- Agent production có tỷ lệ failure cao mà blame rơi vào "model yếu" — cần biết failure thật sự nằm ở đâu (model hay server/contract)
- Bạn có log tool calls nhưng chỉ thấy exit code/refusal code, không thấy arguments thật
- Trước khi đổi model hoặc prompt: muốn sửa failure server-side trước

Tình huống KHÔNG nên dùng: agent không có log structured (không ledger) — phải instrument trước; hoặc failure do task design, không phải tool loop.

## Input cần có
- Agent loop với verifier (đánh giá output: answered/unanswered — "succeeded" ≠ pass)
- Ledger ghi: mỗi tool call (arguments verbatim), refusal code, verdict, process exit, thời gian
- Công cụ phân loại theo thứ tự cố định (bước 2)

## Các bước thực hiện
1. Instrument: record EVERY tool call arguments verbatim + refusal code + verdict (answered/unanswered) + exit status. Ledger chỉ ghi exit status sẽ che mất toàn bộ transport class.
2. Phân loại mỗi run loss theo thứ tự LOAD-BEARING: clock (timeout/turn-limit/deadline) → capability (không invoke tool nào) → verification (report filed nhưng bị reject) → transport (đã invoke tools, hết thời gian, không deliverable). Thứ tự này thay đổi headline — phải report cả ordering đã dùng.
3. Phân rã transport class bằng captured arguments: tìm các shape lặp lại — JSON đúng nằm trong text channel, array close twice, key "name"/"action" thay vì schema key, near-miss key.
4. Sửa SERVER-SIDE (không đụng model, prompt, sampling): reader nhận diện call theo naming thay vì strict JSON parse; đọc SQL kind từ statement; rename trường unambiguous (exactly-one-absent/surplus); sửa instruction "remove <field>" mâu thuẫn với sibling tool.
5. Re-read CÙNG cells (cùng model, cùng task, cùng hardware) trước/sau, so sánh từng cell (ví dụ x/30 → y/30). Báo cáo honest qualification: effect isolated của từng change, đừng gộp.
6. Control confounds hardware: cap serving context (check process listing của engine, cột context — free memory system-wide đọc "healthy" nhưng 1 model có thể giữ phần lớn RAM); watch swap GROWTH trong lúc run (swap tĩnh đầy không sao, swap đang write là máy đang chọn giữa model và mọi thứ).

## Output mong đợi
- Bảng phân loại 4 class với % trên tổng losses; transport decomposition theo shape; bảng before/after per cell của server changes; kết luận failure nằm ở model hay ở contract/server.

## Ví dụ áp dụng
- Agent database 8,199 runs: ledger cho thấy 75.7% losses từ runs ĐÃ invoke tool; 27/69 stopping turns chứa tool call đúng nhưng viết vào text channel. 5 server changes không đụng model/prompt/sampling đã move 6 models 6–21 cells/30 (cogito:8b từ 0/30 lên 21/30).

## Gotchas
- "succeeded" ≠ pass: report rỗng vẫn exit thành công — verifier phải tách answered/unanswered (trong corpus: 2,204 model-stopped, 1,405 unanswered).
- Recovery path yêu cầu JSON parse sẽ thấy 0 call đúng-but-malformed (none of 27 parse được).
- Thứ tự classification là load-bearing: capability-first đảo thành capability 24.3% — luôn nêu rõ thứ tự.
- Uncapped context tạo fake "model yếu": 3B model planning cell 0/5 (51GB RAM) → 5/5 khi cap 32k. Per-model rates là LOWER BOUND.
- Run deadline là product config: model pass 443–444s vẫn fail tại deadline 450s — đừng "fix" bằng cách bỏ deadline.
