# 2609.24152 — Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search at Scale

## Giá trị cốt lẽ (1 câu)

Grad-CIR là phương pháp huấn luyện hệ thống truy xuất hình ảnh kết hợp (composed image retrieval, CIR) trên độ liên quan phân cấp (graded relevance) thay vì nhị phân — sử dụng VLM để tự động tạo dữ liệu huấn luyện và nhãn liên quan 4 cấp, vòng phản hồi liên quan lặp đi lặp lại để khai thác hard negative, và mục tiêu góc có nhận thức phân cấp (hierarchy-aware angular objective) — đạt tăng 4,9%–5,9% NDCG@10 so với nhãn nhị phân, và đã được triển khai production tại Walmart phục vụ lưu lượng tìm kiếm trực quan thực.

## Problem

Tìm kiếm trực quan trên các danh mục thương mại điện tử lớn phải phục vụ cả truy vấn "tương tự" (similarity) và truy vấn "thay đổi" (modifier) — zusamm hợp hình ảnh và văn bản mô tả sự thay đổi mong muốn (ví dụ: thay đổi màu sắc hoặc phong cách). Các phương pháp CIR hiện tại coi liên quan (relevance) là nhị phân và huấn luyện trên triplet với một mục tiêu dương duy nhất — không phù hợp với danh mục thực tế nơi nhiều ứng viên thỏa mãn một phần truy vấn, và xếp hạng trên espectrum sự khớp phần mẫu quyết định trải nghiệm khách hàng.

## Contribution

1. **Grad-CIR**: Phương pháp huấn luyện CIR retriever trên độ liên quan phân cấp, gồm 3 thành phần: (i) VLM để quản lý dữ liệu huấn luyện, tạo truy vấn (phát hiện đối tượng + tổng hợp sửa đổi) và nhãn liên quan 4 cấp mà không cần chú thích thủ công, (ii) vòng phản hồi liên quan lặp lại mở rộng tập huấn luyện bằng cách khai thác hard negative từ retriever đang trong quá trình huấn luyện, (iii) mục tiêu góc có nhận thức phân cấp để huấn luyện retriever trực tiếp trên nhãn phân cấp thay vì sụt noi chúng thành nhị phân.
2. **Triển khai trên PaliGemma2**: Được triển khai trên PaliGemma2 bi-encoder được huấn luyện trên 3,5M cặp phân cấp được quản lý từ dữ liệu danh mục Walmart thô.
3. **Kết quả thí nghiệm**: Khảo sát bịt (ablation) có kiểm soát phân cấp vs nhị phân cho thấy tăng 4,9%–5,9% trong NDCG@10. Cùng công thức áp dụng cho các encoder đa phương thức khác nâng các backbone early-fusion lên đến 8,5% NDCG@10. Trên tiêu chuẩn công khai FashionIQ, GradCIR (áp dụng cho PaliGemma2) đạt mức ghi nhớ trung bình 0,6703 khi được tinh chỉnh, vượt qua một chút strong baseline được đánh giá đồng nghiệp nhất mà chúng ta so sánh, và khớp hoặc vượt tất cả phương pháp CIR zero-shot lớp CLIP-L đã công bố.
4. **Triển khai production**: Hệ thống đã được triển khai production tại Walmart, đang phục vụ lưu lượng tìm kiếm trực quan thực.

## Method

Grad-CIR bao gồm 3 thành phần chính:

1. **VLM curate dữ liệu huấn luyện**: Sử dụng VLM để tạo truy vấn (phát hiện đối tượng + tổng hợp sửa đổi) và nhãn liên quan 4 cấp mà không cần chú thích thủ công.

2. **Vòng phản hồi liên quan lặp lại (iterative relevance-feedback loop)**: Mở rộng tập huấn luyện bằng cách khai thác hard negative từ retriever đang trong quá trình huấn luyện.

3. **Mục tiêu góc có nhận thức phân cấp (hierarchy-aware angular objective)**: Huấn luyện retriever trực tiếp trên nhãn liên quan phân cấp thay vì sụt noi chúng thành nhị phân.

**Quy trình:** Thu thập dữ liệu thô từ danh mục → VLM tạo truy vấn và nhãn phân cấp → Huấn luyện retriever với mục tiêu góc phân cấp → Vòng phản hồi khai thác hard negative → Mở rộng tập huấn luyện → Lặp lại.

## KNOWLEDGE — Số liệu & khái niệm

- 3,5M cặp phân cấp được quản lý từ dữ liệu danh mục Walmart thô.
- Mô hình: PaliGemma2 bi-encoder.
- Tăng 4,9%–5,9% NDCG@10 so với nhãn nhị phân (ablation có kiểm soát).
- Nâng các backbone early-fusion lên đến 8,5% NDCG@10 khi áp dụng cho các encoder đa phương thức khác.
- FashionIQ benchmark: 0,6703 average recall khi tinh chỉnh GradCIR (áp dụng cho PaliGemma2).
- Vượt strong baseline được đánh giá đồng nghiệp nhất; khớp hoặc vượt tất cả phương pháp CIR zero-shot lớp CLIP-L.
- Triển khai production tại Walmart phục vụ lưu lượng tìm kiếm trực quan thực.

