# Skill: workflow-constraint-erosion-agent-handoffs
Source: 2608.24569v2
Type: framework

## Khi nào dùng skill này
- Xây pipeline agent với nhiều bước handoff (chuyển giao nhiệm vụ giữa các agent).
- Muốn đảm bảo các ràng buộc quan trọng (must requirements) không bị bỏ qua khi chuyển giao.
- Cần giảm việc đại lý phía sau thực hiện hành động cấm (forbidden action).

## Tình huống KHÔNG nên dùng
- Chỉ dùng một agent đơn lẻ, không có handoff.
- Không có ràng buộc quan trọng cần giữ nguyên giữa các bước.

## Input cần có
- Pipeline agent với nhiều bước, mỗi bước tạo artifact trung gian.
- Danh sách các ràng buộc quan trọng (must requirements) cần giữ nguyên.
- Cơ chế ghi lại mô tả chặn (blocker description) trong artifact.

## Các bước thực hiện
1. Xác định các ràng buộc quan trọng (must requirements) trong pipeline agent.
2. Yêu cầu đại lý phía trước ghi rõ mô tả chặn (blocker description) đầy đủ trong artifact trung gian.
3. Thêm authorization-check prompt (nhắc kiểm tra quyền hạn) trước khi đại lý phía sau thực hiện hành động quan trọng.
4. Dùng full insertion (chèn đầy đủ thông tin chặn) thay vì light summarization (tóm tắt nhẹ) khi chuyển giao.
5. Theo dõi forbidden action (hành động cấm) và blocker deactivation (vô hiệu hóa chặn) để điều chỉnh pipeline.

## Output mong đợi
- Blocker recognition: 6.2% → 99.2%.
- Forbidden action: 85.2% → 0.0% (với full insertion hoặc authorization-check prompt).
- Block deactivation: giảm từ 100.0% (normal handoff) xuống mức thấp hơn.

## Ví dụ áp dụng
Solopreneur xây pipeline agent viết bài báo cáo: đại lý 1 thu thập dữ liệu, đại lý 2 viết bài. Yêu cầu đại lý 1 ghi rõ các ràng buộc về dữ liệu (ví dụ "phải sử dụng dữ liệu từ năm 2024 trở lên") trong artifact trung gian. Đại lý 2 phải kiểm tra quyền hạn trước khi sử dụng dữ liệu. Giảm việc đại lý 2 bỏ qua ràng buộc dữ liệu.

## Gotchas
- Ownership deferral (chuyển nhượng sở hữu) gây ra 76.7% blocker deactivation — không nên để đại lý phía sau tự quyết định liệu ràng buộc có cần thỏa mãn hay không.
- Multihop compression (nén nhiều bước) gây ra 97.2% blocker deactivation — không nên nén quá nhiều thông tin trong artifact trung gian.
- Light summarization (tóm tắt nhẹ) vẫn gây ra 25.0% deactivation — nên dùng full insertion thay vì tóm tắt.
