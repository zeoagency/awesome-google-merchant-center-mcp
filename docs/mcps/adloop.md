# kLOsk/adloop

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://github.com/kLOsk/adloop) · [Descriptors](../../catalog/adloop.json)

Discover accounts and inspect aggregate product and account issues; feed health may trigger developer registration.

**2 tools:** 1 mixed, 1 read. **Reviewed:** 2026-10-13.

**Extraction:** Runtime FastMCP provider registry inspection; independently re-extracted, with no handlers called.

**Source revision:** [e51d7d649841](https://github.com/kLOsk/adloop/tree/e51d7d6498410755b1e437cc115ef822cbd72e84).

All 2 Merchant Center and relevant setup tools are included; 120 unrelated tools from the 122-tool registry are omitted.

## Implementation notes

- Only Merchant Center tools are included. The shared health_check probes other services and is omitted.
- ADLOOP_TOOLSETS can filter the advertised tools; these definitions use the full default registry.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`list_merchant_accounts`](#list_merchant_accounts) | Manage accounts, inventory, and conversions | read |
| [`get_merchant_feed_health`](#get_merchant_feed_health) | Diagnose products and account issues | mixed |

## list_merchant_accounts

List Google Merchant Center accounts the connected user can access.

<details>
<summary>Full upstream description</summary>

```text
List Google Merchant Center accounts the connected user can access.

Returns each account's numeric ID, name and whether it is a test
account. Provides the account_id used by get_merchant_feed_health;
not needed when merchant.account_id is set in the config.

Merchant API: https://developers.google.com/merchant/api/overview
```

</details>

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/kLOsk/adloop/blob/e51d7d6498410755b1e437cc115ef822cbd72e84/src/adloop/server.py).

**Availability:** Registered by default; ADLOOP_TOOLSETS filters by toolset while core survives. Hosted runtimes can further filter.

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

## get_merchant_feed_health

Merchant Center feed health — disapproved products + account issues.

<details>
<summary>Full upstream description</summary>

```text
Merchant Center feed health — disapproved products + account issues.

Disapproved feed items silently starve Shopping and Performance Max
campaigns; this reports approved/pending/disapproved counts per
reporting context (Shopping ads, free listings, ...), the top product
issues by affected products (with documentation links), and
account-level issues — CRITICAL ones stop offers serving entirely.
Product-status data lags reality by ~30 minutes.

Merchant API: https://developers.google.com/merchant/api/overview
```

</details>

**Effect:** mixed. **Task:** Diagnose products and account issues. [Definition](https://github.com/kLOsk/adloop/blob/e51d7d6498410755b1e437cc115ef822cbd72e84/src/adloop/server.py).

**Availability:** Registered by default; ADLOOP_TOOLSETS filters by toolset while core survives. Hosted runtimes can further filter.

**Note:** Despite its upstream readOnlyHint, this tool automatically POSTs developer registration when the project is not registered.
**Note:** Account issues and aggregate statuses are not paginated. Summed totals cover reporting contexts and countries, so they are not a unique-product count.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | No | "" | Numeric Merchant Center ID from list_merchant_accounts.<br>Defaults to merchant.account_id in the config. |

<details>
<summary>Full parameter schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric Merchant Center ID from list_merchant_accounts.\nDefaults to merchant.account_id in the config."
    }
  },
  "type": "object"
}
```

</details>