## INSIGHT — Cơ chế & tại sao

[Graded relevance tốt hơn binary relevance] xảy ra VÌ [trong danh mục thực tế, nhiều ứng viên thỏa mãn một phần truy vấn và xếp hạng trên espectrum sự khớp phần mẫu quyết định trải nghiệm khách hàng; nhị phân bỏ qua sự phân cấp này]. Điều này nghĩa là [huấn luyện trên nhãn liên quan phân cấp giúp retriever xếp hạng tốt hơn các ứng viên khớp phần mẫu].

[VLM tự động tạo dữ liệu huấn luyện] xảy ra VÌ [VLM có thể tạo truy vấn và nhãn liên quan 4 cấp mà không cần chú thích thủ công, giảm chi phí chú thích dữ liệu]. Điều này nghĩa là [có thể mở rộng dữ liệu huấn luyện CIR mà không cần chi phí lao động lớn].

[Vòng phản hồi liên quan khai thác hard negative] xảy ra VÌ [retriever đang trong quá trình huấn luyện có thể xác định các mẫu khó (hard negatives) để mở rộng tập huấn luyện]. Điều này nghĩa là [huấn luyện liên tục cải thiện retriever bằng cách tập trung vào các trường hợp khó].

## IDEA — Áp dụng được gì

1. Áp dụng graded relevance vào hệ thống tìm kiếm sản phẩm: Thay vì chỉ nhãn có/không, hãy tạo nhãn liên quan 4 cấp (ví dụ: hoàn toàn khớp, khớp phần lớn, khớp một phần, không khớp) cho các cặp truy vấn-sản phẩm. Bước đầu: dùng VLM để tự động gán nhãn liên quan phân cấp cho cặp truy vấn-sản phẩm hiện có.

2. Dùng vòng phản hồi liên quan để cải thiện retriever: Khi retriever đang trong quá trình huấn luyện, hãy khai thác hard negative từ các kết quả truy xuất để mở rộng tập huấn luyện. Bước đầu: sau mỗi эпоch huấn luyện, lấy các mẫu mà retriever xếp hạng sai và thêm vào tập huấn luyện.

3. Áp dụng mục tiêu góc phân cấp vào mô hình truy xuất đa phương thức: Thay vì huấn luyện trên nhãn nhị phân, hãy dùng mục tiêu góc có nhận thức phân cấp để huấn luyện trực tiếp trên nhãn liên quan phân cấp. Bước đầu: thay đổi hàm loss của mô hình truy xuất từ binary contrastive loss sang hierarchy-aware angular loss.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Trong hệ thống truy xuất đa phương thức, nhãn liên quan phân cấp giúp mô hình xếp hạng tốt hơn các ứng viên khớp phần mẫu so với nhãn nhị phân — sự khớp một phần vẫn mang giá trị cho khách hàng.
- Khi nào dùng: Khi xây dựng hệ thống tìm kiếm hoặc truy xuất đa phương thức nơi nhiều ứng viên có thể thỏa mãn một phần truy vấn.
- Khi nào KHÔNG dùng: Khi truy vấn chỉ có một đáp án đúng rõ ràng và không có khái niệm khớp phần mẫu.
- Ví dụ áp dụng ngoài domain gốc: Trong hệ thống đề xuất phim, thay vì chỉ nhãn "xem/không xem", hãy dùng nhãn liên quan phân cấp (xem hết, xem nửa, xem một chút, không xem) để hệ thống đề xuất tốt hơn các phim khách hàng quan tâm một phần.

## Assumptions & Limitations

- Điều kiện phải đúng: có dữ liệu danh mục lớn để quản lý bằng VLM; có thể đo NDCG@10 làm metrics.
- Limitation paper thừa nhận: thí nghiệm trên tập dữ liệu Walmart và FashionIQ; có thể không đại diện cho tất cả các loại danh mục thương mại điện tử.
- Limitation paper KHÔNG nói: chi phí chạy VLM để quản lý dữ liệu ở quy mô lớn; hiệu quả trên các truy vấn không phải hình ảnh + văn bản; tính generalize qua các domain khác ngoài thương mại điện tử.

## Metadata

- Năm: 2026
- Tác giả: Hrushikesh Mohapatra, Anubhav Gupta, Prijith Chandra, Asish Mohapatra, Sudip Datta, Anuj Garg, Venkat Bulusu, Arvind Maan, Sitesh Kumar Jalan
- Category arXiv: cs.AI / cs.IR (Walmart Global Tech)
- Link PDF: https://arxiv.org/pdf/2609.24152
- Citation count: chưa có (paper mới, Oct 2026)