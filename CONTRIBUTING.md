# Contributing to Awesome Google Merchant Center MCP

Thanks for helping improve Awesome Google Merchant Center MCP. This repository is a curated, developer-focused index and benchmark of Model Context Protocol (MCP) servers, shopping automation tools, and agentic commerce protocols for **Google Merchant Center (GMC)** and its technical ecosystem.

**Read [AGENTS.md](./AGENTS.md) first** — it defines the structural information architecture, section taxonomy, description standards, and strict exclusion criteria. Everything required to propose or edit an entry is documented there.

---

## Pull Request Checklist

Before submitting a pull request, verify that:

- [ ] You have reviewed [AGENTS.md](./AGENTS.md).
- [ ] The repository directly interfaces with the **Google Merchant API v1**, **Content API for Shopping v2.1**, Google Shopping feed pipelines, or standard agentic commerce protocols (UCP/ACP).
- [ ] The entry uses the canonical format:
  `| <a id="owner--repo"></a>[**owner/repo**](https://github.com/owner/repo) | Description |`
- [ ] The description is strictly 1–2 plain-English sentences leading with an active verb (*Ingests*, *Validates*, *Synchronizes*, *Monitors*, *Bridges*), free of marketing hype or unsubstantiated superlatives.
- [ ] The project is placed in the single most accurate job-oriented category and subcategory.
- [ ] The Table of Contents count, section banner count, subcategory count, and table row count match exactly.
- [ ] The Developer Comparison Matrix is updated with the tool's verified technical attributes.
- [ ] All URLs and anchor links resolve correctly.
- [ ] Markdown linting passes cleanly via `npx markdownlint-cli2 "**/*.md"`.

---

## Scope & Exclusion Guidelines

We maintain a strict focus on Google Merchant Center and shopping data infrastructure:

- **Included:** Google Merchant API v1 servers, Content API for Shopping bridges, feed validation engines, GS1 GTIN Mod-10 verifiers, Multi-Client Account (MCA) routers, MCQL query tools, e-commerce catalog sync bridges, and agentic commerce protocol implementations (UCP/ACP).
- **Excluded:** Generic Google Ads campaign management tools without feed/inventory capabilities, general SEO keyword scrapers, storefront CMS plugins lacking direct Merchant API integrations, and unmaintained or disposable single-commit repositories.
