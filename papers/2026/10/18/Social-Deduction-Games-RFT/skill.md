# Skill: Social-Cognitive RFT — Huấn luyện social agent bằng reading + influence rewards
Source: 2610.04261v1 (Social Deduction Games + RFT)
Type: workflow (training recipe)

## Khi nào dùng skill này
- Cần huấn luyện LLM agent hoạt động trong multi-agent / human-interactive settings mà success phụ thuộc social reasoning (đọc người khác, influence decisions tập thể): negotiation, customer support, meeting coordination, sales.
- Outcome-only RFT (reward = win/loss cuối cùng) cho training high-variance, non-monotonic → cần decompose reward.
- KHÔNG nên dùng: task đơn agent không có social component; task có verifiable answer trực tiếp (code, math) — reward thông thường đủ; chưa có simulator ghi được intermediate social signals.

## Input cần có
- Game/arena simulator: hidden state (roles, private info), public transcript, structured actions (vote, proposal, approval), terminal outcome; turn-based prompt-chaining protocol.
- Định nghĩa 2 reward components: reading target (latent state cần infer: roles, teams, intentions — F1 cho set, exact-match cho categorical) và influence target (intended effect lên others' next actions: vote direction, approval, target concentration).
- Fixed opponent policies (ít nhất ban đầu) + role distribution; budgets (training steps, group size G cho GRPO).
- Backbone model + reference model cho KL penalty.

## Các bước thực hiện
1. Build arena: mỗi episode record prompts, responses, parsed actions, private role info, public transcript, intermediate social outcomes, terminal outcome. Invalid actions → format failures (log riêng).
2. Định nghĩa reward decomposition: R(τ) = λ_read·R_read + λ_inf·R_inf + λ_aux·R_aux − λ_fmt·P_fmt − λ_leak·P_leak. R_read = trung bình điểm so belief state agent emit với hidden target tại các reading events; R_inf = trung bình điểm đo others' subsequent actions vs intended social target; R_aux = intermediate game events (exile adversary, protect teammate); P_fmt phạt invalid structured output; P_leak phạt reveal hidden info công khai.
3. Đọc trước, influence sau: chạy reading regime (reward nhấn hidden-state inference) để chính sách có belief state ổn định — influence reward chỉ effective khi grounded trong belief chính xác (SI-only giảm win rate Qwen3-4B 21%→12%).
4. GRPO optimization: sample group G trajectories cùng condition; advantage chuẩn hóa trong group Â = (R(τ_g) − μ_R)/(σ_R + ε); clipped policy-gradient + β·KL(π_θ‖π_ref). KHÔNG cần critic.
5. Same-side training (nếu task team-based): gán cùng policy cho mọi role của 1 side, mỗi update conditioned trên private role + public history của role đó — 1 game cho nhiều training samples mà không mix objectives qua 2 bên.
6. Evaluate terminal win rate như HELD-OUT DIAGNOSTIC (không phải online reward): win rate phải cải thiện cùng với reading/influence scores — nếu win lên mà reading/influence không lên, nghi ngờ formatting shortcut.
7. Cross-model check: chơi policy đã học với opponents chưa từng gặp (≥9 opponents, 100 games mỗi opponent) — win rate + SR-F1 + SI-Follow + outcome metrics phải ổn định cross-family.
8. Human blinded eval (nếu có thể): matched base-RFT pairs, ratings 1–5 trên 5 dimensions (overall value, reading quality, influence & coordination, human-likeness, strategic correctness); evaluators KHÔNG được high-score chỉ vì side thắng; sign-flip permutation test.

## Output mong đợi
- Policy cải thiện: reading accuracy (hidden-state F1/accuracy), influence metrics (target hit rate, approval outcome), terminal win rate (held-out), human ratings (overall value +~1.09/5, strategic correctness +~1.17/5). Expected pattern: gains mạnh hơn ở later evidence-rich states (Day-3 F1 +0.41 vs Day-1 +0.11).

## Ví dụ áp dụng
- Solopreneur sales-negotiation agent: reading reward = infer customer's budget/urgency từ messages (F1 vs CRM labels); influence reward = customer's next action (book demo, share docs) move đúng hướng; aux = meeting booked; fmt penalty = invalid JSON; leak penalty = reveal other customers' data. GRPO train trên simulated negotiations; eval trên held-out negotiations + human rating. Expected: better qualification + higher booking rate, không cần thắng mọi negotiation.

## Gotchas
- Đừng dùng terminal win làm online reward — sparse/noisy: Werewolf/Mafia peak 0.88 rồi rơi 0.38; Avalon avg reward chỉ 0.25. Win rate là diagnostic, không phải objective.
- Influence WITHOUT reading là harmful — SI-only có thể cắt win rate một nửa. Always train reading trước hoặc joint, không bao giờ influence-only.
- Prompt scaffold SI-only có thể hại model yếu belief (Qwen3-4B: 21%→12%) — test scaffold ablations (none/SR/SI/SR+SI) trước khi RFT.
- Response length KHÔNG phải proxy cho skill: một số models verbose hơn khi steering, DeepSeek-7B cải thiện dù ngắn hơn — monitor length nhưng đừng optimize nó.
- Role-fixed training (Assassin) cho thấy: khi 1 role's payoff tập trung vào 1 inference problem, outcome reward alignment tốt hơn — mixed-role training cần thiết cho general policy nhưng role-specialized training mạnh hơn cho role payoff-concentrated tasks.
- P_leak bắt buộc: agent có thể học cách reveal hidden info công khai để "win" — phạt rõ ràng.
- Fixed opponents → policy có thể overfit opponent quirks; cross-model eval bắt buộc trước khi tin transfer.
- Human eval nhỏ (178 ratings) là descriptive — đừng overclaim; human-likeness cải thiện ít (+0.36, n.s.) — strategic competence ≠ tự nhiên.
- Reward cho agreement alone có thể train conformity — reward phải include "effect advances appropriate collective goal" (3 components: represent accurately, produce intended effect, effect advances normatively appropriate goal).
