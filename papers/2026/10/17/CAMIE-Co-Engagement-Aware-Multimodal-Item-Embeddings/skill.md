# Skill: camie-co-engagement-embedding
Source: 2608.30255v1
Type: framework

## Khi nào dùng skill này
- Xây dựng hệ thống gợi ý/quảng cáo dùng truy xuất mục-đến-mục (item-to-item, I2I retrieval).
- Cần căn chỉnh embedding với hành vi tương tác chung (co-engagement behavior) thúc đẩy chuyển đổi (conversion).
- Có dữ liệu hành trình người dùng (user journeys) với các cặp mục tương tác chung.

## Tình huống KHÔNG nên dùng
- Hệ thống gợi ý không dùng I2I retrieval.
- Không có dữ liệu tương tác chung từ hành trình người dùng.
- Không cần căn chỉnh embedding với chuyển đổi thực tế.

## Input cần có
- Dữ liệu catalog mục với hình ảnh và metadata.
- Dữ liệu hành trình người dùng chứa các cặp mục tương tác chung.
- Xương sống LLM/MLLM với giao diện multimodal bản địa.

## Các bước thực hiện
1. Xây dựng không gian embedding chung từ hình ảnh mục và metadata dùng giao diện multimodal của xương sống LLM/MLLM.
2. Khai thác các cặp mục tương tác chung từ hành trình người dùng.
3. Điều chỉnh lại xương sống trên các cặp mục tương tác chung với mục tiêu InfoNCE đối xứng trong-lô (symmetric in-batch InfoNCE).
4. Phục vụ cả truy xuất multimodal và chỉ-văn-bản từ cùng một checkpoint.
5. Giám sát Recall@10 (offline) và CTR/CVR (online).

## Output mong đợi
- Hệ thống I2I retrieval với Recall@10 cao hơn mô hình embedding multimodal thương mại mạnh nhất.
- CTR/CVR tăng trực tuyến: +0,390% CTR / +10,832% CVR so với điều khiển multimodal; +18,958% CTR / +13,12% CVR so với điều khiển văn bản; +0,211% CTR / +1,911% CVR trên lưu lượng tổng thể.

## Ví dụ áp dụng
- Xây dựng hệ thống quảng cáo sản phẩm động (DPA) cho nền tảng thương mại điện tử. Dùng CAMIE để điều chỉnh lại embedding trên các cặp mục tương tác chung từ hành trình người dùng, giảm đoạn mảng hóa ngăn xếp truy xuất và cải thiện CTR/CVR.

## Gotchas
- Đánh giá trên hệ thống DPA của Snap, kết quả có thể không chuyển tiếp sang các hệ thống khác.
- Không có thông tin chi tiết về thời gian đào tạo và chi phí tính toán.
