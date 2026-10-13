# yasserstudio/gmc · embedded MCP

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://github.com/yasserstudio/gmc) · [Descriptors](../../catalog/gmc.json)

Insert or delete product inputs, query reports, inspect issues, and validate local feed files before upload.

**12 tools:** 10 read, 2 write. **Reviewed:** 2026-10-13.

**Extraction:** SDK tools/list on in-memory transports, preserving registration code and replacing only application imports/configuration; independently re-extracted.

**Source revision:** [1f12b85cc8e2](https://github.com/yasserstudio/gmc/tree/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1).

All 12 Merchant Center and relevant setup tools are included.

## Implementation notes

- Start the embedded server with gmc mcp. Account defaults can come from CLI profiles; explicit account parameters remain available.
- products_insert and products_delete perform immediate mutations; these tools have no preview or confirmation parameter.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`doctor`](#doctor) | Check setup and API usage | read |
| [`accounts_list`](#accounts_list) | Manage accounts, inventory, and conversions | read |
| [`accounts_get`](#accounts_get) | Manage accounts, inventory, and conversions | read |
| [`products_list`](#products_list) | Manage products, feeds, and promotions | read |
| [`products_get`](#products_get) | Manage products, feeds, and promotions | read |
| [`products_insert`](#products_insert) | Manage products, feeds, and promotions | write |
| [`products_delete`](#products_delete) | Manage products, feeds, and promotions | write |
| [`datasources_list`](#datasources_list) | Manage products, feeds, and promotions | read |
| [`issues_account`](#issues_account) | Diagnose products and account issues | read |
| [`quota_list`](#quota_list) | Check setup and API usage | read |
| [`reports_query`](#reports_query) | Analyze performance and market prices | read |
| [`preflight`](#preflight) | Diagnose products and account issues | read |

## doctor

Diagnose auth, GCP-project registration, and Merchant API access.

<details>
<summary>Full upstream description</summary>

```text
Diagnose auth, GCP-project registration, and Merchant API access. Run this first to verify your setup works.
```

</details>

**Effect:** read. **Task:** Check setup and API usage. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

**Note:** Resolves auth, mints token, and probes Merchant API; diagnoses configuration but does not register project or configure account.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    }
  },
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## accounts_list

List Merchant Center accounts accessible by the current credential.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

No named parameters. See the exact schema below.

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {},
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## accounts_get

Get details for a specific Merchant Center account.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | Yes | — | Merchant Center account id |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "type": "string",
      "description": "Merchant Center account id"
    }
  },
  "required": [
    "account"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## products_list

List products in a Merchant Center account.

<details>
<summary>Full upstream description</summary>

```text
List products in a Merchant Center account. Returns processed products with status and item-level issues.
```

</details>

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

**Note:** page_size defaults to 50 in handler (not a JSON Schema default); service follows all pages, so it is not a total result limit.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |
| `page_size` | integer | No | — | Max products per page (default 50, max 250) |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    },
    "page_size": {
      "description": "Max products per page (default 50, max 250)",
      "type": "integer",
      "minimum": 1,
      "maximum": 250
    }
  },
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## products_get

Get a single product by its product key (e.g.

<details>
<summary>Full upstream description</summary>

```text
Get a single product by its product key (e.g. 'en~US~SKU1').
```

</details>

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |
| `product_id` | string | Yes | — | Product key, e.g. 'en~US~SKU1' |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    },
    "product_id": {
      "type": "string",
      "description": "Product key, e.g. 'en~US~SKU1'"
    }
  },
  "required": [
    "product_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## products_insert

Insert or update a product in a Merchant Center account.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

**Note:** Direct POST productInputs:insert creates/replaces a product input; no preview or commit gate. product is an unrestricted JSON object, not a nested ProductInput schema.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |
| `data_source` | string | Yes | — | Data source id to insert into |
| `product` | object | Yes | — | ProductInput JSON object |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    },
    "data_source": {
      "type": "string",
      "description": "Data source id to insert into"
    },
    "product": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "ProductInput JSON object"
    }
  },
  "required": [
    "data_source",
    "product"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## products_delete

Delete a product from a Merchant Center account.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

**Note:** Direct DELETE productInputs; no preview or commit gate.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |
| `product_id` | string | Yes | — | Product key, e.g. 'en~US~SKU1' |
| `data_source` | string | Yes | — | Data source id the product belongs to |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    },
    "product_id": {
      "type": "string",
      "description": "Product key, e.g. 'en~US~SKU1'"
    },
    "data_source": {
      "type": "string",
      "description": "Data source id the product belongs to"
    }
  },
  "required": [
    "product_id",
    "data_source"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## datasources_list

List data sources (feeds) for a Merchant Center account.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    }
  },
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## issues_account

Get account-level issues (disapprovals, warnings) for a Merchant Center account.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    }
  },
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## quota_list

List daily Merchant API call quota and current usage.

**Effect:** read. **Task:** Check setup and API usage. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    }
  },
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## reports_query

Run an MCQL query against the Merchant Center reports API.

<details>
<summary>Full upstream description</summary>

```text
Run an MCQL query against the Merchant Center reports API. Use product_performance_view for clicks/impressions.
```

</details>

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

**Note:** Generic MCQL read query passed to reports:search POST; follows pagination.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account` | string | No | — | Merchant Center account id |
| `query` | string | Yes | — | MCQL query string, e.g. 'SELECT offer_id, clicks FROM product_performance_view WHERE date BETWEEN "2026-01-01" AND "2026-01-31"' |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account": {
      "description": "Merchant Center account id",
      "type": "string"
    },
    "query": {
      "type": "string",
      "description": "MCQL query string, e.g. 'SELECT offer_id, clicks FROM product_performance_view WHERE date BETWEEN \"2026-01-01\" AND \"2026-01-31\"'"
    }
  },
  "required": [
    "query"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## preflight

Validate product feed files offline against Merchant Center rules — catches disapprovals before upload.

<details>
<summary>Full upstream description</summary>

```text
Validate product feed files offline against Merchant Center rules — catches disapprovals before upload. No API call, no auth needed.
```

</details>

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/yasserstudio/gmc/blob/1f12b85cc8e2e67ab03589c5bc6bf21aea493df1/packages/mcp/src/server.ts).

**Note:** Offline local JSON file read/validation. dir defaults to feeds in handler; strict inherits preflight config unless supplied. No schema defaults.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dir` | string | No | — | Directory of product JSON files to scan (default: 'feeds') |
| `strict` | boolean | No | — | Treat warnings as failures |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "dir": {
      "description": "Directory of product JSON files to scan (default: 'feeds')",
      "type": "string"
    },
    "strict": {
      "description": "Treat warnings as failures",
      "type": "boolean"
    }
  },
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>
