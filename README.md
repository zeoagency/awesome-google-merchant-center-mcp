# Awesome Google Merchant Center MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, verified index of Model Context Protocol (MCP) servers and official developer tooling built for **[Google Merchant Center (GMC)](https://developers.google.com/merchant)**, the **Merchant API v1**, and Google Shopping automation.
>
> **Last verified:** 2026-10-05 · **Ecosystem reality:** No GMC MCP has a 12-month steady record yet; all dedicated servers were created in 2026 following the Google Merchant API v1 migration.

Official links: [Google Merchant API v1](https://developers.google.com/merchant) · [Content API for Shopping v2.1](https://developers.google.com/shopping-content/reference/rest) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Google Cloud Console](https://console.cloud.google.com/) · [Zeo Agency](https://zeo.org/)

---

## Contents

- [Developer Comparison Matrix](#developer-comparison-matrix)

1. [Manage products, inventories, and catalog data sources (3)](#1-manage-products-inventories-and-catalog-data-sources)
   - [Direct Google Merchant API v1 servers (2)](#direct-google-merchant-api-v1-servers)
   - [Official developer documentation tooling (1)](#official-developer-documentation-tooling)
2. [Diagnose disapprovals, policy violations, and feed health (3)](#2-diagnose-disapprovals-policy-violations-and-feed-health)
   - [Disapproval detection and policy triage engines (3)](#disapproval-detection-and-policy-triage-engines)
3. [Query performance analytics and MCQL reports (2)](#3-query-performance-analytics-and-mcql-reports)
   - [Shopping campaign analytics and cross-channel performance (2)](#shopping-campaign-analytics-and-cross-channel-performance)
4. [Enforce operational safety, dry-runs, and mutation rollback (1)](#4-enforce-operational-safety-dry-runs-and-mutation-rollback)
   - [Governed writes and cryptographic approval ledgers (1)](#governed-writes-and-cryptographic-approval-ledgers)
5. [Multi-service marketing suites with Merchant Center modules (2)](#5-multi-service-marketing-suites-with-merchant-center-modules)
   - [Cross-platform marketing and ad operations suites (2)](#cross-platform-marketing-and-ad-operations-suites)
6. [Legacy Content API for Shopping bridges (3)](#6-legacy-content-api-for-shopping-bridges)
   - [Edge proxies and Content API v2.1 gateways (3)](#edge-proxies-and-content-api-v21-gateways)
7. [Defective, deprecated, and hazardous implementations (Audit Warnings) (3)](#7-defective-deprecated-and-hazardous-implementations-audit-warnings)
   - [Quarantined and hazardous implementations (3)](#quarantined-and-hazardous-implementations)
8. [Resources](#resources)
   - [Official Documentation and SDKs](#official-documentation-and-sdks)
   - [Specifications and Standards](#specifications-and-standards)
9. [Reference](#reference)
   - [Merchant API v1 vs Content API v2.1 Architecture](#merchant-api-v1-vs-content-api-v21-architecture)
   - [Evaluation Methodology and Verification Invariants](#evaluation-methodology-and-verification-invariants)
   - [Repository Inclusion and Anti-Slop Policy](#repository-inclusion-and-anti-slop-policy)

---

## Developer Comparison Matrix

*A comparative feature matrix of all 17 verified Model Context Protocol servers, official Google endpoints, and companion tools for Google Merchant Center, detailing language runtime, target API surface, AST-verified tool count, operational safety guardrails, authentication patterns, maintenance longevity, and empirical audit verdicts. Click on any project name to jump directly to its detailed listing below.*

| Project | Runtime | Target API | Tools | Mode | Safety Guardrails | Auth Pattern | Longevity | Verdict / Recommendation |
|---|---|---|:---:|---|---|---|:---:|---|
| [**A1-x-Tech/mcp-google-merchants**](#A1-x-Tech--mcp-google-merchants) | TypeScript | Merchant API v1 | 28 | Read-Write | ⚠️ Unguarded writes | OAuth 2.0 PKCE / Token | 🟡 2 mo steady | ✅ **Primary Self-Hosted** (Pin 1.2.0, Read-Only) |
| [**Google: Merchant API MCP**](#google--merchant-api-mcp) | Hosted Cloud | Merchant API v1 | 13 | Read / Low-Risk | 🛡️ Google-guarded filters | OAuth 2.0 Bearer | 🟡 Alpha | ➕ **Zero-Maintenance Option** (Try first) |
| [**Google: Developer Docs MCP**](#google--developer-docs-mcp) | Hosted Cloud | Merchant API Specs | Docs | Read-Only | 🔒 Read-Only (Docs helper) | Open / None | 🟡 Active | 🧰 **Developer Docs Helper** (Coding assistant) |
| [**webloom-agency/merchant-center-mcp**](#webloom-agency--merchant-center-mcp) | Python (FastMCP) | Merchant API v1 | 25 | Read-Only | 🔒 Read-Only | OAuth 2.1 PKCE | 🔴 Dormant (2 bursts) | 🔧 **Borrow Issue Rendering** |
| [**YerayRodri/merchant-center-mcp**](#YerayRodri--merchant-center-mcp) | Python (FastMCP) | Merchant API v1 | 4 | Read-Only | 🔒 Read-Only | Service Account | 🔴 Dormant (1 commit) | ❌ **Skip** (Unmaintained prototype) |
| [**MoonEyes/google-ecommerce-mcp**](#MoonEyes--google-ecommerce-mcp) | Python (FastMCP) | Merchant API v1 | 13 (3 GMC) | Read-Only | 🔒 Regex endpoint allowlist | Service Account JSON | 🔴 New (Oct 2026) | 🔧 **Borrow Allowlist Pattern** |
| [**googleads/google-ads-mcp**](#googleads--google-ads-mcp) | Python (FastMCP) | Google Ads API | 3 | Read-Only | 🔒 Read-Only | OAuth 2.0 / Developer Token | 🟢 Steady (Official) | ➕ **Shopping/PMax Companion** (GAQL queries) |
| [**MadMaxen92/marketing-mcp**](#MadMaxen92--marketing-mcp) | TypeScript | Merchant API v1 | 56 | Read-Only | 🔒 Read-Only (Merchant slice) | OAuth 2.0 | 🔴 Dormant (Aug 2026) | ❌ **Skip** (Unpublished, single sprint) |
| [**ScaleLean/google-ads-mcp-starter**](#ScaleLean--google-ads-mcp-starter) | Python (FastMCP) | Merchant API v1 | 30 (14 GMC) | Governed Writes | 🛡️ HMAC approvals & rollback | OAuth 2.0 / Firestore | 🔴 Dormant (1 commit) | 🔧 **Borrow Write Safety** (HMAC ledger) |
| [**kLOsk/adloop**](#kLOsk--adloop) | Python | Merchant API v1 | 109 (2 GMC) | Hybrid | 🛡️ Guarded | OAuth 2.0 | 🟡 Active (Ads focus) | ❌ **Skip for GMC** (Only 2 GMC tools) |
| [**marwa-mrwan/google-clarity-mcp-codex**](#marwa-mrwan--google-clarity-mcp-codex) | JavaScript (Node.js) | Merchant API v1 | 213 (40 GMC) | Read-Write | ⚠️ Bloat / No License | OAuth 2.0 | 🔴 Dormant (0 tags) | ❌ **Skip** (Context bloat & legal risk) |
| [**gioenjoy/mcp-google-merchant-center**](#gioenjoy--mcp-google-merchant-center) | JavaScript (Node.js) | Content API v2.1 | 6 | Read-Only | 🔒 Read-Only | Service Account ADC | 🔴 Dormant | ❌ **Skip** (Retired Content API v2.1) |
| [**ai-godfather/google-mcp-universal**](#ai-godfather--google-mcp-universal) | Python | Content API v2.1 | 186 (20 GMC) | Read-Write | ⚠️ Unguarded writes | Service Account | 🔴 Dormant (2 commits) | ❌ **Skip** (Retired Content API v2.1) |
| [**Nas198222/google-mcp-bridge**](#Nas198222--google-mcp-bridge) | TypeScript (Edge) | Content API v2.1 | 2 | Read-Only | ⚠️ Minimal | Service Account | 🔴 Dormant (4 commits) | ❌ **Skip** (Retired Content API v2.1) |
| [**kiwoongeom/gmc-mcp**](#kiwoongeom--gmc-mcp) | Python (FastMCP) | Merchant API v1 | 126 | Destructive Writes | ❌ **Critical bug: Ignored filter** | OAuth 2.0 PKCE | 🔴 Dormant (1-day burst) | ❌ **HAZARD: Do Not Use** (Bulk delete defect) |
| [**archpeng/GMC-mcp-server**](#archpeng--GMC-mcp-server) | Python (FastMCP) | Merchant API v1beta | 34 | Read-Write | ⚠️ Sunset API / No License | gRPC / Service Account | 🔴 Abandoned (Feb 2026) | ❌ **Skip** (Sunset v1beta / No License) |
| [**akelaonline/MCP-Google-Ads**](#akelaonline--MCP-Google-Ads) | Python (FastMCP) | Content API v2.1 | 461 (17 GMC) | Read-Write | ⚠️ Massive context bloat | Dual SA / OAuth | 🔴 Dormant | ❌ **Skip** (461 tools, retired Content API) |

---

## 1. Manage products, inventories, and catalog data sources

*3 projects. Model Context Protocol servers and official endpoints connecting to the modern Google Merchant API v1 for product catalog ingestion, inventory management, and developer documentation.*

### Direct Google Merchant API v1 servers

*2 projects. Production-oriented Model Context Protocol servers implementing the modern Google Merchant API v1 surface.*

| Project | What it does |
|---|---|
| <a id="A1-x-Tech--mcp-google-merchants"></a>[**A1-x-Tech/mcp-google-merchants**](https://github.com/A1-x-Tech/mcp-google-merchants) | Implements a dedicated TypeScript Model Context Protocol server wrapping Google Merchant API v1 with Zod schema validation and StdioServerTransport. Provides 22 core Merchant Center tools and 6 authentication management tools with automated CI and daily health-check workflows. |
| <a id="google--merchant-api-mcp"></a>[**Google: Merchant API MCP Access Service**](https://merchantapi.googleapis.com/mcp) | Provides Google's official hosted remote Model Context Protocol endpoint for direct access to Merchant API v1 diagnostics, MCQL performance queries, and data sources. Serves 13 filtered tools (11 read-only and 2 low-risk data source operations) over standard OAuth 2.0 bearer authorization. |

### Official developer documentation tooling

*1 project. Google's official documentation assistant providing schema specifications and migration guidance.*

| Project | What it does |
|---|---|
| <a id="google--developer-docs-mcp"></a>[**Google: Developer Docs MCP Server**](https://merchantapi.googleapis.com/devdocs/mcp) | Retrieves official Google Merchant API documentation, schema references, and Content API v2.1 migration guides for AI coding agents. Operates strictly as a read-only developer documentation helper without accessing live merchant catalog accounts. |

---

## 2. Diagnose disapprovals, policy violations, and feed health

*3 projects. Specialized read-only diagnostic servers providing item-level disapproval triage, policy violation resolution, and endpoint allowlisting.*

### Disapproval detection and policy triage engines

*3 projects. Focused diagnostic engines inspecting Merchant Center issue codes and feed processing errors.*

| Project | What it does |
|---|---|
| <a id="webloom-agency--merchant-center-mcp"></a>[**webloom-agency/merchant-center-mcp**](https://github.com/webloom-agency/merchant-center-mcp) | Inspects Google Merchant API v1 product disapproval codes and account-level policy violations via 25 read-only FastMCP tools. Formats human-readable remediation instructions and diagnostic summaries for marketing consultants. |
| <a id="YerayRodri--merchant-center-mcp"></a>[**YerayRodri/merchant-center-mcp**](https://github.com/YerayRodri/merchant-center-mcp) | Queries real-time item disapproval codes and data source statuses using 4 focused Python FastMCP diagnostic tools over Merchant API v1. Provides basic disapproval inspection but lacks automatic Google Cloud Project developer registration. |
| <a id="MoonEyes--google-ecommerce-mcp"></a>[**MoonEyes/google-ecommerce-mcp**](https://github.com/MoonEyes/google-ecommerce-mcp) | Audits merchant issues and primary data sources through 3 dedicated Google Merchant Center tools within a 13-tool FastMCP e-commerce suite. Enforces a strict regex-based read-only endpoint allowlist that prevents unintended mutations. |

---

## 3. Query performance analytics and MCQL reports

*2 projects. Reporting servers executing Merchant Center Query Language (MCQL) and Google Ads Query Language (GAQL) queries for Shopping campaign intelligence.*

### Shopping campaign analytics and cross-channel performance

*2 projects. Query engines extracting impression share, product partitions, and catalog revenue metrics.*

| Project | What it does |
|---|---|
| <a id="googleads--google-ads-mcp"></a>[**googleads/google-ads-mcp**](https://github.com/googleads/google-ads-mcp) | Queries Google Ads and Performance Max campaign metrics via 3 official Python FastMCP tools using Google Ads Query Language (GAQL). Delivers essential Shopping campaign reporting, product partition performance, and impression share telemetry to complement Merchant Center catalog data. |
| <a id="MadMaxen92--marketing-mcp"></a>[**MadMaxen92/marketing-mcp**](https://github.com/MadMaxen92/marketing-mcp) | Correlates Google Merchant Center product statuses with advertising performance across Google and Meta marketing channels. Exposes 56 cross-network tools with a read-only Merchant API v1 slice, though unmaintained since August 2026. |

---

## 4. Enforce operational safety, dry-runs, and mutation rollback

*1 project. Governed architectures enforcing cryptographic approval gates, before-state ledgers, and rollback snapshots for catalog mutations.*

### Governed writes and cryptographic approval ledgers

*1 project. FastMCP implementation featuring two-phase mutation approvals and before-state audit ledgers.*

| Project | What it does |
|---|---|
| <a id="ScaleLean--google-ads-mcp-starter"></a>[**ScaleLean/google-ads-mcp-starter**](https://github.com/ScaleLean/google-ads-mcp-starter) | Secures Merchant API v1 and Google Ads mutations through 14 dedicated merchant tools governed by cryptographic HMAC approvals and Firestore audit logs. Captures before-and-after state snapshots to enable deterministic rollback of accidental catalog changes. |

---

## 5. Multi-service marketing suites with Merchant Center modules

*2 projects. Broad marketing orchestration platforms packaging limited Google Merchant Center connectors alongside extensive advertising toolsets.*

### Cross-platform marketing and ad operations suites

*2 projects. Enterprise suites bundling multi-network ad management with secondary Merchant Center utilities.*

| Project | What it does |
|---|---|
| <a id="kLOsk--adloop"></a>[**kLOsk/adloop**](https://github.com/kLOsk/adloop) | Orchestrates advertising workflows across Google Ads, Meta, and LinkedIn with 109 tools, including 2 dedicated Google Merchant Center tools for account discovery and feed health. Automates Google Cloud developer project registration but provides minimal native catalog management. |
| <a id="marwa-mrwan--google-clarity-mcp-codex"></a>[**marwa-mrwan/google-clarity-mcp-codex**](https://github.com/marwa-mrwan/google-clarity-mcp-codex) | Bundles 40 Google Merchant API v1 tools with Microsoft Clarity behavioral analytics across a massive 213-tool Node.js suite. Connects product disapprovals to user session recordings, but imposes heavy LLM context bloat and lacks an open-source license grant. |

---

## 6. Legacy Content API for Shopping bridges

*3 projects. Legacy Model Context Protocol servers connecting to the retired Content API for Shopping v2.1.*

### Edge proxies and Content API v2.1 gateways

*3 projects. Historical bridges and Cloudflare workers querying deprecated Google Content API endpoints.*

| Project | What it does |
|---|---|
| <a id="gioenjoy--mcp-google-merchant-center"></a>[**gioenjoy/mcp-google-merchant-center**](https://github.com/gioenjoy/mcp-google-merchant-center) | Connects to legacy Content API for Shopping v2.1 via 6 basic JavaScript tools for product catalog listings and account statuses. Relies on Application Default Credentials (ADC) but remains dormant and unmaintained. |
| <a id="ai-godfather--google-mcp-universal"></a>[**ai-godfather/google-mcp-universal**](https://github.com/ai-godfather/google-mcp-universal) | Audits Google Shopping campaign coverage against merchant catalogs using 20 merchant tools within a 186-tool Python advertising suite. Targets the legacy Content API for Shopping v2.1 without migration to Merchant API v1. |
| <a id="Nas198222--google-mcp-bridge"></a>[**Nas198222/google-mcp-bridge**](https://github.com/Nas198222/google-mcp-bridge) | Bridges Google Cloud and legacy Content API for Shopping v2.1 services using a TypeScript Cloudflare Pages edge deployment. Exports 2 basic catalog tools but has seen only 4 commits since initial upload. |

---

## 7. Defective, deprecated, and hazardous implementations (Audit Warnings)

*3 projects. Documented implementations carrying critical functional bugs, API deprecation blocks, or extreme schema bloat that disqualify them from production use.*

### Quarantined and hazardous implementations

*3 projects. Servers evaluated during independent technical audits and flagged with severe operational warnings.*

| Project | What it does |
|---|---|
| <a id="kiwoongeom--gmc-mcp"></a>[**kiwoongeom/gmc-mcp**](https://github.com/kiwoongeom/gmc-mcp) | Implements 126 Python FastMCP tools across Merchant API v1 but carries a critical data-loss defect in catalog management. Leaves the `filter_status` argument in `gmc_bulk_delete_products` implemented as a no-op `pass`, causing the tool to unconditionally delete all products in the catalog up to `max_delete`. |
| <a id="archpeng--GMC-mcp-server"></a>[**archpeng/GMC-mcp-server**](https://github.com/archpeng/GMC-mcp-server) | Wraps 34 Google Merchant Center tools in Python FastMCP across accounts, products, and reports. Remains abandoned since February 2026, relies on deprecated `merchant_*_v1beta` endpoints sunset by Google, and lacks an open-source license. |
| <a id="akelaonline--MCP-Google-Ads"></a>[**akelaonline/MCP-Google-Ads**](https://github.com/akelaonline/MCP-Google-Ads) | Assembles 461 tools across Google Ads and legacy Content API for Shopping v2.1 in a monolithic FastMCP server. Exhausts LLM context windows due to massive schema token bloat and targets retired Google Shopping API endpoints. |

---

## Resources

Curated official developer documentation, protocols, and technical resources for building Google Merchant Center agent tooling.

### Official Documentation and SDKs

- [Google Merchant API v1 Documentation](https://developers.google.com/merchant) — Official developer guides for the modern sub-API architecture covering Products, Accounts, Inventories, Promotions, and Data Sources.
- [Google Content API for Shopping Reference](https://developers.google.com/shopping-content/reference/rest) — Upstream REST reference for legacy v2.1 services and supplemental feed pipelines.
- [Google Merchant Center Help Center](https://support.google.com/merchants) — Policy guides, account suspension troubleshooting, and feed specification rules.
- [Google Cloud API Client Libraries](https://cloud.google.com/apis/docs/client-libraries-explained) — Official client SDKs across Python, Node.js, Go, and Java supporting Application Default Credentials (ADC).

### Specifications and Standards

- [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io/) — Open protocol standard defining client-server JSON-RPC messaging, stdio/SSE transports, and dynamic tool invocation for AI agents.
- [Universal Commerce Protocol (UCP) Specification](https://github.com/NVIDIA-AI-Blueprints/Retail-Agentic-Commerce) — Open standard for decentralized agentic commerce, autonomous product discovery, and merchant catalog federation.
- [GS1 GTIN Validation Rules](https://www.gs1.org/services/check-digit-calculator) — Specification and Mod-10 checksum validation algorithms for Global Trade Item Numbers (UPC, EAN, ISBN).

---

## Reference

Architectural principles, upstream API comparisons, and verification standards governing this index.

### Merchant API v1 vs Content API v2.1 Architecture

Google has transitioned merchant infrastructure from the monolithic **Content API for Shopping v2.1** to the modular **Google Merchant API v1**:

| Architectural Dimension | Legacy Content API for Shopping v2.1 | Modern Google Merchant API v1 |
|---|---|---|
| **API Structure** | Monolithic single-service REST endpoint | Modular sub-APIs (`products_v1`, `accounts_v1`, `datasources_v1`, `inventories_v1`, `promotions_v1`) |
| **Transport Protocol** | REST / JSON-RPC over HTTP/1.1 | Native gRPC over HTTP/2 with high-performance protobuf serialization + REST fallback |
| **Data Ingestion** | Monolithic batch feeds with high latency | Real-time incremental sub-feeds and primary/supplemental data sources |
| **Query Engine** | Rigid parameter-based list queries | Flexible Merchant Center Query Language (MCQL) with SQL-like syntax and field projections |
| **Authentication** | Basic Service Account JSON or OAuth 2.0 | OAuth 2.1 PKCE with scoped fine-grained IAM roles and Multi-Client Account (MCA) delegation |

### Evaluation Methodology and Verification Invariants

All 17 repositories and endpoints listed in this catalog were evaluated against empirical engineering standards (Last verified: 2026-10-05):

1. **AST & Code Inspection:** Every tool was audited at the source-code level to verify callable tool counts, Zod/Pydantic input schemas, error handling, and target API alignment.
2. **Longevity & Ecosystem Ground Truth:** No Google Merchant Center MCP in existence has a 12-month steady development record. Google Merchant API v1 reached general stability only in 2026 following the sunset of Content API v2.1 and v1beta. Every dedicated GMC MCP was created in 2026.
3. **Developer Provenance & Anti-Slop Audit:** Maintainer GitHub profiles, commit histories, package registrations, and PR workflows were audited to separate sustained human engineering from disposable single-commit synthetic boilerplate or closed paywalls.
4. **Operational Safety Audit:** Tools modifying live merchant inventories were evaluated for dry-run validation modes, spending guardrails, and audit rollback ledgers. Implementations with destructive defects (such as `kiwoongeom/gmc-mcp`) are explicitly flagged with hazard warnings.

### Repository Inclusion and Anti-Slop Policy

This catalog maintains strict boundaries to protect developers and consultants from unmaintained code, AI hallucination, and off-scope dilution.

During our October 2026 empirical audit, **31 non-qualifying repositories** were pruned from this index:

- **Official Code Samples & SDKs without MCP Runtimes (2):** `google/merchant-api-alpha-client` (client library bindings only), `googleads/googleads-shopping-samples` (Java Content API reference code).
- **Standalone CMS Feed Plugins & Generators (4):** `haerriz/magento2-google-shopping-feed` (Magento 2 PHP extension), `umeshravani/spree_google_products` (Spree Rails gem), `BurhanBeigh/merchant-feed-builder` (standalone Python CLI feed builder), `GajewskiMarcin/FeedForge` (PrestaShop CLI feed validator).
- **Search Engine SERP Scrapers (4):** `GreXLin85/serper.dev-mcp` (Serper SERP scraper), `alessandrobenigni/ScrapingDog-MCP` (scraping proxy), `ShoppingResult/shoppingscraper-cli` (Node.js SERP scraper), `roblouw2nd/fetchgate` (scraping proxy).
- **Storefront-Only & Third-Party E-Commerce Connectors (5):** `rushikeshmore/shopify-partner-agent` (Shopify Partner analytics), `msalihk/catalog-mcp` (Shopify Storefront GTIN validator), `prajapatimehul/shopify-cowork` (Shopify GraphQL theme plugin), `agentic-commerce-lab/shopware-claude-commerce` (Shopware 6.7 Admin bridge), `agidesigner/OpenLucid` (social marketing copy generator with 0 GMC tools).
- **Documentation & Roadmap Stubs with Zero GMC Code (2):** `itallstartedwithaidea/advertising-hub` (ad docs with zero GMC tools), `markifact/markifact-mcp` (zero GMC tools in code, roadmap mention only).
- **Installer Shell Scripts (1):** `christyandas/google-ads-brasil` (duplicate shell script installing `kiwoongeom/gmc-mcp` from PyPI).
- **Closed Commercial SaaS Paywalls (4):** `PaidSync/paidsync-mcp` (closed SaaS, unverified backend), `HYPD-AI/ads-mcp-plugin` (closed SaaS, no public code), `Ryze-AI-Adgent/cursor-plugin` (closed commercial connector), `simpleproductfeeds/skills` (proprietary backend, 0 public MCP tools).
- **Generic Agentic Commerce & Settlement Testbeds (6):** `davillafer/mcp-merchant-scout` (UCP search tool), `flovoice53-tech/acp-sandbox` (ACP protocol sandbox), `api-evangelist/agenthaven-dev` (DNS-AID flight seller PoC), `ihint/merchant-context` (x402 protocol inspector), `ViryaZheng/ucp-onboard` (UCP onboarding agent), `NVIDIA-AI-Blueprints/Retail-Agentic-Commerce` (multimodal retail blueprint without GMC).
- **Misclassified Scripts & Bots (2):** `aakashraj7/vocalize` (voice-to-MongoDB inventory script), `gonbenvindo-debug/google-tools-manager` (Playwright browser bot, not an MCP server).
- **Non-MCP CLI Skill Packs (1):** `almoretti/martech-ai-skills-and-tools` (gmc-cli; contains 0 MCP tools or JSON-RPC protocol transport).
