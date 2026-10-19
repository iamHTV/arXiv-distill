# [2609.14896v1] Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning

## Giá trị cốt lõi (1 câu)
MODA (MOde-conditioned Diversity Alignment) là thuật toán RL hậu huấn luyện online cùng lúc tối ưu chất lượng và sự đa dạng của phản hồi: điều kiện mode qua token abstract trong một policy chia sẻ, mỗi mode đại diện cho một agent MARL cạnh tranh tạo ra output khác biệt, kèm cổng chất lượng tùy prompt để chống reward hacking.

## Problem
Prior work chưa giải quyết việc mode collapse (sự suy giảm dần sự đa dạng đầu ra) là phransழ của quá trình huấn luyện khăn chỉnh (alignment) LLM: model thuần túy hạn bị thu hẹp không gian biểu đạt tại thời điểm suy luận, hạn chế các ứng dụng cần khám phá mở và nhận thức đa dạng như ý tưởng khoa học và viết sáng tạo.

## Contribution
- Giới thiệu MODA, thuật toán RL hậu huấn luyện online cùng lúc tối ưu chất lượng và sự đa dạng, lấy cảm hứng từ quan điểm phối hợp trong RL đa agent (MARL).
- Huấn luyện một policy LLM chia sẻ đơn với điều kiện theo token mode abstract; mỗi mode đóng vai trò một agent cạnh tranh tạo ra output khác nhau về những vùng bổ sung nhau của không gian đầu ra chất lượng cao, không cần persona thủ công hay sửa đổi kiến trúc.
- Cổng chất lượng tùy prompt (prompt-adaptive quality gating): điều chỉnh ngưỡng chất lượng so với policy tham chiếu đóng băng, chỉ trao thưởng đa dạng cho các phản hồi đạt ngưỡng, ngăn hành vi hack thưởng như chuyển đổi ngôn ngữ và verbosity.
- Đánh giá trên benchmark toàn diện bùm 7 tác vụ năng lực chung và 4 tác vụ đa dạng chuyên ngành (ý tưởng khoa học, viết sáng tạo).

## Method
MODA sử dụng điều kiện mode: điền các mã định danh vai trò (role identifiers) vào đầu prompt hệ thống, một policy chung πθ(y | zi, x) được điều kiện theo mã vai trò zi, tất cả các role tham số θ. Trong quá trình huấn luyện, mỗi role tạo một phản hồi cho K prompt trong batch, tạo thành nhóm phản hồi Yx = {yi,k}. Mỗi phản hồi nhận phần thưởng Quality-Gated Diversity Reward gồm 4 thành phần: phần thưởng chất lượng, cổng chất lượng tùy prompt, điểm đa dạng theo cấp phản hồi, và phạt rõ ràng chống hack thưởng. Policy được tối ưu bằng GRPO (Group Relative Policy Optimization) với KL regularization đến policy cơ sở. Cổng chất lượng: điểm chất lượng si = Sϕ(x, yi) từ mô hình thưởng tham chiếu; ngưỡng τq(x) = smin + α(smax − µref), σq(x) = γ(µref − smin + ϵ); cổng nhị phân g(x, yi) = 1[si ≥ τq(x)]; phần thưởng chất lượng rqual = µ tanh((si − τq(x))/σq(x)). Điểm đa dạng: khoảng cách ngữ nghĩa chuẩn hóa đến phương án gần nhất trong nhóm phản hồi d(x, yi, Y) = minj≠i (1 − ei⊤ej/2). Phạt: rlen (dộ dài quá nhiều), rlang (sai ngôn ngữ), rfmt (sự sọn thất định dạng/tràn nhãn role). Hai chế độ suy luận: chuẩn (không có mã role → phản hồi đơn) và đa dạng (nhiều mã role → tập ứng viên đa dạng).

