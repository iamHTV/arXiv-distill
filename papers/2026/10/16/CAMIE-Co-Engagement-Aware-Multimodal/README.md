# [2608.30255v1] CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retrieval

## Problem
Hệ thống quảng cáo sản phẩm động (DPA - Dynamic Product Ads) của Snap cần lấy	item (mục hàng) phù hợp với người dùng dựa trên ảnh và văn bản sản phẩm. Các encoder đa phương (multimodal encoder) hiện có không tận dụng được tín hiệu co-engagement (tương tác cùng nhau) — việc người dùng tương tác với cùng một item trong nhiều ngữ cảnh khác nhau.

## Contribution
- Giới thiệu CAMIE: Co-Engagement-Aware Multimodal Item Embeddings (nhúng đa phương nhận thức tương tác cùng nhau), dùng LLM/MLLM backbone fine-tune trên cặp item cùng tương tác để làm embedding multimodal cho quảng cáo DPA của Snap.
- CAMIE thay thế trực tiếp (drop-in replacement) hai content-based I2I encoder, đã triển khai production.
- Online A/B tests: +0.390% CTR / +10.832% CVR over multimodal control, +18.958% CTR / +13.12% CVR over text control, +0.211% CTR / +1.911% CVR on overall DPA traffic.

## Method (tóm cốt lõi)
CAMIE fine-tune MLLM backbone trên cặp item mà người dùng tương tác cùng nhau (co-engagement pairs), thay vì chỉ dùng nhãn nội dung tĩnh. Content-derived labels (nhãn lấy từ nội dung) thay vì nhãn theo compute. Học embedding multimodal (ảnh + văn bản) với dimension d=512 (smaller embedding so với Gemini Embedding 2 d=3072). Fine-tune Gemma 4 E2B đạt 108.2% R@10 với multimodal input.

## Key Findings
- Production A/B: +0.390% CTR / +10.832% CVR over multimodal control; +18.958% CTR / +13.12% CVR over text control; +0.211% CTR / +1.911% CVR on overall DPA traffic.
- Co-engagement fine-tuning adds 37.7% relative gain to MLLM.
- R@10: CAMIE 137.7% vs pretrained checkpoint 100.0%; improves ~6% relative over Gemini Embedding 2 (129.9%) while using smaller embeddings (d=512 vs d=3072).
- Measurable gain is entirely in conversion: CVR rises +10.832% while CTR change (+0.390%) is not significant, indicating co-engagement supervision makes items more clickable-relevant.

## Actionable Insights
- Dùng co-engagement supervision (huấn luyện theo tương tác cùng nhau) thay vì chỉ dùng nhãn nội dung tĩnh: giúp embedding multimodal học được mối quan hệ giữa các item người dùng thực sự xem cùng nhau. Áp dụng: solopreneur làm hệ thống gợi ý sản phẩm/content nên thu thập cặp item cùng được xem/mua trong cùng phiên và fine-tune embedding model trên đó.
- Thay thế hai encoder riêng biệt (text-only, image-only) bằng unified multimodal checkpoint: giảm chi phí phục vụ (serving) mà không mất nhiều chất lượng (khoảng 1.1pp trên R@10, 0.5pp trên MRR). Áp dụng: khi xây hệ thống retrieval, hãy gộp các encoder thành một checkpoint multimodal duy nhất để tiết kiệm chi phí triển khai.

## Assumptions & Limitations
- Điều kiện: cần có dữ liệu co-engagement pairs (cặp item cùng tương tác) đủ lớn để fine-tune; không áp dụng nếu không có lịch sử tương tác người dùng.
- Paper thừa nhận: spread across backbones là 5.8% relative từ tốt nhất đến kém nhất, chống lại 37.7% relative gain từ co-engagement fine-tuning.
- Limitation paper không nói: chưa đánh giá trên các mặt hàng ngoài quảng cáo Snap, chưa test trên mô hình nhỏ hơn Gemma 4 E2B.

## Metadata
- Năm: 2026
- Tác giả: Xiaodong Liu, Xiao Bai, Yunzhi Zhou, Siman Wang, Congfei Zhang, Wen Zhang, Yajun Wang, Jingxiao Ma, Jinchao Li, Hsiang-wei Chao (Snap Inc.)
- Category arXiv: cs.AI, cs.IR
- Link PDF: https://arxiv.org/pdf/2608.30255
