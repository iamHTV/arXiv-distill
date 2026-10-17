# [2608.30255v1] CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retrieval

## Problem
- Truy xuất mục-đến-mục (item-to-item, I2I retrieval) là thành phần cốt lõi trong hệ thống gợi ý và quảng cáo quy mô lớn. Trong hệ thống quảng cáo sản phẩm động (Dynamic Product Ads, DPA) của Snap, I2I retrieval gặp hai thách thức: các encoder riêng biệt cho hình ảnh, văn bản, và multimodal đoạn mảng hóa ngăn xếp truy xuất (retrieval stack); và đào tạo chỉ dựa trên nội dung (content-only training) không căn chỉnh các embedding với hành vi tương tác chung (co-engagement behavior) thúc đẩy chuyển đổi sau này (downstream conversions).

## Contribtuion
- CAMIE — một khung làm việc embedding mục multimodal có ý thức tương tác chung (co-engagement-aware multimodal item embedding framework) cho truy xuất quảng cáo sản phẩm động (DPA) của Snap.
- CAMIE xây dựng trên xương sống (backbone) LLM/MLLM, sử dụng giao diện multimodal bản địa của chúng để biểu thị hình ảnh mục và metadata trong một không gian embedding chung.
- Sau đó điều chỉnh lại xương sống (fine-tune) trên các cặp mục tương tác chung (co-engaged item pairs) được khai thác từ hành trình người dùng (user journeys) với mục tiêu InfoNCE đối xứng trong-lô (symmetric in-batch InfoNCE objective).
- Ngoại tuyến (offline): CAMIE vượt quá mô hình embedding multimodal thương mại mạnh nhất trên Recall@10 và phục vụ truy xuất chỉ-văn-bản (text-only retrieval) từ cùng một checkpoint với tổn thất chất lượng tối thiểu.
- Trực tuyến (online): CAMIE phục vụ làm thay thế trực tiếp (drop-in replacement) cho hai encoder I2I dựa trên nội dung (content-based I2I encoders) đã triển khai, mang lại +0,390% CTR / +10,832% CVR so với điều khiển multimodal, +18,958% CTR / +13,12% CVR so với điều khiển văn bản, và +0,211% CTR / +1,911% CVR trên lưu lượng DPA tổng thể.
- CAMIE được triển khai trong sản xuất (deployed in production).

## Method (tóm tắt cốt lõi)
- Xây dựng trên xương sống LLM/MLLM, sử dụng giao diện multimodal bản địa để biểu thị hình ảnh mục và metadata trong không gian embedding chung.
- Điều chỉnh lại xương sống trên các cặp mục tương tác chung được khai thác từ hành trình người dùng với mục tiêu InfoNCE đối xứng trong-lô.
- Phục vụ cả truy xuất multimodal và chỉ-văn-bản từ cùng một checkpoint.

## Key Findings
- 12 tác giả từ Snap Inc., category arXiv: cs.IR.
- Offline: CAMIE vượt quá mô hình embedding multimodal thương mại mạnh nhất trên Recall@10.
- Online: +0,390% CTR / +10,832% CVR so với điều khiển multimodal; +18,958% CTR / +13,12% CVR so với điều khiển văn bản; +0,211% CTR / +1,911% CVR trên lưu lượng DPA tổng thể.
- CAMIE được triển khai trong sản xuất.

## Actionable Insights
1. Dùng co-engagement tuning (điều chỉnh dựa trên tương tác chung) để căn chỉnh embedding với hành vi chuyển đổi thực tế. Áp dụng: khi xây dựng hệ thống gợi ý/quảng cáo, hãy điều chỉnh lại embedding trên các cặp mục tương tác chung từ hành trình người dùng thay vì chỉ dùng nội dung.
2. Dùng multimodal backbone duy nhất để phục vụ cả truy xuất multimodal và chỉ-văn-bản. Áp dụng: dùng một xương sống LLM/MLLM duy nhất để phục vụ cả hai trường hợp thay vì duy trì nhiều ngăn xếp truy xuất riêng biệt.

## Assumptions & Limitations
- Đánh giá trên hệ thống DPA của Snap, kết quả có thể không chuyển tiếp sang các hệ thống gợi ý/quảng cáo khác.
- Không có thông tin chi tiết về thời gian đào tạo và chi phí tính toán.

## Metadata
- Năm: 2026, tác giả: Xiaodong Liu, Xiao Bai, Yunzhi Zhou, Siman Wang, Congfei Zhang, Wen Zhang, Yajun Wang, Jingxiao Ma, Jinchao Li, Hsiang-wei Chao, Zhe Liu, Yu Zhang (Snap Inc.), category arXiv: cs.IR, link PDF: https://arxiv.org/pdf/2608.30255v1
