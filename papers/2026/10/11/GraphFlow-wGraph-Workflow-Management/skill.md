# Skill: GraphFlow wGraph Workflow Composition
Source: 2605.22566
Type: framework / workflow

## Khi nào dùng skill này
- Đang build LLM agent system có nhiều workflow (quy trình làm việc) tương tự nhau, chia sẻ operation (thao tác nguyên tử) như tool call, reasoning step (bước suy luận), verification module (mô-đun kiểm chứng).
- Serving nhiều agent request đồng thời mà KV cache (bộ nhớ đệm key-value) là memory bottleneck (nghẽn bộ nhớ).
- KHÔNG dùng: chỉ một workflow fixed duy nhất; hoặc chưa có workflow repository (kho quy trình) nào để build wGraph.

## Input cần có
- Workflow repository: tập workflow hiện có, mỗi workflow là DAG (đồ thị có hướng không chu trình) của các operation.
- Training dataset: cặp (task, workflow) để train GNN (Graph Neural Network — mạng neural đồ thị).
- Execution log (nhật ký thực thi) để thống kê tần suất transition (chuyển tiếp) giữa các operation.
- LLM backbone để extract base KV cache cho mỗi operation.

## Các bước thực hiện
1. Atomicize (nguyên tử hóa): tách mọi workflow thành operation nodes + dependency edges (cạnh phụ thuộc); merge thành wGraph toàn cục — mỗi node là một atomic operation, mỗi cạnh là dependency hợp lệ.
2. Feature extraction (trích xuất đặc trưng): mỗi node gắn vector D chiều gồm functional semantics (ngữ nghĩa chức năng), linguistic trigger patterns (mẫu kích hoạt ngôn ngữ), execution schemas (lược đồ thực thi).
3. Train workflow generation model: thêm virtual task node (nút tác vụ ảo) nối hai chiều tới mọi operation; GNN message passing (truyền thông điệp) tạo node embedding; MLP chấm compatibility score (điểm tương thích) s_i,j = MLP(CONCAT[h_i, h_j, h_task]); greedy selection (chọn tham lam) cạnh score cao nhất từ task node với ràng buộc DAG → workflow subgraph.
4. Precompute base KV cache cho mỗi operation từ standalone description (mô tả độc lập), lưu một lần.
5. Online serving: với mỗi query, generate workflow subgraph; reconstruct KV = KVbase + ΔKV sparse residual (phần dư thưa) của prefix (tiền tố) hiện tại; effective path pruning (cắt tỉa đường đi): materialize residual chỉ cho transition tần suất cao, path rare → fallback on-the-fly (tính trực tiếp).

## Output mong đợi
- Task-specific workflow (subgraph) + reconstructed KV states → agent inference without repeated prefill (tiền xử lý lặp). Memory footprint (dấu chân bộ nhớ) ~4× thấp hơn stateful KV, accuracy gần như không đổi.

## Ví dụ áp dụng
- E-commerce agent: wGraph gồm search, filter, review, coupon, checkout, edit-address. Query "tìm tai nghe chống ồn <$300, nếu ít kết quả nới giá" → subgraph search→filter→review→relax→checkout. Base KV của filter được reuse cho mọi query có filter; path "edit address sau checkout" bị prune vì execution log cho thấy chưa bao giờ xảy ra.

## Gotchas
- Bỏ hoàn toàn prefix context (stateless) → MATH accuracy sụp 52.6%→39.4% — đừng tiết kiệm quá mức.
- Không prune → residual explosion (phần dư bùng nổ): memory scale với branching factor (hệ số phân nhánh) của wGraph.
- GNN phải retrain khi wGraph thay đổi lớn; node feature phụ thuộc hand-crafted schema chất lượng.
- Cold-start (khởi đầu lạnh): domain mới chưa có workflow history → chưa áp dụng được.
