# arXiv Distill Report — October 29, 2026

Summary of 3 papers distilled today. Each paper went through the 6-step distillation process and was committed and pushed to GitHub.

## Overview
- Total papers distilled: 3
- All have practical applications for solopreneurs and AI agent systems.

## [1] Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses (arXiv 2610.36114v1)

**What it does:** The paper studies why AI agents (autonomous agents that can take actions) often lose evidence when calling tools. The agent harness (software between the AI model and the tool) truncates tool results by character position rather than by value, so important evidence at the end is deleted entirely while the context window (the memory region holding the text the model is currently processing) remains 93% empty. Out of 11,189 tool results, 34% were truncated and became broken JSON (JavaScript Object Notation — a data interchange format). Diagnostic errors may lie in the harness rather than the model.

**What we learned:** Do not measure only accuracy (rate of correct results) when evaluating an agent system. Instead, measure yield (the ratio of evidence delivered to the model versus evidence produced) at each boundary (junction point between steps) of the information pipeline, and count tool calls. An agent with an alternative path will find another way before giving a wrong answer, so the first loss is extra work rather than an immediate wrong answer.

**How to apply it:** When building an agent system that calls APIs (e.g., a customer-care agent calling an order API), instrument (install monitoring on) each pipeline boundary, count evidence delivered versus produced, and report yield alongside accuracy on every evaluation. Instead of truncating by character, truncate by line or by JSON field so important evidence is not deleted.

## [2] Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG (arXiv 2610.36915v1)

**What it does:** The paper introduces a decision model (a model that returns probabilities over a fixed set of choices in a single forward pass, without generating text) to classify the type of conflict between information sources in a RAG system (retrieval-augmented generation — a technique that retrieves external information to generate answers). 11 decision models from 7 providers classify nearly as well as an LLM but cost 4–39× less and are 2.6–6.0× faster. The model's confidence (degree of certainty) ranks its errors, so only uncertain queries can be escalated to a high-end LLM (cascade — escalation, sending the hard part to a more expensive model) at just 25–37% of the LLM's cost.

**What we learned:** Classification is cheaper than generation. In a RAG system, replace a long LLM prompt with a cheap decision model to classify conflicts between search results, then generate the answer based on the type. Send the top 25% most uncertain queries to a high-end LLM and keep 75% with the decision model — reducing LLM cost by 63–75% while maintaining LLM-level accuracy.

**How to apply it:** If you use RAG to answer customers from multiple sources (website, documents, email) and the sources contradict each other, use a cheap decision model to classify the type of conflict (complementary information, conflicting opinions, outdated information, misinformation), and only call the expensive LLM for the uncertain part. Example: classify customer emails into fixed topics (complaint, pricing inquiry, technical support) using a decision model, and only escalate uncertain emails to a high-end LLM or a human agent.

## [3] Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation (arXiv 2610.37242v1)

**What it does:** The paper builds a system that helps LLM agents call enterprise APIs (endpoints — specific addresses of an API function for software data exchange) reliably across multiple steps. An agent picks the right API but still fails because it hallucinates codes (generates non-existent codes/values), omits required references, or books a hotel before a flight (violating process order). The paper combines OData metadata (a web service standard for reading and writing data over HTTP) and BPMN processes (a standard for describing business processes) into a typed property graph (a graph that stores data as nodes and directed edges, both carrying type labels and key-value attributes), using hybrid retrieval (hybrid search — combining dense embedding seeds with expansion along process edges). The agent completes 38.7% of tasks versus 10.3% for ChunkRAG, and the rate of invalid API calls drops from 79% to 3%.

**What we learned:** Picking the right endpoint is not enough — the agent also needs process-order constraints (rules about step ordering) and parameter constraints (required keys, valid codes) in the retrieval context. Providing full typed context before calling an API reduces invalid calls to 3%. The benefit only appears on queries with process signals.

**How to apply it:** When building an agent that automates calls to multiple enterprise APIs in sequence (e.g., a ticket-booking system: select flight → reserve seat → book hotel using a reference code, in the right order and with valid fare codes), provide the schema (data structure) and processing workflow in the retrieval context, not just a list of endpoints. Build a typed property graph combining service metadata and reference processes, linking each activity to the data it reads or writes.

## WHAT YOU CAN APPLY TO YOURSELF

1. **Measure yield (result rate) at each pipeline boundary, not just accuracy.** When evaluating a tool-calling agent, count evidence delivered to the model versus evidence produced, and report yield alongside accuracy. Example: for a customer-care agent calling an order API, check whether the API result is complete before the model reads it.

2. **Use a cheap decision model to classify before calling an expensive LLM.** In a RAG system or content classification, replace a long LLM prompt with a low-cost decision model to assign labels, and only escalate the uncertain portion to an expensive LLM. Example: classify customer emails with a decision model, and only escalate uncertain emails to a human or a high-end LLM — cutting cost by 63–75%.

3. **Provide all process and parameter constraints before the agent calls an API.** Do not just give the agent a list of endpoints. Provide the schema, required keys, valid codes, and processing order in the retrieval context. Example: a business travel-booking agent needs valid fare codes and the order of reserving a seat before a hotel — provide this workflow to avoid incorrect API calls (cutting invalid calls from 79% down to 3%).
