# Google Merchant API Developer Documentation MCP

[Catalog](../../README.md) · [Find a tool](../../TOOLS.md) · [Upstream](https://merchantapi.googleapis.com/devdocs/mcp/) · [Descriptors](../../catalog/google-docs.json)

Look up official Merchant API guidance and retrieve task-specific code samples.

**2 tools:** 2 read. **Reviewed:** 2026-10-13.

**Extraction:** Live HTTP MCP tools/list; independently rediscovered and compared every description and input schema.

**Source version:** serverInfo.version: unknown; MCP protocol 2025-03-26.

All 2 Merchant Center and relevant setup tools are included.

## Implementation notes

- Public documentation retrieval only; these tools do not inspect or change Merchant Center accounts.

## Tools

| Tool | Task | Effect |
| --- | --- | --- |
| [`query_mapi_docs`](#query_mapi_docs) | Build Merchant API integrations | read |
| [`find_mapi_code_sample`](#find_mapi_code_sample) | Build Merchant API integrations | read |

## query_mapi_docs

Retrieve official Merchant API guidance for conceptual and integration questions.

<details>
<summary>Full upstream description</summary>

```text
Queries Merchant API (MAPI) documentation (developer guides and reference) to answer conceptual questions about features, endpoints, and resources. Use this for 'how-to', 'what is', or 'why' questions. IMPORTANT: Do NOT send any code, sensitive authentication information (like API keys or secrets), or personal identifiable information (PII). Examples of PII to avoid include names, contact details, financial information, and government IDs.
```

</details>

**Effect:** read. **Task:** Build Merchant API integrations. [Definition](https://merchantapi.googleapis.com/devdocs/mcp/).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `query` | string | Yes | — | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "title": "query_mapi_docsArguments",
  "type": "object"
}
```

</details>

## find_mapi_code_sample

Find a Merchant API code sample for a requested task and optional language.

<details>
<summary>Full upstream description</summary>

```text
Finds specific MAPI code samples to demonstrate how to perform a task. Use this when a user explicitly asks for a code example or snippet. IMPORTANT: Do NOT send any code, sensitive authentication information (like API keys or secrets), or personal identifiable information (PII). Examples of PII to avoid include names, contact details, financial information, and government IDs.
```

</details>

**Effect:** read. **Task:** Build Merchant API integrations. [Definition](https://merchantapi.googleapis.com/devdocs/mcp/).

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `query` | string | Yes | — | — |
| `language` | string / null | No | null | — |

<details>
<summary>Full parameter schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "language": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Language"
    }
  },
  "required": [
    "query"
  ],
  "title": "find_mapi_code_sampleArguments",
  "type": "object"
}
```

</details>
