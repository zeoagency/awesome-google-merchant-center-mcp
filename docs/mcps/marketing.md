# MadMaxen92/marketing-mcp

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://github.com/MadMaxen92/marketing-mcp) · [Descriptors](../../catalog/marketing.json)

Query product performance, price recommendations, eligibility, and read-only MCQL reports.

**8 tools:** 8 read. **Reviewed:** 2026-10-13.

**Extraction:** SDK tools/list on in-memory transports with synthetic configuration and network blocked; independently re-extracted.

**Source revision:** [3b672ae7a9d7](https://github.com/MadMaxen92/marketing-mcp/tree/3b672ae7a9d708247e9dbe9073a2769740864f1a).

All 8 Merchant Center and relevant setup tools are included; 53 unrelated tools from the 61-tool registry are omitted.

## Implementation notes

- Startup also requires the server’s Google Ads and ChatGPT OAuth configuration.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`list_google_connections`](#list_google_connections) | Check setup and API usage | read |
| [`list_merchant_center_accounts`](#list_merchant_center_accounts) | Manage accounts, inventory, and conversions | read |
| [`get_merchant_account_overview`](#get_merchant_account_overview) | Diagnose products and account issues | read |
| [`get_merchant_product_status`](#get_merchant_product_status) | Diagnose products and account issues | read |
| [`get_merchant_product_issues`](#get_merchant_product_issues) | Diagnose products and account issues | read |
| [`get_merchant_product_performance`](#get_merchant_product_performance) | Analyze performance and market prices | read |
| [`get_merchant_price_insights`](#get_merchant_price_insights) | Analyze performance and market prices | read |
| [`run_merchant_center_query`](#run_merchant_center_query) | Analyze performance and market prices | read |

## list_google_connections

Lists Google accounts connected to this private Marketing MCP.

<details>
<summary>Full upstream description</summary>

```text
Lists Google accounts connected to this private Marketing MCP. Does not expose tokens.
```

</details>

**Effect:** read. **Task:** Check setup and API usage. [Definition](https://github.com/MadMaxen92/marketing-mcp/blob/3b672ae7a9d708247e9dbe9073a2769740864f1a/src/mcp.ts#L153).

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

## list_merchant_center_accounts

Lists Merchant Center accounts accessible to a connected Google account using Merchant API v1.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/MadMaxen92/marketing-mcp/blob/3b672ae7a9d708247e9dbe9073a2769740864f1a/src/mcp.ts#L351).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `connectionId` | string | No | — | Connection ID or Google email. Defaults to the first connection. |
| `pageSize` | integer | No | 250 | — |
| `pageToken` | string | No | — | — |
| `filter` | string | No | — | Optional Merchant API account filter. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "connectionId": {
      "type": "string",
      "description": "Connection ID or Google email. Defaults to the first connection."
    },
    "pageSize": {
      "type": "integer",
      "minimum": 1,
      "maximum": 500,
      "default": 250
    },
    "pageToken": {
      "type": "string"
    },
    "filter": {
      "type": "string",
      "maxLength": 2000,
      "description": "Optional Merchant API account filter."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## get_merchant_account_overview

Returns Merchant Center account details, account-level issues, and aggregate product-status statistics.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/MadMaxen92/marketing-mcp/blob/3b672ae7a9d708247e9dbe9073a2769740864f1a/src/mcp.ts#L363).

**Note:** Fetches one page of issues and aggregate statuses; there is no dedicated overview continuation tool.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `connectionId` | string | No | — | — |
| `accountId` | string | Yes | — | Numeric Merchant Center account ID. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "connectionId": {
      "type": "string"
    },
    "accountId": {
      "type": "string",
      "pattern": "^(accounts\\/)?\\d+$",
      "description": "Numeric Merchant Center account ID."
    }
  },
  "required": [
    "accountId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## get_merchant_product_status

Returns products with eligibility status, destination status, and item issues; supports optional filters.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/MadMaxen92/marketing-mcp/blob/3b672ae7a9d708247e9dbe9073a2769740864f1a/src/mcp.ts#L373).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `connectionId` | string | No | — | — |
| `accountId` | string | Yes | — | — |
| `offerId` | string | No | — | — |
| `status` | string | No | — |  Allowed: "ELIGIBLE", "ELIGIBLE_LIMITED", "PENDING", "NOT_ELIGIBLE_OR_DISAPPROVED". |
| `reportingContext` | string | No | — | For example SHOPPING_ADS or FREE_LISTINGS. |
| `limit` | integer | No | 100 | — |
| `pageToken` | string | No | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "connectionId": {
      "type": "string"
    },
    "accountId": {
      "type": "string",
      "pattern": "^(accounts\\/)?\\d+$"
    },
    "offerId": {
      "type": "string",
      "maxLength": 250
    },
    "status": {
      "type": "string",
      "enum": [
        "ELIGIBLE",
        "ELIGIBLE_LIMITED",
        "PENDING",
        "NOT_ELIGIBLE_OR_DISAPPROVED"
      ]
    },
    "reportingContext": {
      "type": "string",
      "pattern": "^[A-Z][A-Z0-9_]*$",
      "description": "For example SHOPPING_ADS or FREE_LISTINGS."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "default": 100
    },
    "pageToken": {
      "type": "string"
    }
  },
  "required": [
    "accountId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## get_merchant_product_issues

Lists limited or disapproved Merchant Center products together with their item-level issues.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/MadMaxen92/marketing-mcp/blob/3b672ae7a9d708247e9dbe9073a2769740864f1a/src/mcp.ts#L388).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `connectionId` | string | No | — | — |
| `accountId` | string | Yes | — | — |
| `reportingContext` | string | No | — | — |
| `limit` | integer | No | 100 | — |
| `pageToken` | string | No | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "connectionId": {
      "type": "string"
    },
    "accountId": {
      "type": "string",
      "pattern": "^(accounts\\/)?\\d+$"
    },
    "reportingContext": {
      "type": "string",
      "pattern": "^[A-Z][A-Z0-9_]*$"
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "default": 100
    },
    "pageToken": {
      "type": "string"
    }
  },
  "required": [
    "accountId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## get_merchant_product_performance

Returns Merchant Center product impressions, clicks, conversions, and conversion value for a date range.

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://github.com/MadMaxen92/marketing-mcp/blob/3b672ae7a9d708247e9dbe9073a2769740864f1a/src/mcp.ts#L401).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `connectionId` | string | No | — | — |
| `accountId` | string | Yes | — | — |
| `startDate` | string | Yes | — | — |
| `endDate` | string | Yes | — | — |
| `limit` | integer | No | 100 | — |
| `pageToken` | string | No | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "connectionId": {
      "type": "string"
    },
    "accountId": {
      "type": "string",
      "pattern": "^(accounts\\/)?\\d+$"
    },
    "startDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "endDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "default": 100
    },
    "pageToken": {
      "type": "string"
    }
  },
  "required": [
    "accountId",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## get_merchant_price_insights

Returns available Merchant Center price recommendations and predicted performance changes.

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://github.com/MadMaxen92/marketing-mcp/blob/3b672ae7a9d708247e9dbe9073a2769740864f1a/src/mcp.ts#L415).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `connectionId` | string | No | — | — |
| `accountId` | string | Yes | — | — |
| `limit` | integer | No | 100 | — |
| `pageToken` | string | No | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "connectionId": {
      "type": "string"
    },
    "accountId": {
      "type": "string",
      "pattern": "^(accounts\\/)?\\d+$"
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "default": 100
    },
    "pageToken": {
      "type": "string"
    }
  },
  "required": [
    "accountId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

## run_merchant_center_query

Runs one read-only Merchant Center Query Language (MCQL) SELECT query for advanced reporting.

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://github.com/MadMaxen92/marketing-mcp/blob/3b672ae7a9d708247e9dbe9073a2769740864f1a/src/mcp.ts#L427).

**Note:** Validation rejects mutation keywords and semicolons even inside quoted values; some valid SELECT queries are therefore rejected.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `connectionId` | string | No | — | — |
| `accountId` | string | Yes | — | — |
| `query` | string | Yes | — | — |
| `pageSize` | integer | No | 1000 | — |
| `pageToken` | string | No | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "connectionId": {
      "type": "string"
    },
    "accountId": {
      "type": "string",
      "pattern": "^(accounts\\/)?\\d+$"
    },
    "query": {
      "type": "string",
      "minLength": 6,
      "maxLength": 12000
    },
    "pageSize": {
      "type": "integer",
      "minimum": 1,
      "maximum": 5000,
      "default": 1000
    },
    "pageToken": {
      "type": "string"
    }
  },
  "required": [
    "accountId",
    "query"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>
