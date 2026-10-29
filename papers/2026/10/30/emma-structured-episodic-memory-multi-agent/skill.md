# Skill: emma-scoped-episodic-memory (bộ nhớ giai thoại có scope cho multi-agent workflow)
Source: 2610.35966
Type: framework / workflow

## Khi nào dùng skill này
- Xây dựng hoặc vận hành multi-agent system (hệ thống đa tác nhân) cho domain chuyên biệt cần procedure (quy trình) mịn mà general model không biết — content pipeline đa kênh, data-to-insight pipeline, tác vụ multi-application (đa ứng dụng).
- Muốn hệ thống tự cải thiện từ failures (thất bại) mà KHÔNG fine-tuning (tinh chỉnh) weights và KHÔNG phụ thuộc expert labor (lao động chuyên gia) viết lại topology mỗi domain mới.
- KHÔNG nên dùng: task đơn giản, 1 agent đủ (dùng episodic context đơn giản như playbook là đủ); domain không có automatic correctness signal (tín hiệu đúng sai tự động — LLM judge, unit tests, exact match) làm gate (cổng); cần inspect gradient-level (cấp gradient) thay vì text-level.

## Input cần có
- Task set có ground truth hoặc automatic verifier (bộ kiểm chứng tự động) per task (gate correctness signal).
- 1 backbone LLM (model ngôn ngữ lớn nền) chạy controller + sub-agents + reflector (bộ phản chiếu) — EMMA dùng chung 1 backbone mỗi run; có thể dùng strong model làm reflector + weak executors (hướng paper gợi ý future work).
- Repository/tool environment để sub-agents execute (thực thi) (Python tool per agent).
- Budget: EMMA re-run chỉ failed tasks, 17–38% ít executions hơn baseline hiệu quả nhất (61.8 vs 96.8–280.0 trên KramaBench mean 5 backbones).

## Các bước thực hiện
1. **Khởi tạo memory 3 pools:** C (controller memory — rules decompose/dispatch/verify, entry có topic + summary + domain tags + generality label), A (agent pool — bắt đầu 1 generalist a0 với prompt p0), S (skill pool — procedure ngắn cho class sub-problem, index 1 dòng "when to use"). Memory persist cross-task, viết CHỈ lúc training; inference freeze (đóng băng), không write.
2. **Attempt chain per task:** fresh environment, controller load selected memory entries (controller tự chọn từ index — load none hợp lệ), emit ordered plan (mỗi step: agent + subtask + skills), dispatch MỘT step mỗi lượt, sub-agent nhận task + subtask + skills + controller-curated summary outputs trước. Gate bằng correctness signal task: đúng → kết thúc; sai → reflection.
3. **Overflow decomposition (khi step cạn):** sub-agent hết context window hoặc rounds → KHÔNG kết luận agent fail mà subtask quá thô: controller dùng partial trace (dấu vết bộ phận) split step thành steps nhỏ hơn trên existing agents, splice vào plan, resume cùng vị trí giữ completed work; ghi overflow làm reflector evidence.
4. **Structured reflection 4 bước cố định:** localize (định vị step sai) → classify vào 1/5 scope: execution_slip (trượt thực thi), agent_behavior (habit chung fail), procedure (method cho class sub-problem sai/thiếu), missing_capability (không agent nào làm được), routing (decompose/dispatch sai) → generalize (correction áp mọi task cùng loại, KHÔNG nêu entity/answer task này) → minimize (edit nhỏ nhất trong scope). Output đúng MỘT action theo ownership table: execution_slip → REVISE_PLAN/NO_CHANGE (plan directive task này, không ghi memory bền); agent_behavior → REFINE_PROMPT (p0 nếu general, specialization prompt nếu role-specific); procedure → REVISE_SKILL/CREATE_SKILL; missing_capability → CREATE_SKILL rồi CREATE_AGENT; routing → MEMORY_NOTE/REVISE_PLAN (CREATE_AGENT khi overflow).
5. **Guarded update — 5 guards programmatic (không phụ thuộc backbone):** (a) scope–action compatibility — action ∈ Act(z); (b) prompt preservation — giữ đa số prompt cũ, chỉ động agent đã chạy trong attempt fail; (c) bounded growth — pools/entries trong fixed sizes, agent mới là specialization thật không duplicate/label; (d) no leakage — không artifact chứa reference answer hay copy span task text; (e) change of strategy — không edit memory level nào >2 lần liên tiếp fail; same step overflow 2 lần liên tiếp → action phải đổi cách chia việc. Refused → trả reason cho reflector thử lại; persistent refusals → no change.
6. **Re-run + exercise + freeze:** skill/agent mới hoặc sửa được NÊM TÊN trong plan re-run (edit thực sự được thực hành); re-run đến success hoặc hết revision budget; KHÔNG edit sau failure cuối (edit chưa re-run = untested memory); end-of-task controller update ghi vài routing lessons; snapshot memory sau mỗi chain; freeze sau 1 pass — không checkpoint selection. Inference: controller giữ selection/replanning/overflow, KHÔNG reflector, KHÔNG write.

