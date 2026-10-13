# Contributing to Awesome Google Merchant Center MCP

Add tools that give people useful Google Merchant Center capabilities. Read [AGENTS.md](AGENTS.md) for the scope and verification rules.

## Add or update an MCP

1. Inspect the upstream implementation and capture its complete tool descriptors, including optional registrations. Prefer MCP tools/list or the runtime registry; avoid calling account operations during discovery.
2. Add or update `catalog/<id>.json`: preserve exact tool names, descriptions, and full input schemas; add pinned source links, extraction provenance, a short summary, task category, and reviewed effect for each tool.
3. Include Merchant Center tools and relevant setup helpers. Record the full registry count and explain omissions from multi-service servers.
4. Add the server to `catalog/manifest.json`, choose its primary task group from its tools, and select concrete examples. Follow an existing entry's structure.
5. Generate the pages with `python3 scripts/build_catalog.py` and review the resulting main-page entry, tool reference, and alphabetical index.

## Add or update a CLI or SDK

Verify implemented Merchant Center functionality against its source or official package documentation, then edit the companion section in `catalog/manifest.json`.

## Before submitting

- Check source URLs, parameter completeness, optional-tool availability, and the effects of each handler.
- Run `python3 scripts/build_catalog.py --check`.
- Run `npx --yes markdownlint-cli2@latest "**/*.md"`.
- Explain the source revision and any material implementation limits in your pull request.
