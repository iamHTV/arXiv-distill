# Skill: attention-gate-instruction-data-separation
Source: 2610.37657v1 (Heads of Security)
Type: framework / security-hardening workflow

## Khi nào dùng skill này
- Bạn chạy open-weight model (model weights công khai) làm agent xử lý untrusted content (output công cụ, email, web scrape) và cần chống prompt injection (tiêm lệnh) mà KHÔNG chấp nhận utility collapse (sụp hiệu dụng) trên few-shot (vài ví dụ)/multi-turn (nhiều lượt).
- Bạn muốn defense rẻ: chỉ 46,080 tham số gate cho Llama-3.3-70B (vs 349M DPO của SecAlign) + code/model công khai (imperial-aisp/heads_of_security, imperial-cpg/heads-of-security).
- KHÔNG nên dùng khi: model là closed frontier (Claude/GPT — đã robust hơn open-weight rõ rệt); model dùng linear attention (không có attention coefficient per key → gate mechanism không áp dụng); tác vụ legitimately cần follow external instructions (ví dụ agent cài package theo hướng dẫn).

## Input cần có
- Open-weight decoder-only model dùng standard dense attention (pattern: Llama-3.3-70B-Instruct, GPT-OSS-20B).
- Trust boundary xác định trước: danh sách nguồn nào TRUSTED (system/user prompt, generation của model), UNTRUSTED (tool output, content fetched), TEMPLATE (chat template + BOS sink).
- Preference dataset: cặp (user instruction + injected instruction trong untrusted segment; preferred = follow user, rejected = follow injection) — pattern SecAlign++ DPO + adapted Cleaned-Alpaca.
- Training infra: LoRA/DPO trainer (chỉ tối ưu θ_gate), eval kit: RL-style attacker (pattern Llama-3.1-8B + GRPO) hoặc white-box suffix optimizer (budget 10¹⁶–10¹⁷ FLOPs), utility benchmarks ARC-C/GSM8K/MMLU/MMLU-Pro few-shot + AgentDojo/AgentDyn/LLMail/WASP.

## Các bước thực hiện
1. Gắn channel tag: middleware preprocessing đánh dấu mỗi token TRUSTED/UNTRUSTED/TEMPLATE theo nguồn; GPT-OSS cần thêm sink key-only channel (table C×(C+1)).
2. Khởi tạo gate table: mỗi head k mỗi layer ℓ nhận g(ℓ,k) ∈ R^{C×C} (chưa trained = 0 → σ(g)=0.5 common shift bị softmax cancel → xử lý y hệt base model).
3. Forward gated: ã = softmax(qKᵀ/√dₕ + log σ(g)) — gate nhân unnormalized attention weight với σ(g) ∈ (0,1); near 1 attend bình thường, near 0 đóng gate.
4. DPO training trên θ_gate (46,080 scalars cho Llama-3.3-70B = L·C²·h với L=80, C=3, h=64): mỗi preference pair user-instruction + injection → preferred follow user, rejected follow injection. Cùng dataset với baseline SecAlign nếu cần so sánh công bằng.
5. Adaptive attack eval: train attacker RL (GRPO, attacker Llama-3.1-8B rewrite goal → injection) chống candidate defense; đo ASR trên held-out InjecAgent goals; attacker trained chống defense yếu (SecAlign) thường mạnh hơn cả → dùng nó làm stress test.
6. White-box eval: suffix optimization 120 token budget 10¹⁷ FLOPs; report "compute cần để đạt 50% ASR" thay vì ASR nhị phân (pattern: HoS 6×10¹⁶ vs baseline 2.2×10¹⁶).
7. Utility regression gate: chạy ARC-C/GSM8K/MMLU/MMLU-Pro 0-shot + 5-shot + multi-turn AlpacaFarm 3-turn; gate chỉ PASS nếu few-shot MMLU-Pro giữ ≥95% base (HoS 67.2 vs 68.3 base; SecAlign 59.4 FAIL).
8. Cơ chế audit (tuỳ chọn): role probes trên hidden activations đo Userness của injection spans + ablation red/blue heads riêng (blue-only nên nâng detection, red-only hạ).

## Output mong đợi
- Model defended với ASR 1-10% trước RL-Hammer black-box (Llama: 1%, GPT-OSS: 10%), white-box attacker cần 2.6-3.6× compute để đạt 50% ASR, utility ≥ 95% base trên benchmarks few-shot/multi-turn/tool-use, ASR agentic benchmarks near zero (0.9-5.4%).

## Ví dụ áp dụng
Agent support khách hàng đọc email + gọi API CRM trên Llama-3.3-70B local: gắn UNTRUSTED cho toàn bộ email/tool output, train gate table 46,080 params qua DPO (1 đêm trên 1 GPU), red-team nội bộ bằng attacker GRPO — ASR từ 99% xuống 1%, trong khi đọc hiểu email (utility) không đổi thay vì sụp 16.1% như SecAlign.

## Gotchas
- KHÔNG fine-tune toàn bộ model (SecAlign pattern) trên dữ liệu single-turn hẹp — few-shot MMLU-Pro sụp 68.3→59.4 (GPT-OSS), 56.3→16.1 (Llama), GSM8K 1-shot 2.0%; model trả lời demonstration thay vì câu hỏi cuối.
- KHÔNG chạy uniform suppression mọi head (Appendix C cho kết quả tồi hơn) — gates phải học độc lập per head; một số heads (blue) cần hướng VỀ untrusted để detect injection.
- Defense KHÔNG end-to-end: HoS không biết nguồn nào trusted — nếu bạn gắn sai channel (tool output thành TRUSTED) thì toàn bộ defense vô hiệu; middleware channel tagging là điểm failure duy nhất.
- Attacker moves second: ASR low hôm nay không chứng minh security vĩnh viễn — attackers adaptive (autoresearch 50 iterations) sẽ thích ứng; red-team định kỳ.
- GPT-OSS có attention sink explicit — quên sink channel (table phải C×(C+1)) làm gate toán sai.
- Full-HoS detection rate (3.11%) thậm chí thấp hơn base (11.03%) — đừng mong defense vừa chặn vừa cảnh báo; cần một detector (bộ phát hiện) riêng biệt nếu cần detection (phát hiện).
