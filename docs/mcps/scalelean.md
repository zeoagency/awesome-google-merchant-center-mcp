# ScaleLean/google-ads-mcp-starter

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://github.com/ScaleLean/google-ads-mcp-starter) · [Descriptors](../../catalog/scalelean.json)

Prepare, validate, approve, apply, and verify controlled feed and product changes; inspect products, issues, and reports.

**14 tools:** 2 mixed, 10 read, 2 write. **Reviewed:** 2026-10-13.

**Extraction:** Runtime FastMCP registries inspected with both default and Merchant-enabled configurations; independently re-extracted.

**Source revision:** [aa162a6e538b](https://github.com/ScaleLean/google-ads-mcp-starter/tree/aa162a6e538b1899973ad20ec59de3246cd29764).

All 14 Merchant Center and relevant setup tools are included; 16 unrelated tools from the 30-tool registry are omitted.

## Implementation notes

- The Merchant module is disabled by default. Enable it using the upstream merchant tool configuration and separate Merchant credentials.
- Writes require policy, an approval signer, and a private ledger. Supported changes are limited to the server’s validated Merchant operations.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`merchant_list_accounts`](#merchant_list_accounts) | Manage accounts, inventory, and conversions | read |
| [`merchant_list_products`](#merchant_list_products) | Manage products, feeds, and promotions | read |
| [`merchant_get_product`](#merchant_get_product) | Manage products, feeds, and promotions | read |
| [`merchant_list_product_inputs`](#merchant_list_product_inputs) | Manage products, feeds, and promotions | read |
| [`merchant_get_product_input`](#merchant_get_product_input) | Manage products, feeds, and promotions | read |
| [`merchant_list_data_sources`](#merchant_list_data_sources) | Manage products, feeds, and promotions | read |
| [`merchant_account_issues`](#merchant_account_issues) | Diagnose products and account issues | read |
| [`merchant_render_product_issues`](#merchant_render_product_issues) | Diagnose products and account issues | read |
| [`merchant_reports_search`](#merchant_reports_search) | Analyze performance and market prices | read |
| [`merchant_prepare_write`](#merchant_prepare_write) | Manage products, feeds, and promotions | mixed |
| [`merchant_validate_prepared_write`](#merchant_validate_prepared_write) | Manage products, feeds, and promotions | mixed |
| [`merchant_issue_write_approval`](#merchant_issue_write_approval) | Manage products, feeds, and promotions | write |
| [`merchant_apply_approved_write`](#merchant_apply_approved_write) | Manage products, feeds, and promotions | write |
| [`merchant_verify_applied_write`](#merchant_verify_applied_write) | Manage products, feeds, and promotions | read |

## merchant_list_accounts

List every current Merchant account under the configured manager.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L37).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

No named parameters. See the exact schema below.

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

</details>

## merchant_list_products

List all processed products from the requested page through completion.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L43).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |
| `page_token` | string / null | No | null | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "type": "string"
    },
    "page_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "account_id"
  ],
  "type": "object"
}
```

</details>

## merchant_get_product

Get one processed product with destination statuses and item issues.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L51).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |
| `product_name` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "type": "string"
    },
    "product_name": {
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "product_name"
  ],
  "type": "object"
}
```

</details>

## merchant_list_product_inputs

Report the Merchant API v1 raw product-input read limitation.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L57).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

**Note:** Reports raw product-input read limitation and gateway-managed ledger state; not a Merchant API raw product-input reader.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "type": "object"
}
```

</details>

## merchant_get_product_input

Report the Merchant API v1 raw product-input read limitation.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L66).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

**Note:** Reports raw product-input read limitation and gateway-managed ledger state; not a Merchant API raw product-input reader.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |
| `product_name` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "type": "string"
    },
    "product_name": {
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "product_name"
  ],
  "type": "object"
}
```

</details>

## merchant_list_data_sources

List primary and supplemental sources with safe fetch status details.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L77).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "type": "object"
}
```

</details>

## merchant_account_issues

List all current Merchant account issues and warnings.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L83).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "type": "object"
}
```

</details>

## merchant_render_product_issues

Render current product issue actions, including review action context.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L89).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |
| `product_name` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "type": "string"
    },
    "product_name": {
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "product_name"
  ],
  "type": "object"
}
```

</details>

## merchant_reports_search

Run a fully paged read-only MCQL report query on approved views.

<details>
<summary>Full upstream description</summary>

```text
Run a fully paged read-only MCQL report query on approved views.

Price competitiveness example (id and report_country_code are required):
SELECT id, offer_id, report_country_code, price, benchmark_price
FROM price_competitiveness_product_view

Price insights example (id is required):
SELECT id, offer_id, price, suggested_price FROM price_insights_product_view

Also accepts product_view and product_performance_view. Use explicit
field names in SELECT. Price objects contain amountMicros and currencyCode;
divide amountMicros by 1,000,000 for the currency amount. A successful empty
price report returns availability=no_matching_data with no inferred cause.
Query, permission, and service failures remain errors, not missing data.
```

</details>

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L95).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |
| `query` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "type": "string"
    },
    "query": {
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "query"
  ],
  "type": "object"
}
```

</details>

## merchant_prepare_write

Prepare one exact Merchant write and record its live before state.

<details>
<summary>Full upstream description</summary>

```text
Prepare one exact Merchant write and record its live before state.

Data-source reference fields must use the complete Merchant resource name:
accounts/{account_id}/dataSources/{id}. API supplemental creation accepts
either an empty configuration or both contentLanguage and feedLabel.

Insert titles with this complete MCP input:
{"request":{"account_id":"1111111111","operation":
"product_inputs_insert_titles","reason":"Title test",
"data_source":"accounts/1111111111/dataSources/123456789",
"inputs":[{"offerId":"SKU-EXAMPLE-1","contentLanguage":"en",
"feedLabel":"-","title":"Test title"}]}}.

Insert attributes with this complete MCP input:
{"request":{"account_id":"1111111111","operation":
"product_inputs_insert_attributes","reason":"Label test",
"data_source":"accounts/1111111111/dataSources/123456789",
"products":[{"offerId":"SKU-EXAMPLE-1","contentLanguage":"en",
"feedLabel":"-","attributes":{"customLabel1":"hero",
"customLabel2":"margin_high"}}]}}.

Allowed attributes are title and customLabel1 through customLabel4.
customLabel0 is protected. Labels must be non-empty and at most 100
characters. Both insert operations merge with the full gateway-recorded
input in this source, preserving existing title and label overrides.

Delete those managed inputs with this complete MCP input:
{"request":{"account_id":"1111111111","operation":
"product_inputs_delete","reason":"Undo title test",
"data_source":"accounts/1111111111/dataSources/123456789",
"inputs":[{"offerId":"SKU-EXAMPLE-1","contentLanguage":"en",
"feedLabel":"-"}]}}.

Delete removes all overrides for that product in this source. The manifest
records full prior inputs for a separately approved partial restoration.

Supply 1 to 25 inputs. Copy offerId, contentLanguage, and feedLabel exactly
from merchant_get_product. The data source must be a gateway-managed
HERMES_ API supplemental source. Then call validate, issue approval, apply,
and verify in that order.
```

</details>

**Effect:** mixed. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L115).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

**Note:**  Preparation or validation may persist private ledger state despite readOnlyHint=True.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request` | object | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "request": {
      "additionalProperties": true,
      "type": "object"
    }
  },
  "required": [
    "request"
  ],
  "type": "object"
}
```

</details>

## merchant_validate_prepared_write

Recheck hierarchy, source, processed product, and managed input state.

**Effect:** mixed. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L172).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

