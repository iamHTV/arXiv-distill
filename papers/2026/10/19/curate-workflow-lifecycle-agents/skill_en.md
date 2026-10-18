# Skill: CURATE Lifecycle Loop (Sketch–Reify–Test–Deploy with Module Catalog)
Source: 2608.04270v2
Type: framework / workflow

## When to use this skill
- You need to build or automate a multi-step workflow (content pipeline, data processing, automation) with an LLM coding agent, and you want the workflow reproducible + deployable, not just loose code.
- You have verified modules worth reusing across workflows to save tokens and improve reliability.
- Do NOT use: tasks needing runtime dynamic scheduling (CURATE requires the DAG known ahead of runtime); tasks not expressible as functions with defined I/O; no WMS target to deploy to.

## Inputs required
- A natural-language workflow description from the user (sketch) + optional context: user-provided modules, PDF documents, example I/O, markdown files.
- An on-disk module catalog: each entry has ID, name, description, inputs/outputs, dependencies, secret names (not values), rank, keywords, provenance, usage count; BM25 index on keywords.
- A coding agent (Claude Agent SDK or equivalent) + LLM backbone (paper: Claude Opus 4.8).
- A WMS target (paper: FaaSr → GitHub Actions; extensible to AWS Lambda, OpenWhisk, SLURM, GCP, Kubernetes) + local testing stubs mirroring the actual WMS API.
- Sandbox isolation (containers/VMs) for module execution.

## Steps
1. **Skeleton (Gate 1):** the WCA (composition agent) generates a candidate skeleton — the workflow structure + a natural-language description of each step. The user reviews and approves, and may supply their own modules + context. This catches decomposition errors BEFORE code generation.
2. **Resolution (Gate 2):** the WCA fills in input/output edge descriptions between functions. The MCA resolves the source of each function (an LLM call with the user request, WMS description, and previous revisions as context): [Catalog] (catalog match), [Cache] (earlier revision), [User Provided Module], or [New] (MGA generates); optional [Adapt] = use an existing function as context but adapt it. The WCA fills concrete dataflow (file names) + likely PyPI dependencies. The user approves.
3. **Generation (Gate 3):** the MGA topologically sorts the skeleton and traverses it sequentially, each function in its own scratch directory containing a CONTEXT.md (user prompt, data integrity requirements, WMS testing stubs) plus a per-function file (description, signature, I/O files/dataflow, dependencies, secret names). A single coding-agent session, one function per turn, validated against local stubs before moving on. The MGA must not return an implementation until it has tested with real data / public API data / local synthetic data. The user scrolls the code + workflow file and approves.
4. **Deploy (Gate 4):** build the workflow JSON deterministically with a tool (not an agent) translating the skeleton to the WMS schema; extra dependencies go to a manifest merged into the config. Deploy to the WMS (FaaSr → GitHub Actions). The user approves.
5. **Post-run (Gate 5):** the WDA spawns a post-run chatbot: an NL summary of the run + artifacts, Q&A (invoking MCP tools to download artifacts/view logs), workflow revision, committing functions to the catalog, saving the workflow. On failure, the WDA reviews artifacts/logs and advises an adaptation for the user to submit as a revision.
6. **Revision routing:** an LLM classifies the revision as structural (modify the DAG → loop back to step 1) or functional (modify existing functions → loop back to step 2).
7. **Catalog growth:** after each completed workflow, the user is prompted to store modules in the catalog; entries are shared by copying from trusted users.

## Expected output
- A deployed, reproducible workflow on the WMS target with a clear DAG, each function carrying a provenance label ([Catalog]/[Cache]/[User]/[New]/[Adapt]).
- A catalog that grows over time; reusing verified modules cuts token usage (paper: nearly halved E5→E6) and improves reliability.
- The post-run agent catches configuration errors / missing files / code issues the generation agent missed (paper: E5 hard-coded T spikes, E6 hard-coded q_ad).

## Example application
- A solopreneur's content workflow: sketch "fetch RSS feeds → LLM summaries → publish blog + newsletter"; Gate 1 skeleton of 4 steps; Gate 2 the MCA reuses a verified "summarize" module from a previous workflow ([Catalog]) and generates new "rss-fetch" and "publish" functions; Gate 3 generate + local test; Gate 4 deploy as a daily cron; Gate 5 the chatbot reports "3/10 feeds fail, suggest retry logic"; commit the new "summarize" to the catalog for later workflows.

## Gotchas
- Don't skip Gate 1: the WCA tends to merge concurrent tasks into one function (E1) — the user must review the skeleton and split tasks clearly before any code exists.
- Catalog search is BM25 keywords, NOT semantic — a poorly described or under-keyworded module retrieves wrong matches; write specific descriptions with complete keywords.
- Reuse ≠ correct: [User Provided Modules] still need I/O wrapping + parity checks; catalog modules may need [Adapt] for new contexts.
- Hard-coded parameters inside reused modules (E5's T, E6's q_ad) make sweeps/parameterization meaningless — the post-run agent must check parameter flow, not just runtime errors.
- Multi-agent costs more tokens than a single agent on simple workflows — use it only when the lifecycle (deploy/reuse/monitor) is worth it.
- The baseline comparison had no HITL — don't misread "multi-agent is always better"; the benefits come from the gates + catalog + deployment automation, not the agent count itself.
- Secret handling: the catalog stores secret NAMES, not values — you still need a separate mechanism to inject secret values at runtime.
