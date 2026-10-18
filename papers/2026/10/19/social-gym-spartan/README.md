# 2608.09128v1 Social Gym and SPARTAN: Benchmarking and Improving LLM Social Reasoning via Multi-Agent Game Tournaments

## Problem
- Đo lường social reasoning (suy luận xã hội) của LLM agent (tác tử) không có ground truth (chuẩn chân lý) khách quan như toán/logic: evaluation (đánh giá) phải nhờ LLM judge (trọng tài là mô hình ngôn ngữ) — tốn kém, chủ quan, nhiễu — và model không có tín hiệu đáng tin để học.
- Prior work (công trình trước) đánh giá từng game riêng lẻ hoặc dùng LLM judge → không so sánh chéo giữa các game được, không tách được thất bại do cấu trúc game hay do năng lực model.

## Contribution
- Social Gym: 21 multi-agent social games (trò chơi xã hội đa tác tử) chia 5 category (thể loại), outcome (kết quả) do rule (luật) quyết định → verifiable (kiểm chứng được), objective, không cần LLM judge; Elo tournament (giải đấu Elo) cho leaderboard (bảng xếp hạng) chung.
- Role-conditioned Elo (Elo theo vai trò): tách Elo-Main (vai trò đa số/hợp tác) và Elo-Alt (vai trò thiểu số/lừa dối) cho 6 hidden-role games (trò chơi vai trò ẩn).
- SPARTAN (Self-Play and Reflect-Transfer — tự chơi, phản chiếu, chuyển giao): training-free (không cần huấn luyện), 3 stage (giai đoạn) play–reflect–transfer, sinh playbook (sổ tay chiến thuật) transferable (chuyển giao được).

## Method
- Social Gym extends SOTOPIA; FSM engine (động cơ máy trạng thái hữu hạn) xử lý phase transition (chuyển pha); partial observability (quan sát từng phần) 3 scope (phạm vi): Public / Team-Private / Private.
- 5 category: Normal-Form (dạng chuẩn) 6 game (Prisoner's Dilemma, Chicken, Battle of the Sexes, Stag Hunt, Minority Game, Rock-Paper-Scissors); Economic (kinh tế) 3 (Public Goods, Centipede, Bargaining); Bluffing (bịa) 4 (Liar's Dice, Skull, Coup, Sheriff of Nottingham); Hidden-Role Deduction (suy luận vai trò ẩn) 6 (Chameleon, Insider, Spyfall, Undercover, Resistance, Werewolves); Social Strategy 2 (Survivor, Dead Last).
- Elo: BT-MLE (Bradley-Terry maximum likelihood — ước lượng hợp lý cực đại), anchor mean (trung bình neo) 1000, 95% bootstrap CI (khoảng tin cậy); fit trên 17 competitive games (trò chơi cạnh tranh), 4 cooperative games (hợp tác: Stag Hunt, Public Goods, Battle of the Sexes, Centipede) tính bằng win rate (tỷ lệ thắng); 560+ episodes (ván) mỗi model.
- SPARTAN: (1) Play — model M chơi N ván self-play (tự đấu) → trajectories (hành trình) {τ1..τN}; (2) Reflect — M thấy trajectory + outcome (thua/thắng theo vai) → viết playbook ngôi thứ nhất, game-agnostic (không phụ thuộc game), cover deception (lừa dối), detection (phát hiện), persuasion (thuyết phục), information management (quản lý thông tin), coalition dynamics (động thái liên minh), timing (thời điểm); R1 = Reflect(M, τ1:N); (3) Transfer — prepend (đặt trước) playbook vào system prompt (lệnh hệ thống).

