# Skill: SPARTAN Playbook Loop (Self-Play and Reflect-Transfer)
Source: 2608.09128v1
Type: workflow

## Khi nào dùng skill này
- Cần cải thiện AI agent ở nhiệm vụ xã hội/bất đối xứng (đàm phán, chăm sóc khách hàng, đấu giá, hợp tác nhóm) mà KHÔNG được phép fine-tuning (tinh chỉnh) hay cập nhật trọng số.
- Vai trò yếu thế (thiểu số, phe thiếu thông tin, bên bị động) đang underperform (dưới mức) so với vai mạnh trong cùng nhiệm vụ.
- Tình huống KHÔNG nên dùng: model open-weights nhỏ (≤32B) cho workflow discussion-heavy (nhiều bàn luận) — paper cho kết quả gần như null; nhiệm vụ không có outcome (kết quả) đo khách quan được.

## Input cần có
- Model agent (dùng model mạnh làm teacher nếu muốn distillation — chưng cất sang model yếu).
- Bộ self-play scenario (tình huống tự đấu) có outcome khách quan (win/loss theo vai).
- N ≥ 30 ván mỗi condition (điều kiện) — cho binomial 95% CI (khoảng tin cậy) ≈ ±18pp; nhiều hơn nếu cần precision (độ chính xác).
- Khả năng prepend (đặt trước) text vào system prompt (lệnh hệ thống).
- Log full trajectory (hành trình) của mỗi ván, gắn nhãn vai (main/alt).

## Các bước thực hiện
1. **Play (chơi):** cho model M tự chơi N ván, log đầy đủ trajectory + outcome theo vai. Xác định vai nào structurally weaker (yếu cấu trúc) — thường là vai thiểu số/thiếu thông tin.
2. **Reflect (phản chiếu):** prompt M (ngôi thứ nhất) viết playbook game-agnostic (không phụ thuộc game) từ {trajectory, outcome}. Playbook phải cover 6 chiều: deception (lừa dối), detection (phát hiện), persuasion (thuyết phục), information management (quản lý thông tin), coalition dynamics (động thái liên minh), timing (thời điểm). KHÔNG nhắc số liệu/sự kiện riêng game. Ký hiệu R1 = Reflect(M, τ1:N).
3. **Transfer (chuyển giao):** prepend playbook vào system prompt cho các ván tiếp theo. Đo win rate (tỷ lệ thắng) theo vai, so với baseline (đường cơ sở).
4. **Iterate (lặp, tùy chọn):** Rn = Reflect(M, τ dưới playbook Rn−1). Đo mỗi round — bulk of gain (phần lớn lợi ích) đến ở R1, peak thường R1–R3; dừng khi alt-side win rate không tăng (round thêm chỉ redistribute — phân phối lại).
5. **Verify transfer:** test playbook trên (a) held-out scenario (tình huống giữ lại) và (b) student model (model học trò) yếu hơn. Inject playbook vào student, đo CẢ HAI vai — expect gain chỉ ở phía yếu (+13–24pp với teacher GPT-5-mini, n=30).

## Output mong đợi
- Playbook (vài trăm token) prepend được vào system prompt.
- Alt-side (phe yếu) win rate tăng (GPT-5-mini: trung bình 24%→43% peak R3 trên 3 hidden-role game); main-side có thể giảm (76%→59% worst R2) — đây là trade-off (đánh đổi) dự kiến, không phải lỗi.
- Với model đủ lớn: transfer cross-game (median +7pp alt-side, max +27pp) và strong-to-weak distillation (+13–24pp) hoạt động.

## Ví dụ áp dụng
- Solopreneur dùng agent đàm phán giá với nhà cung cấp: chạy 30 ván self-play (agent vs agent, hai vai buyer/seller), phản chiếu vai buyer (phe yếu thế) thành playbook (giữ budget thật kín, phát hiện anchoring — neo giá, quản lý thông tin, thời điểm ra giá cuối), prepend vào system prompt agent đàm phán thật. Đo tỷ lệ có được giá tốt hơn baseline.

## Gotchas
- Chỉ phản chiếu 1 round (R1) đã lấy bulk of gain; lặp 4 round có thể làm main side sập (76→59%) mà alt side không thêm.
- Playbook kế thừa bad habit (thói quen xấu) của teacher — Qwen3-32B codify (mã hóa) cả parroting (lặp ý người trước) vào playbook mà không bỏ được.
- Paper KHÔNG có placebo control (đối chứng giả) → một phần effect có thể là prompt perturbation (nhiễu prompt); khi tự verify, luôn A/B với text giả cùng độ dài.
- Multigame playbook KHÔNG stack (chồng chất): gộp nhiều nguồn không tốt hơn 1 nguồn liên quan nhất.
- Model ≤32B học không được từ trajectory discussion-heavy — chỉ hiệu quả khi action (hành động) rút gọn thành 1 discrete token (token rời rạc), ví dụ vote yes/no.
- Luôn đo win rate theo vai riêng biệt: overall average che mất "lift the weaker side" pattern.
