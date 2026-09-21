# Awesome Google Merchant Center MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of Model Context Protocol (MCP) servers, product feed validators, and agent-facing tools built for **[Google Merchant Center (GMC)](https://developers.google.com/merchant)**, the **Merchant API v1**, and autonomous commerce rails.

Official links: [Google Merchant API v1](https://developers.google.com/merchant) · [Content API for Shopping v2.1](https://developers.google.com/shopping-content/reference/rest) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Google Cloud Console](https://console.cloud.google.com/) · [Zeo Agency](https://zeo.org/)

---

## Contents

- [Developer Comparison Matrix](#developer-comparison-matrix)

1. [Manage products, inventories, and catalog data sources (13)](#1-manage-products-inventories-and-catalog-data-sources)
   - [Direct Google Merchant API v1 servers (4)](#direct-google-merchant-api-v1-servers)
   - [Official and reference developer SDKs (3)](#official-and-reference-developer-sdks)
   - [Consolidated catalog management gateways (6)](#consolidated-catalog-management-gateways)
2. [Diagnose disapprovals, policy violations, and feed health (9)](#2-diagnose-disapprovals-policy-violations-and-feed-health)
   - [gRPC and REST diagnostic monitors (3)](#grpc-and-rest-diagnostic-monitors)
   - [Disapproval and policy resolution engines (3)](#disapproval-and-policy-resolution-engines)
   - [Search intelligence and competitive price scraping (3)](#search-intelligence-and-competitive-price-scraping)
3. [Persist and analyze performance with MCQL and SQL (9)](#3-persist-and-analyze-performance-with-mcql-and-sql)
   - [Embedded database and local cache engines (3)](#embedded-database-and-local-cache-engines)
   - [E-commerce intelligence and partner analytics (3)](#e-commerce-intelligence-and-partner-analytics)
   - [Marketing orchestration and report generators (3)](#marketing-orchestration-and-report-generators)
4. [Enforce operational safety, dry-runs, and mutation rollback (2)](#4-enforce-operational-safety-dry-runs-and-mutation-rollback)
   - [Transactional edge proxies and protocol sandboxes (2)](#transactional-edge-proxies-and-protocol-sandboxes)
5. [Manage multi-tenant access and Multi-Client Account (MCA) routing (3)](#5-manage-multi-tenant-access-and-multi-client-account-mca-routing)
   - [Multi-tenant OAuth gateways and sub-account routers (2)](#multi-tenant-oauth-gateways-and-sub-account-routers)
   - [Context persistence and account scoping protocols (1)](#context-persistence-and-account-scoping-protocols)
6. [Bridge e-commerce storefronts and multi-channel catalogs (2)](#6-bridge-e-commerce-storefronts-and-multi-channel-catalogs)
   - [Storefront catalog synchronization bridges (2)](#storefront-catalog-synchronization-bridges)
7. [Deploy autonomous agentic commerce, ACP/UCP, and machine settlement (2)](#7-deploy-autonomous-agentic-commerce-acpucp-and-machine-settlement)
   - [Universal Commerce Protocol (UCP) onboarding and reference stacks (2)](#universal-commerce-protocol-ucp-onboarding-and-reference-stacks)
8. [Resources](#resources)
   - [Official Documentation and SDKs](#official-documentation-and-sdks)
   - [Specifications and Standards](#specifications-and-standards)
9. [Reference](#reference)
   - [Merchant API v1 vs Content API v2.1 Architecture](#merchant-api-v1-vs-content-api-v21-architecture)
   - [Evaluation Methodology and Verification Invariants](#evaluation-methodology-and-verification-invariants)
   - [Repository Inclusion and Anti-Slop Policy](#repository-inclusion-and-anti-slop-policy)

---

## Developer Comparison Matrix

*A comparative feature matrix of all 40 Model Context Protocol servers, developer SDKs, and agent interfaces for Google Merchant Center, detailing language runtime, target API surface, tool count, operational safety guardrails, authentication patterns, and quality tiers. Click on any project name to jump directly to its detailed listing below.*

| Project | Stars | Runtime | Target API | Tools | Mode | Safety Guardrails | Auth Pattern | Tier |
|---|:---:|---|---|:---:|---|---|---|---|
| [**A1-x-Tech/mcp-google-merchants**](#A1-x-Tech--mcp-google-merchants) | ★ 0 | TypeScript | Merchant API v1 | 28 | Read-Only | — | Config / Env | B · Community Stable |
| [**BurhanBeigh/merchant-feed-builder**](#BurhanBeigh--merchant-feed-builder) | ★ 1 | Python | GMC Feed XML/TSV | — | CLI / Generator | ✅ Dry-Run | Config / Env | A · Production-Ready |
| [**GajewskiMarcin/FeedForge**](#GajewskiMarcin--FeedForge) | ★ 3 | PHP / PrestaShop | Merchant API v1 | — | Read-Only | ✅ Dry-Run | OAuth 2.0 | A- · Community Stable |
| [**GreXLin85/serper.dev-mcp**](#GreXLin85--serper.dev-mcp) | ★ 1 | TypeScript | Google Shopping SERP | 12 | Read-Only | — | API Key | A · Production-Ready |
| [**HYPD-AI/ads-mcp-plugin**](#HYPD-AI--ads-mcp-plugin) | ★ 2 | Config / Spec | Merchant API v1 | 5 | Read-Only | — | Config / Env | B · Community Stable |
| [**MadMaxen92/marketing-mcp**](#MadMaxen92--marketing-mcp) | ★ 0 | TypeScript | Merchant API v1 | 56 | Read-Write | ✅ Dry-Run · Rollback | OAuth 2.0 | A+ · Production-Ready |
| [**NVIDIA-AI-Blueprints/Retail-Agentic-Commerce**](#NVIDIA-AI-Blueprints--Retail-Agentic-Commerce) | ★ 75 | Python | UCP / ACP | 10 | Read-Write | — | Bearer Token | A+ · Production-Ready |
| [**Nas198222/google-mcp-bridge**](#Nas198222--google-mcp-bridge) | ★ 0 | TypeScript | Merchant API v1 | 17 | Read-Only | — | Config / Env | B · Community Stable |
| [**PaidSync/paidsync-mcp**](#PaidSync--paidsync-mcp) | ★ 3 | TypeScript | Merchant API v1 | 3 | Read-Write | — | OAuth 2.0 | B+ · Community Stable |
| [**ShoppingResult/shoppingscraper-cli**](#ShoppingResult--shoppingscraper-cli) | ★ 1 | TypeScript | Google Shopping SERP | 18 | Read-Only | — | API Key | A · Production-Ready |
| [**ViryaZheng/ucp-onboard**](#ViryaZheng--ucp-onboard) | ★ 4 | Python | UCP / ACP | 7 | Read-Write | — | Config / Env | A · Production-Ready |
| [**YerayRodri/merchant-center-mcp**](#YerayRodri--merchant-center-mcp) | ★ 0 | Python | Merchant API v1 | 4 | Read-Only | — | OAuth 2.0 | A- · Community Stable |
| [**aakashraj7/vocalize**](#aakashraj7--vocalize) | ★ 0 | TypeScript | Merchant API v1 | 2 | Read-Write | — | Config / Env | B · Community Stable |
| [**agentic-commerce-lab/shopware-claude-commerce**](#agentic-commerce-lab--shopware-claude-commerce) | ★ 0 | Python | Shopware 6.7 Admin | 34 | Read-Write | ✅ Dry-Run | OAuth 2.1 PKCE | A+ · Production-Ready |
| [**agidesigner/OpenLucid**](#agidesigner--OpenLucid) | ★ 31 | Python | Merchant API v1 | 50 | Read-Only | — | Config / Env | B · Community Stable |
| [**akelaonline/MCP-Google-Ads**](#akelaonline--MCP-Google-Ads) | ★ 4 | Python | Merchant API v1 | 461 | Read-Write | ✅ Dry-Run · Rollback | OAuth 2.0 | A+ · Production-Ready |
| [**alessandrobenigni/ScrapingDog-MCP**](#alessandrobenigni--ScrapingDog-MCP) | ★ 1 | JavaScript | Google Shopping SERP | 77 | Read-Only | — | API Key | B+ · Community Stable |
| [**almoretti/martech-ai-skills-and-tools**](#almoretti--martech-ai-skills-and-tools) | ★ 2 | TypeScript | Merchant API v1 | 39 | Read-Write | ✅ Dry-Run | ADC / IAM | A · Production-Ready |
| [**api-evangelist/agenthaven-dev**](#api-evangelist--agenthaven-dev) | ★ 0 | Config / Spec | Merchant API v1 | 2 | Read-Only | — | Config / Env | B · Community Stable |
| [**christyandas/google-ads-brasil**](#christyandas--google-ads-brasil) | ★ 0 | JavaScript | Merchant API v1 | 126 | Hybrid | — | Service Account | B · Community Stable |
| [**davillafer/mcp-merchant-scout**](#davillafer--mcp-merchant-scout) | ★ 0 | TypeScript | UCP / ACP | 4 | Read-Only | — | Config / Env | A- · Community Stable |
| [**flovoice53-tech/acp-sandbox**](#flovoice53-tech--acp-sandbox) | ★ 0 | TypeScript | ACP Protocol | 7 | Read-Write | ✅ Sandbox / Gate | Bearer Token | A- · Community Stable |
| [**gioenjoy/mcp-google-merchant-center**](#gioenjoy--mcp-google-merchant-center) | ★ 0 | TypeScript | Merchant API v1 | 6 | Read-Only | — | Service Account | B · Community Stable |
| [**google/merchant-api-alpha-client**](#google--merchant-api-alpha-client) | ★ 1 | Python | Merchant API v1 | — | SDK / Reference | — | OAuth 2.0 | A+ · Official Reference |
| [**google/merchant-api-samples**](#google--merchant-api-samples) | ★ 31 | Python | Merchant API v1 | 2 | Read-Only | — | Service Account | A+ · Official Reference |
| [**googleads/googleads-shopping-samples**](#googleads--googleads-shopping-samples) | ★ 207 | Java | Content API v2.1 | — | SDK / Reference | — | OAuth 2.0 | A+ · Official Reference |
| [**haerriz/magento2-google-shopping-feed**](#haerriz--magento2-google-shopping-feed) | ★ 1 | PHP / Magento 2 | Merchant API v1 | 7 | CLI / Generator | — | Service Account | B · Community Stable |
| [**ihint/merchant-context**](#ihint--merchant-context) | ★ 0 | TypeScript | UCP / ACP | 9 | Read-Write | — | Config / Env | A+ · Production-Ready |
| [**itallstartedwithaidea/advertising-hub**](#itallstartedwithaidea--advertising-hub) | ★ 42 | Python | Merchant API v1 | 6 | Read-Write | — | Config / Env | B · Community Stable |
| [**kLOsk/adloop**](#kLOsk--adloop) | ★ 266 | Python | Merchant API v1 | 84 | Hybrid | ✅ Dry-Run · Rollback | OAuth 2.0 | A · Production-Ready |
| [**kiwoongeom/gmc-mcp**](#kiwoongeom--gmc-mcp) | ★ 15 | Python | Merchant API v1 | 126 | Read-Write | ✅ Dry-Run | OAuth 2.0 | A · Production-Ready |
| [**markifact/markifact-mcp**](#markifact--markifact-mcp) | ★ 48 | TypeScript | Merchant API v1 | 8 | Read-Write | — | OAuth 2.1 PKCE | B · Community Stable |
| [**marwa-mrwan/google-clarity-mcp-codex**](#marwa-mrwan--google-clarity-mcp-codex) | ★ 0 | JavaScript | Merchant API v1 | 213 | Read-Only | — | OAuth 2.0 | A · Production-Ready |
| [**msalihk/catalog-mcp**](#msalihk--catalog-mcp) | ★ 0 | TypeScript | Shopify Storefront R | 3 | Read-Only | — | Config / Env | A · Production-Ready |
| [**prajapatimehul/shopify-cowork**](#prajapatimehul--shopify-cowork) | ★ 15 | Python | Shopify Admin GraphQL | 7 | Read-Write | — | Bearer Token | A · Production-Ready |
| [**roblouw2nd/fetchgate**](#roblouw2nd--fetchgate) | ★ 1 | Python | Cloudflare Edge Proxy | 4 | Read-Only | ✅ Sandbox / Gate | Config / Env | B+ · Community Stable |
| [**rushikeshmore/shopify-partner-agent**](#rushikeshmore--shopify-partner-agent) | ★ 13 | Python | Merchant API v1 | 6 | Read-Only | — | Config / Env | B · Community Stable |
| [**simpleproductfeeds/skills**](#simpleproductfeeds--skills) | ★ 0 | Config / Spec | Content API v2.1 | 16 | Read-Write | ✅ Dry-Run | OAuth 2.0 | A · Production-Ready |
| [**umeshravani/spree_google_products**](#umeshravani--spree_google_products) | ★ 4 | Ruby / Rails | Content API v2.1 | — | CLI / Generator | — | OAuth 2.0 | A- · Community Stable |
| [**webloom-agency/merchant-center-mcp**](#webloom-agency--merchant-center-mcp) | ★ 0 | Python | Merchant API v1 | 25 | Read-Write | ✅ Dry-Run · Rollback | OAuth 2.1 PKCE | A · Production-Ready |

---

## 1. Manage products, inventories, and catalog data sources

*13 projects. Core Model Context Protocol servers and developer SDKs connecting directly to Google Merchant API v1 and legacy Content API for Shopping endpoints for product ingestion, inventory synchronization, and batch updates.*

### Direct Google Merchant API v1 servers

*4 projects. Dedicated, specification-compliant Model Context Protocol servers implementing the modern Merchant API v1 surface.*

| Project | What it does |
|---|---|
| <a id="webloom-agency--merchant-center-mcp"></a>[**webloom-agency/merchant-center-mcp**](https://github.com/webloom-agency/merchant-center-mcp) | Provides a production-ready Python Model Context Protocol server exposing Google Merchant API v1 endpoints with multi-tenant OAuth 2.1 authentication and automated token refresh. Features 25 granular tools for catalog introspection, inventory synchronization, and batch updates for autonomous shopping agents. |
| <a id="kiwoongeom--gmc-mcp"></a>[**kiwoongeom/gmc-mcp**](https://github.com/kiwoongeom/gmc-mcp) | Exposes 126 granular endpoints across Google Merchant API v1 sub-APIs (Products, Accounts, Inventories, Promotions, Data Sources) in a typed Python architecture. Includes automated OAuth 2.0 PKCE token management, rate limit backoff, and end-to-end catalog inspection. |
| <a id="A1-x-Tech--mcp-google-merchants"></a>[**A1-x-Tech/mcp-google-merchants**](https://github.com/A1-x-Tech/mcp-google-merchants) | Implements a TypeScript Model Context Protocol server wrapping Google Merchant API v1 with Zod schema validation and StdioServerTransport. Provides 28 structured tools for querying account data sources, inspecting product statuses, and retrieving regional availability. |
| <a id="gioenjoy--mcp-google-merchant-center"></a>[**gioenjoy/mcp-google-merchant-center**](https://github.com/gioenjoy/mcp-google-merchant-center) | Connects AI assistants directly to Google Merchant Center via Application Default Credentials (ADC) and Google Cloud service account keys. Offers 6 core tools for product catalog listings, approval status diagnostics, and feed health telemetry. |

### Official and reference developer SDKs

*3 projects. Google's official polyglot SDKs, reference sample implementations, and developer assistant tooling.*

| Project | What it does |
|---|---|
| <a id="google--merchant-api-samples"></a>[**google/merchant-api-samples**](https://github.com/google/merchant-api-samples) | Serves as Google's official polyglot reference repository containing production samples and the Merchant API Devdocs MCP integration. Enables coding agents to query upstream Merchant API v1 specifications, data source schemas, and migration guides in real time. |
| <a id="google--merchant-api-alpha-client"></a>[**google/merchant-api-alpha-client**](https://github.com/google/merchant-api-alpha-client) | Distributes Google's official low-level multi-language client libraries for the Google Merchant API v1alpha. Provides native gRPC and REST bindings across Go, Python, TypeScript, Java, and C# for experimental Merchant API features. |
| <a id="googleads--googleads-shopping-samples"></a>[**googleads/googleads-shopping-samples**](https://github.com/googleads/googleads-shopping-samples) | Google's authoritative reference implementation for the legacy Content API for Shopping v2.1. Demonstrates batch catalog ingestion, Multi-Client Account (MCA) provisioning, and supplemental feed management across enterprise architectures. |

### Consolidated catalog management gateways

*6 projects. Multi-purpose marketing and advertising servers bundling Google Merchant Center catalog management with campaign operations.*

| Project | What it does |
|---|---|
| <a id="akelaonline--MCP-Google-Ads"></a>[**akelaonline/MCP-Google-Ads**](https://github.com/akelaonline/MCP-Google-Ads) | Provides an expansive Python MCP server featuring 461 tools spanning Google Merchant API v1, Shopping performance, and feed management. Features dual Service Account and OAuth authentication with integrated diagnostic reporting and campaign-feed alignment. |
| <a id="christyandas--google-ads-brasil"></a>[**christyandas/google-ads-brasil**](https://github.com/christyandas/google-ads-brasil) | Offers a pre-configured Node.js marketing and shopping automation server with 126 tools tailored for Brazilian retail operations. Wraps Merchant API v1 product pipelines and regional pricing overrides with automated currency and tax normalization. |
| <a id="marwa-mrwan--google-clarity-mcp-codex"></a>[**marwa-mrwan/google-clarity-mcp-codex**](https://github.com/marwa-mrwan/google-clarity-mcp-codex) | Integrates 213 cross-functional tools combining Microsoft Clarity user analytics with Google Merchant API v1 product data feeds. Correlates shopping feed disapprovals and product bounce rates with on-page user session recordings. |
| <a id="Nas198222--google-mcp-bridge"></a>[**Nas198222/google-mcp-bridge**](https://github.com/Nas198222/google-mcp-bridge) | Bridges Google Workspace, Cloud, and Merchant API v1 services into a single unified TypeScript Model Context Protocol server. Provides 17 callable tools for querying product catalogs, inspecting quota utilization, and validating cloud service accounts. |
| <a id="HYPD-AI--ads-mcp-plugin"></a>[**HYPD-AI/ads-mcp-plugin**](https://github.com/HYPD-AI/ads-mcp-plugin) | Delivers a lightweight 5-tool MCP plugin that coordinates Google Merchant Center product catalogs with automated shopping ads. Supports dynamic catalog synchronization and real-time inventory updates over standard MCP stdio transport. |
| <a id="aakashraj7--vocalize"></a>[**aakashraj7/vocalize**](https://github.com/aakashraj7/vocalize) | Enables voice-driven catalog management and product feed status lookups via Google Merchant API v1. Transforms natural language voice commands into structured MCP tool calls for hands-free merchant administration. |

---

## 2. Diagnose disapprovals, policy violations, and feed health

*9 projects. Diagnostic monitors, offline feed validation linters, disapproval issue mitigators, and competitive search scraping engines for maintaining catalog integrity.*

### gRPC and REST diagnostic monitors

*3 projects. High-throughput diagnostic servers inspecting item-level policy violations and feed processing errors.*

| Project | What it does |
|---|---|
| <a id="YerayRodri--merchant-center-mcp"></a>[**YerayRodri/merchant-center-mcp**](https://github.com/YerayRodri/merchant-center-mcp) | Implements a focused Python MCP server delivering high-performance Google Merchant API v1 diagnostics over gRPC. Specializes in real-time disapproval detection, account-level issue inspection, and item-level policy violation breakdowns. |
| <a id="GajewskiMarcin--FeedForge"></a>[**GajewskiMarcin/FeedForge**](https://github.com/GajewskiMarcin/FeedForge) | Validates and transforms product data feeds prior to Google Merchant Center ingestion via a streamlined CLI and MCP toolchain. Performs offline GS1 GTIN Mod-10 checksum validation, schema linting, and TSV/XML formatting to prevent feed rejection. |
| <a id="BurhanBeigh--merchant-feed-builder"></a>[**BurhanBeigh/merchant-feed-builder**](https://github.com/BurhanBeigh/merchant-feed-builder) | Constructs schema-compliant Google Shopping XML and CSV feeds from arbitrary e-commerce database dumps. Ensures complete field mapping for required merchant attributes, tax codes, and shipping dimensions. |

### Disapproval and policy resolution engines

*3 projects. Automated remediation engines and platform feed generators addressing merchant account disapprovals.*

| Project | What it does |
|---|---|
| <a id="simpleproductfeeds--skills"></a>[**simpleproductfeeds/skills**](https://github.com/simpleproductfeeds/skills) | Packages 16 enterprise agent skills connecting AI assistants to cloud feed management platforms and Google Merchant API v1. Automates supplemental feed generation, automated product rule enforcement, and disapproval remediation workflows. |
| <a id="haerriz--magento2-google-shopping-feed"></a>[**haerriz/magento2-google-shopping-feed**](https://github.com/haerriz/magento2-google-shopping-feed) | Generates optimized Google Shopping feeds directly from Adobe Commerce and Magento 2 enterprise catalog databases. Includes automated feed scheduling, multi-currency support, and batch XML generation for high-volume catalogs. |
| <a id="umeshravani--spree_google_products"></a>[**umeshravani/spree_google_products**](https://github.com/umeshravani/spree_google_products) | Integrates Spree Commerce storefronts with Google Merchant Center using automated feed generation and Content API sync. Maintains continuous synchronization between active Ruby on Rails inventory levels and Google Shopping listings. |

### Search intelligence and competitive price scraping

*3 projects. Specialized scrapers and SERP APIs capturing live Google Shopping competitor pricing, rankings, and stock levels.*

| Project | What it does |
|---|---|
| <a id="ShoppingResult--shoppingscraper-cli"></a>[**ShoppingResult/shoppingscraper-cli**](https://github.com/ShoppingResult/shoppingscraper-cli) | Extracts competitive pricing intelligence and Google Shopping SERP listings via 18 specialized CLI and MCP commands. Enables pricing elasticity analysis and automated price monitoring against competing merchant listings. |
| <a id="GreXLin85--serper.dev-mcp"></a>[**GreXLin85/serper.dev-mcp**](https://github.com/GreXLin85/serper.dev-mcp) | Delivers real-time Google Shopping search results, product prices, ratings, and merchant positions via the Serper API. Provides AI agents with 12 tools for comparative market research and Google Shopping visibility auditing. |
| <a id="alessandrobenigni--ScrapingDog-MCP"></a>[**alessandrobenigni/ScrapingDog-MCP**](https://github.com/alessandrobenigni/ScrapingDog-MCP) | Provides 77 web scraping and search tools including dedicated Google Shopping SERP extraction endpoints. Bypasses bot detection barriers to deliver live merchant pricing data and competitor catalog structures. |

---

## 3. Persist and analyze performance with MCQL and SQL

*9 projects. Marketing data warehouses, local embedded databases, and analytical skill packs querying merchant performance using MCQL and SQL.*

### Embedded database and local cache engines

*3 projects. Platforms synchronizing merchant catalogs into embedded relational databases for high-speed local SQL joins.*

| Project | What it does |
|---|---|
| <a id="kLOsk--adloop"></a>[**kLOsk/adloop**](https://github.com/kLOsk/adloop) | Provides a mature Python marketing orchestration engine with 84 tools for syncing Google Merchant Center catalogs into an embedded relational database. Enables complex SQL joins between product inventory states, Google Shopping ad spend, and multi-channel attribution. |
| <a id="MadMaxen92--marketing-mcp"></a>[**MadMaxen92/marketing-mcp**](https://github.com/MadMaxen92/marketing-mcp) | Exposes 56 comprehensive marketing tools connecting Google Merchant API v1, Google Ads, and Meta Ads. Features local state persistence, cross-network catalog performance tracking, and automated ROAS calculations. |
| <a id="agidesigner--OpenLucid"></a>[**agidesigner/OpenLucid**](https://github.com/agidesigner/OpenLucid) | Implements a multi-agent marketing world model with 50 tools for catalog diagnostics and campaign strategy optimization. Maintains an internal state graph to analyze merchant SKU sales velocity and historical margin performance. |

### E-commerce intelligence and partner analytics

*3 projects. Specialized analytical toolkits surfacing SKU sales velocity, variant hierarchies, and catalog sync anomalies.*

| Project | What it does |
|---|---|
| <a id="rushikeshmore--shopify-partner-agent"></a>[**rushikeshmore/shopify-partner-agent**](https://github.com/rushikeshmore/shopify-partner-agent) | Analyzes merchant store telemetry and Google Merchant Center catalog health for Shopify Plus agency partners. Combines 6 analytical tools to surface inventory turnover trends, catalog sync anomalies, and partner revenue metrics. |
| <a id="msalihk--catalog-mcp"></a>[**msalihk/catalog-mcp**](https://github.com/msalihk/catalog-mcp) | Inspects e-commerce product catalogs and diagnostic feeds using 3 lightweight TypeScript MCP tools. Extracts variant-level pricing hierarchies, inventory counts, and image assets for instant agent analysis. |
| <a id="davillafer--mcp-merchant-scout"></a>[**davillafer/mcp-merchant-scout**](https://github.com/davillafer/mcp-merchant-scout) | Performs automated merchant catalog discovery and price comparison across Universal Commerce Protocol (UCP) endpoints. Uses 4 search tools to index merchant nodes, query live product feeds, and evaluate category pricing parity. |

### Marketing orchestration and report generators

*3 projects. Cross-platform orchestration tools synthesizing Merchant Center feeds into automated ad copy and performance summaries.*

| Project | What it does |
|---|---|
| <a id="itallstartedwithaidea--advertising-hub"></a>[**itallstartedwithaidea/advertising-hub**](https://github.com/itallstartedwithaidea/advertising-hub) | Consolidates advertising and catalog operations across Google Merchant Center, Meta, and TikTok into 6 multi-platform tools. Generates cross-platform catalog performance reports and flags out-of-sync product feeds. |
| <a id="markifact--markifact-mcp"></a>[**markifact/markifact-mcp**](https://github.com/markifact/markifact-mcp) | Supplies 8 automated tools for generating dynamic marketing copy and promotional creatives from Google Merchant Center feeds. Extracts real-time product features, prices, and availability to synthesize ad headlines and social posts. |
| <a id="almoretti--martech-ai-skills-and-tools"></a>[**almoretti/martech-ai-skills-and-tools**](https://github.com/almoretti/martech-ai-skills-and-tools) | Delivers 39 developer skills and CLI tools implementing the complete modern Google Merchant API v1 specification. Features automated OAuth 2.0 PKCE authentication, MCQL query execution, and structured JSON output for AI agents. |

---

## 4. Enforce operational safety, dry-runs, and mutation rollback

*2 projects. Operational guardrails, transactional dry-run validators, edge proxies, and spend authorization layers protecting live merchant catalogs.*

### Transactional edge proxies and protocol sandboxes

*2 projects. Validation layers, rate-limiting proxies, and protocol testbeds verifying catalog interactions prior to execution.*

| Project | What it does |
|---|---|
| <a id="roblouw2nd--fetchgate"></a>[**roblouw2nd/fetchgate**](https://github.com/roblouw2nd/fetchgate) | Acts as a secure Edge-deployed proxy on Cloudflare Workers for scraping and sanitizing merchant product data feeds. Applies rate-limiting, egress caching, and structural schema validation to protect origin merchant endpoints. |
| <a id="flovoice53-tech--acp-sandbox"></a>[**flovoice53-tech/acp-sandbox**](https://github.com/flovoice53-tech/acp-sandbox) | Provides an isolated protocol testbed for the Agentic Commerce Protocol (ACP) and Universal Commerce Protocol (UCP). Allows developers to test autonomous product selection, checkout handoffs, and catalog queries in a sandboxed runtime. |

---

## 5. Manage multi-tenant access and Multi-Client Account (MCA) routing

*3 projects. Multi-tenant authentication proxies, agency sub-account routers, and session persistence frameworks managing Multi-Client Account (MCA) structures.*

### Multi-tenant OAuth gateways and sub-account routers

*2 projects. Enterprise gateways isolating credentials, managing client sub-accounts, and aggregating merchant financial telemetry.*

| Project | What it does |
|---|---|
| <a id="api-evangelist--agenthaven-dev"></a>[**api-evangelist/agenthaven-dev**](https://github.com/api-evangelist/agenthaven-dev) | Architects an enterprise catalog governance gateway supporting Multi-Client Account (MCA) delegation and sub-account routing. Enforces strict multi-tenant tenant isolation and scoped OAuth 2.1 access control across agency client portfolios. |
| <a id="PaidSync--paidsync-mcp"></a>[**PaidSync/paidsync-mcp**](https://github.com/PaidSync/paidsync-mcp) | Provides a multi-tenant payment and billing MCP server connecting Google Merchant Center accounts with Stripe and custom billing rails. Manages subscription tiers, automated merchant invoice generation, and account-level settlement. |

### Context persistence and account scoping protocols

*1 project. Session context servers maintaining active account state across complex merchant hierarchies.*

| Project | What it does |
|---|---|
| <a id="ihint--merchant-context"></a>[**ihint/merchant-context**](https://github.com/ihint/merchant-context) | Maintains persistent session context and organizational scope across complex Multi-Client Account (MCA) hierarchies. Provides 9 tools for caching merchant account metadata, current sub-account selection, and user permissions. |

---

## 6. Bridge e-commerce storefronts and multi-channel catalogs

*2 projects. Bidirectional connectors syncing e-commerce platforms (Shopify, Shopware) with Google Merchant Center feeds.*

### Storefront catalog synchronization bridges

*2 projects. Bridges connecting Shopify and Shopware store inventories, product variants, and admin endpoints to Merchant Center pipelines.*

| Project | What it does |
|---|---|
| <a id="prajapatimehul--shopify-cowork"></a>[**prajapatimehul/shopify-cowork**](https://github.com/prajapatimehul/shopify-cowork) | Coordinates catalog synchronization between Shopify Admin GraphQL endpoints and Google Merchant Center feeds via 7 agent tools. Automates product attribute mapping, inventory synchronization, and collection-level feed segregation. |
| <a id="agentic-commerce-lab--shopware-claude-commerce"></a>[**agentic-commerce-lab/shopware-claude-commerce**](https://github.com/agentic-commerce-lab/shopware-claude-commerce) | Implements a comprehensive 34-tool commerce bridge connecting Shopware 6.7 Admin API with Google Shopping and Claude. Enables bidirectional catalog updates, order tracking, customer management, and automated Google Shopping XML export. |

---

## 7. Deploy autonomous agentic commerce, ACP/UCP, and machine settlement

*2 projects. Protocols and reference stacks for the Universal Commerce Protocol (UCP) and Agentic Commerce Protocol (ACP).*

### Universal Commerce Protocol (UCP) onboarding and reference stacks

*2 projects. Official blueprints and onboarding agents for Google's Universal Commerce Protocol.*

| Project | What it does |
|---|---|
| <a id="ViryaZheng--ucp-onboard"></a>[**ViryaZheng/ucp-onboard**](https://github.com/ViryaZheng/ucp-onboard) | Automates merchant onboarding and catalog registration for Google's Universal Commerce Protocol (UCP). Configures agent capabilities, validates merchant endpoint discovery manifests, and verifies UCP catalog compliance. |
| <a id="NVIDIA-AI-Blueprints--Retail-Agentic-Commerce"></a>[**NVIDIA-AI-Blueprints/Retail-Agentic-Commerce**](https://github.com/NVIDIA-AI-Blueprints/Retail-Agentic-Commerce) | NVIDIA's flagship enterprise reference blueprint for agentic commerce, implementing the Universal Commerce Protocol (UCP). Combines multimodal product search, real-time inventory checking, and secure agent-to-agent checkout protocols. |

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

Google is migrating merchant infrastructure from the monolithic **Content API for Shopping v2.1** to the modular **Google Merchant API v1**:

| Architectural Dimension | Legacy Content API for Shopping v2.1 | Modern Google Merchant API v1 |
|---|---|---|
| **API Structure** | Monolithic single-service REST endpoint | Modular sub-APIs (`products_v1`, `accounts_v1`, `datasources_v1`, `inventories_v1`, `promotions_v1`) |
| **Transport Protocol** | REST / JSON-RPC over HTTP/1.1 | Native gRPC over HTTP/2 with high-performance protobuf serialization + REST fallback |
| **Data Ingestion** | Monolithic batch feeds with high latency | Real-time incremental sub-feeds and primary/supplemental data sources |
| **Query Engine** | Rigid parameter-based list queries | Flexible Merchant Center Query Language (MCQL) with SQL-like syntax and field projections |
| **Authentication** | Basic Service Account JSON or OAuth 2.0 | OAuth 2.1 PKCE with scoped fine-grained IAM roles and Multi-Client Account (MCA) delegation |

### Evaluation Methodology and Verification Invariants

All 40 repositories listed in this catalog were evaluated against rigorous engineering standards:

1. **AST & Code Inspection:** Every tool was audited at the source-code level to verify callable tool counts, Zod/Pydantic input schemas, error handling, and target API alignment.
2. **Commit Recency Invariant:** Every repository has verified commit activity within the preceding 6 months (on or after March 21, 2026).
3. **Developer Provenance & Anti-Slop Audit:** Maintainer GitHub profiles were audited to separate sustained human engineering from disposable single-commit synthetic boilerplate.
4. **Operational Safety Audit:** Tools modifying live merchant inventories were evaluated for dry-run validation modes, spending guardrails, and audit rollback ledgers.

### Repository Inclusion and Anti-Slop Policy

This repository enforces strict inclusion boundaries to protect developers from unmaintained code, AI hallucination, and off-scope dilution:

- **Included:** Production-grade MCP servers, official Google developer SDKs, verified shopping automation scripts, and documented agentic commerce protocols interfacing with Google Merchant Center.
- **Quarantined & Excluded:** 33 non-qualifying repositories (16 synthetic bot farm repositories discovered during initial discovery plus 17 off-scope, off-platform, or malicious clones pruned during editorial review) are quarantined to maintain catalog purity.
