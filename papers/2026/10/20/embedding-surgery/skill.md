# Skill: embedding-surgery
Source: 2609.05110v1
Type: framework

## Khi nào dùng skill này
- Hệ thống truy xuất dense (tìm kiếm, đềovas, RAG) cần sửa lỗi xếp hạng cụ thể theo từng truy vấn mà không retraining hay re-indexing.
- Có tín hiệu phản hồi (biên soạn, tương tác người dùng, nhãn giả từ LLM) để xác định tài liệu liên quan hơn/ít liên quan hơn.
- Muốn áp dụng cập nhật cục bộ, tối thiểu vào embedding tài liệu tại thời điểm truy vấn.

## Tình huống KHÔNG nên dùng
- Giả định embedding tài liệu cố định không bao giờ cần thay đổi (không có phản hồi hoặc ý định tìm kiếm ổn định hoàn toàn).
- Dùng nhãn giả từ LLM làm duy nhất nguồn phản hồi mà không kiểm tra chất lượng (LLM labels có điểm yếu hệ thống).

## Input cần có
- Hệ thống truy xuất dense với embedding tài liệu đã lập chỉ mục (FAISS, HNSW, IVF, v.v.).
- Tín hiệu phản hồi: phán xét biên soạn, tương tác người dùng (nhấp chuột), hoặc nhãn giả từ LLM reranker (BGE, Qwen).
- Bộ giải bài toán tối ưu hóa凸 (CVXPY hoặc tương đương) trên CPU đơn.
- Ngân sách tính toán mỗi truy vấn (phẫu thuật embedding diễn ra độc lập cho mỗi truy vấn).

## Các bước thực hiện
1. Truy xuất top-k tài liệu cho truy vấn (ví dụ k=20) qua hệ thống dense retrieval hiện có.
2. Nhận tín hiệu phản hồi cho truy vấn: xác định cặp ưu tiên (dr, dn) trong đó dr nên xếp hạng trên dn (từ biên soạn, tương tác người dùng mô phỏng, hoặc LLM reranker).
3. Diễn giải bài toán tối ưu hóa凸: tối thiểu hoá tổng ∥Δdi∥2^2 qua các tài liệu trong top-k, dự phó với ràng buộc ⟨q, dr + Δdr⟩ ≥ ⟨q, dn + Δdn⟩ + ε cho mọi cặp (dr, dn) ∈ R.
4. Chọn biến thể phẫu thuật: đối xứng (cả hai đều điều chỉnh — mặc định, hiệu quả nhất), hạ thấp (chỉ sửa embedding tài liệu ít liên quan hơn), nâng cao (chỉ sửa embedding tài liệu liên quan hơn).
5. Giải quyết bài toán tối ưu hàm bậc hai (CVXPY) để lấy các cập nhật Δdi.
6. Áp dụng cập nhật ngay vào chỉ mục (in-place overwriting): d'i = di + Δdi, chỉ sửa embedding của các tài liệu trong ràng buộc, tất cả embedding khác không đổi.
7. Tính toán lại xếp hạng với embedding đã sửa và trả về kết quả cho truy vấn.
8. (Tùy chọn) Kết hợp với CoRocchio (thích ứng truy vấn) để sinh thêm điểm gain.

## Output mong đợi
- Độ chính xác xếp hạng (nDCG@10) cải thiện nhất quán, lên đến +60.64% tương đối (TAS-B trên DL-Hard dưới phản hồi biên soạn); cập nhật cục bộ, bảo toàn cấu trúc tổng thể không gian nhúng, áp dụng an toàn trên chỉ mục ANN (IVF, HNSW) mà không cần lập chỉ mục lại.

## Ví dụ áp dụng
- Hệ thống tìm kiếm tài liệu doanh nghiệp: khi người dùng cho phản hồi rằng kết quả thứ 3 liên quan hơn kết quả thứ 1, áp dụng embedding surgery để nâng cao embedding tài liệu thứ 3 và/hoặc hạ thấp tài liệu thứ 1, rồi sắp xếp lại kết quả cho cùng truy vấn trong tương lai.

## Gotchas
- Không dùng nhãn giả từ LLM làm duy nhất nguồn phản hồi không kiểm tra (LSTM/LLM labels có điểm yếu hệ thống, không thể thay thế hoàn toàn đánh giá con người).
- Phản hồi gần ngẫu nhiên (Near-Random) cho lợi ích hạn chế và có thể làm kém hiệu quả trên một số tập (Robust '04).
- Không quên bảo toàn cấu trúc tổng thể không gian nhúng — cập nhật phải tối thiểu (minimize ∥Δdi∥2^2).
- Không retraining hay re-indexing sau mỗi phản hồi — đó là điểm mạnh của embedding surgery.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 8 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 3 (diễn giải bài toán tối ưu hóa凸 với ràng buộc xếp hạng) cần triển khai cụ thể với CVXPY.
- Input section có đủ không? [YES] — hệ thống truy xuất dense, tín hiệu phản hồi, bộ giải tối ưu hóa, ngân sách tính toán.

## Dry run (tình huống giả)
- Tình huống: Hệ thống tìm kiếm nội bộ doanh nghiệp; người dùng báo kết quả thứ 3 liên quan hơn thứ 1 cho truy vấn "quy trình chốt hàng".
- Chạy skill: (1) Truy xuất top-20 tài liệu cho truy vấn; (2) xác định cặp (thứ 3, thứ 1) từ phản hồi; (3) diễn giải bài toán tối ưu hóa凸 với ràng buộc xếp hạng thứ 3 trên thứ 1; (4) chọn biến thể đối xứng; (5) giải quyết bằng CVXPY, lấy Δembedding; (6) áp dụng in-place overwriting vào chỉ mục; (7) tính toán lại xếp hạng và trả về kết quả đã sửa.

## Verdict: [SKILL VALID]
