# Catalog editing rules

## Scope

List MCP servers, CLIs, and SDKs with implemented Google Merchant Center support. Multi-service MCP pages include Merchant tools and relevant setup helpers; record the full registry count and explain omitted tools. Merchant feed generation or validation qualifies when exposed through a CLI or SDK.

Exclude general advertising tools, scrapers, storefront plugins, commerce protocols, standalone examples, and general documentation. Merchant-specific documentation MCPs qualify. Remove unavailable, broken, or unverifiable implementations rather than maintaining a warning catalog. Commit count and project age alone do not establish abandonment.

## Tool verification

Audit one MCP at a time. Prefer actual MCP tools/list or runtime registry descriptors; resolve pagination, imported schemas, and optional registrations. When runtime extraction is impractical, evaluate the actual descriptor factories and verify their registration wiring. Distinguish source extraction from server startup and live API testing.

Preserve exact names, full descriptions, and complete inputSchema objects, including nested definitions, required fields, defaults, enums, and free-form objects. Keep undefined constraints undefined; document implementation-only defaults or restrictions separately. Pin code links to the inspected revision and record extraction date and method.

Review the tool handlers before assigning task categories and effects. Classify POST report queries as reads, direct mutations as writes, authentication/registration changes as setup, and reads that can persist setup or ledger state as mixed. Describe limitations that materially affect returned results or mutation behavior. Check API lifecycle claims against current Google documentation.

## Editing and completion

catalog/manifest.json defines server order, task categories, and companion CLI/SDK content. catalog/<id>.json is the source of truth for each MCP's reviewed descriptors and editorial metadata. README.md, TOOLS.md, and docs/mcps/*.md are generated; edit their catalog sources and run `python3 scripts/build_catalog.py`.

Choose an MCP's primary group from its implemented tools. Use one main-page entry per MCP with concrete tool examples; the alphabetical index must include every published tool/provider pair and link to its detailed definition. Keep full descriptions and schemas on the detail pages, with short summaries and parameter tables visible.

Before completion, compare published descriptors with the extraction output, review source behavior, run `python3 scripts/build_catalog.py --check` and the Markdown lint command in .github/workflows/ci.yml, and verify changed upstream links. Generated page counts and local anchors must match the catalog. Keep temporary extraction environments and research logs outside the repository.
