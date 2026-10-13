# MoonEyes/google-ecommerce-mcp

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://github.com/MoonEyes/google-ecommerce-mcp) · [Descriptors](../../catalog/mooneyes.json)

Inspect product-level issues, view configured data sources, and run Merchant reports.

**4 tools:** 4 read. **Reviewed:** 2026-10-13.

**Extraction:** Runtime FastMCP registry inspection; independently re-extracted, with no handlers called.

**Source revision:** [55cae2ade854](https://github.com/MoonEyes/google-ecommerce-mcp/tree/55cae2ade8547b92554f4adf90c0d7faaf3cd28b).

All 4 Merchant Center and relevant setup tools are included; 9 unrelated tools from the 13-tool registry are omitted.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`server_status`](#server_status) | Check setup and API usage | read |
| [`merchant_data_sources`](#merchant_data_sources) | Manage products, feeds, and promotions | read |
| [`merchant_product_issues`](#merchant_product_issues) | Diagnose products and account issues | read |
| [`merchant_report_query`](#merchant_report_query) | Analyze performance and market prices | read |

## server_status

Which Google services are configured for this server, and whether the stored OAuth token works.

<details>
<summary>Full upstream description</summary>

```text
Which Google services are configured for this server, and whether the stored OAuth token works.
Call it first when another tool answers not_configured or not_authenticated. Returns one boolean per
service, the token storage (os-keyring or file), "token": "ok" or the error, and the package version.
```

</details>

**Effect:** read. **Task:** Check setup and API usage. [Definition](https://github.com/MoonEyes/google-ecommerce-mcp/blob/55cae2ade8547b92554f4adf90c0d7faaf3cd28b/src/google_ecommerce_mcp/server.py#L272).

No named parameters. See the exact schema below.

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {},
  "title": "server_statusArguments",
  "type": "object"
}
```

</details>

## merchant_data_sources

Merchant Center data sources (feeds): labels, countries, languages, fetch URLs.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/MoonEyes/google-ecommerce-mcp/blob/55cae2ade8547b92554f4adf90c0d7faaf3cd28b/src/google_ecommerce_mcp/server.py#L462).

**Note:** Returns one API page; this tool does not expose a continuation parameter.

No named parameters. See the exact schema below.

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {},
  "title": "merchant_data_sourcesArguments",
  "type": "object"
}
```

</details>

## merchant_product_issues

Merchant Center products with their item-level issues (disapprovals, demotions, warnings) per destination,

<details>
<summary>Full upstream description</summary>

```text
Merchant Center products with their item-level issues (disapprovals, demotions, warnings) per destination,
with the attribute to fix. Scans every page of products up to max_pages. Returns {"products": [{offer_id,
feed_label, title, link, issues: [{code, severity, description, attribute, destination}]}], "scanned": n,
"truncated": bool}.
```

</details>

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/MoonEyes/google-ecommerce-mcp/blob/55cae2ade8547b92554f4adf90c0d7faaf3cd28b/src/google_ecommerce_mcp/server.py#L470).

**Note:** Scanning stops at max_pages or limit. Check the returned truncated field and any partial-result error before treating the result as complete.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `limit` | integer | No | 50 | Maximum products returned (1 to 1000) |
| `only_with_issues` | boolean | No | true | True: only products with at least one issue; False: every product |
| `max_pages` | integer | No | 20 | Pages of 250 products to scan at most |

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {
    "limit": {
      "default": 50,
      "description": "Maximum products returned (1 to 1000)",
      "maximum": 1000,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    },
    "only_with_issues": {
      "default": true,
      "description": "True: only products with at least one issue; False: every product",
      "title": "Only With Issues",
      "type": "boolean"
    },
    "max_pages": {
      "default": 20,
      "description": "Pages of 250 products to scan at most",
      "maximum": 200,
      "minimum": 1,
      "title": "Max Pages",
      "type": "integer"
    }
  },
  "title": "merchant_product_issuesArguments",
  "type": "object"
}
```

</details>

## merchant_report_query

Run a Merchant Center report (Merchant API reports:search) with an MCQL query, for example product status

<details>
<summary>Full upstream description</summary>

```text
Run a Merchant Center report (Merchant API reports:search) with an MCQL query, for example product status
or free-listing performance. Returns Google's raw result rows.
```

</details>

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://github.com/MoonEyes/google-ecommerce-mcp/blob/55cae2ade8547b92554f4adf90c0d7faaf3cd28b/src/google_ecommerce_mcp/server.py#L514).

**Note:** Returns one reports:search response; this tool does not follow continuation tokens.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `query` | string | No | "SELECT id, offer_id, title, aggregated_reporting_context_status FROM product_view LIMIT 50" | Merchant Center Query Language (MCQL) statement. Tables include product_view (must select id) and product_performance_view (clicks, impressions by date or offer) |

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {
    "query": {
      "default": "SELECT id, offer_id, title, aggregated_reporting_context_status FROM product_view LIMIT 50",
      "description": "Merchant Center Query Language (MCQL) statement. Tables include product_view (must select id) and product_performance_view (clicks, impressions by date or offer)",
      "title": "Query",
      "type": "string"
    }
  },
  "title": "merchant_report_queryArguments",
  "type": "object"
}
```

</details>
