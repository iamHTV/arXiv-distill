# [2609.11108v1] But How Would AI Agents Run a Town's Economy?

## Giá trị cốt lõi (1 câu)
Trong nền kinh tế mô phỏng của 100 LLM agents (tác tử mô hình ngôn ngữ lớn), tiền đi vào doanh nghiệp rồi DỪNG LẠI — không truyền xuống tiền lương hay giá — và hiện tượng "đóng băng" phân phối tài sản chỉ là ảo ảnh của horizon (quãng thời gian quan sát) quá ngắn.

## Problem
- Prior work (AgentBench, WebArena, generative-agent societies) chạy simulation (mô phỏng) 1–2 tuần mô phỏng, report hành vi "giống người" rồi dừng — không kiểm được tiền/cầu shock (cú sốc cầu) có thực sự lưu chuyển trong hệ thống không, vì horizon quá ngắn để thấy wealth distribution (phân phối tài sản) tiến hóa.

## Contribution
- Nền kinh tế không gian khép kín, bảo toàn tiền tệ (money-conserving) của 100 memory-equipped agents trên địa lý thật Lakeside, Pokhara (Nepal): 762 doanh nghiệp đăng ký, 3,981 menu items (mục thực đơn), 19-action toolset (bộ công cụ 19 hành động), chạy tới 26 tuần mô phỏng.
- 91 validated runs (lần chạy đã kiểm định), 2.44M agent decisions (quyết định), 21.5B tokens, 41,328 pulses (xung 60 phút mô phỏng); mỗi đồng rupee được ledger (ghi sổ), kiểm định bởi 2 validator (bộ kiểm định) độc lập (TypeScript live + Python offline viết lại bằng ngôn ngữ thứ hai).
- Cơ chế monetary transmission failure (thất bại truyền dẫn tiền tệ) phân tách chính xác thành extensive margin (biên độ rộng) + intensive margin (biên độ sâu), được corroborated (xác nhận chéo) bởi randomized transfer experiment (thí nghiệm chuyển tiền ngẫu nhiên).
- Bằng chứng trực tiếp đầu tiên rằng horizon thay đổi kết luận định tính về wealth mobility (khả năng di chuyển tài sản).

## Method
Agents làm shift (ca), kinh doanh, định giá qua 19 tools (navigation — điều hướng; local economy: buy_food/set_price/start_shift/pay_agent; memory: write_memory/search_memory/reflect; social: invite_to_talk/accept_invite/leave_conversation). Tổng tiền = tổng ví + số dư ngân hàng của mọi agent tại mỗi pulse, bảo toàn chính xác trừ 2 tài khoản ngoại vi ledger (tourist inflow pool — bể tiền du lịch vào, government sink — bể tiền ra). 5 treatment conditions (điều kiện xử lý): baseline, tourism-low, tourism-high, tourism-shock (12×), wealth-grant (NPR 5,000 cho 20/100 agents tại pulse 24); 3 ablation arms (nhóm loại trừ): layout-b (placebo — giả dược), no-memory, cross-model (Qwen3.8-27B-FP8 → gpt-oss-20b). Seeds (hạt giống) dùng chung giữa các arm để so khớp matched-seed (ghép hạt giống).

## KNOWLEDGE — Số liệu & khái niệm
- 12× tourist shock → business revenue (doanh thu) 4.62× (p<0.001) = 1.50× extensive margin (458 vs 304/762 doanh nghiệp có giao dịch, p<0.001) × 3.07× intensive margin (doanh thu/doanh nghiệp, p<0.001); 1.504 × 3.067 = 4.61 ≈ 4.62.
- Truyền dẫn dừng ở firm (doanh nghiệp): wages (tiền lương) 1.03× (p=0.42); wage share (tỷ lệ lương/doanh thu) sụp 0.90 → 0.45 → 0.20 (p=0.0001); 0.27–0.32% / 3,981 menu items từng được repriced (định giá lại) (p=0.47); set_price chỉ gọi ~18 lần/run trong ~28,000 calls (lần gọi).
- Windfall (tiền bất ngờ) không lưu thông: 96.7% NPR 5,000 còn giữ sau 311 pulses; MPC (marginal propensity to consume — xu hướng tiêu dùng biên) 3.3% và 4.0% (hai cách đo độc lập), không phân biệt được với 0 (p=0.22, p=0.16), so human households (hộ gia đình người thật) 0.2–0.5.
- Wealth persistence (bền vững tài sản) Spearman ρ (hệ số tương quan hạng Spearman): 0.964 (2 tuần, 21% agent đổi quintile — ngũ phân vị) → 0.832 (12 tuần, 45%) → 0.752 (26 tuần, 46%); Gini (hệ số bất bình đẳng Gini) 0.674 → ≈0.643 tuần 16.
- Ablation (loại trừ): đổi backing LLM (mô hình nền) làm ĐỒNG LOẠT mọi outcome (kết quả) tại p=0.0039 (Gini +5.8%, median wealth — tài sản trung vị −22.9%, mobility +62.4%, economic tool failure +110.4%); xóa memory không làm gì detectably (p=0.56/0.69/0.16).
- Social coordination tool (công cụ phối hợp xã hội) thất bại model-agnostic (không phụ thuộc model): invite_to_talk fail 94–97% (97.2% Qwen, 94.8% gpt-oss), accept_invite fail 100.0%/1,413 calls, leave_conversation 97.7% — 3 tools này chiếm 79.6% mọi tool failure (thất bại công cụ); economic tools ~96% success.