## KNOWLEDGE — Số liệu & khái niệm
- Mode collapse: mất dần sự đa dạng đầu ra sau khi huấn luyện khăn chỉnh, làm hẹp không gian biểu đạt của model.
- MODA cải thiện SBERT diversity 265% trên Infinite-Chat held-out prompts đồng thời tăng hiệu năng năng lực chung 10.3% so với Qwen3-8B cơ sở.
- So với DivPO baseline mạnh nhất: SBERT diversity từ 0.274 lên 0.482 (+75.9%), E-Vendi từ 2.86 lên 4.4 (+53.8%), đồng thời tăng avg general capability pass@1 7.0%.
- Chế độ suy luận không nghĩ (thinking disabled): SBERT diversity +155.5%, E-Vendi +94.0% so với Qwen3-8B chính sách ban đầu; tăng avg pass@1 10.3 điểm phần trăm so với chính sách ban đầu, và 7.0 điểm phần trăm so với DivPO baseline mạnh nhất trên các benchmark năng lực chung.
- 100 phản hồi cho từ ghép "Name a shade of blue": MODA tạo ra 40 sắc xanh riêng biệt, nhiều hơn 122% so với chính sách ban đầu Qwen3-8B và 150% hơn SSoT.
- Huấn luyện: verl codebase, vLLM suy luận, FSDP huấn luyện, Qwen3-8B-Instruct cơ sở, 6 cặp role-phản hồi cho mỗi prompt làm nhóm phản hồi, GRPO, 10K prompt huấn luyện (mixture 4:1 Tulu3-SFT-Mixture : Infinite-Chat).
- 7 benchmark năng lực chung: GSM8K, MMLU, GPQA, BoolQ, HellaSwag, TruthfulQA, IFEval.
- 4 benchmark đa dạng chuyên ngành: HypoBench, PreScience, NoveltyBench, held-out split Infinite-Chat.
- Đo đa dạng: SBERT (mức ngữ nghĩa), E-Vendi (mức entropy), Discriminator (mức cách liên kiến).
- Mã nguồn: github.com/yuanjiayiy/mode-conditioned-diversity-alignment
- Danh mục arXiv: cs.CL

## INSIGHT — Cơ chế & tại sao
[Mode collapse xảy ra sau alignment] VÌ [RL tối ưu expected reward làm policy tập trung vào tập nhỏ phản hồi cao thưởng, từ đè các lựa chọn thay thế cũng hợp lệ, giảm entropy của policy]. Điều này nghĩa là [cần thiết kế lại thuật toán hậu huấn luyện để bảo toàn expressivity từ structural level, không chỉ can thiệp ở thời điểm suy luận].
[MODA chia nhiều vai trò trong một policy chung] VÌ [mỗi mode đóng vai trò agent MARL cạnh tranh tạo output khác biệt, khuyến khích các agent chuyên biệt các vùng khác nhau của không gian đầu ra chất lượng cao]. Điều này nghĩa là [một model duy nhất có thể phục vụ cả mode đơn (không có mã role) và mode đa dạng (có mã role), hỗ trợ cả câu trả lời đơn cho truy vấn 사실 và tập ý tưởng cho tác vụ sáng tạo].
[Cổng chất lượng tùy prompt ngăn reward hacking] VÌ [chỉ trao thưởng đa dạng cho phản hồi vượt ngưỡng chất lượng tính từ policy tham chiếu đóng băng, phản hồi bất thường không liên quan hoặc quá dài không nhận điểm đa dạng]. Điều này nghĩa là [phần thưởng đa dạng không được dùng đơn độc, phải gắn với cổng chất lượng để đảm bảo phản hồi đa dạng vẫn hữu ích].

## IDEA — Áp dụng được gì
Áp dụng MODA vào tinh chỉnh model tạo ý tưởng content cho doanh nghiệp nhỏ: bước đầu là thêm mã role abstract vào system prompt, huấn luyện RL với phần thưởng đa dạng gated chất lượng để tạo nhiều ý tưởng content khác nhau từ cùng một prompt.
Dùng dual inference mode: không có mã role cho câu trả lời đơn (truy vấn fact), có mã role cho nhiều ý tưởng (tác vụ sáng tạo).

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Bảo toàn sự đa dạng đầu ra không phải thêm phần thưởng đa dạng đơn độc, mà kết hợp điều kiện mode (role conditioning) với cổng chất lượng tùy prompt; một model duy nhất có thể phục vụ cả chế độ đơn và chế độ đa dạng.

## Assumptions & Limitations
- Điều kiện đúng: tác vụ cần nhiều đầu ra chất lượng cao khác nhau, có sẵn policy tham chiếu đóng băng để tính ngưỡng chất lượng, tài nguyên GPU để huấn luyện GRPO.
- Limitation paper thừa nhận: đánh giá chủ yếu trên Qwen3-8B và một số model khác (Llama-3.1-8B, GLM-4-9B); chưa đánh giá tất cả các kiến trúc model lớn hơn; training hai chế độ (thinking-enabled/disabled) có thể khác biệt kết quả.
- Limitation paper KHÔNG nói: chi phí vận hành huấn luyện GRPO với 6 role-response pairs mỗi prompt tại quy mô lớn; tính ổn định qua nhiều lần retraining khi data mix thay đổi; tác động lên độ trễ suy luận khi tạo nhiều ứng viên mode.

## Metadata
- Năm: 2026
- Tác giả: Jiayi Yuan, Hangoo Kang, James Jihao Liu, Yejin Choi, Vikram Iyer, Liwei Jiang, Natasha Jaques (University of Washington, Stanford University)
- Category arXiv: cs.CL
- Link PDF: https://arxiv.org/pdf/2609.14896v1
- arXiv ID: 2609.14896v1
- Nhãn: [applied]
- Skill: forty-shades-of-blue-moda | Test: [SKILL VALID]
