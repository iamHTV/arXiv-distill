# Skill: co-engagement-multimodal-embedding-ads
Source: 2608.30255v1
Type: workflow

## Khi nào dùng skill này
- Xây hệ thống gợi ý sản phẩm/content (recommendation/retrieval) có hình ảnh và văn bản.
- Có dữ liệu người dùng tương tác với cùng nhiều item trong một phiên (co-engagement pairs).
- Muốn cải thiện chất lượng retrieval mà không tăng chi phí phục vụ.

## Tình huống KHÔNG nên dùng
- Không có dữ liệu tương tác người dùng (chỉ có nội dung tĩnh).
- Chỉ làm retrieval văn bản thuần hoặc ảnh thuần, không cần multimodal.

## Input cần có
- Dữ liệu item có ảnh và văn bản mô tả.
- Lịch sử tương tác người dùng: cặp item cùng được xem/mua/nhấp trong cùng phiên.
- Mô hình MLLM/embedding backbone có thể fine-tune.

## Các bước thực hiện
1. Thu thập cặp item cùng tương tác (co-engagement pairs): hai item người dùng xem hoặc mua trong cùng phiên.
2. Fine-tune MLLM/embedding backbone trên các cặp này với content-derived labels (nhãn từ nội dung tương tác), không dùng nhãn tĩnh.
3. Xây unified multimodal checkpoint thay cho hai encoder riêng biệt (text-only + image-only).
4. Thay thế trực tiếp (drop-in replacement) encoder cũ trong hệ thống retrieval đang chạy.
5. Đo CTR/CVR trên A/B test để xác nhận hiệu quả.

## Output mong đợi
- Tăng CVR +10.832% và CTR +0.390% so với multimodal control (trong sản phẩm Snap).
- Tăng CTR +18.958% và CVR +13.12% so với text-only control.
- Giảm chi phí phục vụ bằng cách gộp hai encoder thành một multimodal checkpoint (khoảng 1.1pp R@10, 0.5pp MRR chênh lệch).

## Ví dụ áp dụng
Solopreneur làm trang gợi ý sản phẩm thời trang: thu thập cặp sản phẩm cùng được khách hàng xem trong cùng phiên (ví dụ áo + quần), fine-tune embedding model học rằng hai sản phẩm này đi cùng nhau. Thay thế hai encoder cũ (một encoder ảnh, một encoder văn bản) bằng một multimodal checkpoint duy nhất. Hệ thống gợi ý chính xác hơn, chi phí triển khai thấp hơn.

## Gotchas
- Lợi ích đo được chủ yếu nằm ở conversion (CVR +10.832%), CTR thay đổi không đáng kể (+0.390%) so với multimodal control — co-engagement giúp item phù hợp hơn, không nhất là nhấp nhiều hơn.
- Cần đủ dữ liệu co-engagement pairs; nếu dữ liệu ít, fine-tune không hiệu quả.
- Chênh lệch giữa các backbone là 5.8% relative, nhỏ hơn lợi ích 37.7% từ co-engagement fine-tuning — nên tập trung vào dữ liệu tương tác chứ không phải chọn backbone.