## Output mong đợi
- Frozen episodic memory artifact (1/benchmark/backbone): controller routing rules + specialist agent prompts (mỗi specialist p̃_j = p_0 ∥ p_j — general habit viết 1 lần ở p0 lan tới mọi specialist) + procedural skill pool.
- Hiệu suất đã verify: best mean mọi benchmark (KramaBench 0.654 vs 0.584 GEPA (+7.0 điểm); BBEH-mini 0.663 vs 0.605 (+5.8); AppWorld normal +11.9 TGC/+17.4 SGC, challenge +6.4/+5.3 over ACE); first 17/20 settings; weakest backbone EMMA (58.5 KB, 61.2 TGC AppW challenge, 56.3 BBEH) mạnh hơn mọi baseline weakest backbone; lên tới +32.5% over strongest baseline; 17–38% ít training executions hơn.
- Ablation verify: skills +8.5 điểm (0.506→0.591), agents +5.6 (0.591→0.647) trên KramaBench Opus 4.5; test-time adaptation (DACode 0.443, Reflexion 0.476, DeepResearch 0.535, EvoMAS-test 0.532) all well below EMMA 0.647.

## Ví dụ áp dụng
- Content factory 3 kênh (blog, email, social): generalist a0 prompt chứa house style; training trên 30 bài có verifier (fact-check + format check): failure "bài blog thiếu nguồn" classify procedure → CREATE_SKILL "mỗi claim số phải kèm source"; failure "social agent đăng sai giờ" classify routing → MEMORY_NOTE "channel social → dispatch sau khi blog approve"; overflow trên task data analysis → CREATE_AGENT analyst specialist kế thừa p0. Sau 1 pass memory freeze; inference 3 kênh chạy với memory, không reflector.

## Gotchas
- Ill-scoped evolution là cạm bẫy chính: KHÔNG có scope constraints, backbone quyết định cấu trúc — Opus tích lũy skills, DeepSeek liên tục tạo agents (Figure 1). Guards là bắt buộc, không phải optional; bỏ guard (a)/(e) → memory drift (trôi) về habit backbone.
- execution_slip KHÔNG bao giờ ghi memory bền (1 lần slip không pattern) — phản trực giác nhưng đúng: persist mọi failure → memory noise (nhiễu).
- Generalize step bắt buộc: correction nêu entity/answer task cụ thể → lesson không transfer, "never fires again hoặc contaminates unrelated tasks" (Table 1 caption).
- Generalist prompt inheritance (p̃_j = p_0 ∥ p_j) nghĩa là edit p0 lan everywhere — tốt cho consistency nhưng 1 harmful edit ở p0 ảnh hưởng mọi specialist; guard prompt preservation chỉ kiểm agent đã chạy attempt fail, nên review thủ công edit p0.
- Edits persist kể cả chain unsolved — paper thừa nhận ineffective/harmful entries có thể còn (không thấy systematic degradation); hygiene: định kỳ cross-verify memory trên mini-batch hoặc replay old tasks (future work của paper — tự làm lấy).
- Gate cần verifier tự động tin cậy: LLM judge noise → reflection học từ false failure; unit tests miss behavior (như paper #265 cảnh báo) → scoped edits sửa sai layer.
- Controller tự chọn memory entries ("loading none valid") — controller yếu bỏ memory hữu ích: monitor (giám sát) load rate (tỷ lệ tải) của memory entries, entry nào never loaded → candidate dọn.
