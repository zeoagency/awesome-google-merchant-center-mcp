# AGENTS.md

Architectural invariants, structural standards, and operational guidelines for AI agents and human contributors editing this repository. This project is a curated, developer-focused index and technical benchmark of the **Google Merchant Center (GMC)** Model Context Protocol (MCP) and agentic commerce ecosystem.

---

## 1. Project Philosophy & Minimalist Structure

- **Direct Developer Utility:** Maintain a clean, minimalist document flow without promotional onboarding essays or redundant walkthroughs. The root `README.md` must consist exclusively of: title & badge, positioning blockquote, official links line, Table of Contents with parenthesized counts, Developer Comparison Matrix, 7 numbered problem-domain sections, Resources, and Reference.
- **Immediate Navigation:** Developers and AI agents must be able to navigate from the Table of Contents or the Developer Comparison Matrix down to any specific tool's detailed description in one click.
- **Mathematical Count Integrity (Tripartite Invariant):** The count displayed in `## Contents` must equal the section banner count, the sum of subcategory counts, and the exact count of table rows in that section without exception:
  $$\text{Contents}(N) = \text{SectionBanner}(N) = \sum \text{Subcategory}(n) = \text{TableRows}(N)$$

---

## 2. Language & Voice Standards

Prose must remain concise, technical, and objective:

### 2.1. Plain-English, Active-Verb Syntax

- Always open descriptions with active third-person verbs (*Ingests*, *Validates*, *Synchronizes*, *Monitors*, *Bridges*, *Orchestrates*, *Inspects*, *Provisions*).
- Eliminate promotional marketing fluff (*"revolutionary"*, *"best-in-class"*, *"blazing fast"*, *"ultimate"*).
- Specify exact technical surfaces (e.g., Merchant API v1, Content API v2.1, MCQL, GS1 GTIN Mod-10, OAuth 2.1 PKCE, SQLite caching).

### 2.2. The 1–2 Sentence Rule

Every catalog table entry must be strictly 1 or 2 sentences:

- **Sentence 1:** Core functionality, primary runtime, and target API or protocol surface.
- **Sentence 2 (optional):** Key architectural discriminator (e.g., two-phase commit rollback, embedded SQLite worker, multi-tenant MCA routing).

---

## 3. Formatting Invariants

### 3.1. Detailed Table Entries

Each project entry in subcategory tables must follow this exact HTML anchor and markdown pattern:

```markdown
| <a id="owner--repo"></a>[**owner/repo**](https://github.com/owner/repo) | Description leading with an active verb. Optional second sentence on architectural details. |
```

- The `<a id="owner--repo"></a>` anchor enables direct jump links from the Developer Comparison Matrix.
- The project link uses bold brackets `[**owner/repo**](url)`.

### 3.2. Developer Comparison Matrix

- Located in Section 8 or immediately following the Table of Contents.
- Must not exceed 20 columns.
- Uses internal jump links formatted as: `[**owner/repo**](#owner--repo)`.
- Center alignment for checkmarks and status flags (`:---:`).

---

## 4. Scope & Inclusion Boundaries

### Strict Inclusions

- Direct Google Merchant API v1 and legacy Content API for Shopping v2.1 MCP servers.
- Product feed generators, XML/TSV formatters, and GS1 GTIN Mod-10 barcode validators.
- Disapproval inspection, account diagnostic monitors, and policy issue mitigators.
- Merchant Center Query Language (MCQL) search and reporting tools.
- Multi-Client Account (MCA) and multi-tenant sub-account routing gateways.
- E-commerce storefront bridges (Shopify, Shopware, commercetools) syncing with GMC.
- Agentic commerce protocols (Universal Commerce Protocol / UCP, Agentic Commerce Protocol / ACP) interfacing with merchant catalogs and checkout.

### Strict Exclusions

- Generic Google Ads campaign management tools lacking product feed or catalog components.
- General SEO web scrapers without dedicated Google Shopping or product SERP capabilities.
- Unmaintained single-commit boilerplate repositories or unverified AI stock dumps.