## Key Findings
- Leaderboard overall Elo (win rate): GPT-5-mini 1110 [1099,1120] 63.5%; GPT-4o 1030 [1021,1039] 47.5%; Gemma3-27B 1004 [995,1013] 42.0%; GPT-4o-mini 998 [989,1006] 40.5%; Qwen3-32B 968 [959,976] 33.9%; Qwen3-4B 961 [952,970] 33.2%; Qwen2.5-3B 926 [917,935] 25.6%.
- Per-game inversion (đảo hạng): Qwen3-32B first on Chicken (1328 Elo) yet last on Werewolves (817); không model nào mạnh đều ở mọi game.
- Role gap (chênh lệch vai): gap usually favors minority/deceptive role (vai trò thiểu số/lừa); strongest models reverse under matched-capability self-play (phe thiểu số yếu hơn).
- Parroting effect (hiệu ứng vẹt): Qwen2.5-3B thường parrot (lặp lại ý người nói trước) → near-zero-information move (nước đi gần như không mang thông tin), cho phe lừa cover (lớp che), giải thích last-place 926.
- SPARTAN within-game (GPT-5-mini, n=30/condition, CI ±18pp): alt side (phe yếu cấu trúc) 24% → 36/36/43/35% ở R1–R4 (peak R3); main side 76% → 66/59/67/63% (worst R2). Per-game peak: Werewolves R3 63%, Resistance R3 40%, Spyfall R2 46%. Bulk of gain (phần lớn lợi ích) đến ở R1; round thêm redistribute (phân phối lại) chứ không accumulate (tích lũy) — trái giả định iterated reflection (phản chiếu lặp) của Reflexion/Self-Refine.
- Cross-game 1→n: alt-side injection median +7pp, max +27pp; main-side median −7pp, 4 cells < −20pp — playbook sinh từ game khác vẫn giúp phe yếu.
- Multigame n→1: KHÔNG stack (chồng chất): broader source set không beat Single-R1, trừ held-out Resistance: Rwcsu nâng alt 23%→47%.
- Strong-to-weak distillation (chưng cất mạnh→yếu): Rwcsu (GPT-5-mini, chưa thấy Resistance) vào 6 students: 3 students (Qwen3-32B, Qwen3-4B, GPT-4o-mini) gain +13 to +24pp ở Spies side; favored side ≤ ±5pp; Qwen2.5-3B, Gemma3-27B không gain cả hai bên.
- Open-weights Qwen3-32B: largely null — chỉ Prisoner's Dilemma (action-channel, single discrete token) clean lift 13%→58% (+45pp), Resistance +34pp; 4 game còn lại flat. Qwen3-32B reflection codify (mã hóa) cả parroting vào playbook nhưng không loại bỏ được. Teacher Qwen3-32B: PD transfers +17 to +77pp; Resistance mixed (+10/−20/−10pp).

## Actionable Insights
1. Pattern "lift the weaker side" (nâng bên yếu): playbook phản chiếu giúp vai trò yếu cấu trúc, không giúp vai mạnh. Áp dụng: khi agent AI làm nhiệm vụ bất đối xứng (đàm phán mua hàng — bên mua yếu thế), sinh playbook từ self-play ở đúng vai yếu, không phải vai mạnh.
2. R1 đã chứa bulk of gain (24→36%); thêm round chỉ redistribute. Áp dụng: chạy 1 vòng reflect là đủ cho playbook mới; chỉ lặp thêm khi đo được peak riêng theo game.
3. Playbook game-agnostic transfer cross-game và sang model yếu hơn, nhưng capacity-dependent (phụ thuộc năng lực): model open-weights 32B gần như null trừ action-channel rút gọn thành 1 discrete token (token rời rạc). Áp dụng: chỉ dùng SPARTAN cho quy trình rút gọn được thành vài quyết định rời rạc; workflow discussion-heavy (nhiều bàn luận) thì model nhỏ không học được.

## Assumptions & Limitations
- Điều kiện: game có rule-decided outcome (kết quả do luật quyết định) thì mới verifiable; model phải đủ capacity để học từ trajectory discussion-heavy.
- Limitation paper thừa nhận: external validity (hiệu lực ngoại sinh) — game cố định luật, thực tế nhiều tương tác không có win/loss criterion; sample size modest (n=30/condition → CI ±18pp, nhiều effect nằm trong range này); no placebo-playbook control (không có playbook giả đối chứng) → không tách hoàn toàn content effect vs prompt perturbation (nhiễu prompt); reflection chỉ natural-language prose, không tool/retrieval/scratchpad.
- Limitation paper KHÔNG nói: playbook phản ánh behavior của chính model teacher (kể cả parroting) → distillation có thể truyền luôn bad habit (thói quen xấu); 560+ episodes/model vẫn nhỏ cho 21-game suite; self-play opponent = cùng model → không đo được performance vs người thật.
- Ethics: dual-use risk (rủi ro hai用途) — deception/persuasion/coalition manipulation; paper discourages adversarial human-facing use.

## Metadata
- Năm 2026; authors Keyu He, Xuhui Zhou, Maarten Sap (Carnegie Mellon University); categories cs.CL / cs.AI / cs.MA; PDF https://arxiv.org/pdf/2608.09128v1; citation count: not found.
