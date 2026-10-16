# Skill: hybrid-agentic-supply-chain-analytics
Source: 2609.13561v1
Type: framework

## Khi nào dùng skill này
- Xây hệ thống phân tích chuỗi cung ứng (supply chain analytics) cho doanh nghiệp.
- Cần xử lý các tác vụ đòi hỏi chuyên môn đa dạng (truy vấn CSDL, phân tích KPI, dự báo nhu cầu, chẩn đoán hiệu suất).
- Có dữ liệu chuỗi cung ứng và muốn dùng LLM agent để đưa ra quyết định.

## Tình huống KHÔNG nên dùng
- Không có dữ liệu chuỗi cung ứng.
- Chỉ cần phân tích đơn giản, không cần multi-agent.

## Input cần có
- Dữ liệu supply chain (bán hàng, tồn kho, nhà cung cấp, nhu cầu).
- Các mô hình LLM (reasoning và non-reasoning).
- Khung agentic (coordinator + specialist agents).

## Các bước thực hiện
1. Xác định các vùng chuyên môn cần xử lý (database querying, KPI analysis, demand forecasting, performance diagnosis).
2. Tạo specialist agent cho mỗi vùng, mỗi specialist phụ trách một loại tác vụ.
3. Tạo coordinator agent để phối hợp giữa các specialist và đưa ra quyết định cuối cùng.
4. Dùng reasoning model cho các tác vụ phức tạp (đạt >90% accuracy), non-reasoning model cho tác vụ đơn giản (~65%).
5. Đánh giá độ chính xác trên dữ liệu thực tế trước khi triển khai.

## Output mong đợi
- 90% accuracy cho multi-agent design, cạnh tranh với single agent baseline.
- Reasoning models đạt >90%, non-reasoning models đạt ~65%.

## Ví dụ áp dụng
Solopreneur làm hệ thống quản lý tồn kho cho cửa hàng online: tạo specialist agent dự báo nhu cầu (dùng dữ liệu bán hàng lịch sử), specialist agent phân tích KPI (tỷ lệ bán hàng, tồn kho dư), coordinator tổng hợp để đề xuất mức tồn kho tối ưu. Dùng reasoning model cho dự báo nhu cầu phức tạp, non-reasoning model cho truy vấn dữ liệu đơn giản.

## Gotchas
- Reasoning models cần thiết cho tác vụ phức tạp (>90% accuracy vs ~65% non-reasoning).
- Multi-agent design cần coordinator hoạt động tốt; nếu coordinator kém, hệ thống không hiệu quả.
- Cần dữ liệu supply chain đầy đủ và chính xác để agent đưa ra quyết định đúng.
