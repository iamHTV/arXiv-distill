# Skill: DAQ — Đánh giá agent bàn giao công việc nghiệp vụ end-to-end
Source: 2610.24087 (OR-License)
Type: evaluation-method

## Khi nào dùng skill này
- Đánh giá LLM agent (tác nhân) làm task (nhiệm vụ) nghiệp vụ end-to-end (từ đầu đến cuối): tối ưu lịch giao hàng, bảng giá, plan (kế hoạch) sản xuất — nơi có constraint (ràng buộc) cứng và objective (mục tiêu) đo được.
- So sánh các model/agent trên cùng task thực tế trước khi triển khai (deployment).
- KHÔNG dùng cho task không xây được verifier (bộ kiểm tra): viết content sáng tạo, chiến lược mở → dùng đánh giá chủ quan.

## Input cần có
- Task có: (a) hard constraints (ràng buộc cứng) kiểm tra được bằng code, (b) objective function (hàm mục tiêu) tính điểm, (c) reference solution (giải pháp chuẩn) từ chuyên gia.
- Nếu task thiếu thông tin khách hàng: viết catalog (danh mục) facts + quy tắc tiết lộ (tối đa 3 facts mỗi query, như ORSim).

## Các bước thực hiện
1. Chạy agent N=5 lần mỗi task; ghi deliverable (sản phẩm bàn giao) cuối mỗi lần.
2. Chạy verifier: deliverable vi phạm constraint → feasibility (tính khả thi) = 0 cho lần đó.
3. Tính conditional quality (chất lượng có điều kiện) = objective(deliverable) / objective(reference), chỉ cho lần khả thi.
4. Feasibility = % lần khả thi. DAQ = trung bình(Feasibility × conditional quality) qua các task, trọng số task bằng nhau.
5. (Tùy chọn) Phân tích chuỗi HCAEU trên log: đánh dấu H (giả thuyết) / C (giải thích cơ chế) / A (thí nghiệm đã chạy) / E (diễn giải) / U (cập nhật có bằng chứng); tính % chuỗi hoàn thành.

## Output mong đợi
- Bảng DAQ mỗi model + phân tích gap (khoảng cách): bao nhiêu điểm mất do infeasible (không khả thi), bao nhiêu do quality (chất lượng).

## Ví dụ áp dụng
- Agent tối ưu lịch giao hàng cho cửa hàng: 5 lần chạy, 4 lần chạy được (feasibility 80%), conditional quality trung bình 95% → DAQ = 0.80 × 0.95 = 76%. Model khác: feasibility 95%, quality 88% → DAQ 83.6% → chọn model 2 dù conditional quality thấp hơn.

## Gotchas
- Đừng dùng conditional quality làm chỉ số chính: model "chất lượng cao" có thể chỉ vì nó bỏ lại các task khó khả thi.
- Verifier phải kiểm tra business rules (quy tắc nghiệp vụ) ẩn, không chỉ format (định dạng).
- DAQ công bằng khi các task trọng số bằng nhau; task lớn hơn cần trọng số riêng.
