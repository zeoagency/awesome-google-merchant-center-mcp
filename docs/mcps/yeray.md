# YerayRodri/merchant-center-mcp

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://github.com/YerayRodri/merchant-center-mcp) · [Descriptors](../../catalog/yeray.json)

Find product issues and query catalog reports through a small read-only interface.

**4 tools:** 4 read. **Reviewed:** 2026-10-13.

**Extraction:** Runtime FastMCP registry inspection; independently re-extracted, with no handlers called.

**Source revision:** [0c6685c26d6c](https://github.com/YerayRodri/merchant-center-mcp/tree/0c6685c26d6c732daf6b29fccceb3358140c7f61).

All 4 Merchant Center and relevant setup tools are included.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`get_account`](#get_account) | Manage accounts, inventory, and conversions | read |
| [`list_datasources`](#list_datasources) | Manage products, feeds, and promotions | read |
| [`search_report`](#search_report) | Analyze performance and market prices | read |
| [`get_product_issues`](#get_product_issues) | Diagnose products and account issues | read |

## get_account

Retrieve account details such as name, language, and time zone.

<details>
<summary>Full upstream description</summary>

```text
Obtiene la información básica de una cuenta de Merchant Center
(nombre, account_id, idioma, zona horaria, si es cuenta de test).

Args:
    account_id: ID numérico de la cuenta de Merchant Center.
```

</details>

**Effect:** read. **Task:** Manage accounts, inventory, and conversions. [Definition](https://github.com/YerayRodri/merchant-center-mcp/blob/0c6685c26d6c732daf6b29fccceb3358140c7f61/server.py).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_accountArguments",
  "type": "object"
}
```

</details>

## list_datasources

List configured primary, supplemental, and local-inventory data sources.

<details>
<summary>Full upstream description</summary>

```text
Lista las fuentes de datos (feeds) de una cuenta de Merchant Center
con su configuración (primaria, suplementaria, inventario local, etc.).

Args:
    account_id: ID numérico de la cuenta de Merchant Center.
```

</details>

**Effect:** read. **Task:** Manage products, feeds, and promotions. [Definition](https://github.com/YerayRodri/merchant-center-mcp/blob/0c6685c26d6c732daf6b29fccceb3358140c7f61/server.py).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "list_datasourcesArguments",
  "type": "object"
}
```

</details>

## search_report

Run an MCQL query and return up to the requested number of report rows.

<details>
<summary>Full upstream description</summary>

```text
Ejecuta una query en Merchant Center Query Language (MCQL) contra la Reports API.
Solo se puede consultar una vista por request. Vistas más útiles: product_view
(catálogo procesado + item_issues), product_performance_view (clics/impresiones),
price_competitiveness_product_view, price_insights_product_view,
best_sellers_brand_view, best_sellers_product_cluster_view.

Nota: la Reports API solo funciona en cuentas standalone o sub-cuentas
individuales, no en cuentas "advanced" (agregadoras).

Args:
    account_id: ID numérico de la cuenta de Merchant Center.
    query: Query MCQL completa, ej.
        "SELECT offer_id, title, item_issues, availability FROM product_view"
    limit: Máximo de filas a devolver (por defecto 100).
```

</details>

**Effect:** read. **Task:** Analyze performance and market prices. [Definition](https://github.com/YerayRodri/merchant-center-mcp/blob/0c6685c26d6c732daf6b29fccceb3358140c7f61/server.py).

**Note:** Reports work on standalone accounts or individual subaccounts, not an advanced aggregator account.
**Note:** limit has no schema minimum; supply a positive integer.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |
| `query` | string | Yes | — | — |
| `limit` | integer | No | 100 | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "query": {
      "title": "Query",
      "type": "string"
    },
    "limit": {
      "default": 100,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "account_id",
    "query"
  ],
  "title": "search_reportArguments",
  "type": "object"
}
```

</details>

## get_product_issues

Find products with active item issues by filtering catalog report rows locally.

<details>
<summary>Full upstream description</summary>

```text
Auditoría rápida de feed: lista productos con issues activos (rechazados,
con warnings, etc.) vía product_view. Atajo sobre search_report para el
caso de uso más habitual de QA de catálogo.

Nota: MCQL no permite filtrar el campo repetido item_issues en WHERE, así
que se trae product_view completo y se filtra en Python los productos que
sí tienen issues.

Args:
    account_id: ID numérico de la cuenta de Merchant Center.
    limit: Máximo de productos con issues a devolver (por defecto 50).
```

</details>

**Effect:** read. **Task:** Diagnose products and account issues. [Definition](https://github.com/YerayRodri/merchant-center-mcp/blob/0c6685c26d6c732daf6b29fccceb3358140c7f61/server.py).

**Note:** Scans at most 5,000 rows. Products with issues beyond that boundary can be omitted; limit controls matches, not total catalog coverage.
**Note:** limit has no schema minimum; supply a positive integer.

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | Yes | — | — |
| `limit` | integer | No | 50 | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "limit": {
      "default": 50,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_product_issuesArguments",
  "type": "object"
}
```

</details>
