# Awesome Google Merchant Center MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Find rejected products, inspect market prices, refresh feeds, and update catalog data through Merchant Center MCP tools.

**10 MCPs · 127 tools** · [Search every tool](TOOLS.md). Each server has a reference page with descriptions and full input schemas.

Merchant Center tools and their setup helpers are included; unrelated tools from multi-service servers are omitted. Groups follow the implemented tools, with each MCP listed once under its primary task.

**Latest source review:** 2026-10-13, using runtime tool discovery and source inspection. No authenticated account operations were tested. Tool references distinguish reads, writes, setup, and mixed operations.

## Contents

- [Diagnose products and account issues (4)](#diagnose-products-and-account-issues)
- [Analyze performance and market prices (1)](#analyze-performance-and-market-prices)
- [Manage products, feeds, and promotions (3)](#manage-products-feeds-and-promotions)
- [Manage accounts, inventory, and conversions (1)](#manage-accounts-inventory-and-conversions)
- [Build Merchant API integrations (1)](#build-merchant-api-integrations)
- [CLIs (3)](#clis)
- [SDKs (8)](#sdks)

## Diagnose products and account issues

4 MCPs. Find disapprovals, inspect eligibility, and check feed health.

| MCP | What you can do | Tools |
| --- | --- | --- |
| [**Google Merchant API MCP Access Service**](docs/mcps/google-data.md) | Inspect product status, account issues, program eligibility, and upload results; query reports or create and refresh data sources. Try [`list_aggregate_product_statuses`](docs/mcps/google-data.md#list_aggregate_product_statuses), [`get_file_upload`](docs/mcps/google-data.md#get_file_upload). | [13](docs/mcps/google-data.md#tools) |
| [**YerayRodri/merchant-center-mcp**](docs/mcps/yeray.md) | Find product issues and query catalog reports through a small read-only interface. Try [`get_product_issues`](docs/mcps/yeray.md#get_product_issues), [`search_report`](docs/mcps/yeray.md#search_report). | [4](docs/mcps/yeray.md#tools) |
| [**MoonEyes/google-ecommerce-mcp**](docs/mcps/mooneyes.md) | Inspect product-level issues, view configured data sources, and run Merchant reports. Try [`merchant_product_issues`](docs/mcps/mooneyes.md#merchant_product_issues), [`merchant_report_query`](docs/mcps/mooneyes.md#merchant_report_query). | [4](docs/mcps/mooneyes.md#tools) |
| [**kLOsk/adloop**](docs/mcps/adloop.md) | Discover accounts and inspect aggregate product and account issues; feed health may trigger developer registration. Try [`list_merchant_accounts`](docs/mcps/adloop.md#list_merchant_accounts), [`get_merchant_feed_health`](docs/mcps/adloop.md#get_merchant_feed_health). | [2](docs/mcps/adloop.md#tools) |

## Analyze performance and market prices

1 MCP. Query product clicks, conversions, price suggestions, and MCQL reports.

| MCP | What you can do | Tools |
| --- | --- | --- |
| [**MadMaxen92/marketing-mcp**](docs/mcps/marketing.md) | Query product performance, price recommendations, eligibility, and read-only MCQL reports. Try [`get_merchant_product_performance`](docs/mcps/marketing.md#get_merchant_product_performance), [`get_merchant_price_insights`](docs/mcps/marketing.md#get_merchant_price_insights). | [8](docs/mcps/marketing.md#tools) |

## Manage products, feeds, and promotions

3 MCPs. Create or update product inputs, prepare feed changes, and inspect promotions.

| MCP | What you can do | Tools |
| --- | --- | --- |
| [**A1-x-Tech/mcp-google-merchants**](docs/mcps/a1.md) | Insert, patch, or delete product inputs; create and refresh data sources; manage promotions and inspect price reports. Try [`update_product_input`](docs/mcps/a1.md#update_product_input), [`price_competitiveness`](docs/mcps/a1.md#price_competitiveness). | [28](docs/mcps/a1.md#tools) |
| [**ScaleLean/google-ads-mcp-starter**](docs/mcps/scalelean.md) | Prepare, validate, approve, apply, and verify controlled feed and product changes; inspect products, issues, and reports. Try [`merchant_prepare_write`](docs/mcps/scalelean.md#merchant_prepare_write), [`merchant_apply_approved_write`](docs/mcps/scalelean.md#merchant_apply_approved_write). | [14](docs/mcps/scalelean.md#tools) |
| [**yasserstudio/gmc · embedded MCP**](docs/mcps/gmc.md) | Insert or delete product inputs, query reports, inspect issues, and validate local feed files before upload. Try [`products_insert`](docs/mcps/gmc.md#products_insert), [`preflight`](docs/mcps/gmc.md#preflight). | [12](docs/mcps/gmc.md#tools) |

## Manage accounts, inventory, and conversions

1 MCP. Work with account settings, local and regional inventory, and conversion sources.

| MCP | What you can do | Tools |
| --- | --- | --- |
| [**marwa-mrwan/google-clarity-mcp-codex**](docs/mcps/marwa.md) | Manage subaccounts, local and regional inventory, and conversion sources alongside product, feed, and promotion operations. Try [`merchant_insert_local_inventory`](docs/mcps/marwa.md#merchant_insert_local_inventory), [`merchant_create_conversion_source`](docs/mcps/marwa.md#merchant_create_conversion_source). | [40](docs/mcps/marwa.md#tools) |

## Build Merchant API integrations

1 MCP. Retrieve official guides and task-specific code samples.

| MCP | What you can do | Tools |
| --- | --- | --- |
| [**Google Merchant API Developer Documentation MCP**](docs/mcps/google-docs.md) | Look up official Merchant API guidance and retrieve task-specific code samples. Try [`query_mapi_docs`](docs/mcps/google-docs.md#query_mapi_docs), [`find_mapi_code_sample`](docs/mcps/google-docs.md#find_mapi_code_sample). | [2](docs/mcps/google-docs.md#tools) |

## CLIs

3 command-line tools for Merchant Center operations or product-feed preparation.

| Project | Merchant Center functionality |
| --- | --- |
| [**almoretti/gmc-cli**](https://github.com/almoretti/gmc-cli) | Manages Merchant API v1 accounts, products, data sources, reports, and promotions through a Python CLI with JSON output and dry-run support. |
| [**yasserstudio/gmc**](https://github.com/yasserstudio/gmc) | Manages Merchant API accounts and products, validates feeds, and runs setup and migration diagnostics through a TypeScript CLI. Includes an [embedded MCP server](docs/mcps/gmc.md) with a complete tool reference. |
| [**BurhanBeigh/merchant-feed-builder**](https://github.com/BurhanBeigh/merchant-feed-builder) | Generates local Google Merchant Center XML or TSV feeds from Shopify catalog data through a Python CLI with product-field validation. Produces feed files for submission rather than uploading them to Merchant Center. |

## SDKs

8 official client-library entries: seven language-specific Merchant API library families and the experimental alpha distribution. Each language family contains separate packages for Merchant sub-APIs.

| Project | Merchant Center functionality |
| --- | --- |
| [**Google Merchant API — Java**](https://developers.google.com/merchant/api/client-libraries/java) | Provides Java client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — PHP**](https://developers.google.com/merchant/api/client-libraries/php) | Provides PHP client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — Python**](https://developers.google.com/merchant/api/client-libraries/python) | Provides Python client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — Node.js**](https://developers.google.com/merchant/api/client-libraries/nodejs) | Provides Node.js client libraries with TypeScript support for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — .NET/C#**](https://developers.google.com/merchant/api/client-libraries/dotnet) | Provides .NET client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — Go**](https://developers.google.com/merchant/api/client-libraries/go) | Provides Go client packages for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — Ruby**](https://developers.google.com/merchant/api/client-libraries/ruby) | Provides Ruby client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**google/merchant-api-alpha-client**](https://github.com/google/merchant-api-alpha-client) | Distributes experimental Merchant API alpha client libraries for testing and demonstration in seven languages. Requires local installation of the supplied library archives. |

[Contribute a tool](CONTRIBUTING.md).
