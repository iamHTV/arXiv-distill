# Skill: chronos-code-agents-software-evolution
Source: 2610.11578v1
Type: framework

## Khi nào dùng skill này
- Xây agent hỗ trợ phát triển phần mềm (code agent) sử dụng lịch sử pull requests.
- Muốn agent hiểu tại sao code được viết như vậy (design decisions, compatibility constraints, implementation patterns).
- Có lịch sử pull requests và dữ liệu codebase thật.

## Tình huống KHÔNG nên dùng
- Không có lịch sử pull requests hoặc dữ liệu codebase thật.
- Chỉ cần agent viết code từ không (from scratch), không cần hiểu lịch sử.

## Input cần có
- Lịch sử pull requests và dữ liệu codebase thật.
- Hệ thống LLM agent có thể truy cập và sử dụng lịch sử pull requests.
- Cơ chế truy xuất kinh nghiệm từ lịch sử pull requests (graph-grounded retrieval).

## Các bước thực hiện
1. Thu thập lịch sử pull requests và dữ liệu codebase thật.
2. Xây hệ thống LLM agent có thể truy cập lịch sử pull requests.
3. Xây cơ chế truy xuất kinh nghiệm từ lịch sử pull requests (graph-grounded retrieval) thay vì flat semantic retrieval.
4. Trước khi agent viết code hoặc sửa lỗi, agent truy xuất kinh nghiệm liên quan từ lịch sử pull requests.
5. Agent sử dụng kinh nghiệm này để đưa ra quyết định tốt hơn về việc sửa lỗi, triển khai tính năng, và tái cấu trúc code.

## Output mong đợi
- Mean resolution rate từ 69.2% lên 72.9% (+3.7pp).
- SWE-Bench Pro: 48.3% → 51.7%; FEA-Bench Lite: 41.0% → 43.5%.
- Fraction of tasks receiving useful experience: 68% → 89%.

## Ví dụ áp dụng
Solopreneur xây agent hỗ trợ sửa lỗi (bug-fixing agent) cho dự án phần mềm của mình: agent truy xuất lịch sử pull requests để hiểu tại sao code được viết như vậy, sau đó sử dụng kinh nghiệm này để sửa lỗi đúng cách. Giảm việc agent đưa ra giải pháp không phù hợp hoặc gây lỗi mới.

## Gotchas
- Cần đủ lịch sử pull requests và dữ liệu codebase thật; không có dữ liệu thì không có kinh nghiệm để truy xuất.
- Cần xây cơ chế truy xuất kinh nghiệm (graph-grounded retrieval) phù hợp; không dùng flat semantic retrieval đơn thuần.
- Cần đánh giá chất lượng kinh nghiệm được truy xuất để đảm bảo agent không sử dụng kinh nghiệm không liên quan.