**Note:**  Preparation or validation may persist private ledger state despite readOnlyHint=True.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `manifest_hash` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "manifest_hash": {
      "type": "string"
    }
  },
  "required": [
    "manifest_hash"
  ],
  "type": "object"
}
```

</details>

## merchant_issue_write_approval

Issue a signed approval for one validated Merchant write.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L199).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `manifest_hash` | string | Yes | — | — |
| `authorization_reference` | string | Yes | — | — |
| `expires_in_minutes` | integer | No | 10 | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "manifest_hash": {
      "type": "string"
    },
    "authorization_reference": {
      "type": "string"
    },
    "expires_in_minutes": {
      "default": 10,
      "type": "integer"
    }
  },
  "required": [
    "manifest_hash",
    "authorization_reference"
  ],
  "type": "object"
}
```

</details>

## merchant_apply_approved_write

Apply only the exact signed Merchant manifest from the private ledger.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L229).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `approval_id` | string | Yes | — | — |
| `idempotency_key` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "approval_id": {
      "type": "string"
    },
    "idempotency_key": {
      "type": "string"
    }
  },
  "required": [
    "approval_id",
    "idempotency_key"
  ],
  "type": "object"
}
```

</details>

## merchant_verify_applied_write

Read back the processed product and compare the intended fields.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/ScaleLean/google-ads-mcp-starter/blob/aa162a6e538b1899973ad20ec59de3246cd29764/ads_mcp/tools/merchant.py#L322).

**Availability:** Requires the optional Merchant module; absent from the default configuration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `approval_id` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "approval_id": {
      "type": "string"
    }
  },
  "required": [
    "approval_id"
  ],
  "type": "object"
}
```

</details>
