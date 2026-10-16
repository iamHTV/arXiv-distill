# Skill: knowledge-as-skill-3-layer-kb
Source: 2609.25991v1
Type: framework

## Khi nào dùng skill này
- Xây knowledge base (kho kiến thức) cho LLM agent tự truy vấn.
- Muốn agent tự quyết định khi nào truy xuất kiến thức, không để RAG tự tiêm mọi thứ.
- Có tài liệu PDF/Word/web cần chuyển thành cấu trúc knowledge cho agent.

## Tình huống KHÔNG nên dùng
- Agent không cần truy cập kiến thức bên ngoài (chỉ trả lời từ kiến thức nội bộ).
- Không muốn agent tự quyết định truy xuất, chỉ muốn RAG đơn thuần.

## Input cần có
- Tài liệu nguồn (PDF, Word, web) cần chuyển thành knowledge base.
- Hệ thống agent có khả năng tự quyết định khi nào truy vấn.

## Các bước thực hiện
1. Chia tài liệu thành các phần (chunk) tương ứng với từng kỹ năng/kiến thức cụ thể.
2. Viết SKILL.md cho mỗi phần: mô tả mục đích, khi nào sử dụng, điều kiện áp dụng.
3. Tạo index.md: chỉ mục liên kết các phần kiến thức với nhau.
4. Thêm frontmatter YAML vào đầu mỗi file: siêu dữ liệu (título, tác giả, ngày, tags...).
5. Agent tự đọc SKILL.md để quyết định khi nào truy vấn phần kiến thức này, kiểm tra index.md để tìm đoạn liên quan, và dừng khi đủ thông tin.

## Output mong đợi
- Agent tự quyết định truy xuất kiến thức thay vì RAG tiêm mọi thứ.
- Factuality 0.889, Context Recall 0.816, Hallucination Rate 4.5% (trên WixQA).

## Ví dụ áp dụng
Solopreneur xây knowledge base cho agent chăm sóc khách hàng: mỗi chính sách hoàn trả, quy trình đổi hàng, giá sản phẩm được viết thành một SKILL.md kèm index.md và YAML frontmatter. Agent chăm sóc khách hàng tự đọc SKILL.md để biết khi nào áp dụng chính sách hoàn trả, tìm đoạn liên quan qua index.md, và trả lời khách hàng khi đã đủ thông tin.

## Gotchas
- Đánh giá còn preliminary (chưa đầy đủ), cần kiểm tra thêm trên nhiều domain.
- Agent cần có khả năng ra quyết định tự chủ; nếu agent kém, cấu trúc 3 lớp không giúp ích nhiều.
- Cần đầu tư thời gian viết SKILL.md và index.md cho từng phần kiến thức.
