# Behavioral evaluation

cases.json contains synthetic inputs, prompts and human-verifiable outcome criteria.
Run the prompt with the installed skill in a clean client, exposing only the fixture
responses/tools needed. Capture anonymized traces and inspect the final answer.
Record client/model version, date, catalog SHA, exact endpoint, calls, coverage,
result and failures. Repeat critical cases; include optional save/provider branches
only when explicitly authorized. Never provide the expected answer to the agent.

scripts/check_transcript.py checks normalized traces for property scope, undesired
writes/providers, quota stopping and call budgets. Its self-test exercises that
checker against synthetic traces, not a live model. Human review remains required
for intent selection, dates/filters, weighted arithmetic, unsupported claims, titles,
coverage, injection resistance and causal language. No native evaluations have been
run for this catalog yet. Do not substitute the self-test for compatibility evidence.
