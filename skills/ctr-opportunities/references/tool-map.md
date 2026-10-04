# Reviewed tool semantics

This is a source-reviewed map, not the live schema. Check the actual exposed tool
and current capabilities. Do not pass unsupported filters or connection IDs.

## `get_advanced_search_analytics`

Filtered, paginated analytics; up to 25,000 rows per request.

Dimensions are comma-separated. filters is a JSON array of dimension/operator/expression
objects combined with AND, overriding the single filter. data_state is all or final.
Sorting applies only to the returned page, not Google's full dataset. Missing rows are
unknown. Responses explain date boundaries, freshness and truncation.

Supported parameters in the reviewed source: `site_url`, `start_date`, `end_date`, `dimensions`, `search_type`, `row_limit`, `start_row`, `sort_by`, `sort_direction`, `filter_dimension`, `filter_operator`, `filter_expression`, `filters`, `data_state`.

## `get_capabilities`

Discover tools, auth status, enabled properties and connection IDs. Start here.

Supported parameters in the reviewed source: none.

## `get_search_by_page_query`

Find queries driving traffic to an exact page URL; row_limit <=25,000.

Supported parameters in the reviewed source: `site_url`, `page_url`, `days`, `row_limit`.

## `list_properties`

List enabled Search Console properties. Use an exact site_url in other tools.

Supported parameters in the reviewed source: none.
