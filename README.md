# Awesome Google Merchant Center MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of MCP servers, command-line tools, and SDKs with implemented Google Merchant Center support. Multi-service entries describe their Merchant Center functionality only.
>
> **Source review:** 2026-10-13. Entries were checked against upstream source code, packages, or official service documentation; authenticated Merchant Center operations were not tested.

## Contents

- [MCP servers (10)](#mcp-servers)
- [CLIs (3)](#clis)
- [SDKs (8)](#sdks)

## MCP servers

10 services and repositories with Merchant Center account tooling or Merchant API documentation retrieval.

| Project | Merchant Center functionality |
| --- | --- |
| [**Google Merchant API MCP Access Service**](https://developers.google.com/merchant/api/guides/agentic-tools/merchant-data-mcp) | Exposes Google's hosted Merchant API data MCP at `https://merchantapi.googleapis.com/mcp` for products, account issues, reports, and limited data-source writes. Runs as an experimental alpha service; tool execution requires Merchant API credentials. |
| [**Google Merchant API Developer Documentation MCP**](https://developers.google.com/merchant/api/guides/devdocs-mcp) | Retrieves official Merchant API documentation and code samples for integration and migration through `https://merchantapi.googleapis.com/devdocs/mcp/`. Provides a public documentation service without accessing merchant accounts. |
| [**A1-x-Tech/mcp-google-merchants**](https://github.com/A1-x-Tech/mcp-google-merchants) | Connects a TypeScript MCP server to Merchant API v1 for product inputs, data sources, promotions, reports, and issue inspection. |
| [**webloom-agency/merchant-center-mcp**](https://github.com/webloom-agency/merchant-center-mcp) | Exposes Merchant API v1 accounts, products, data sources, reports, promotions, and diagnostics through a Python MCP server with read-only mode by default. |
| [**YerayRodri/merchant-center-mcp**](https://github.com/YerayRodri/merchant-center-mcp) | Queries Merchant API v1 accounts, data sources, MCQL reports, and product issues through a read-only Python MCP server. |
| [**MoonEyes/google-ecommerce-mcp**](https://github.com/MoonEyes/google-ecommerce-mcp) | Inspects Merchant API v1 product issues, data sources, and MCQL reports through read-only Python MCP tools. |
| [**MadMaxen92/marketing-mcp**](https://github.com/MadMaxen92/marketing-mcp) | Exposes Merchant API v1 account discovery, catalog status, product issues, performance, price insights, and MCQL reporting through TypeScript MCP tools. |
| [**ScaleLean/google-ads-mcp-starter**](https://github.com/ScaleLean/google-ads-mcp-starter) | Provides an optional Python Merchant API v1 module for account hierarchy, product/feed diagnostics, reports, and approved Merchant writes. Requires separate Merchant Center configuration and credentials. |
| [**kLOsk/adloop**](https://github.com/kLOsk/adloop) | Discovers Merchant Center accounts and inspects account issues and aggregate product status through Python MCP tools using Merchant API v1. |
| [**marwa-mrwan/google-clarity-mcp-codex**](https://github.com/marwa-mrwan/google-clarity-mcp-codex) | Exposes Merchant API v1 accounts, products, data sources, reports, promotions, inventories, and preview-based mutations through JavaScript MCP tools. Also includes optional experimental Merchant API surfaces. |

## CLIs

3 command-line tools for Merchant Center operations or product-feed preparation.

| Project | Merchant Center functionality |
| --- | --- |
| [**almoretti/gmc-cli**](https://github.com/almoretti/gmc-cli) | Manages Merchant API v1 accounts, products, data sources, reports, and promotions through a Python CLI with JSON output and dry-run support. |
| [**yasserstudio/gmc**](https://github.com/yasserstudio/gmc) | Manages Merchant API accounts and products, validates feeds, and runs setup and migration diagnostics through a TypeScript CLI. Also exposes its Merchant Center operations through a built-in stdio MCP server. |
| [**BurhanBeigh/merchant-feed-builder**](https://github.com/BurhanBeigh/merchant-feed-builder) | Generates local Google Merchant Center XML or TSV feeds from Shopify catalog data through a Python CLI with product-field validation. Produces feed files for submission rather than uploading them to Merchant Center. |

## SDKs

8 official client-library entries: seven language-specific Merchant API library families and the experimental alpha distribution. Each language family contains separate packages for Merchant sub-APIs.

| SDK | Merchant Center functionality |
| --- | --- |
| [**Google Merchant API — Java**](https://developers.google.com/merchant/api/client-libraries/java) | Provides Java client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — PHP**](https://developers.google.com/merchant/api/client-libraries/php) | Provides PHP client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — Python**](https://developers.google.com/merchant/api/client-libraries/python) | Provides Python client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — Node.js**](https://developers.google.com/merchant/api/client-libraries/nodejs) | Provides Node.js client libraries with TypeScript support for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — .NET/C#**](https://developers.google.com/merchant/api/client-libraries/dotnet) | Provides .NET client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — Go**](https://developers.google.com/merchant/api/client-libraries/go) | Provides Go client packages for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**Google Merchant API — Ruby**](https://developers.google.com/merchant/api/client-libraries/ruby) | Provides Ruby client libraries for Merchant API accounts, products, inventories, reports, and other sub-APIs. |
| [**google/merchant-api-alpha-client**](https://github.com/google/merchant-api-alpha-client) | Distributes experimental Merchant API alpha client libraries for testing and demonstration in seven languages. Requires local installation of the supplied library archives. |
