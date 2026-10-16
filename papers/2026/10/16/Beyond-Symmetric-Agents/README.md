# [2609.35875v1] Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models

## Problem
Multi-agent debate (MAD - tranh luận đa đại lý) được tin là cải thiện reasoning (suy luận) và factuality (độ chính xác sự thật) so với single-model inference (phán mismos một model), nhưng prior work (công trình trước) coi các agent là symmetric peers (các bạn cùng cấp), để mở ở mức điều gì tạo ra lợi ích.

## Contribution
- Kiểm tra giả thuyết rằng cognitive diversity (đa dạng nhận thức) giữa các agent là yếu tố tạo ra lợi ích, trong bối cảnh small open-weight models (mô hình trọng lượng mở nhỏ) với benchmark headroom (khả năng cải thiện trên benchmark).
- Across 23 models from eleven vendor families (trên 23 mô hình từ mười một họ nhà cung cấp).
- Pool spans solo accuracies from roughly 30% to 92% (khoảng accuracies đơn độc từ 30% đến 92%).

## Method (tóm cốt lõi)
Thử nghiệm multi-agent debate với 23 mô hình từ 11 họ nhà cung cấp, small open-weight models. So sánh debate ensemble với solo generation, homogeneous teams (đội đồng nhất) và mixed teams (đội hỗn hợp), persona teams (đội nhân cách). Đo claim precision (độ chính xác 주장), accuracy (độ chính xác), wall-clock (thời gian tường reloj), token cost (chi phí token).

## Key Findings
- Solo accuracies từ 30% đến 92%.
- Team accuracy monotone in tier composition: 93.7% (SSS all-strong) → 87.0% (MMM) → 75.6% (WWW all-weak).
- Debate loses by 1.04pp vs solo generation, winning only 83 of 320 team-task cells.
- Mixed teams overturn 63.7% of wrong round-one majorities vs 42.9% for homogeneous.
- Independent biographies pooled through same panel reach 64.6% against debate's 55.6% (+8.9pp).
- Helpful flips outnumber harmful ones roughly two to one (7.6% vs 4.0% of agent-problem pairs).
- Debate at n=3 edges solo generation (55.6% vs 54.6% claim precision), persona teams reduce to 51.8%.
- Debate benefit comes from the first exchange (pooled 84.6% at one round, 87.2 at two, flat through five).
- 3.4× wall-clock and token cost.

## Actionable Insights
- Không nên coi tất cả agent là cùng cấp: đa dạng nhận thức (cognitive diversity) giữa các agent tạo ra lợi ích, không phải số lượng agent. Áp dụng: solopreneur xây MAS nên kết hợp các agent có tính cách/phương pháp khác nhau, không sao chép cùng một agent nhiều lần.
- Debate chỉ có lợi ích trong vòng trao đổi đầu tiên (first exchange), sau đó bị phẳng (flat through five rounds). Áp dụng: khi dùng debate, hãy giới hạn ở 1-2 vòng trao đổi, không cần tranh luận dài dòng.
- Các đội độc lập (independent biographies pooled) tốt hơn debate (+8.9pp). Áp dụng: thay để agent tranh luận, hãy để các agent làm độc lập rồi tổng hợp kết quả (voting/pooling).

## Assumptions & Limitations
- Điều kiện: small open-weight models với benchmark headroom; có thể khác trên frontier models lớn.
- Paper thừa nhận: debate loses by 1.04pp vs solo generation — debate không luôn tốt hơn.
- Limitation paper không nói: chưa đánh giá trên nhiều tác vụ ngoài GSM8K, MMLU, biography; chưa test chi phí thực tế của 3.4× token.

## Metadata
- Năm: 2026
- Tác giả: Leonardo Ferreira, Gardenia Liu, Kaden Zheng (Boston Children's Hospital, Harvard Medical School, Harvard SEAS, Harvard College)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.35875
