# Skill: unreal-internal-evidence-selection
Source: 2610.08463v1
Type: framework

## Khi nào dùng skill này
- Xây dựng hệ thống truy xuất và suy luận ngữ cảnh dài dùng cùng một mô hình (single model) thay vì hai mô hình riêng (trình truy xuất + LLM).
- Cần chọn bằng chứng (evidence selection) ở cả thang độ corpus (truy xuất từ hàng triệu đoạn văn bản) và thang độ ngữ cảnh dài (suy luận trên prompt dài).
- Có thể thêm ít hơn 500K tham số có thể huấn luyện lên trên backbone LLM đóng băng.

## Tình huống KHÔNG nên dùng
- Cần đào tạo lại toàn bộ mô hình (full fine-tuning) thay vì chỉ thêm tham số nhỏ.
- Không có quyền truy cập vào các trạng thái nội bộ (internal states/residual stream) của LLM.
- Nhiệm vụ không liên quan đến việc lựa chọn bằng chứng (ví dụ: sinh văn bản thuần túy).

## Input cần có
- Mô hình LLM đóng băng (frozen LLM) với quyền truy cập vào residual stream.
- Tập hợp đoạn văn bản ứng viên (candidate chunks) để mã hóa.
- Truy vấn truy xuất (retrieval query).
- Hàm tổn thất đối lập (contrastive loss) để đào tạo soft prompt và trọng số lớp.

## Các bước thực hiện
1. Mã hóa các đoạn văn bản ứng viên (candidate chunks) từ các trạng thái nội bộ (internal states) của LLM đóng băng.
2. Lấy các truy vấn truy xuất (retrieval queries) trực tiếp từ các trạng thái nội bộ của LLM.
3. Thêm soft prompt để khơi gợi chế độ truy xuất (retrieval mode) và trọng số lớp (layer weights) kết hợp các trạng thái nội bộ cho việc xếp hạng bằng chứng (evidence ranking).
4. Đào tạo bằng tổn thất đối lập (contrastive loss) trên backbone đóng băng.
5. Tại thang độ corpus: truy xuất từ chỉ mục Wikipedia 21M đoạn văn bản (3B token).
6. Tại thang độ ngữ cảnh dài: xếp hạng các đoạn văn bản trong prompt dài và chỉ trả về văn bản đã chọn cho cùng một LLM đóng băng để trả lời.

## Output mong đợi
- Hệ thống chọn bằng chứngingle mô hình cho cả truy xuất corpus và suy luận ngữ cảnh dài.
- Recall cải thiện: HotpotQA 49.1%→73.2%, 2WikiMultiHopQA 31.7%→60.1%, MuSiQue 8.8%→14.4%.
- Độ chính xác ngữ cảnh dài cải thiện: NoLiMa 1.0%→24.83% (128K token), LV-Eval F1 49.97%→54.66% (256K).
- Giảm FLOPs và thời gian đến token đầu tiên (time-to-first-token) từ khoảng 32K token trở đi.

## Ví dụ áp dụng
- Xây dựng hệ thống hỏi đáp trên tài liệu dài: dùng UNREAL để xếp hạng các đoạn văn bản trong prompt dài và chỉ trả về các đoạn liên quan cho LLM tạo câu trả lời, thay vì đưa toàn bộ prompt dài vào mô hình.

## Gotchas
- Đánh giá trên 4 xương sống (backbone models).
- Corpus là Wikipedia (3B token, 21M đoạn văn bản).
- Các tác vụ ngữ cảnh dài: NoLiMa, LV-Eval, HELMET.
- Thêm ít hơn 500K tham số có thể huấn luyện — không phải giải pháp không có tham số (zero-parameter).
