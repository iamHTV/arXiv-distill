# Skill: CURATE Lifecycle Loop (Sketch–Reify–Test–Deploy with Module Catalog)
Source: 2608.04270v2
Type: framework / workflow

## Khi nào dùng skill này
- Cần build hoặc automate một workflow nhiều bước (content pipeline, data processing, automation) với LLM coding agent, và muốn workflow reproducible + deployable, không chỉ là code rời rạc.
- Có các module đã verified (đã kiểm chứng) nên tái dùng across workflows để tiết kiệm token và tăng reliability (độ tin cậy).
- Tình huống KHÔNG nên dùng: task cần dynamic scheduling tại runtime (CURATE yêu cầu DAG known ahead of runtime); task không expressible thành functions với defined I/O; không có WMS (workflow management system) target để deploy.

## Input cần có
- Mô tả workflow bằng natural language từ user (sketch) + context tùy chọn: user-provided modules, PDF documents, example I/O, markdown files.
- Module catalog trên disk: mỗi entry có ID, name, description, inputs/outputs, dependencies, secret names (không values), rank, keywords, provenance, usage count; index BM25 trên keywords.
- Coding agent (Claude Agent SDK hoặc tương đương) + LLM backbone (paper dùng Claude Opus 4.8).
- WMS target (paper dùng FaaSr → GitHub Actions; extensible AWS Lambda, OpenWhisk, SLURM, GCP, Kubernetes) + local testing stubs mirror actual WMS API.
- Sandbox isolation (containers/VMs) cho module execution.

## Các bước thực hiện
1. **Skeleton (Gate 1):** WCA (composition agent) generate candidate skeleton — cấu trúc workflow + mô tả từng bước bằng natural language. User review + approve, có thể cung cấp modules riêng + context. Bước này catch decomposition errors TRƯỚC khi sinh code.
2. **Resolution (Gate 2):** WCA fill mô tả input/output edges giữa các functions. MCA resolve source cho mỗi function (LLM call với context: user request, WMS description, previous revisions): [Catalog] (match trong catalog), [Cache] (revision trước), [User Provided Module], hoặc [New] (MGA generate); optional [Adapt] = dùng existing function làm context nhưng adapt. WCA fill concrete dataflow (file names) + likely PyPI dependencies. User approve.
3. **Generation (Gate 3):** MGA topological sort skeleton, duyệt tuần tự, mỗi function trong scratch directory riêng chứa CONTEXT.md (user prompt, data integrity requirements, WMS testing stubs) + per-function file (description, signature, I/O files/dataflow, dependencies, secret names). Single coding-agent session, one function per turn, validate against local stubs trước khi sang function kế. MGA KHÔNG return implementation cho đến khi tested với real data / public API data / local synthetic data. User scroll code + workflow file, approve.
4. **Deploy (Gate 4):** tạo workflow JSON deterministic bằng tool (không agent) translate skeleton → WMS schema; dependencies extra → manifest → merge vào config. Deploy lên WMS (FaaSr → GitHub Actions). User approve.
5. **Post-run (Gate 5):** WDA spawn post-run chatbot: NL summary của run + artifacts, chat hỏi đáp (invoke MCP tools download artifacts/view logs), revise workflow, commit functions vào catalog, save workflow. Failure → WDA review artifacts/logs, advise adaptation để user submit revision.
6. **Revision routing:** LLM classify revision là structural (modify DAG → loop về bước 1) hay functional (modify functions đã có → loop về bước 2).
7. **Catalog growth:** sau mỗi workflow hoàn thành, user được prompt store modules vào catalog; entries được share bằng cách copy từ trusted users.

## Output mong đợi
- Workflow deployed, reproducible trên WMS target với DAG rõ ràng, mỗi function có provenance label ([Catalog]/[Cache]/[User]/[New]/[Adapt]).
- Catalog grows theo thời gian; reuse verified modules → token usage giảm (paper: nearly halved E5→E6) + reliability tăng.
- Post-run agent phát hiện cấu hình sai / missing files / code issues mà generation agent missed (paper: E5 T-spike hard-code, E6 q_ad hard-code).

## Ví dụ áp dụng
- Solopreneur content: sketch "lấy RSS feeds → tóm tắt bằng LLM → đăng blog + newsletter"; Gate 1 skeleton 4 steps; Gate 2 MCA tái dùng module "summarize" đã verified từ workflow trước ([Catalog]), generate mới "rss-fetch" và "publish"; Gate 3 gen + test local; Gate 4 deploy cron hàng ngày; Gate 5 chatbot báo "3/10 feeds fail, suggest retry logic"; commit "summarize" mới vào catalog cho workflow sau.

## Gotchas
- Đừng skip Gate 1: WCA có xu hướng gộp các concurrent tasks thành 1 function (E1) — user phải review skeleton và split rõ ràng trước khi code.
- Catalog search là BM25 keyword, KHÔNG semantic — mô tả module sai/thiếu keywords → retrieve sai module; viết description cụ thể + keywords đầy đủ.
- Reuse ≠ đúng: [User Provided Module] vẫn cần wrap I/O + parity checks; module reused từ catalog có thể cần [Adapt] cho context mới.
- Hard-coded parameters trong reused modules (E5 T, E6 q_ad) làm sweep/parameterization vô nghĩa — post-run agent phải kiểm tra parameter flow, không chỉ runtime errors.
- Multi-agent tốn token hơn single-agent ở workflow đơn giản — chỉ dùng khi lifecycle (deploy/reuse/monitor) có giá trị.
- Baseline so sánh không có HITL — đừng hiểu nhầm "multi-agent luôn tốt hơn"; lợi ích nằm ở gates + catalog + deployment automation, không phải bản thân số lượng agent.
- Secret handling: catalog lưu TÊN secrets, không values — vẫn cần mechanism riêng để inject secret values tại runtime.
