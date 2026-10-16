# Skill: open-source-mas-issues-causes-solutions
Source: 2610.00905v1
Type: framework

## Khi nào dùng skill này
- Xây hoặc duy trì hệ thống đa đại lý (MAS) dựa trên LLM.
- Muốn hiểu các vấn đề phổ biến, nguyên nhân và giải pháp trong MAS mã nguồn mở.
- Cần ưu tiên đầu tư vào thiết kế nào khi xây MAS.

## Tình huống KHÔNG nên dùng
- Không xây MAS, chỉ dùng agent đơn lẻ.
- Không có danh sách issues/bugs để phân tích.

## Input cần có
- Danh sách issues/bugs từ hệ thống MAS đang vận hành.
- Hiểu biết về kiến trúc MAS (coordinator, specialist, workflow, v.v.).

## Các bước thực hiện
1. Phân loại mỗi issue vào 17 danh mục (Orchestration & Execution, Memory & State Management, Tool Issue, v.v.).
2. Trích xuất nguyên nhân từ mỗi issue (Workflow Problem, Tool Integration Problem, Memory Problem, v.v.).
3. Áp dụng giải pháp tương ứng (Optimize Workflow, Adjust Configuration, Optimize Tool Integration, v.v.).
4. Ưu tiên tối ưu hóa workflow (OW) vì đây là giải pháp phổ biến nhất (26.0%) và giải quyết được phần lớn vấn đề orchestration.
5. Theo dõi tỷ lệ giải quyết (resolution rate): Documentation Issue cao nhất (76.9%), Output Issue thấp nhất (24.1%).

## Output mong đợi
- Hiểu rõ các vấn đề phổ biến trong MAS (Orchestration & Execution 22.0% là nhiều nhất).
- Biết ưu tiên đầu tư vào thiết kế workflow và điều phối agent.

## Ví dụ áp dụng
Solopreneur xây MAS chăm sóc khách hàng: gặp vấn đề agent chuyển hàng cho nhau không đúng (orchestration issue). Áp dụng Optimize Workflow: thiết kế lại luồng chuyển giao giữa các agent, thêm gate validation trước khi chuyển. Giảm thời gian gỡ lỗi so với việc sửa từng agent riêng lẻ.

## Gotchas
- Orchestration & Execution Issue chiếm 22.0% — đây là vấn đề lớn nhất, không phải vấn đề của từng agent đơn lẻ.
- Workflow Problem là nguyên nhân phổ biến nhất (29.4%) — kiểm tra workflow trước khi sửa code từng agent.
- Documentation Issue có tỷ lệ giải quyết cao nhất (76.9%) — đầu tư tài liệu giúp giải quyết vấn đề nhanh hơn.
