# [2605.22566] GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving

## Problem
- Prior work (MetaGPT, TaskWeaver, AFlow) lưu workflow (quy trình làm việc) dạng template (mẫu sẵn) trong repository (kho), chọn bằng retrieval (truy xuất theo độ tương đồng) → không nắm được correspondence (sự tương ứng) fine-grained (chi tiết) giữa requirement (yêu cầu) của task (tác vụ) và cấu trúc procedural → fail trên task unseen (chưa thấy) hoặc compositional (tổ hợp).
- Hệ thống quản lý KV cache (bộ nhớ đệm key-value — trạng thái attention trung gian) ở granularity (độ chi tiết) per-workflow (mỗi workflow riêng) → operation (thao tác nguyên tử) dùng chung bị lưu nhiều bản → memory duplication (nhân bản bộ nhớ).

## Contribution
1. wGraph: đồ thị operation toàn cục dạng DAG (directed acyclic graph — đồ thị có hướng không chu trình), gộp atomic operation (tool call, reasoning step, verification module) và dependency (quan hệ phụ thuộc) từ nhiều workflow thành một representation (biểu diễn) duy nhất; workflow được instantiate (khởi tạo) động dưới dạng subgraph (đồ thị con).
2. Task-adaptive workflow generation (tạo workflow thích ứng theo tác vụ): GNN (Graph Neural Network — mạng neural đồ thị) + virtual task node (nút tác vụ ảo) + MLP edge scoring (chấm cạnh) → conditional subgraph generation thay vì retrieve template.
3. Topology-aware state management (quản lý trạng thái theo cấu trúc đồ thị): differential KV cache = base KV (độc lập context) + sparse residual (phần dư thưa) theo prefix (tiền tố execution); effective path pruning (cắt tỉa đường đi).

## Method
- Offline: build wGraph từ workflow repository; node feature (đặc trưng nút) = functional semantics + linguistic trigger patterns + execution schemas; train GNN; precompute base KV mỗi operation.
- Online: thêm virtual task node (cạnh hai chiều tới mọi operation); GNN message passing → node embedding; MLP tính compatibility score (điểm tương thích) s_i,j = MLP(CONCAT[h_i, h_j, h_task]); greedy selection (chọn tham lam) cạnh score cao nhất từ task node với ràng buộc DAG → workflow subgraph Wc.
- Execution: KV(P,v) = KVbase(v) + ΔKV(P,v) — load base KV rồi áp residual thưa của prefix hiện tại.
- Path pruning: materialize (hiện thực) residual chỉ cho transition (chuyển tiếp) tần suất cao; path rare → fallback on-the-fly (tính trực tiếp).

## Key Findings
- 5 benchmarks: GSM8K, MATH (accuracy), HotpotQA (F1), HumanEval, MBPP (pass@1); backbone: Qwen-2.5-7B, Llama-3.1-8B, Gemma-2-9B; 7 baseline.
- Trung bình +4.95 percentage points so với state-of-the-art.
- HumanEval pass@1: 78.1%→86.2% (Qwen-2.5-7B), 75.4%→82.5% (Gemma-2-9B); MATH: 72.1%→76.4% (Qwen); HotpotQA F1: 67.5→70.4 (Qwen).
- P90 latency (độ trễ percentile 90): 12.25s vs 14.06s (AFlow, Qwen, aggregated).
- KV memory ~4× reduction: GSM8K 50GB→11GB, HotpotQA 85GB→25GB (vs stateful); batch size 50: <0.5GB vs >2.4GB (stateful).
- Sparsity (độ thưa) KV: >75% key entries, >70% value entries dưới ngưỡng nhỏ.
- Path pruning: GSM8K 15.0→11.5GB, MBPP 9.9→7.2GB, MATH -5.3GB, HotpotQA -4.2GB.
- Stateless KV (bỏ prefix): MATH accuracy 39.4%, HotpotQA F1 58.6% — vỡ correctness (đúng đắn).

## Actionable Insights
1. Tách workflow thành atomic operation trong một đồ thị chung, compose (tổ hợp) theo request thay vì retrieve template. Ví dụ: agent hỗ trợ khách hàng build workflow từ các operation "tra đơn", "hoàn tiền", "escalate" theo intent (ý định) truy vấn.
2. Cache trạng thái LLM ở granularity operation: base KV một lần + sparse residual cho prefix phổ biến → ~4× memory reduction với gap accuracy nhỏ (MATH 52.6% vs 53.8% stateful). Ví dụ: serving multi-agent trên 1 GPU thay vì 4.
3. Dùng execution log để prune transition invalid/rare → memory scale với effective working set (tập đường đi thực dùng), không phải combinatorial paths. Ví dụ: workflow e-commerce không bao giờ "edit address" sau "checkout" → xóa đường đó.

## Assumptions & Limitations
- Phải có workflow repository + training dataset (task, workflow) để build wGraph và train GNN → cold-start (khởi đầu lạnh) với domain mới.
- Residual chỉ materialize cho transition đã thống kê; path lạ fallback on-the-fly (chậm hơn).
- Evaluation trên benchmark reasoning/QA/code, KHÔNG test real enterprise workflow.
- Paper KHÔNG có section Limitations; KHÔNG nói: cost GNN inference thêm mỗi request; node feature phụ thuộc hand-crafted schema.

## Metadata
- Năm: 2026 (ICML 2026, PMLR 306). Tác giả: Ao Li, Shangpeng Yang, Fahao Chen, Tianheng Xu, Peng Li, Zhou Su (Xi'an Jiaotong Univ, Shandong Univ, CAS Shanghai).
- arXiv: 2605.22566, category cs.CL. PDF: https://arxiv.org/pdf/2605.22566. Citation count: [NO CITATION DATA — API rate-limited].