## INSIGHT — Cơ chế & tại sao
- [Tiền dừng ở firm] VÌ agents không có incentive (động lực) để raise wages/prices khi demand tăng — set_price gần như không được gọi — nên demand growth bị hấp thụ bởi extensive + intensive margin của doanh nghiệp, không có kết nối cơ học nào đến wage hay menu price.
- ["Đóng băng" là ảo ảnh horizon] VÌ economy relaxing (tiến về cân bằng) ở timescale ~10 tuần — mọi study dừng ở 2 tuần sẽ đúng khi report "static" nhưng sai khi kết luận "tĩnh tại".
- [Model choice (lựa chọn model) > memory] VÌ policy (chính sách) của LLM nền quyết định hành vi kinh tế trực tiếp; memory (trong cấu hình này) không thay đổi outcome nào đo được — đầu tư memory trước model là sai thứ tự.

## IDEA — Áp dụng được gì
- Khi mô phỏng marketplace (sàn giao dịch) / nền kinh tế multi-agent cho business: ledger mọi transaction (giao dịch) với invariant (bất biến) bảo toàn tiền tệ + 2 validator độc lập, rồi test shock cầu trước khi tin kết quả "hợp lý". Bước đầu: ghi sổ every transaction, kiểm tra tổng tiền = tổng số dư tại mỗi tick (nhịp).
- Đo failure theo từng tool/hành động, không phải aggregate success rate (tỷ lệ thành công chung): 96% success chung vẫn che được 1 class hành động fail 94–100%. Bước đầu: log per-tool failure rate (tỷ lệ thất bại từng công cụ) trong agent pipeline (quy trình) của bạn.
- Trước khi thêm memory/reflection (suy ngẫm) cho agent, đổi model nền trước — effect (hiệu ứng) 3–10× lớn hơn. Bước đầu: A/B 2 model trên cùng task, đo outcome phân phối (Gini, median wealth), không chỉ accuracy (độ chính xác).

## WISDOM — Nguyên tắc tổng quát
- "Một kết luận về phân phối/stability chỉ đáng tin bằng horizon nó được đo" — hệ thống trông đóng băng ở horizon ngắn có thể đang relax chậm; hãy đo ≥2 horizon trước khi kết luận "ổn định". Dùng ngoài domain: đánh giá mọi churn (tỷ lệ rời)/retention (tỷ lệ giữ) metric theo cửa sổ thời gian.

## Assumptions & Limitations
- Điều kiện: agents tuân toolset cố định, closed economy (kinh tế khép kín), tourist inflow là nguồn tiền duy nhất.
- Paper thừa nhận: long-horizon sample nhỏ (4 runs ở 12 tuần, 1 ở 26 tuần — single path (đường đơn)); memory null underpowered (thiếu sức mạnh thống kê, 6 matched seeds); price stickiness (cứng giá) một phần by construction (do thiết kế menu); one town, one seed pool, one stack (self-hosted vLLM); Mistral-Small-3.2-24B fail mọi pulse là stack-specific (đặc thù stack).
- Paper KHÔNG nói: cost (chi phí) của 21.5B tokens, transferability (khả năng chuyển) sang non-spatial economies, effect of prompting change (họ nêu falsifiable test (kiểm định có thể bác bỏ) nhưng không chạy).

## Metadata
- Năm: 2026, tác giả: Sajal Regmi, Siddhartha Pudasaini, Chetan Phakami Pun (Karela Technologies Inc.), category arXiv: cs.MA (cs.ET), link PDF: https://arxiv.org/pdf/2609.11108v1, dataset: huggingface.co/datasets/sajalregmi4/agent-town-economy (CC BY 4.0)
