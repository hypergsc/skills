# Data quality

Report the exact property, inclusive dates, America/Los_Angeles calendar boundaries
for Search Console, filters, source, freshness, row limits and truncation. Respect
requested dates and markets. Prefer confirmed final data; if freshness is unavailable,
ending three Pacific calendar days ago is a conservative fallback, not proof of
completeness. Disclose incomplete data and insufficient history rather than inventing
a comparison. Adjacent equal-length weeks preserve weekday mix.

Absent rows are unknown, not zero. Google may omit rows even below a row limit.
Sorting returned rows by impressions does not sort Google's entire dataset. Describe
a shortlist as candidates within retrieved coverage, not the site's biggest gains.
Grouped query/page sums may double-count impressions and are not property totals.

Compute aggregate CTR as total clicks / total impressions. With zero impressions,
CTR is undefined. Report CTR changes in percentage points; percentage change from a
zero baseline is undefined, so use absolute differences. Do not average row CTRs
without weights. Average position describes an impression mix, not a fixed ranking.

Separate GSC observations, third-party estimates and hypotheses. Compare reasonably
similar intent, position, device and market; separate brand only when supported by
evidence. There is no universal CTR curve. Multiple landing pages are a review signal,
not proven cannibalization. Correlation after an SEO change is not causation. Missing
queries do not establish missing content. Read actual page content before asserting
current titles or proposing specific rewrites. Label synthetic examples at the point
of display; never describe them as the visitor's site data or predicted uplift.
