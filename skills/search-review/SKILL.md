---
name: search-review
description: Review changes in Google Search Console performance using HyperGSC when the user asks for a weekly search review or traffic diagnosis.
license: MIT
compatibility: Requires an existing HyperGSC MCP connection and an enabled Search Console property for live data.
---

# Weekly SEO review

Read [execution policy](references/execution-policy.md) and
[data quality](references/data-quality.md) before tool calls. Consult the
[tool map](references/tool-map.md) for semantics and scope limitations. Format
results using the [report template](references/report-template.md). The
[sample report](references/sample-report.md) is synthetic and needs no account.

## Workflow

Resolve exact property, connection and requested dates/filters. Default to the last
complete seven days and the preceding seven, with the same weekday mix, final data
where supported, and matching search type and dimensions. Confirm usable history.
Use `get_performance_overview` for totals/trend only when its days-based range and
unfiltered scope match the request and a daily trend is useful. Use
`compare_search_periods` with empty dimensions for property-wide totals in both
windows when supported; its default query grouping is bounded query evidence, not
property totals. For equal inclusive windows, period1 is earlier, period2 later;
click changes are later minus earlier, position improvement is earlier minus later.
The returned CTR difference uses a 0–1 ratio; multiply it by 100 for percentage points.
Neither helper accepts arbitrary
filters; for filtered reviews, use `get_advanced_search_analytics` in each period,
including an ungrouped totals read if supported. Do not substitute page/query sums
for property totals or request the same evidence twice.

Investigate material changes with advanced page/query breakdowns, using
`get_search_by_page_query` only when its relative range matches. Keep initial analysis
to four calls, with up to two justified deeper reads; disclose incomplete coverage.
Return exact periods, clicks and impressions, absolute/relative changes, CTR change
in percentage points, cautious position interpretation, contributing pages/queries
and three supported actions (fewer if evidence cannot support three).

Missing history or rows cannot become a fabricated comparison. Zero baseline
percentage change is undefined. Separate demand, query mix and seasonality hypotheses
from observations. Do not claim a change caused traffic gains. This weekly review
runs on demand; do not schedule it or chain every other skill automatically.
