---
name: ctr-opportunities
description: Find pages with impressions but weak click-through performance using HyperGSC when the user asks for CTR improvements or search snippet opportunities.
license: MIT
compatibility: Requires an existing HyperGSC MCP connection and an enabled Search Console property for live data.
---

# Find search snippet opportunities

Read [execution policy](references/execution-policy.md) and
[data quality](references/data-quality.md) before tool calls. Consult the
[tool map](references/tool-map.md) for semantics and scope limitations. Format
results using the [report template](references/report-template.md). The
[sample report](references/sample-report.md) is synthetic and needs no account.

## Workflow

Resolve the user's period and filters. Default to 28 complete days, preferring
confirmed final data. Fetch page candidates with `get_advanced_search_analytics`,
using exact dates, dimensions=page, final data and an initial row limit of 50 when
supported. Inspect returned ordering; sorting by impressions orders only retrieved
rows. Describe coverage explicitly, even when fewer than the limit return.

Inspect up to three candidates with `get_search_by_page_query`, initial row limit
20, only if its relative period matches and it preserves the selected scope.
Otherwise use advanced analytics with the exact page filter, dates and original
filters. Initial budget: one candidate call plus up to three breakdowns, apart from
minimum access discovery. Tell the user if coverage or budget prevents a conclusion.

Compare similar position, intent, device and market when available. Separate brand
and non-brand only with evidence. Poor position and weak CTR require different
investigations; do not apply a universal CTR curve. Return observed metrics and an
experiment with what remains to check. If titles are requested, read the actual
page through a permitted tool or ask for content. Never invent the current title.
Any uplift arithmetic is a scenario with explicit assumptions, not expected clicks.
Do not publish changes, save research or call providers by default.
