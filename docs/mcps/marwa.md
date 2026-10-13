# marwa-mrwan/google-clarity-mcp-codex

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://github.com/marwa-mrwan/google-clarity-mcp-codex) · [Descriptors](../../catalog/marwa.json)

Manage subaccounts, local and regional inventory, and conversion sources alongside product, feed, and promotion operations.

**40 tools:** 1 mixed, 19 read, 1 setup, 19 write. **Reviewed:** 2026-10-13.

**Extraction:** Evaluated upstream descriptor factories and checked their registration wiring; independently re-extracted. Server startup was not exercised.

**Source revision:** [2a6881b03cc8](https://github.com/marwa-mrwan/google-clarity-mcp-codex/tree/2a6881b03cc8825ff634f8512100c8b566b6758f).

All 40 Merchant Center and relevant setup tools are included; 165 unrelated tools from the 205-tool registry are omitted.

## Implementation notes

- Only the Google MCP server’s Merchant tools are included; the separate Clarity server is outside this catalog.
- Writes default to previews. Execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true.
- Generic merchant_api_call includes alpha/beta service choices whose endpoint availability was not exercised; named core operations target Merchant API v1.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`merchant_list_accounts`](#merchant_list_accounts) | Manage accounts, inventory, and conversions | read |
| [`merchant_get_account`](#merchant_get_account) | Manage accounts, inventory, and conversions | read |
| [`merchant_get_developer_registration`](#merchant_get_developer_registration) | Check setup and API usage | read |
| [`merchant_register_gcp`](#merchant_register_gcp) | Check setup and API usage | setup |
| [`merchant_list_subaccounts`](#merchant_list_subaccounts) | Manage accounts, inventory, and conversions | read |
| [`merchant_create_and_configure_account`](#merchant_create_and_configure_account) | Manage accounts, inventory, and conversions | write |
| [`merchant_update_account`](#merchant_update_account) | Manage accounts, inventory, and conversions | write |
| [`merchant_delete_account`](#merchant_delete_account) | Manage accounts, inventory, and conversions | write |
| [`merchant_list_products`](#merchant_list_products) | Manage products, feeds, and promotions | read |
| [`merchant_get_product`](#merchant_get_product) | Manage products, feeds, and promotions | read |
| [`merchant_insert_product_input`](#merchant_insert_product_input) | Manage products, feeds, and promotions | write |
| [`merchant_update_product_input`](#merchant_update_product_input) | Manage products, feeds, and promotions | write |
| [`merchant_delete_product_input`](#merchant_delete_product_input) | Manage products, feeds, and promotions | write |
| [`merchant_list_data_sources`](#merchant_list_data_sources) | Manage products, feeds, and promotions | read |
| [`merchant_get_data_source`](#merchant_get_data_source) | Manage products, feeds, and promotions | read |
| [`merchant_create_data_source`](#merchant_create_data_source) | Manage products, feeds, and promotions | write |
| [`merchant_update_data_source`](#merchant_update_data_source) | Manage products, feeds, and promotions | write |
| [`merchant_delete_data_source`](#merchant_delete_data_source) | Manage products, feeds, and promotions | write |
| [`merchant_fetch_data_source`](#merchant_fetch_data_source) | Manage products, feeds, and promotions | write |
| [`merchant_list_promotions`](#merchant_list_promotions) | Manage products, feeds, and promotions | read |
| [`merchant_get_promotion`](#merchant_get_promotion) | Manage products, feeds, and promotions | read |
| [`merchant_insert_promotion`](#merchant_insert_promotion) | Manage products, feeds, and promotions | write |
| [`merchant_list_local_inventories`](#merchant_list_local_inventories) | Manage accounts, inventory, and conversions | read |
| [`merchant_insert_local_inventory`](#merchant_insert_local_inventory) | Manage accounts, inventory, and conversions | write |
| [`merchant_delete_local_inventory`](#merchant_delete_local_inventory) | Manage accounts, inventory, and conversions | write |
| [`merchant_list_regional_inventories`](#merchant_list_regional_inventories) | Manage accounts, inventory, and conversions | read |
| [`merchant_insert_regional_inventory`](#merchant_insert_regional_inventory) | Manage accounts, inventory, and conversions | write |
| [`merchant_delete_regional_inventory`](#merchant_delete_regional_inventory) | Manage accounts, inventory, and conversions | write |
| [`merchant_list_conversion_sources`](#merchant_list_conversion_sources) | Manage accounts, inventory, and conversions | read |
| [`merchant_get_conversion_source`](#merchant_get_conversion_source) | Manage accounts, inventory, and conversions | read |
| [`merchant_create_conversion_source`](#merchant_create_conversion_source) | Manage accounts, inventory, and conversions | write |
| [`merchant_update_conversion_source`](#merchant_update_conversion_source) | Manage accounts, inventory, and conversions | write |
| [`merchant_archive_conversion_source`](#merchant_archive_conversion_source) | Manage accounts, inventory, and conversions | write |
| [`merchant_undelete_conversion_source`](#merchant_undelete_conversion_source) | Manage accounts, inventory, and conversions | write |
| [`merchant_search_report`](#merchant_search_report) | Analyze performance and market prices | read |
| [`merchant_list_issues`](#merchant_list_issues) | Diagnose products and account issues | read |
| [`merchant_render_account_issues`](#merchant_render_account_issues) | Diagnose products and account issues | read |
| [`merchant_render_product_issues`](#merchant_render_product_issues) | Diagnose products and account issues | read |
| [`merchant_list_quotas`](#merchant_list_quotas) | Check setup and API usage | read |
| [`merchant_api_call`](#merchant_api_call) | Call other Merchant API endpoints | mixed |

## merchant_list_accounts

List Merchant Center accounts accessible to the OAuth user.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": []
}
```

</details>

## merchant_get_account

Get one Merchant Center account.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    }
  },
  "required": [
    "account_name"
  ]
}
```

</details>

## merchant_get_developer_registration

Get the Google Cloud project registration for a Merchant Center account.

**Effect:** read. **Task:** Check setup and API usage. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | No | — | accounts/{accountId} |
| `account_id` | string | No | — | Legacy shorthand Merchant Center account ID. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "account_id": {
      "type": "string",
      "description": "Legacy shorthand Merchant Center account ID."
    }
  },
  "required": []
}
```

</details>

## merchant_register_gcp

Register the current Google Cloud project and developer contact with a Merchant Center account.

**Effect:** setup. **Task:** Check setup and API usage. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | No | — | accounts/{accountId} |
| `account_id` | string | No | — | Legacy shorthand Merchant Center account ID. |
| `developer_email` | string | Yes | — | Developer contact that will receive the API_DEVELOPER role or invitation. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "account_id": {
      "type": "string",
      "description": "Legacy shorthand Merchant Center account ID."
    },
    "developer_email": {
      "type": "string",
      "format": "email",
      "description": "Developer contact that will receive the API_DEVELOPER role or invitation."
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "developer_email"
  ]
}
```

</details>

## merchant_list_subaccounts

List subaccounts under an advanced account.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | No | — | accounts/{accountId} |
| `account_id` | string | No | — | Legacy shorthand Merchant Center account ID. |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "account_id": {
      "type": "string",
      "description": "Legacy shorthand Merchant Center account ID."
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": []
}
```

</details>

## merchant_create_and_configure_account

Create and configure a Merchant Center account.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request` | object | Yes | — | CreateAndConfigureAccount request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "request": {
      "type": "object",
      "description": "CreateAndConfigureAccount request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "request"
  ]
}
```

</details>

## merchant_update_account

Update a Merchant Center account.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `update_mask` | string | Yes | — | — |
| `account` | object | Yes | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "update_mask": {
      "type": "string"
    },
    "account": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "account_name",
    "update_mask",
    "account"
  ]
}
```

</details>

## merchant_delete_account

Delete a Merchant Center account.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `force` | boolean | No | false | — |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "force": {
      "type": "boolean",
      "default": false
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "account_name"
  ]
}
```

</details>

## merchant_list_products

List processed products.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | No | — | accounts/{accountId} |
| `account_id` | string | No | — | Legacy shorthand Merchant Center account ID. |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "account_id": {
      "type": "string",
      "description": "Legacy shorthand Merchant Center account ID."
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": []
}
```

</details>

## merchant_get_product

Get one processed product.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product_name` | string | Yes | — | accounts/{accountId}/products/{product} |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string",
      "description": "accounts/{accountId}/products/{product}"
    }
  },
  "required": [
    "product_name"
  ]
}
```

</details>

## merchant_insert_product_input

Insert a product input into a data source.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `data_source` | string | Yes | — | accounts/{accountId}/dataSources/{dataSourceId} |
| `product_input` | object | Yes | — | ProductInput body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "data_source": {
      "type": "string",
      "description": "accounts/{accountId}/dataSources/{dataSourceId}"
    },
    "product_input": {
      "type": "object",
      "description": "ProductInput body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "account_name",
    "data_source",
    "product_input"
  ]
}
```

</details>

## merchant_update_product_input

Patch a product input.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product_input_name` | string | Yes | — | accounts/{accountId}/productInputs/{productInput} |
| `data_source` | string | Yes | — | accounts/{accountId}/dataSources/{dataSourceId} |
| `update_mask` | string | Yes | — | — |
| `product_input` | object | Yes | — | ProductInput body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_input_name": {
      "type": "string",
      "description": "accounts/{accountId}/productInputs/{productInput}"
    },
    "data_source": {
      "type": "string",
      "description": "accounts/{accountId}/dataSources/{dataSourceId}"
    },
    "update_mask": {
      "type": "string"
    },
    "product_input": {
      "type": "object",
      "description": "ProductInput body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "product_input_name",
    "data_source",
    "update_mask",
    "product_input"
  ]
}
```

</details>

## merchant_delete_product_input

Delete a product input.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product_input_name` | string | Yes | — | accounts/{accountId}/productInputs/{productInput} |
| `data_source` | string | Yes | — | accounts/{accountId}/dataSources/{dataSourceId} |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_input_name": {
      "type": "string",
      "description": "accounts/{accountId}/productInputs/{productInput}"
    },
    "data_source": {
      "type": "string",
      "description": "accounts/{accountId}/dataSources/{dataSourceId}"
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "product_input_name",
    "data_source"
  ]
}
```

</details>

## merchant_list_data_sources

List data source configurations.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": [
    "account_name"
  ]
}
```

</details>

## merchant_get_data_source

Get one data source configuration.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data_source_name` | string | Yes | — | accounts/{accountId}/dataSources/{dataSourceId} |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "data_source_name": {
      "type": "string",
      "description": "accounts/{accountId}/dataSources/{dataSourceId}"
    }
  },
  "required": [
    "data_source_name"
  ]
}
```

</details>

## merchant_create_data_source

Create a data source configuration.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `data_source` | object | Yes | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "data_source": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "account_name",
    "data_source"
  ]
}
```

</details>

## merchant_update_data_source

Update a data source configuration.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data_source_name` | string | Yes | — | accounts/{accountId}/dataSources/{dataSourceId} |
| `update_mask` | string | Yes | — | — |
| `data_source` | object | Yes | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "data_source_name": {
      "type": "string",
      "description": "accounts/{accountId}/dataSources/{dataSourceId}"
    },
    "update_mask": {
      "type": "string"
    },
    "data_source": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "data_source_name",
    "update_mask",
    "data_source"
  ]
}
```

</details>

## merchant_delete_data_source

Delete a data source configuration.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data_source_name` | string | Yes | — | accounts/{accountId}/dataSources/{dataSourceId} |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "data_source_name": {
      "type": "string",
      "description": "accounts/{accountId}/dataSources/{dataSourceId}"
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "data_source_name"
  ]
}
```

</details>

## merchant_fetch_data_source

Trigger an immediate fetch for a file data source.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data_source_name` | string | Yes | — | accounts/{accountId}/dataSources/{dataSourceId} |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "data_source_name": {
      "type": "string",
      "description": "accounts/{accountId}/dataSources/{dataSourceId}"
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "data_source_name"
  ]
}
```

</details>

## merchant_list_promotions

List Merchant Center promotions.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": [
    "account_name"
  ]
}
```

</details>

## merchant_get_promotion

Get one promotion.

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `promotion_name` | string | Yes | — | accounts/{accountId}/promotions/{promotion} |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "promotion_name": {
      "type": "string",
      "description": "accounts/{accountId}/promotions/{promotion}"
    }
  },
  "required": [
    "promotion_name"
  ]
}
```

</details>

## merchant_insert_promotion

Insert a promotion.

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `data_source` | string | Yes | — | accounts/{accountId}/dataSources/{dataSourceId} |
| `promotion` | object | Yes | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "data_source": {
      "type": "string",
      "description": "accounts/{accountId}/dataSources/{dataSourceId}"
    },
    "promotion": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "account_name",
    "data_source",
    "promotion"
  ]
}
```

</details>

## merchant_list_local_inventories

List local inventory for a product.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product_name` | string | Yes | — | accounts/{accountId}/products/{product} |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string",
      "description": "accounts/{accountId}/products/{product}"
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": [
    "product_name"
  ]
}
```

</details>

## merchant_insert_local_inventory

Insert local inventory for a product.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product_name` | string | Yes | — | accounts/{accountId}/products/{product} |
| `local_inventory` | object | Yes | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string",
      "description": "accounts/{accountId}/products/{product}"
    },
    "local_inventory": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "product_name",
    "local_inventory"
  ]
}
```

</details>

## merchant_delete_local_inventory

Delete local inventory.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `inventory_name` | string | Yes | — | accounts/{accountId}/products/{product}/localInventories/{storeCode} |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "inventory_name": {
      "type": "string",
      "description": "accounts/{accountId}/products/{product}/localInventories/{storeCode}"
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "inventory_name"
  ]
}
```

</details>

## merchant_list_regional_inventories

List regional inventory for a product.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product_name` | string | Yes | — | accounts/{accountId}/products/{product} |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string",
      "description": "accounts/{accountId}/products/{product}"
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": [
    "product_name"
  ]
}
```

</details>

## merchant_insert_regional_inventory

Insert regional inventory for a product.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product_name` | string | Yes | — | accounts/{accountId}/products/{product} |
| `regional_inventory` | object | Yes | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string",
      "description": "accounts/{accountId}/products/{product}"
    },
    "regional_inventory": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "product_name",
    "regional_inventory"
  ]
}
```

</details>

## merchant_delete_regional_inventory

Delete regional inventory.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `inventory_name` | string | Yes | — | accounts/{accountId}/products/{product}/regionalInventories/{region} |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "inventory_name": {
      "type": "string",
      "description": "accounts/{accountId}/products/{product}/regionalInventories/{region}"
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "inventory_name"
  ]
}
```

</details>

## merchant_list_conversion_sources

List conversion sources.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": [
    "account_name"
  ]
}
```

</details>

## merchant_get_conversion_source

Get one conversion source.

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `conversion_source_name` | string | Yes | — | accounts/{accountId}/conversionSources/{sourceId} |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "conversion_source_name": {
      "type": "string",
      "description": "accounts/{accountId}/conversionSources/{sourceId}"
    }
  },
  "required": [
    "conversion_source_name"
  ]
}
```

</details>

## merchant_create_conversion_source

Create a conversion source.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `conversion_source` | object | Yes | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "conversion_source": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "account_name",
    "conversion_source"
  ]
}
```

</details>

## merchant_update_conversion_source

Update a conversion source.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `conversion_source_name` | string | Yes | — | accounts/{accountId}/conversionSources/{sourceId} |
| `update_mask` | string | Yes | — | — |
| `conversion_source` | object | Yes | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "conversion_source_name": {
      "type": "string",
      "description": "accounts/{accountId}/conversionSources/{sourceId}"
    },
    "update_mask": {
      "type": "string"
    },
    "conversion_source": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "conversion_source_name",
    "update_mask",
    "conversion_source"
  ]
}
```

</details>

## merchant_archive_conversion_source

Archive a conversion source.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `conversion_source_name` | string | Yes | — | accounts/{accountId}/conversionSources/{sourceId} |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "conversion_source_name": {
      "type": "string",
      "description": "accounts/{accountId}/conversionSources/{sourceId}"
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "conversion_source_name"
  ]
}
```

</details>

## merchant_undelete_conversion_source

Re-enable an archived conversion source.

**Effect:** write. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `conversion_source_name` | string | Yes | — | accounts/{accountId}/conversionSources/{sourceId} |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "conversion_source_name": {
      "type": "string",
      "description": "accounts/{accountId}/conversionSources/{sourceId}"
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "conversion_source_name"
  ]
}
```

</details>

## merchant_search_report

Run a Merchant Center Query Language report.

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | No | — | accounts/{accountId} |
| `account_id` | string | No | — | Legacy shorthand Merchant Center account ID. |
| `query` | string | Yes | — | Merchant Center Query Language query. |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "account_id": {
      "type": "string",
      "description": "Legacy shorthand Merchant Center account ID."
    },
    "query": {
      "type": "string",
      "description": "Merchant Center Query Language query."
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": [
    "query"
  ]
}
```

</details>

## merchant_list_issues

List account issues with resolution guidance.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | No | — | accounts/{accountId} |
| `account_id` | string | No | — | Legacy shorthand Merchant Center account ID. |
| `language_code` | string | No | — | Optional BCP-47 language code. |
| `time_zone` | string | No | — | Optional IANA time zone. |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "account_id": {
      "type": "string",
      "description": "Legacy shorthand Merchant Center account ID."
    },
    "language_code": {
      "type": "string",
      "description": "Optional BCP-47 language code."
    },
    "time_zone": {
      "type": "string",
      "description": "Optional IANA time zone."
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": []
}
```

</details>

## merchant_render_account_issues

Render account issues with resolution actions.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `request` | object | No | — | RenderAccountIssues request body. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "request": {
      "type": "object",
      "description": "RenderAccountIssues request body.",
      "additionalProperties": true
    }
  },
  "required": [
    "account_name"
  ]
}
```

</details>

## merchant_render_product_issues

Render product issues with resolution actions.

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `product_name` | string | Yes | — | accounts/{accountId}/products/{product} |
| `request` | object | No | — | RenderProductIssues request body. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string",
      "description": "accounts/{accountId}/products/{product}"
    },
    "request": {
      "type": "object",
      "description": "RenderProductIssues request body.",
      "additionalProperties": true
    }
  },
  "required": [
    "product_name"
  ]
}
```

</details>

## merchant_list_quotas

List Merchant API quota usage for an account.

**Effect:** read. **Task:** Check setup and API usage. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_name` | string | Yes | — | accounts/{accountId} |
| `page_size` | number | No | 100 | Page size. |
| `page_token` | string | No | — | Optional next-page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_name": {
      "type": "string",
      "description": "accounts/{accountId}"
    },
    "page_size": {
      "type": "number",
      "description": "Page size.",
      "default": 100
    },
    "page_token": {
      "type": "string",
      "description": "Optional next-page token."
    }
  },
  "required": [
    "account_name"
  ]
}
```

</details>

## merchant_api_call

Call any documented Merchant API endpoint using a fixed Google service allowlist.

**Effect:** mixed. **Task:** Call other Merchant API endpoints. [Definition](https://github.com/marwa-mrwan/google-clarity-mcp-codex/blob/2a6881b03cc8825ff634f8512100c8b566b6758f/google-mcp/lib/merchant-center.js).

**Note:** Mutation execution requires dry_run=false, confirm=true, and MERCHANT_ENABLE_MUTATIONS=true; otherwise returns a request preview. GET through merchant_api_call executes without mutation gates.
**Note:** Generic dispatcher supports GET/POST/PUT/PATCH/DELETE over fixed service allowlist. Non-GET methods are treated as mutations, including arbitrary POST. Optional beta/alpha service entries do not affect core v1 service registration.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `service` | string | Yes | — |  Allowed: "accounts", "products", "reports", "data_sources", "inventories", "promotions", "conversions", "quota", "issue_resolution", "notifications", "lfp", "order_tracking", "reviews_v1beta", "reviews_v1alpha", "product_studio_v1alpha", "loyalty_customers_v1alpha", "youtube_shopping_checkout_v1beta", "youtube_shopping_checkout_v1alpha", "youtube_v1alpha". |
| `method` | string | Yes | "GET" |  Allowed: "GET", "POST", "PUT", "PATCH", "DELETE". |
| `path` | string | Yes | — | Relative API path only; full URLs are rejected. |
| `query` | object | No | — | Optional query parameters. |
| `body` | object | No | — | Official Merchant API request body. |
| `dry_run` | boolean | No | true | Preview the Merchant API request without changing data. Defaults to true. |
| `confirm` | boolean | No | false | Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "type": "object",
  "properties": {
    "service": {
      "type": "string",
      "enum": [
        "accounts",
        "products",
        "reports",
        "data_sources",
        "inventories",
        "promotions",
        "conversions",
        "quota",
        "issue_resolution",
        "notifications",
        "lfp",
        "order_tracking",
        "reviews_v1beta",
        "reviews_v1alpha",
        "product_studio_v1alpha",
        "loyalty_customers_v1alpha",
        "youtube_shopping_checkout_v1beta",
        "youtube_shopping_checkout_v1alpha",
        "youtube_v1alpha"
      ]
    },
    "method": {
      "type": "string",
      "enum": [
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE"
      ],
      "default": "GET"
    },
    "path": {
      "type": "string",
      "description": "Relative API path only; full URLs are rejected."
    },
    "query": {
      "type": "object",
      "description": "Optional query parameters.",
      "additionalProperties": true
    },
    "body": {
      "type": "object",
      "description": "Official Merchant API request body.",
      "additionalProperties": true
    },
    "dry_run": {
      "type": "boolean",
      "description": "Preview the Merchant API request without changing data. Defaults to true.",
      "default": true
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true with dry_run=false and MERCHANT_ENABLE_MUTATIONS=true before a write executes.",
      "default": false
    }
  },
  "required": [
    "service",
    "method",
    "path"
  ]
}
```

</details>
