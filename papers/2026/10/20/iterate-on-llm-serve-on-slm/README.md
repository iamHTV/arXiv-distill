# [2610.14576v1] Iterate on an LLM, Serve on an SLM

## Giá trị cốt lõi (1 câu)
Phát triển hành vi agent trong prompt space (không gian câu lệnh) trên mô hình frontier (mô hình ranh giới/tiền tiến), rồi distill (chưng cất kiến thức) hành vi đã ổn định vào SLM (mô hình ngôn ngữ nhỏ) nhỏ và rẻ qua dữ liệu production thực — không phải dữ liệu tổng hợp (synthetic data).

## Problem
Prior work chưa giải quyết được việc lấy đúng hành vi từ SLM (mô hình ngôn ngữ nhỏ) cho tác vụ agent hẹp, lặp lại, vì mỗi lần hành vi thay đổi thì phải retraining (huấn luyện lại) model từ đầu — tốn ngày/tuần, trong khi engineer thường mặc định dùng model lớn hơn chỉ vì nó "chạy được ngay".

## Contribution
- Phương pháp 2 giai đoạn: (1) phát triển hành vi trong prompt space trên frontier model với phản hồi ngay từ live traffic (tín hiệu lưu lượng thực), (2) distill hành vi đã hội tụ vào SLM qua SFT (chỉnh sửa dưới sự giám sát) trên dữ liệu production đã ghi lại (recorded production behavior), không dùng dữ liệu tổng hợp.
- Dùng self-agreement (tính nhất quán tự đồng ý) của teacher (mô hình giáo/dạy) trên các bản ghi riêng lẻ làm noise floor (sàn tiếng/Components nhiễu) để quyết định SLM đủ tốt để chạy production hay chưa.
- Case study thực tế trên tác vụ phân loại yes/no cho gỡ ca làm việc (caregiver-shift) tại home-care agency, với đánh giá mù (blinded evaluation) bởi người điều phối chuyên nghiệp.

## Method
Pipeline 2 giai đoạn. Giai đoạn 1: agent chạy trên GPT-5.4-nano, mỗi thay đổi prompt được kiểm tra ngay qua live traffic, mọi trace (dòng vết thực thi) được lưu lại. Giai đoạn 2: khi hành vi ổn định, hệ thống replay (phát lại byte-exact) từng batch đã ghi lại bằng cùng prompt builder và serializer mà live evaluator dùng, tạo ra ngữ cảnh chat giống hệt thời điểm phục vụ, rồi ghép với tool call (lệnh gọi công cụ) đã ghi lại làm mục tiêu (target). Contract filtering (lọc theo hợp đồng) loại bỏ mẫu whose reasoning thiếu lý do xung đột cứng (hard-conflict justification), deduplicate (loại trùng), giữ quyết định mới nhất, chia train/validation theo source batch. Cuối cùng LoRA-tune (tinh chỉnh cấp thấp) Qwen3-4B và Qwen3-8B trên corpus này. Gate duyệt: SLM phải vượt self-agreement của teacher (72.7%) và vượt đánh giá mù con người.

## KNOWLEDGE — Số liệu & khái niệm
- Teacher GPT-5.4-nano tự đồng ý với bản thân chỉ 72.7% (95% CI 0.65–0.79) khi chạy lại các prompt đã ghi lại → noise floor (sàn nhiễu) của teacher.
- Tuned Qwen3-8B đạt 0.913 agreement (95% CI 0.89–0.93) trên 880 trường hợp validation, nhất quán với trace production hơn chính teacher.
- Tuned Qwen3-4B: 0.863 agreement nhưng 12% malformed output (kết quả sai định dạng) → không dùng được production.
- Base Qwen3-8B zero-shot (không tinh chỉnh): 0.774 agreement*, 23% malformed output, latency 14.9s p50.
- Người điều phối chuyên nghiệp phê student 48 lần vs teacher 29 lần trên 77 trường hợp bất đồng (62%–38%, p=0.040).
- Corpus huấn luyện: 549 production batches, 11,621 train + 1,604 validation examples, 17 tổ chức.
- Chi phí: teacher ~$1.9–7.7 trên 1.000 quyết định (tùy trạng thái cache prompt), SLM ~$0.19–0.38 trên 1.000.
- Độ trễ: teacher 7.1s p50 / 13.1s p95, SLM tuned 8B 2.9s p50 / 4.3s p95 (~2.5× nhanh hơn).
- Huấn luyện: LoRA, khoảng 1.023 bước tối ưu hóa (optimizer steps), khoảng 1B token huấn luyện, context tối đa 65,536. Eval loss cuối: 0.534 (4B), 0.254 (8B).

