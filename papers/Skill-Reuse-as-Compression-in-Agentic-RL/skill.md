# Skill: Nén Kỹ năng Tái sử dụng cho Tác nhân RL (ReuseRL)
Nguồn: 2605.31509v1
Loại: framework (khung phương pháp)

## Khi nào dùng skill này
- Khi train (huấn luyện) LLM agent (tác nhân mô hình ngôn ngữ lớn) bằng RL (học tăng cường) và muốn cải thiện generalization (tổng quát hóa)
- Khi agent học shortcuts (lối tắt) cụ thể cho task thay vì reusable skills (kỹ năng tái sử dụng)
- Khi có nhiều successful trajectories (lượt hành trình thành công) cần extract (trích xuất) patterns chung

## KHÔNG nên dùng khi
- Tasks không có reusable substructure (cấu trúc con tái sử dụng) — mỗi task hoàn toàn khác biệt
- Không có enough successful trajectories để build dictionary (ít nhất 50+)
- Agent quá nhỏ (< 1B parameters) hoặc domain quá lớn (alphabet > 100 atomic skills)

## Input cần có
- RL training environment (môi trường huấn luyện) với definable actions (hành động có thể định nghĩa)
- Rule-based skill mapping φ: action verbs → atomic skills (kỹ năng nguyên tử)
- Base RL algorithm (GRPO recommended)
- Successful trajectory buffer (bộ đệm lượt hành trình thành công)
- Hyperparameters: phrase length cap L=4, BPE merge threshold

## Các bước thực hiện

### Bước 1 — Define Atomic Skill Alphabet (định nghĩa bảng chữ cái kỹ năng nguyên tử)
1. Liệt kê tất cả possible actions (hành động có thể) trong environment
2. Group (nhóm) actions thành atomic skills Σ (kỹ năng nguyên tử) — mỗi skill là 1 symbol
3. Ví dụ ALFWorld: {go_to, pick_up, put, toggle, open, look, inventory}
4. Mapping phải: đủ nhỏ để capture reusable structure, đủ lớn để distinguish behaviors

### Bước 2 — Extract Skill Sequences (trích xuất chuỗi kỹ năng)
1. Chạy agent, collect (thu thập) successful trajectories (τ where R(τ)=1)
2. Áp dụng φ mapping: τ → skill sequence s = φ(τ) ∈ Σ*
3. Store (lưu) vào global success buffer G (bộ đệm thành công toàn cục) — FIFO structure
4. Combine (kết hợp) current successful batch B+ với G thành cluster T

### Bước 3 — BPE Dictionary Extraction (trích xuất từ điển BPE)
1. Start với singleton phrases (cụm từ đơn) — mỗi atomic skill = 1 phrase
2. Rank (xếp hạng) candidate pairs (cặp ứng viên) theo frequency trong T
3. Accept merge (chấp nhận hợp nhất) nếu: ΔBDL = L_BDL(T, C ∪ {p_a∘p_b}) - L_BDL(T, C) < 0
4. Cap phrase length (giới hạn độ dài cụm từ) tại L=4
5. Terminate (kết thúc) khi không merge nào giảm MDL objective
6. Output: shared skill dictionary C (từ điển kỹ năng chia sẻ)

### Bước 4 — Compute Segmentation Cost (tính chi phí phân đoạn)
1. Với mỗi successful skill sequence s: seg(s, C) = số phrases cần để cover (phủ) s using C
2. Segmentation cost = seg(s, C) / T (chia cho trajectory length)
3. Thấp = tốt (nhiều reuse); Cao = xấu (nhiều idiosyncratic behavior)

### Bước 5 — Augment GRPO Reward (tăng cường phần thưởng GRPO)
1. Standard GRPO reward: r_outcome (binary — nhị phân)
2. Augmented: r = r_outcome - λ · seg_cost
3. λ = segmentation cost coefficient (hệ số chi phí phân đoạn) — tune (tinh chỉnh) trên validation
4. EM-style: alternate (luân phiên) giữa E-step (extract dictionary) và M-step (RL update)

## Output mong đợi
- Agent học reusable skill patterns thay vì task-specific shortcuts
- Cải thiện OOD generalization (tổng quát hóa ngoài phân phối)
- Giảm repeat actions (hành động lặp) và invalid actions (hành động không hợp lệ)
- Improvement: +5-13% trên agentic benchmarks

## Ví dụ áp dụng
**Tình huống**: Train AI agent tự động xử lý IT support tickets (vé hỗ trợ IT). Agent cần: diagnose issue (chẩn đoán vấn đề) → search knowledge base (tìm kiếm cơ sở tri thức) → apply fix (áp dụng sửa) → verify (xác minh) → close ticket (đóng vé).

**Áp dụng**:
1. Atomic skills: {diagnose, search_kb, apply_fix, verify, escalate, ask_user}
2. Collect successful ticket resolutions, extract skill sequences
3. BPE merge: [diagnose, search_kb] → "investigate" (điều tra); [apply_fix, verify] → "resolve" (giải quyết)
4. Segmentation cost: agent dùng "investigate → resolve → close" = 3 phrases = low cost = reward cao
5. Agent học generalizable workflow thay vì memorize specific ticket patterns

## Lưu ý quan trọng
1. **Rule-based φ limitation**: Mapping thủ công → cần redesign cho mỗi domain mới. Trade-off: manual effort vs learned extraction (chưa explored)
2. **Greedy BPE approximation**: Không guarantee optimal dictionary. Gap tăng với alphabet size — nếu |Σ| > 100, consider alternative heuristics (heuristic thay thế)
3. **Assumption 2**: Successful trajectories phải share reusable structure. Nếu domain hoàn toàn unstructured → segmentation cost degenerate (thoái hóa) thành round-length penalty
4. **λ tuning**: Quá cao → agent over-compress (nén quá mức), mất fine-grained skills. Quá thấp → không enforce reuse
5. **Buffer size**: Global success buffer quá nhỏ → unstable BPE. Quá lớn → outdated patterns dominate. FIFO với appropriate capacity (dung lượng phù hợp)
6. **Compute overhead**: BPE merging mỗi training step tốn compute — cache (lưu cache) dictionary nếu possible
