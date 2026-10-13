# Google Merchant API MCP Access Service

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://merchantapi.googleapis.com/mcp) · [Descriptors](../../catalog/google-data.json)

Inspect product status, account issues, program eligibility, and upload results; query reports or create and refresh data sources.

**13 tools:** 11 read, 2 write. **Reviewed:** 2026-10-13.

**Extraction:** Live HTTP MCP tools/list; independently rediscovered and compared every description and input schema.

**Source version:** serverInfo.name=StatelessServer; serverInfo.version=ESF; protocolVersion=2025-03-26.

All 13 Merchant Center and relevant setup tools are included.

## Implementation notes

- Experimental alpha. Tool discovery is public; executing account operations requires Merchant API credentials.
- Some upstream descriptions mention lookup_products, which this endpoint does not advertise. Use the listed product tools.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`get_product_by_name`](#get_product_by_name) | Manage products, feeds, and promotions | read |
| [`get_automatic_improvements`](#get_automatic_improvements) | Manage accounts, inventory, and conversions | read |
| [`list_account_issues`](#list_account_issues) | Diagnose products and account issues | read |
| [`list_aggregate_product_statuses`](#list_aggregate_product_statuses) | Diagnose products and account issues | read |
| [`list_programs`](#list_programs) | Diagnose products and account issues | read |
| [`list_products`](#list_products) | Manage products, feeds, and promotions | read |
| [`list_data_sources`](#list_data_sources) | Manage products, feeds, and promotions | read |
| [`get_data_source`](#get_data_source) | Manage products, feeds, and promotions | read |
| [`create_data_source`](#create_data_source) | Manage products, feeds, and promotions | write |
| [`fetch_data_source`](#fetch_data_source) | Manage products, feeds, and promotions | write |
| [`get_file_upload`](#get_file_upload) | Diagnose products and account issues | read |
| [`report_search`](#report_search) | Analyze performance and market prices | read |
| [`list_accounts`](#list_accounts) | Manage accounts, inventory, and conversions | read |

## get_product_by_name

Get product info for a given merchant using the exact product resource name (e.g.

<details>
<summary>Full upstream description</summary>

```text
Get product info for a given merchant using the exact product resource name (e.g. accounts/123/products/online~en~US~offer456).

Returns the detailed product status containing reporting context and potential product-level issues.
Use this when you know the specific product's name. If you need to list multiple products, use the 'lookup_products' tool instead.
```

</details>

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://merchantapi.googleapis.com/mcp).

**Note:** Upstream description references lookup_products, which is not an exposed tool in this tools/list response; preserved verbatim.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | — | Required. The name of the product. Format: `accounts/{account}/products/{product}` The `{product}` segment is a unique identifier for the product. This identifier must be unique within a merchant account and generally follows the structure: `content_language~feed_label~offer_id`. Example: `en~US~sku123` For legacy local products, the structure is: `local~content_language~feed_label~offer_id`. Example: `local~en~US~sku123` The format of the `{product}` segment in the URL is automatically detected by the server, supporting two options: 1. **Encoded Format**: The `{product}` segment is an unpadded base64url encoded string (RFC 4648 Section 5). The decoded string must result in the `content_language~feed_label~offer_id` structure. This encoding MUST be used if any part of the product identifier (like `offer_id`) contains characters such as `/`, `%`, or `~`. * Example: To represent the product ID `en~US~sku/123`, the `{product}` segment must be the unpadded base64url encoding of this string, which is `ZW5-VVN-c2t1LzEyMw`. The full resource name for the product would be `accounts/123/products/ZW5-VVN-c2t1LzEyMw`. 2. **Plain Format**: The `{product}` segment is the tilde-separated string `content_language~feed_label~offer_id`. This format is suitable only when `content_language`, `feed_label`, and `offer_id` do not contain URL-problematic characters like `/`, `%`, or `~`. We recommend using the **Encoded Format** for all product IDs to ensure correct parsing, especially those containing special characters. The presence of tilde (`~`) characters in the `{product}` segment is used to differentiate between the two formats. Note: For calls to the v1beta version, the plain format is `channel~content_language~feed_label~offer_id`, for example: `accounts/123/products/online~en~US~sku123`. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the GetProduct method.",
  "properties": {
    "name": {
      "description": "Required. The name of the product. Format: `accounts/{account}/products/{product}` The `{product}` segment is a unique identifier for the product. This identifier must be unique within a merchant account and generally follows the structure: `content_language~feed_label~offer_id`. Example: `en~US~sku123` For legacy local products, the structure is: `local~content_language~feed_label~offer_id`. Example: `local~en~US~sku123` The format of the `{product}` segment in the URL is automatically detected by the server, supporting two options: 1. **Encoded Format**: The `{product}` segment is an unpadded base64url encoded string (RFC 4648 Section 5). The decoded string must result in the `content_language~feed_label~offer_id` structure. This encoding MUST be used if any part of the product identifier (like `offer_id`) contains characters such as `/`, `%`, or `~`. * Example: To represent the product ID `en~US~sku/123`, the `{product}` segment must be the unpadded base64url encoding of this string, which is `ZW5-VVN-c2t1LzEyMw`. The full resource name for the product would be `accounts/123/products/ZW5-VVN-c2t1LzEyMw`. 2. **Plain Format**: The `{product}` segment is the tilde-separated string `content_language~feed_label~offer_id`. This format is suitable only when `content_language`, `feed_label`, and `offer_id` do not contain URL-problematic characters like `/`, `%`, or `~`. We recommend using the **Encoded Format** for all product IDs to ensure correct parsing, especially those containing special characters. The presence of tilde (`~`) characters in the `{product}` segment is used to differentiate between the two formats. Note: For calls to the v1beta version, the plain format is `channel~content_language~feed_label~offer_id`, for example: `accounts/123/products/online~en~US~sku123`.",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "type": "object"
}
```

</details>

## get_automatic_improvements

Get automatic improvements for a given merchant.

<details>
<summary>Full upstream description</summary>

```text
Get automatic improvements for a given merchant.

It contains information about the settings of item updates, image
improvements and shipping improvements. Use this tool specifically when asked about automated updates to prices, conditions, or images.
```

</details>

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | — | Required. The resource name of the automatic improvements. Format: `accounts/{account}/automaticImprovements` |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the `GetAutomaticImprovements` method.",
  "properties": {
    "name": {
      "description": "Required. The resource name of the automatic improvements. Format: `accounts/{account}/automaticImprovements`",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "type": "object"
}
```

</details>

## list_account_issues

List account-level issues for a given merchant.

<details>
<summary>Full upstream description</summary>

```text
List account-level issues for a given merchant.

Account issues are broad problems that affect your entire account, product visibility, and ability to participate in Merchant Center programs (e.g., missing business information, policy violations, account suspension).
Use this tool to find account-wide problems. For issues specific to individual products, use 'list_aggregate_product_statuses' or 'lookup_products'.

For more information on how to resolve account-level issues, see [Issues in Merchant Center](https://support.google.com/merchants/answer/12153802#account).
To request a review after fixing the issues, see [Request a review of your issues](https://support.google.com/merchants/answer/13585221).
```

</details>

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://merchantapi.googleapis.com/mcp).

**Note:** Upstream description references lookup_products, which is not an exposed tool in this tools/list response; preserved verbatim.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `languageCode` | string | No | — | Optional. The issues in the response will have human-readable fields in the given language. The format is [BCP-47](https://tools.ietf.org/html/bcp47), such as `en-US` or `sr-Latn`. If not value is provided, `en-US` will be used. |
| `pageSize` | integer | No | — | Optional. The maximum number of issues to return. The service may return fewer than this value. If unspecified, at most 50 issues will be returned. The maximum value is 100; values above 100 will be coerced to 100 |
| `pageToken` | string | No | — | Optional. A page token, received from a previous `ListAccountIssues` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccountIssues` must match the call that provided the page token. |
| `parent` | string | Yes | — | Required. The parent, which owns this collection of issues. Format: `accounts/{account}` |
| `timeZone` | string | No | — | Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in human-readable fields. For example 'America/Los_Angeles'. If not set, 'America/Los_Angeles' will be used. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the `ListAccountIssues` method.",
  "properties": {
    "languageCode": {
      "description": "Optional. The issues in the response will have human-readable fields in the given language. The format is [BCP-47](https://tools.ietf.org/html/bcp47), such as `en-US` or `sr-Latn`. If not value is provided, `en-US` will be used.",
      "type": "string"
    },
    "pageSize": {
      "description": "Optional. The maximum number of issues to return. The service may return fewer than this value. If unspecified, at most 50 issues will be returned. The maximum value is 100; values above 100 will be coerced to 100",
      "format": "int32",
      "type": "integer"
    },
    "pageToken": {
      "description": "Optional. A page token, received from a previous `ListAccountIssues` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccountIssues` must match the call that provided the page token.",
      "type": "string"
    },
    "parent": {
      "description": "Required. The parent, which owns this collection of issues. Format: `accounts/{account}`",
      "type": "string"
    },
    "timeZone": {
      "description": "Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in human-readable fields. For example 'America/Los_Angeles'. If not set, 'America/Los_Angeles' will be used.",
      "type": "string"
    }
  },
  "required": [
    "parent"
  ],
  "type": "object"
}
```

</details>

## list_aggregate_product_statuses

List aggregated product-level issues for a given merchant.

<details>
<summary>Full upstream description</summary>

```text
List aggregated product-level issues for a given merchant.

This is useful for monitoring the overall health of your product data without needing to
fetch every individual product. This method provides the total count of
products broken down by status (approved, pending, disapproved),
and lists the specific product data issues affecting your inventory.
Use this for a high-level summary of product issues. To find the account-wide issues, use 'list_account_issues'. To find issues for specific individual products, use 'lookup_products'.

For more information on product-level issues and preemptive disapprovals, see [Issues in Merchant Center](https://support.google.com/merchants/answer/12153802#product).
To request a review after fixing the issues, see [Request a review of your issues](https://support.google.com/merchants/answer/13585221).
To ensure your product data complies with requirements, see the [Product data specification](https://support.google.com/merchants/answer/7052112).
```

</details>

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://merchantapi.googleapis.com/mcp).

**Note:** Upstream description references lookup_products, which is not an exposed tool in this tools/list response; preserved verbatim.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `filter` | string | No | — | Optional. A filter expression that filters the aggregate product statuses. Filtering is only supported by the `reporting_context` and `country` field. For example: `reporting_context = "SHOPPING_ADS" AND country = "US"`. |
| `pageSize` | integer | No | — | Optional. The maximum number of aggregate product statuses to return. The service may return fewer than this value. If unspecified, at most 25 aggregate product statuses are returned. The maximum value is 250; values above 250 are coerced to 250. |
| `pageToken` | string | No | — | Optional. A page token, received from a previous `ListAggregateProductStatuses` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAggregateProductStatuses` must match the call that provided the page token. |
| `parent` | string | Yes | — | Required. The account to list aggregate product statuses for. Format: `accounts/{account}` Can only be sub-accounts and standalone accounts. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the `ListAggregateProductStatuses` method.",
  "properties": {
    "filter": {
      "description": "Optional. A filter expression that filters the aggregate product statuses. Filtering is only supported by the `reporting_context` and `country` field. For example: `reporting_context = \"SHOPPING_ADS\" AND country = \"US\"`.",
      "type": "string"
    },
    "pageSize": {
      "description": "Optional. The maximum number of aggregate product statuses to return. The service may return fewer than this value. If unspecified, at most 25 aggregate product statuses are returned. The maximum value is 250; values above 250 are coerced to 250.",
      "format": "int32",
      "type": "integer"
    },
    "pageToken": {
      "description": "Optional. A page token, received from a previous `ListAggregateProductStatuses` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAggregateProductStatuses` must match the call that provided the page token.",
      "type": "string"
    },
    "parent": {
      "description": "Required. The account to list aggregate product statuses for. Format: `accounts/{account}` Can only be sub-accounts and standalone accounts.",
      "type": "string"
    }
  },
  "required": [
    "parent"
  ],
  "type": "object"
}
```

</details>

## list_programs

List programs for a given merchant.

<details>
<summary>Full upstream description</summary>

```text
List programs for a given merchant.

It contains the participation state, active regions and any unmet
requirements for each program (like Free Listings, Shopping Ads, etc.).
Use this to check if a merchant is eligible or active in specific Merchant Center programs.
```

</details>

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `pageSize` | integer | No | — | Optional. The maximum number of programs to return in a single response. If unspecified (or 0), a default size of 1000 is used. The maximum value is 1000; values above 1000 will be coerced to 1000. |
| `pageToken` | string | No | — | Optional. A continuation token, received from a previous `ListPrograms` call. Provide this to retrieve the next page. |
| `parent` | string | Yes | — | Required. The name of the account for which to retrieve all programs. Format: `accounts/{account}` |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the ListPrograms method.",
  "properties": {
    "pageSize": {
      "description": "Optional. The maximum number of programs to return in a single response. If unspecified (or 0), a default size of 1000 is used. The maximum value is 1000; values above 1000 will be coerced to 1000.",
      "format": "int32",
      "type": "integer"
    },
    "pageToken": {
      "description": "Optional. A continuation token, received from a previous `ListPrograms` call. Provide this to retrieve the next page.",
      "type": "string"
    },
    "parent": {
      "description": "Required. The name of the account for which to retrieve all programs. Format: `accounts/{account}`",
      "type": "string"
    }
  },
  "required": [
    "parent"
  ],
  "type": "object"
}
```

</details>

## list_products

List or search for multiple products for a given merchant.

<details>
<summary>Full upstream description</summary>

```text
List or search for multiple products for a given merchant.

Returns the detailed product status containing reporting context and potential product-level issues.
Use this to search for products or list products. If you already have the exact product name, use 'get_product_by_name'.

This tool should not be used for retrieving an aggregated report of
product issues; use 'list_aggregate_product_statuses' for that.
For fetching performance metrics (like clicks or impressions), use 'report_search' instead.
```

</details>

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `pageSize` | integer | No | — | The maximum number of products to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000. If unspecified, the default page size of 25 products will be returned. |
| `pageToken` | string | No | — | A page token, received from a previous `ListProducts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListProducts` must match the call that provided the page token. |
| `parent` | string | Yes | — | Required. The account to list processed products for. Format: `accounts/{account}` |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the ListProducts method.",
  "properties": {
    "pageSize": {
      "description": "The maximum number of products to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000. If unspecified, the default page size of 25 products will be returned.",
      "format": "int32",
      "type": "integer"
    },
    "pageToken": {
      "description": "A page token, received from a previous `ListProducts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListProducts` must match the call that provided the page token.",
      "type": "string"
    },
    "parent": {
      "description": "Required. The account to list processed products for. Format: `accounts/{account}`",
      "type": "string"
    }
  },
  "required": [
    "parent"
  ],
  "type": "object"
}
```

</details>

## list_data_sources

List the data sources (also known as feeds) for a given merchant

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `pageSize` | integer | No | — | Optional. The maximum number of data sources to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000. If unspecified, the maximum number of data sources will be returned. |
| `pageToken` | string | No | — | Optional. A page token, received from a previous `ListDataSources` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataSources` must match the call that provided the page token. |
| `parent` | string | Yes | — | Required. The account to list data sources for. Format: `accounts/{account}` |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the ListDataSources method.",
  "properties": {
    "pageSize": {
      "description": "Optional. The maximum number of data sources to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000. If unspecified, the maximum number of data sources will be returned.",
      "format": "int32",
      "type": "integer"
    },
    "pageToken": {
      "description": "Optional. A page token, received from a previous `ListDataSources` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataSources` must match the call that provided the page token.",
      "type": "string"
    },
    "parent": {
      "description": "Required. The account to list data sources for. Format: `accounts/{account}`",
      "type": "string"
    }
  },
  "required": [
    "parent"
  ],
  "type": "object"
}
```

</details>

## get_data_source

Get a data source (also known as feed) for a given merchant

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | — | Required. The name of the data source to retrieve. Format: `accounts/{account}/dataSources/{datasource}` |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the GetDataSource method.",
  "properties": {
    "name": {
      "description": "Required. The name of the data source to retrieve. Format: `accounts/{account}/dataSources/{datasource}`",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "type": "object"
}
```

</details>

## create_data_source

Create a data source (also known as feed) for a given merchant

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dataSource` | DataSource | Yes | — | Required. The data source to create. |
| `parent` | string | Yes | — | Required. The account where this data source will be created. Format: `accounts/{account}` |

<details>
<summary>Full parameter schema</summary>

```json
{
  "$defs": {
    "DataSource": {
      "description": "The [data source](/merchant/api/guides/data-sources/overview) for the Merchant Center account.",
      "properties": {
        "dataSourceId": {
          "description": "Output only. The data source id.",
          "format": "int64",
          "readOnly": true,
          "type": "string"
        },
        "displayName": {
          "description": "Required. The displayed data source name in the Merchant Center UI.",
          "type": "string"
        },
        "fileInput": {
          "$ref": "#/$defs/FileInput",
          "description": "Optional. The field is used only when data is managed through a file."
        },
        "input": {
          "description": "Output only. Determines the type of input to the data source. Based on the input some settings might not work. Only generic data sources can be created through the API.",
          "enum": [
            "INPUT_UNSPECIFIED",
            "API",
            "FILE",
            "UI",
            "AUTOFEED"
          ],
          "readOnly": true,
          "type": "string",
          "x-google-enum-descriptions": [
            "Input unspecified.",
            "Represents data sources for which the data is primarily provided through the API.",
            "Represents data sources for which the data is primarily provided through file input. Data can still be provided through the API.",
            "The data source for products added directly in Merchant Center. This type of data source can not be created or updated through this API, only by Merchant Center UI. This type of data source is read only.",
            "This is also known as [Automated feeds](https://support.google.com/merchants/answer/12158480) used to automatically build your product data. This type of data source can be enabled or disabled through the Accounts sub-API."
          ]
        },
        "localInventoryDataSource": {
          "$ref": "#/$defs/LocalInventoryDataSource",
          "description": "The [local inventory](https://support.google.com/merchants/answer/7023001) data source."
        },
        "merchantReviewDataSource": {
          "$ref": "#/$defs/MerchantReviewDataSource",
          "description": "The [merchant review](https://support.google.com/merchants/answer/7045996) data source."
        },
        "name": {
          "description": "Required. Identifier. The name of the data source. Format: `accounts/{account}/dataSources/{datasource}`",
          "type": "string",
          "x-google-identifier": true
        },
        "primaryProductDataSource": {
          "$ref": "#/$defs/PrimaryProductDataSource",
          "description": "The [primary data source](https://support.google.com/merchants/answer/7439058) for local and online products."
        },
        "productReviewDataSource": {
          "$ref": "#/$defs/ProductReviewDataSource",
          "description": "The [product review](https://support.google.com/merchants/answer/7045996) data source."
        },
        "promotionDataSource": {
          "$ref": "#/$defs/PromotionDataSource",
          "description": "The [promotion](https://support.google.com/merchants/answer/2906014) data source."
        },
        "regionalInventoryDataSource": {
          "$ref": "#/$defs/RegionalInventoryDataSource",
          "description": "The [regional inventory](https://support.google.com/merchants/answer/7439058) data source."
        },
        "supplementalProductDataSource": {
          "$ref": "#/$defs/SupplementalProductDataSource",
          "description": "The [supplemental data source](https://support.google.com/merchants/answer/7439058) for local and online products."
        }
      },
      "required": [
        "name",
        "displayName"
      ],
      "type": "object"
    },
    "DataSourceReference": {
      "description": "Data source reference can be used to manage related data sources within the data source service.",
      "properties": {
        "primaryDataSourceName": {
          "deprecated": true,
          "description": "Optional. Deprecated: Use `self` instead to reference the primary data source. The name of the primary data source. Format: `accounts/{account}/dataSources/{datasource}`",
          "type": "string"
        },
        "self": {
          "description": "Self should be used to reference the primary data source itself.",
          "type": "boolean"
        },
        "supplementalDataSourceName": {
          "description": "Optional. The name of the supplemental data source. Format: `accounts/{account}/dataSources/{datasource}`",
          "type": "string"
        }
      },
      "type": "object"
    },
    "DefaultRule": {
      "description": "Default rule management of the data source.",
      "properties": {
        "takeFromDataSources": {
          "description": "Required. The list of data sources linked in the [default rule](https://support.google.com/merchants/answer/7450276). This list is ordered by the default rule priority of joining the data. It might include none or multiple references to `self` and supplemental data sources. The list must not be empty. To link the data source to the default rule, you need to add a new reference to this list (in sequential order). To unlink the data source from the default rule, you need to remove the given reference from this list. Changing the order of this list will result in changing the priority of data sources in the default rule. For example, providing the following list: [`1001`, `self`] will take attribute values from supplemental data source `1001`, and fallback to `self` if the attribute is not set in `1001`. Warning: The update (patch) and create call replaces the entire default rule setup. It doesn't work as an addition or append. If `self` is missing from the list of `take_from_data_sources`, the API will ignore attributes from the primary data source itself.",
          "items": {
            "$ref": "#/$defs/DataSourceReference"
          },
          "type": "array"
        }
      },
      "required": [
        "takeFromDataSources"
      ],
      "type": "object"
    },
    "Destination": {
      "description": "Destinations also known as [Marketing methods](https://support.google.com/merchants/answer/15130232) selections.",
      "properties": {
        "destination": {
          "description": "[Marketing methods](https://support.google.com/merchants/answer/15130232) (also known as destination) selections.",
          "enum": [
            "DESTINATION_ENUM_UNSPECIFIED",
            "SHOPPING_ADS",
            "DISPLAY_ADS",
            "LOCAL_INVENTORY_ADS",
            "FREE_LISTINGS",
            "FREE_LOCAL_LISTINGS",
            "YOUTUBE_SHOPPING",
            "YOUTUBE_SHOPPING_CHECKOUT",
            "YOUTUBE_AFFILIATE",
            "FREE_VEHICLE_LISTINGS",
            "VEHICLE_ADS",
            "CLOUD_RETAIL",
            "LOCAL_CLOUD_RETAIL",
            "RENTAL_ADS"
          ],
          "type": "string",
          "x-google-enum-descriptions": [
            "Not specified.",
            "[Shopping ads](https://support.google.com/google-ads/answer/2454022).",
            "[Display ads](https://support.google.com/merchants/answer/6069387).",
            "[Local inventory ads](https://support.google.com/merchants/answer/3057972).",
            "[Free listings](https://support.google.com/merchants/answer/9199328).",
            "[Free local product listings](https://support.google.com/merchants/answer/9825611).",
            "[YouTube Shopping](https://support.google.com/merchants/answer/12362804).",
            "Youtube shopping checkout.",
            "[Youtube Affiliate](https://support.google.com/youtube/answer/13376398).",
            "[Free vehicle listings](https://support.google.com/merchants/answer/11189169).",
            "[Vehicle ads](https://support.google.com/merchants/answer/11189169).",
            "[Cloud retail](https://cloud.google.com/solutions/retail).",
            "[Local cloud retail](https://cloud.google.com/solutions/retail).",
            "Real Estate Rental Ads. ."
          ]
        },
        "state": {
          "description": "The state of the destination.",
          "enum": [
            "STATE_UNSPECIFIED",
            "ENABLED",
            "DISABLED"
          ],
          "type": "string",
          "x-google-enum-descriptions": [
            "Not specified.",
            "Indicates that the destination is enabled.",
            "Indicates that the destination is disabled."
          ]
        }
      },
      "type": "object"
    },
    "FetchSettings": {
      "description": "Fetch details to deliver the data source.",
      "properties": {
        "dayOfMonth": {
          "description": "Optional. The day of the month when the data source file should be fetched (1-31). This field can only be set for monthly frequency.",
          "format": "int32",
          "type": "integer"
        },
        "dayOfWeek": {
          "description": "Optional. The day of the week when the data source file should be fetched. This field can only be set for weekly frequency.",
          "enum": [
            "DAY_OF_WEEK_UNSPECIFIED",
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY"
          ],
          "type": "string",
          "x-google-enum-descriptions": [
            "The day of the week is unspecified.",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ]
        },
        "enabled": {
          "description": "Optional. Enables or pauses the fetch schedule.",
          "type": "boolean"
        },
        "fetchUri": {
          "description": "Optional. The URL where the data source file can be fetched. Google Merchant Center supports automatic scheduled uploads using the HTTP, HTTPS or SFTP protocols, so the value will need to be a valid link using one of those three protocols. Immutable for Google Sheets files.",
          "type": "string"
        },
        "frequency": {
          "description": "Required. The frequency describing fetch schedule.",
          "enum": [
            "FREQUENCY_UNSPECIFIED",
            "FREQUENCY_DAILY",
            "FREQUENCY_WEEKLY",
            "FREQUENCY_MONTHLY"
          ],
          "type": "string",
          "x-google-enum-descriptions": [
            "Frequency unspecified.",
            "The fetch happens every day.",
            "The fetch happens every week.",
            "The fetch happens every month."
          ]
        },
        "password": {
          "description": "Optional. An optional password for fetch_uri. Used for [submitting data sources through SFTP](https://support.google.com/merchants/answer/13813117).",
          "type": "string"
        },
        "timeOfDay": {
          "$ref": "#/$defs/TimeOfDay",
          "description": "Optional. The hour of the day when the data source file should be fetched. Minutes and seconds are not supported and will be ignored."
        },
        "timeZone": {
          "description": "Optional. [Time zone](https://cldr.unicode.org) used for schedule. UTC by default. For example, \"America/Los_Angeles\".",
          "type": "string"
        },
        "username": {
          "description": "Optional. An optional user name for fetch_uri. Used for [submitting data sources through SFTP](https://support.google.com/merchants/answer/13813117).",
          "type": "string"
        }
      },
      "required": [
        "frequency"
      ],
      "type": "object"
    },
    "FileInput": {
      "description": "The data specific for file data sources. This field is empty for other data source inputs.",
      "properties": {
        "fetchSettings": {
          "$ref": "#/$defs/FetchSettings",
          "description": "Optional. Fetch details to deliver the data source. It contains settings for `FETCH` and `GOOGLE_SHEETS` file input types. The required fields vary based on the frequency of fetching."
        },
        "fileInputType": {
          "description": "Output only. The type of file input.",
          "enum": [
            "FILE_INPUT_TYPE_UNSPECIFIED",
            "UPLOAD",
            "FETCH",
            "GOOGLE_SHEETS"
          ],
          "readOnly": true,
          "type": "string",
          "x-google-enum-descriptions": [
            "File input type unspecified.",
            "The file is uploaded through SFTP, Google Cloud Storage or manually in the Merchant Center.",
            "The file is fetched from the configured fetch_uri.",
            "The file is fetched from Google Sheets specified in the fetch_uri. However, you can't set up `GOOGLE_SHEETS` as a data source through the API. To add `GOOGLE_SHEETS` as a data source through the Merchant Center, see [Add products to Merchant Center](https://support.google.com/merchants/answer/12158053)."
          ]
        },
        "fileName": {
          "description": "Optional. The file name of the data source. Required for `UPLOAD` file input type.",
          "type": "string"
        }
      },
      "type": "object"
    },
    "LocalInventoryDataSource": {
      "description": "The local inventory data source type is only available for file inputs and can't be used to create API local inventory data sources.",
      "properties": {
        "contentLanguage": {
          "description": "Required. Immutable. The two-letter ISO 639-1 language of the items to which the local inventory is provided.",
          "type": "string",
          "x-google-immutable": true
        },
        "feedLabel": {
          "description": "Required. Immutable. The feed label of the offers to which the local inventory is provided. Must be less than or equal to 20 uppercase letters (A-Z), numbers (0-9), and dashes (-).",
          "type": "string",
          "x-google-immutable": true
        }
      },
      "required": [
        "feedLabel",
        "contentLanguage"
      ],
      "type": "object"
    },
    "MerchantReviewDataSource": {
      "description": "The merchant review data source.",
      "properties": {},
      "type": "object"
    },
    "PrimaryProductDataSource": {
      "description": "The primary data source for local and online products.",
      "properties": {
        "contentLanguage": {
          "description": "Optional. Immutable. The two-letter ISO 639-1 language of the items in the data source. `feedLabel` and `contentLanguage` must be either both set or unset. The fields can only be unset for data sources without file input. If set, the data source will only accept products matching this combination. If unset, the data source will accept products without that restriction.",
          "type": "string",
          "x-google-immutable": true
        },
        "countries": {
          "description": "Optional. The countries where the items may be displayed. Represented as a [CLDR territory code](https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml).",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "defaultRule": {
          "$ref": "#/$defs/DefaultRule",
          "description": "Optional. Default rule management of the data source. If set, the linked data sources will be replaced. Warning: The update (patch) and create call replaces the entire default rule setup. It doesn't work as an addition or append. If `self` is missing from the list of `take_from_data_sources`, the API will ignore attributes from the primary data source itself."
        },
        "destinations": {
          "description": "Optional. A list of destinations describing where products of the data source can be shown. When retrieving the data source, the list contains all the destinations that can be used for the data source, including the ones that are disabled for the data source but enabled for the account. Only destinations that are enabled on the account, for example through program participation, can be enabled on the data source. If unset, during creation, the destinations will be inherited based on the account level program participation. If set, during creation or update, the data source will be set only for the specified destinations. Updating this field requires at least one destination.",
          "items": {
            "$ref": "#/$defs/Destination"
          },
          "type": "array"
        },
        "feedLabel": {
          "description": "Optional. Immutable. The feed label that is specified on the data source level. Must be less than or equal to 20 uppercase letters (A-Z), numbers (0-9), and dashes (-). For more information about feed label, see [Create a primary data source for products](https://developers.google.com/merchant/api/guides/data-sources/api-sources#create-primary-data-source). `feedLabel` and `contentLanguage` must be either both set or unset for data sources with product content type. They must be set for data sources with a file input. If set, the data source will only accept products matching this combination. If unset, the data source will accept products without that restriction.",
          "type": "string",
          "x-google-immutable": true
        },
        "legacyLocal": {
          "description": "Optional. Immutable. Determines whether the products of this data source are **only** targeting local destinations. Legacy local products are prefixed with `local~` in the product resource ID. For example, `accounts/123/products/local~en~US~sku123`.",
          "type": "boolean",
          "x-google-immutable": true
        }
      },
      "type": "object"
    },
    "ProductReviewDataSource": {
      "description": "The product review data source.",
      "properties": {},
      "type": "object"
    },
    "PromotionDataSource": {
      "description": "The promotion data source.",
      "properties": {
        "contentLanguage": {
          "description": "Required. Immutable. The two-letter ISO 639-1 language of the items in the data source.",
          "type": "string",
          "x-google-immutable": true
        },
        "targetCountry": {
          "description": "Required. Immutable. The target country used as part of the unique identifier. Represented as a [CLDR territory code](https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml). Promotions are only available in selected [countries](https://support.google.com/merchants/answer/4588460).",
          "type": "string",
          "x-google-immutable": true
        }
      },
      "required": [
        "targetCountry",
        "contentLanguage"
      ],
      "type": "object"
    },
    "RegionalInventoryDataSource": {
      "properties": {
        "contentLanguage": {
          "description": "Required. Immutable. The two-letter ISO 639-1 language of the items to which the regional inventory is provided.",
          "type": "string",
          "x-google-immutable": true
        },
        "feedLabel": {
          "description": "Required. Immutable. The feed label of the offers to which the regional inventory is provided. Must be less than or equal to 20 uppercase letters (A-Z), numbers (0-9), and dashes (-).",
          "type": "string",
          "x-google-immutable": true
        }
      },
      "required": [
        "feedLabel",
        "contentLanguage"
      ],
      "type": "object"
    },
    "SupplementalProductDataSource": {
      "description": "The [supplemental data source](https://developers.google.com/merchant/api/guides/data-sources/api-sources#link-supplemental-data-source) for local and online products. After creation,you should make sure to link the supplemental product data source into one or more primary product data sources.",
      "properties": {
        "contentLanguage": {
          "description": "Optional. Immutable. The two-letter ISO 639-1 language of the items in the data source. `feedLabel` and `contentLanguage` must be either both set or unset. The fields can only be unset for data sources without file input. If set, the data source will only accept products matching this combination. If unset, the data source will accept produts without that restriction.",
          "type": "string",
          "x-google-immutable": true
        },
        "feedLabel": {
          "description": "Optional. Immutable. The feed label that is specified on the data source level. Must be less than or equal to 20 uppercase letters (A-Z), numbers (0-9), and dashes (-). `feedLabel` and `contentLanguage` must be either both set or unset for data sources with product content type. They must be set for data sources with a file input. The fields must be unset for data sources without file input. If set, the data source will only accept products matching this combination. If unset, the data source will accept produts without that restriction.",
          "type": "string",
          "x-google-immutable": true
        },
        "referencingPrimaryDataSources": {
          "description": "Output only. The (unordered and deduplicated) list of all primary data sources linked to this data source in either default or custom rules. Supplemental data source cannot be deleted before all links are removed.",
          "items": {
            "$ref": "#/$defs/DataSourceReference"
          },
          "readOnly": true,
          "type": "array"
        }
      },
      "type": "object"
    },
    "TimeOfDay": {
      "description": "Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are google.type.Date and `google.protobuf.Timestamp`.",
      "properties": {
        "hours": {
          "description": "Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.",
          "format": "int32",
          "type": "integer"
        },
        "minutes": {
          "description": "Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.",
          "format": "int32",
          "type": "integer"
        },
        "nanos": {
          "description": "Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.",
          "format": "int32",
          "type": "integer"
        },
        "seconds": {
          "description": "Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.",
          "format": "int32",
          "type": "integer"
        }
      },
      "type": "object"
    }
  },
  "description": "Request message for the CreateDataSource method.",
  "properties": {
    "dataSource": {
      "$ref": "#/$defs/DataSource",
      "description": "Required. The data source to create."
    },
    "parent": {
      "description": "Required. The account where this data source will be created. Format: `accounts/{account}`",
      "type": "string"
    }
  },
  "required": [
    "parent",
    "dataSource"
  ],
  "type": "object"
}
```

</details>

## fetch_data_source

Fetch and process the file that is associated with a data source (also known as feed) for a given merchant

**Effect:** write. **Task:** Manage products, feeds, and promotions. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | — | Required. The name of the data source resource to fetch. Format: `accounts/{account}/dataSources/{datasource}` |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the FetchDataSource method.",
  "properties": {
    "name": {
      "description": "Required. The name of the data source resource to fetch. Format: `accounts/{account}/dataSources/{datasource}`",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "type": "object"
}
```

</details>

## get_file_upload

Gets the status of the latest file upload for a given data source (also known as feed) for a given merchant

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | — | Required. The name of the data source file upload to retrieve. Format: `accounts/{account}/dataSources/{datasource}/fileUploads/latest` |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the GetFileUploadRequest method.",
  "properties": {
    "name": {
      "description": "Required. The name of the data source file upload to retrieve. Format: `accounts/{account}/dataSources/{datasource}/fileUploads/latest`",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "type": "object"
}
```

</details>

## report_search

Look up performance data for a given merchant using an SQL like query.

<details>
<summary>Full upstream description</summary>

```text
Look up performance data for a given merchant using an SQL like query.

For product performance related queries use the product_performance_view table
with the following fields:

date, marketing_method, customer_country_code, offer_id,
title, brand, clicks, impressions, click_through_rate,

For price competitiveness and suggestions use the price_insights_product_view
table with the following fields:

price, suggested_price, effectiveness, id (required in SELECT), offer_id, title, brand,
predicted_impressions_change_fraction, predicted_clicks_change_fraction,
predicted_conversions_change_fraction

Here is how you should structure your queries. Note that SELECT and FROM
clauses are always required.
1.  The SELECT Clause (Required)
This is the first part of your query. You must specify a comma-separated list
of all the fields
you want to retrieve. You should use the field names as is, without any
additional prefixes or
suffixes. Using '*' is not supported, fields must be listed explicitly.

Requirement: You must select at least one metric field for performance
queries, such as impressions or clicks .
Fields: You can select from metrics (like impressions, clicks) and segments
(like date, offer_id, marketing_method) .
Example:

SELECT date, offer_id, clicks, impressions

2.  The FROM Clause (Required)
After SELECT, specify the table to retrieve data from . You can only specify
one table.

Requirement: The FROM clause is required for all queries .
Example:

FROM product_view

3.  The WHERE Clause (Required for performance queries)
Use the WHERE clause to filter the data .

Requirement: This clause is required for performance queries, and you must
specify a date range .
Conditions: You can filter by any segment fields. You can also filter by
metrics, but only if you have included them in the SELECT clause .
Multiple Conditions: To combine conditions, use the AND operator. The OR
operator is not supported .
Date Ranges:
Custom: Use BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD' .
Relative: Use DURING with a predefined range like LAST_30_DAYS or THIS_MONTH.
Example:

WHERE clicks > 100
AND marketing_method = 'ADS'
AND date BETWEEN '2023-08-01' AND '2023-08-31'

Do not use any other filters like "NOT NULL".

4.  The ORDER BY Clause (Optional)
Use this clause to sort your results .

Fields: You can only order by fields specified in the SELECT clause .
Direction: Specify the order with ASC for ascending (the default) or DESC for
descending .
Multiple Fields: You can sort by multiple fields by listing them, separated by
commas .
Example:

ORDER BY clicks DESC, offer_id ASC

5.  The LIMIT Clause (Optional)
Use the LIMIT clause to specify the maximum number of results to return .

Example:

LIMIT 50

For more information on performance metrics, see [Track your product performance in Merchant Center](https://support.google.com/merchants/answer/12159540).
For more information on custom reports and available dimensions/metrics, see [Create custom reports and dashboards in Merchant Center](https://support.google.com/merchants/answer/14152817).
```

</details>

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `pageSize` | integer | No | — | Optional. Number of `ReportRows` to retrieve in a single page. Defaults to 1000. Values above 100,000 are coerced to 100,000. |
| `pageToken` | string | No | — | Optional. Token of the page to retrieve. If not specified, the first page of results is returned. In order to request the next page of results, the value obtained from `next_page_token` in the previous response should be used. |
| `parent` | string | Yes | — | Required. Id of the account making the call. Must be a standalone account or a subaccount of an advanced account. Format: accounts/{account} |
| `query` | string | Yes | — | Required. Query that defines a report to be retrieved. For details on how to construct your query, see the [Query Language guide](https://developers.google.com/merchant/api/guides/reports/query-language). For the full list of available tables and fields, see the Available fields. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the `ReportService.Search` method.",
  "properties": {
    "pageSize": {
      "description": "Optional. Number of `ReportRows` to retrieve in a single page. Defaults to 1000. Values above 100,000 are coerced to 100,000.",
      "format": "int32",
      "type": "integer"
    },
    "pageToken": {
      "description": "Optional. Token of the page to retrieve. If not specified, the first page of results is returned. In order to request the next page of results, the value obtained from `next_page_token` in the previous response should be used.",
      "type": "string"
    },
    "parent": {
      "description": "Required. Id of the account making the call. Must be a standalone account or a subaccount of an advanced account. Format: accounts/{account}",
      "type": "string"
    },
    "query": {
      "description": "Required. Query that defines a report to be retrieved. For details on how to construct your query, see the [Query Language guide](/merchant/api/guides/reports/query-language). For the full list of available tables and fields, see the Available fields.",
      "type": "string"
    }
  },
  "required": [
    "parent",
    "query"
  ],
  "type": "object"
}
```

</details>

## list_accounts

List accounts for a given user.

<details>
<summary>Full upstream description</summary>

```text
List accounts for a given user.

Note: To list sub-accounts for a given advanced account, use this tool with the following filter:
`relationship(providerId={parent} AND service(type="ACCOUNT_AGGREGATION"))`
where `{parent}` is the resource name of the advanced account (e.g., `accounts/123`).
```

</details>

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://merchantapi.googleapis.com/mcp).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `filter` | string | No | — | Optional. Returns only accounts that match the [filter](https://developers.google.com/merchant/api/guides/accounts/filter). For more details, see the [filter syntax reference](https://developers.google.com/merchant/api/guides/accounts/filter-syntax). |
| `pageSize` | integer | No | — | Optional. The maximum number of accounts to return. The service may return fewer than this value. If unspecified, at most 250 accounts are returned. The maximum value is 500; values above 500 are coerced to 500. |
| `pageToken` | string | No | — | Optional. A page token, received from a previous `accounts.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided in the `accounts.list` request must match the call that provided the page token. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "description": "Request message for the `accounts.list` method.",
  "properties": {
    "filter": {
      "description": "Optional. Returns only accounts that match the [filter](https://developers.google.com/merchant/api/guides/accounts/filter). For more details, see the [filter syntax reference](https://developers.google.com/merchant/api/guides/accounts/filter-syntax).",
      "type": "string"
    },
    "pageSize": {
      "description": "Optional. The maximum number of accounts to return. The service may return fewer than this value. If unspecified, at most 250 accounts are returned. The maximum value is 500; values above 500 are coerced to 500.",
      "format": "int32",
      "type": "integer"
    },
    "pageToken": {
      "description": "Optional. A page token, received from a previous `accounts.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided in the `accounts.list` request must match the call that provided the page token.",
      "type": "string"
    }
  },
  "type": "object"
}
```

</details>
