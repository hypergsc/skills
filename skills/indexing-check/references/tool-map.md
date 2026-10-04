# Reviewed tool semantics

This is a source-reviewed map, not the live schema. Check the actual exposed tool
and current capabilities. Do not pass unsupported filters or connection IDs.

## `batch_url_inspection` (conditional)

Inspect up to ten URLs, one per line. Return successes and individual errors.

Supported parameters in the reviewed source: `site_url`, `urls`.

## `get_capabilities`

Discover tools, auth status, enabled properties and connection IDs. Start here.

Supported parameters in the reviewed source: none.

## `get_sitemap_details` (conditional)

Read one sitemap's processing state, errors, warnings, and submitted URL counts.

Supported parameters in the reviewed source: `site_url`, `sitemap_url`.

## `get_sitemaps` (conditional)

List property sitemaps and their processing state.

Supported parameters in the reviewed source: `site_url`.

## `inspect_url_enhanced` (conditional)

Read stored index, crawl, canonical, robots and rich-result observations for a URL.

This is Google's indexed snapshot, not a live crawl or request to index the URL.

Supported parameters in the reviewed source: `site_url`, `page_url`.

## `list_properties`

List enabled Search Console properties. Use an exact site_url in other tools.

Supported parameters in the reviewed source: none.
