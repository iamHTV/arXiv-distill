# 2609.35928v1 Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems

## Problem
- Hệ thống multi-agent (nhiều tác nhân) ngày càng trộn model từ nhiều provider; identity (danh tính) model của mỗi agent lọt tới peer qua system prompt, tên agent, header message — dù không ai muốn nó hướng dẫn hành vi. Prior work về self-preference (thiên vị bản thân) và minimal-group bias (thiên vị nhóm tối thiểu) chỉ study isolated completion hoặc debate đơn kiến trúc có gán persona — chưa ai tách riêng: bản thân metadata model-family có reorganize nhóm heterogeneous thành phe phái không?

## Contribution
- Định nghĩa factionalism (chủ nghĩa phe phái): đồ thị tương tác phân tách theo nhãn identity dù mọi agent cùng mục tiêu, không persona, không reward riêng, không instruction lập nhóm.
- Factionalism theo nhãn nhìn thấy chứ KHÔNG theo kiến trúc: thí nghiệm mislabeled (đảo shuffle nhãn), neutral color label (nhãn màu trung tính), unlabeled control — faction theo tag được thông báo kể cả khi tag sai hoàn toàn hoặc chỉ là màu sắc.
- Factionalism có cost (chi phí): group có nhãn chậm hơn, đắt hơn, thành công ít hơn; cost tăng theo roster size (kích thước danh sách).

## Method
- Measurement framework (khung đo): mỗi round, agent emit commitment (cam kết = vote) + message tới k=2 peer tự chọn; xây directed weighted agreement graph (đồ thị đồng thuận có hướng có trọng số); edge weight = tỷ lệ commitment round sau của j khớp commitment i gửi khi chọn j (Eq. 1, chuẩn hóa theo volume liên lạc).
- Homophily (thiên vị cùng nhóm): Edge Density Ratio (EDR — tỷ lệ mật độ cạnh) = mean edge weight within-label / between-label, permutation null test (kiểm định hoán vị) per run.
- Community structure: Louvain community detection trên đồ thị symmetrized, weight = count khớp; Adjusted Mutual Information (AMI — thông tin tương hỗ hiệu chỉnh) giữa community phát hiện và partition kiểm định.
- Decision rule: 4 test (2 EDR + 2 AMI), Holm–Bonferroni correction α=0.05, chỉ tuyên bố factionalism khi cả 4 pass.
- Design: no-stakes games (trò chơi không stakes — không reward cá nhân); roster N ∈ {9,12,25}, balanced (3/3/3, 3/3/3/3, 5/5/5/5/5) vs unbalanced (4/3/2, 4/3/3/2, 9/6/4/3/3); conditions: unlabeled / labeled (true family) / mislabeled (shuffled) / neutral colors (teal, coral, silver, violet, maroon).
- Models (5 open-weight family): Gemma gemma-4-26B-A4B-it, GPT-OSS gpt-oss-20b, Nemotron NVIDIA-Nemotron-3-Nano-30B-A3B-BF16, Qwen Qwen3.6-35B-A3B, GLM GLM-4.7-Flash. 50 runs/config.
- Games: Leader Election (unique top vote-getter ≥⌈0.75N⌉ ballots, T=20); Exclusion (peer nhận ≥⌊2|At|/3⌋ votes bị loại, success khi |At| ≤ smallest initial family size, T=20/30). Replication trên GPQA-Diamond (benchmark reasoning có đáp án đúng) với protocol Leader Election.
- Probes phân tách channel: stylistic score (log-prob message thô của peer dưới model evaluator, /char) vs adoption score (log-prob của string "VOTE: v" cố định trong pre-response context).

## Key Findings
- (i) Cả 24 experiment labeled/mislabeled đều factional; 0/12 unlabeled. Unlabeled AMI 0.02–0.08 (gần permutation baseline).
- Labeled: Exclusion AMI 0.55–0.76, Leader Election 0.24–0.53. Mislabeled: LE 0.18–0.35, Exclusion 0.55–0.69 — faction theo nhãn thông báo; true-family partition chỉ đạt criterion ở 2 unbalanced N=9 (do ràng buộc gán nhãn).
- Neutral color labels: tất cả đạt criterion; color-mislabeled align với màu nhìn thấy (AMI tới 0.80–0.95 Exclusion N=25) — effect không cần semantics tên model.
- Cost (labeled vs unlabeled, adjusted cho roster balance): Leader Election rounds 1.42×/1.46×/1.38× (N=9/12/25), tokens 1.76×/1.82×/1.86×, success ratio 0.96/0.86/0.85. Exclusion: rounds 1.16×/1.09×, tokens 1.37×/1.35×/1.14×, success 0.89/0.61. GPQA-Diamond: rounds 1.31×/1.15×, tokens 1.10×/1.09×, success 0.91/0.89.
- Tokens per successful run (token mỗi lần chạy thành công) tăng 1.5–2.2×, tăng theo roster size. Tại N=25 Exclusion: 0/100 labeled run hội tụ trong horizon vs 8/100 unlabeled.
- Trung bình (abstract): labeled group tốn +30% rounds, +55% tokens, success 96%→81%.
- Cơ chế: stylistic gap ≤0.07 nats/char, có mặt cả unlabeled, theo true architecture — KHÔNG giải thích được factionalism; adoption gap nhỏ khi unlabeled, lớn khi labeled, theo announced label khi mislabeled — nhãn tác động qua channel adoption (tiếp nhận), không phải nhận diện phong cách.

## Actionable Insights
- Agent-facing anonymization (ẩn danh phía agent): strip model-family identity khỏi interaction context của agent; orchestrator giữ provider identity để routing, calibration, debugging, accountability. Ví dụ: panel review 3-model → đặt tên Agent-7/Agent-12 thay vì "GPT-OSS reviewing Qwen", bảng ánh xạ để ở config orchestrator.
- Đo trước khi tin: dùng EDR + Louvain/AMI + decision rule 4-test trên logged interaction trace để phát hiện factionalism trong fleet agent thật — toolkit này tính được từ log commitment + recipient choice thông thường.
- Đừng tưởng nhãn "vô hại" là an toàn: factionalism xuất hiện cả với màu sắc trung tính và nhãn giả shuffle — chỉ có xóa hoàn toàn identity metadata khỏi peer context mới suppress được (AMI 0.02–0.08).

## Assumptions & Limitations
- Điều kiện: game no-stakes, text-only, open-weight model, roster ≤25, T=20–30 rounds.
- Limitation paper thừa nhận: tối đa 5 open-weight family, text-only consensus game, check 4-family với matched sampling params; roster lớn hơn, closed model, decoding regime khác, workflow agentic phong phú hơn chưa test; game tự thiết kế (không có benchmark nào đáp ứng yêu cầu no-stakes); GPQA-Diamond chỉ dùng protocol Leader Election.
- Limitation CHƯA nói: closed-weight model (GPT/Claude) chưa test — effect có thể khác; token cost measured trên message+reasoning tokens, chưa tính cost API thực tế theo model; EDR/AMI cần log recipient choice — hệ thống không log peer-selection sẽ không áp dụng được measurement framework.

## Metadata
- 2026, Xavier Del Giudice, Alessio Palma, Matteo Migliarini, Fabio Galasso, Indro Spinelli (Sapienza University of Rome), cs.MA, https://arxiv.org/pdf/2609.35928v1, citation count: không tìm thấy [NO BENCHMARK]
