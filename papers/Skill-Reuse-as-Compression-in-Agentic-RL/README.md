# [2605.31509v1] Skill Reuse as Compression in Agentic RL (Tái sử dụng kỹ năng dưới dạng nén trong học tăng cường cho tác nhân)

## Vấn đề
Các nghiên cứu trước chưa giải quyết được bài toán generalization (khả năng tổng quát hóa) của LLM agents (tác nhân mô hình ngôn ngữ lớn) trained (huấn luyện) bằng RL (học tăng cường) vì: agents học được shortcuts (lối tắt) cụ thể cho từng task (nhiệm vụ), không học được reusable skills (kỹ năng tái sử dụng). Prior work như SkillRL và ERL (Experience-Augmented RL) tích lũy self-generated trajectories (lượt hành trình tự tạo) nhưng không enforce (ép buộc) shared compositional patterns (khuôn mẫu chia sẻ có tính tổ hợp) across trajectories — dẫn đến reasoning collapse (suy sụp lý luận).

## Đóng góp
1. **ReuseRL**: Framework grounding agentic RL trong MDL principle (nguyên lý độ dài mô tả tối thiểu) — nén successful trajectories (lượt hành trình thành công) thành shared skill dictionary (từ điển kỹ năng chia sẻ) và penalize (phạt) idiosyncratic behaviors (hành vi đặc thù)
2. **PAC-Bayes generalization bound (giới hạn tổng quát hóa PAC-Bayes)**: Chứng minh formal rằng nếu dictionary nén tốt một batch thành công, expected description length (độ dài mô tả kỳ vọng) trên future trajectories được bounded (giới hạn)
3. **Unifying interpretation**: Chứng minh SkillRL và ERL là implicit partial MDL minimizers (bộ tối thiểu MDL ngầm một phần) — ReuseRL explicit minimize full MDL objective

## Phương pháp (tóm tắt cốt lõi)
Pipeline 3 bước: (1) Extract atomic skills (kỹ năng nguyên tử) từ successful trajectories bằng rule-based mapping (ánh xạ dựa trên quy tắc) trên action verbs (động từ hành động); (2) Greedy BPE-style merging (hợp nhất kiểu BPE tham lam) — lặp lại hợp nhất cặp phrases (cụm từ) có tần suất cao nhất trong successful cluster (nhóm thành công), chỉ accept nếu batch MDL objective giảm; (3) Augment GRPO reward (tăng cường phần thưởng GRPO) với segmentation cost (chi phí phân đoạn) = seg(s, 𝒞)/T — phạt trajectories dùng nhiều phrases không tái sử dụng. Global success buffer (bộ đệm thành công toàn cục) FIFO stabilize quá trình EM.

## Kết quả chính
- ALFWorld IID: ReuseRL đạt 97.14% vs vanilla GRPO 84.29% (+12.85%), vs pure round-length 96.43% (+0.71%)
- ALFWorld OOD: 93.28% vs 79.85% (+13.43%), vs 91.79% (+1.49%)
- TW-Cooking Pass@1: 81.73% vs 74.97% (+6.76%)
- Countdown-Stepwise Pass@1: 80.37% vs 68.46% (+11.91%)
- Case study ALFWorld: GRPO có 40.4% repeat actions (lặp hành động), ReuseRL chỉ 14.4%; invalid actions: 23.5% → 1.8%
- Case study TW-Cooking: pure round-length có 74% burned failures (thiêu đốt thất bại), ReuseRL chỉ 3.3%
- Lớn nhất gains trên OOD split — structural compression (nén cấu trúc) dẫn đến reasoning generalization

## Insight có thể áp dụng ngay
1. **Nén hành vi thành công thành patterns tái sử dụng**: Khi train AI agent, không chỉ optimize cho task completion (hoàn thành nhiệm vụ) mà còn nén successful behaviors thành reusable patterns. Ví dụ: khi train chatbot xử lý customer complaints (phàn nàn khách hàng), extract common response patterns (identify issue → empathize → offer solution → follow up) và reward responses tuân theo patterns đó, thay vì mỗi response là unique.

2. **Phạt hành vi đặc thù, thưởng hành vi tổ hợp được**: Thay vì chỉ reward short trajectories (lượt ngắn), reward trajectories dùng shared skill vocabulary (từ vựng kỹ năng chia sẻ). Ví dụ: sales team — không thưởng mỗi deal close nhanh, mà thưởng process reuse (tái sử dụng quy trình): qualify lead → demo → handle objection → close — patterns chia sẻ across deals.

3. **Global success buffer stabilizes learning**: Lưu successful trajectories vào buffer global (bộ đệm toàn cục) để stabilize quá trình học. Ví dụ: knowledge base của công ty — không chỉ học từ batch hiện tại mà giữ best practices từ quá khứ, dùng để guide (hướng dẫn) future training.

## Giả định & Hạn chế
**Điều kiện để phương pháp work:**
- Successful trajectories phải admit shared reusable decomposition (chấp nhận phân rã tái sử dụng chia sẻ) với bounded dictionary complexity (Assumption 2)
- Cần rule-based skill projection φ — manual schema design (thiết kế lược đồ thủ công) cho mỗi domain mới
- Greedy BPE là approximation (xấp xỉ) cho NP-hard optimal dictionary search — gap tăng với vocabulary size

**Hạn chế paper thừa nhận:**
- Skill projection φ là rule-based per-environment mapping — cần manual schema design cho domain mới
- Greedy BPE approximation gap tăng với |Σ| (alphabet size)
- Assumption 2 có thể fail trong unstructured reasoning domains (miền lý luận không có cấu trúc)
- Chỉ test trên text-based benchmarks với 1.5-1.7B parameter models

**Hạn chế paper KHÔNG nói:**
- Không compare với experience replay methods (phương pháp phát lại kinh nghiệm) trong fair setting
- Rule-based φ limiting — không explore learned skill extraction (trích xuất kỹ năng học được)
- Không discuss compute cost của BPE merging overhead
- 1.5-1.7B models quá nhỏ cho real-world agent deployment

## Metadata
- Năm: 2026
- Tác giả: Zhikun Xu, Yu Feng, Jacob Dineen, Taiwei Shi, Jieyu Zhao, Ben Zhou
- Category: cs.LG, cs.AI
- Link PDF: https://arxiv.org/pdf/2605.31509v1
- Citation count: [EXTRACTION FAILED]
