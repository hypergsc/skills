---
name: content-planning
description: Plan SEO content improvements, review keyword overlap, or save a keyword shortlist and site context using HyperGSC when the user requests content planning or ongoing keyword research.
license: MIT
compatibility: Requires an existing HyperGSC MCP connection and an enabled Search Console property for live data.
---

# Find pages worth improving

Read [execution policy](references/execution-policy.md) and
[data quality](references/data-quality.md) before tool calls. Consult the
[tool map](references/tool-map.md) for semantics and scope limitations. Format
results using the [report template](references/report-template.md). The
[sample report](references/sample-report.md) is synthetic and needs no account.

## Workflow

Default to 28 comparable complete days unless the user chooses another period.
Resolve exact dates, filters and connection before metrics. Use
`get_content_opportunities` when the exposed contract supports this scope. The
reviewed implementation makes one bounded final GSC request without saving a report;
it accepts days, not arbitrary dates or filters. For a custom period/market, or if
its semantics change to persistence, use `get_advanced_search_analytics` grouped by
query,page with the requested dates, filters and final data instead. Explain loss
of built-in screening if using that fallback. Its screening thresholds are not
universal CTR benchmarks.

Inspect at most three promising pages with `get_search_by_page_query` when its
relative day range matches the candidate period. Otherwise use advanced analytics
with exact page equals filters and the same dates. Keep initial analytic calls to
five, excluding minimal access discovery; disclose insufficient coverage when that
budget prevents deeper analysis. Do not silently omit a user filter to fit a helper.
Use `find_keyword_overlap` only when considering a new URL or consolidation and
only if its period and filters match; otherwise inspect scoped query,page results.
Several URLs do not establish cannibalization.

Return up to five justified actions (fewer when evidence is sparse), using the
report template. Effort is a qualitative estimate. Check actual content before
specific title, section or internal-link assertions. No automatic providers, briefs,
saves, website edits or promised rankings.

## Explicit research and saving

If asked to recover prior goals, read `get_project_context` and
`list_saved_keywords`, following pagination only as needed. For requested keyword
expansion, `keyword_research` and `competitor_keyword_gap` are optional provider
branches; check availability and shared quota first. Keep estimates distinct.
Draft a brief only when requested, using real content or clearly marked hypotheses.

For requested saving, use `save_keywords` in batches of at most 50 (1,000 per
property); matching keyword/country/language records replace existing fields, so
retain requested data. Read latest context before `update_project_context` and
pass its expected version; omitted fields are preserved. On conflict, reread and
preserve newer work. Missing write scope requires client reconnection with gsc:read
and projects:write, not secrets in chat. Deletion/clearing requires user intent.
