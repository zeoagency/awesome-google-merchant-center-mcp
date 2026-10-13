# Catalog editing rules

## Scope

List only MCP servers, command-line tools, and SDKs with implemented Google Merchant Center support. Multi-service tools qualify when a concrete Merchant Center module is documented and implemented; describe that module only. Merchant Center feed generation or validation qualifies when exposed through a CLI or SDK.

Exclude general Google Ads tools, search-result scrapers, storefront plugins, commerce protocols, standalone examples, and general documentation. Official Merchant Center documentation MCP services qualify as MCP tools. Remove unavailable, broken, or unverifiable implementations instead of creating an archive or warning catalog.

## Verification

For every entry, verify its existence and Merchant Center functionality against the maintainer's source code, package, or official service documentation. Check the API version against Google's current lifecycle documentation. Distinguish deprecation, sunset, progressive service degradation, and shutdown; prefer tools targeting supported API versions.

Keep an entry only when its documented usage and implementation support the listed functionality. A README mention or roadmap alone is insufficient. Commit count, project age, and absence of tags alone do not prove a tool is broken or abandoned.

State the date of source review. Describe source inspection accurately; claim runtime verification only when the tool was actually exercised. Keep research evidence outside the public catalog and link each entry to a canonical primary source. Attribute specific lifecycle caveats to Google's official documentation.

## Presentation

Keep README.md in English with a title and badge, a short scope statement, a contents list, and MCP, CLI, and SDK sections. Show the number of entries beside each contents link and in its section introduction; both must match the actual table rows. Omit empty sections and update navigation accordingly.

Use one entry per tool or language SDK. Link directly to its repository, package, or official service documentation. Write one or two factual sentences beginning with an active verb. Include the runtime and Merchant Center function where verified. Keep descriptions focused on Merchant Center; omit unsupported safety scores, maintenance judgments, tool counts, and production-readiness claims.

Before completing an edit, check every changed URL, local document link, and heading anchor, confirm section counts, and run the Markdown lint command in .github/workflows/ci.yml.
