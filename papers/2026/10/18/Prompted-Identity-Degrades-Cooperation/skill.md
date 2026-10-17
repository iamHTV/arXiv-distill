# Skill: Factionalism Detection & Agent-Facing Anonymization (phát hiện phe phái + ẩn danh phía agent)
Source: 2609.35928v1
Type: evaluation-method + workflow

## Khi nào dùng skill này
- Hệ thống multi-agent trộn nhiều model family (heterogeneous fleet) mà agent nhìn thấy identity của nhau (tên, header, system prompt có nhãn model).
- Task dạng consensus/coordination (bầu leader, loại trừ, hội đồng review) — nơi factionalism (phân phe theo nhãn) làm chậm và giảm success.
- KHÔNG nên dùng: system đơn model; task không cần peer interaction; hoặc agent đã hoàn toàn ẩn danh (không có nhãn nào để strip).

## Input cần có
- Interaction trace log: mỗi round, commitment (vote/quyết định) của mỗi agent + danh sách recipient (peer nhận message). Nếu không log recipient choice → phải bật logging trước.
- Danh sách nhãn identity đang hiển thị cho agent (model family, tên, tag).
- Roster composition: số agent mỗi family (balanced/unbalanced).

## Các bước thực hiện
1. **Xây agreement graph (đồ thị đồng thuận):** từ trace, tính edge weight w(i→j) = tỷ lệ commitment round sau của j khớp commitment i gửi khi i chọn j làm recipient (chuẩn hóa theo volume liên lạc, Eq. 1 của paper).
2. **Đo homophily (thiên vị cùng nhóm):** EDR (Edge Density Ratio) = mean edge weight within-label / between-label; chạy permutation null test (hoán vị nhãn, giữ size nhóm) per run.
3. **Đo community structure:** symmetrize đồ thị (cộng 2 chiều, thiếu = 0), weight bằng count khớp, chạy Louvain community detection, tính AMI (Adjusted Mutual Information) giữa community và partition nhãn.
4. **Áp decision rule:** 4 test (2 EDR + 2 AMI), Holm–Bonferroni correction α=0.05 — chỉ tuyên bố factionalism khi cả 4 pass (EDR cần thiết nhưng chưa đủ).
5. **Anonymize (ẩn danh):** xóa model-family identity khỏi interaction context của agent (tên → Agent-k, bỏ header model, bỏ nhãn family trong system prompt); orchestrator giữ bảng ánh xạ cho routing/calibration/debugging/accountability.
6. **A/B verify:** chạy lại cùng config (≥50 seeds) ở 2 điều kiện labeled vs anonymized; đo rounds, tokens, success; tính tokens per successful run — expect anonymized: rounds ~1.0× (vs 1.38–1.46×), tokens ~1.0× (vs 1.35–1.86×), success ratio trở về baseline.

## Output mong đợi
- Báo cáo AMI/EDR per configuration + verdict factionalism (pass/fail 4-test).
- Sau anonymize: AMI về mức 0.02–0.08 (permutation baseline), tokens per successful run giảm 1.5–2.2×.

## Ví dụ áp dụng
- Workflow 9 agent (3 Gemma, 3 Qwen, 3 GLM) review nội dung, tên agent hiện model: log 50 runs → AMI 0.43 (Exclusion-like), EDR significant, 4/4 test pass → factionalism confirmed. Đổi tên Agent-1..Agent-9, orchestrator giữ map → 50 runs mới: AMI 0.05, rounds 1.42×→1.00×, success 0.89→0.96 baseline.

## Gotchas
- EDR một mình chưa đủ: homophily cần thiết nhưng chưa đủ — phải có community alignment (AMI) nữa, và decision rule yêu cầu cả 4 test pass.
- Chuẩn hóa contact volume: cặp liên lạc nhiều không được weight cao chỉ vì nói nhiều (dùng ratio, Eq. 1).
- Mislabeled control: nếu nghi ngờ effect do "nhận diện phong cách viết" chứ không phải nhãn — chạy mislabeled (shuffle nhãn) + stylistic-vs-adoption probe: factionalism theo announced label = do nhãn, không phải style.
- Roster unbalanced: đưa balance vào covariate của model GLM khi so sánh cost, hoặc kết quả lệch.
- N=25 Exclusion: labeled run có thể KHÔNG BAO GIỜ hội tụ (0/100) — đừng so sánh round count, so sánh success rate.
- Neutral color label cũng gây faction (AMI tới 0.95) — "đổi tên model thành mã màu" KHÔNG phải giải pháp; chỉ xóa hoàn toàn identity khỏi peer context mới work.
