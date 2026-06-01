# [2605.31492v1] LinTree: Cải thiện LLM Reasoning với Search Histories có Cấu trúc Rõ ràng

## Vấn đề
LLMs giải reasoning problems bằng cách generate intermediate traces (dấu vết trung gian) explore và revise (khám phá và sửa đổi) partial solutions (giải pháp một phần). Từ search perspective (góc nhìn tìm kiếm), traces là linearized search trees (cây tìm kiếm tuyến tính hóa). Nhưng khi model backtrack (quay lui) hoặc switch branches (chuyển nhánh), trace KHÔNG explicitly identify (xác định rõ ràng) search state nào đang được revisit (xem lại). Prior work chưa test whether raw search history alone đủ để outperform (vượt trội) heuristic search.

## Đóng góp
1. **So sánh trace-conditioned vs local-state heuristic**: Across 3 reasoning environments (Blocks World, Navigation, Sokoban), raw search history alone KHÔNG reliably outperform heuristic search
2. **LinTree — parent pointers**: Thêm simple parent pointers để explicitly represent tree structure → cải thiện cả task performance và search efficiency
3. **Key insight**: Search history trở nên useful khi tree structure được make explicit — implicit traces không đủ

## Phương pháp (tóm tắt cốt lõi)
LLM reasoning traces = linearized search trees: model extends partial solution, abandons khi fails, backtracks to try alternatives. So sánh: (1) Implicit reasoning — model conditions on flat trace (no structure); (2) BFS (RL) — best-first search với LLM heuristic, chỉ observe local state; (3) LinTree — thêm parent pointers vào trace, explicitly label parent-child relationships trong search tree. Parent pointers chỉ là simple addition: mỗi step ghi "parent: step_N" để identify search state nào đang expanded.

## Kết quả chính
- Implicit reasoning model: LOWER success rates than BFS (RL), chỉ modest improvements trong search expansions
- GRPO improves implicit policy over SFT, nhưng vẫn không establish advantage over local-state heuristic
- LinTree (parent pointers): cải thiện BOTH solve rate và search efficiency vs implicit reasoning
- Key: tree structure must be explicit — flat serialization loses structure
- Tested trên 3 controlled environments: Blocks World, Navigation, Sokoban

## Insight có thể áp dụng ngay
1. **Structured traces > flat traces**: Khi design reasoning prompts cho LLM, thêm explicit structure markers. Không chỉ "Step 1, Step 2, Step 3" — thêm parent references: "Step 3 (from Step 1): trying alternative". Ví dụ: khi debug code, structured trace "Line 45 ← Line 30 ← Line 10 (root cause)" better than flat log "Line 10, Line 30, Line 45".

2. **Parent pointers là minimal change với big impact**: Chỉ thêm 1 field "parent: step_N" vào mỗi reasoning step → cải thiện performance. Ví dụ: khi build AI reasoning system, mỗi step trong chain-of-thought thêm reference đến step nó branched from. Đơn giản nhưng helps model track search state.

3. **Search history alone không đủ**: Raw history flat = model không exploit được. Phải make tree structure explicit. Ví dụ: khi train AI explore solution space, KHÔNG chỉ log sequential steps — log branching structure: "tried A → failed → backtracked to root → tried B → succeeded".

## Giả định & Hạn chế
**Điều kiện để method work:**
- Task phải có tree-structured search space
- Model phải capable enough để utilize structured traces
- Parent pointers phải correctly identify search states

**Hạn chế paper thừa nhận:**
- Tested trên 3 controlled environments — generalizability unclear
- Parent pointers là minimal structure — more complex representations possible
- GRPO alone không đủ establish advantage

**Hạn chế paper KHÔNG nói:**
- Chỉ test small-scale reasoning tasks — không test real-world complex reasoning
- Parent pointers add overhead vào trace length
- Không compare với other structured representations (graphs, DAGs)
- Không address cost của generating structured traces
- 3 environments specific — coding, math, khác có thể different

## Metadata
- Năm: 2026
- Tác giả: Liwei Kang, Yee Whye Teh, Wee Sun Lee
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.31492v1
- Citation count: [EXTRACTION FAILED]