## INSIGHT — Cơ chế & tại sao
[SLM đạt agreement cao hơn teacher] VÌ [teacher không deterministic (không xác định), chỉ đồng ý với bản thân 72.7% thời gian, nên đóng vai trò noisy annotator (nhãn giả có tiếng/Components nhiễu) chứ không phải ground truth (sự thật nền tảng)]. Điều này nghĩa là [SLM có thể được huấn luyện để ổn định hơn chính teacher đã định nghĩa nó].
[Base SLM zero-shot thất bại 23% trường hợp do malformed output] VÌ [SLM chưa được điều chỉnh cho contract/định dạng cụ thể của tác vụ]. Điều này nghĩa là [zero-shot SLM không phải lựa chọn khả thi, phải fine-tune (tinh chỉnh)].
[Phát triển hành vi trong prompt space trong phút-giây so với ngày-tuan retraining] VÌ [thay đổi prompt có phản hồi ngay từ live traffic, không cần huấn luyện lại trọng số mô hình]. Điều này nghĩa là [vòng lặp thiết kế hành vi agent nên diễn ra ở mức prompt, không phải mức weight (trọng số)].

## IDEA — Áp dụng được gì
Áp dụng quy trình 2 giai đoạn vào phân loại lead (tiêm khách tiềm năng) cho gọi điện bán hàng: bước đầu là dùng frontier model để thiết kế prompt quyết định lead chất lượng cao, thu trace production từ cuộc gọi thật, rồi distill vào SLM nhỏ để chạy hàng ngàn cuộc gọi/ngày với chi phí thấp.
Áp dụng contract filtering khi xây dựng dữ liệu huấn luyện SLM từ production trace: bước đầu là định nghĩa hard-conflict justification (lý do xung đột cứng) trong reasoning trace (dòng vết suy luận), loại mẫu không có lý do này trước khi SFT.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Phát triển hành vi agent ở mức prompt (rẻ, nhanh), compile (biên dịch) thành SLM qua dữ liệu production thực (không phải synthetic data) khi hành vi đã ổn định. Áp dụng khi tác vụ hẹp, lặp lại, chạy hàng ngàn lần/ngày. KHÔNG áp dụng khi hành vi còn thay đổi liên tục hoặc tác vụ cần reasoning rộng mở.

## Assumptions & Limitations
- Điều kiện đúng: tác vụ là yes/no classification hẹp, có production trace đã ghi lại, hành vi đã hội tụ (không thay đổi liên tục).
- Limitation paper thừa nhận: model chưa phục vụ production traffic thực, mọi số là offline replay; ground truth từ một người điều phối duy nhất; không mô hình hóa tương quan giữa các trường hợp từ cùng tổ chức/batch; chỉ bao quát một subtask, một domain, một teacher.
- Limitation paper KHÔNG nói: chi phí lưu trữ trace production hàng ngàn batch; thời gian thu thập đủ trace để hành vi ổn định; tác động của prompt-cache dynamics và traffic mix trong online A/B.

## Metadata
- Năm: 2026
- Tác giả: Keegan Wang (Carnegie Mellon University)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.14576v1
- arXiv ID: 2610.14576v1
- Nhãn: [applied]
- Skill: iterate-on-llm-serve-on-slm | Test: [SKILL VALID]
