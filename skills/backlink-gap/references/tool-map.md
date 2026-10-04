# Reviewed tool semantics

This is a source-reviewed map, not the live schema. Check the actual exposed tool
and current capabilities. Do not pass unsupported filters or connection IDs.

## `backlink_gap` (conditional)

Compare referring-domain samples with 1–3 explicit competitors. Max.

Uses 1 backlinks unit for the selected domain and 1 per competitor (up to 4).
Charges dispatched failures, returns partial results and actual quota receipts.
Target-provider failure stops comparison. Domains absent from bounded target rows
are unobserved candidates, not proven gaps; review relevance and current link status.

Supported parameters in the reviewed source: `site_url`, `competitors`, `row_limit`, `limit`, `connection_id`.

## `get_capabilities`

Discover tools, auth status, enabled properties and connection IDs. Start here.

Supported parameters in the reviewed source: none.

## `list_properties`

List enabled Search Console properties. Use an exact site_url in other tools.

Supported parameters in the reviewed source: none.

## `referring_domains` (conditional)

Read up to 100 external referring domains ordered by provider rank. Max.

Uses one backlinks unit. Bounded rows cannot establish absence or dofollow links.

Supported parameters in the reviewed source: `target`, `limit`.
