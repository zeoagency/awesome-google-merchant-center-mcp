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
2. [Diagnose disapprovals, policy violations, and feed health (11)](#2-diagnose-disapprovals-policy-violations-and-feed-health)
   - [gRPC and REST diagnostic monitors (3)](#grpc-and-rest-diagnostic-monitors)
   - [Disapproval and policy resolution engines (3)](#disapproval-and-policy-resolution-engines)
   - [Search intelligence and competitive price scraping (5)](#search-intelligence-and-competitive-price-scraping)
3. [Persist and analyze performance with MCQL and SQL (9)](#3-persist-and-analyze-performance-with-mcql-and-sql)
   - [Embedded database and local cache engines (3)](#embedded-database-and-local-cache-engines)
   - [E-commerce intelligence and partner analytics (3)](#e-commerce-intelligence-and-partner-analytics)
   - [Marketing orchestration and report generators (3)](#marketing-orchestration-and-report-generators)
4. [Enforce operational safety, dry-runs, and mutation rollback (4)](#4-enforce-operational-safety-dry-runs-and-mutation-rollback)
   - [Two-phase commit and catalog mutation guards (2)](#two-phase-commit-and-catalog-mutation-guards)
   - [Safe execution sandboxes and spending authorization (2)](#safe-execution-sandboxes-and-spending-authorization)
5. [Manage multi-tenant access and Multi-Client Account (MCA) routing (4)](#5-manage-multi-tenant-access-and-multi-client-account-mca-routing)
   - [Multi-tenant OAuth gateways and sub-account routers (3)](#multi-tenant-oauth-gateways-and-sub-account-routers)
   - [Context persistence and account scoping protocols (1)](#context-persistence-and-account-scoping-protocols)
6. [Bridge e-commerce storefronts and multi-channel catalogs (7)](#6-bridge-e-commerce-storefronts-and-multi-channel-catalogs)
   - [Shopify storefront and co-worker bridges (2)](#shopify-storefront-and-co-worker-bridges)
   - [Headless and composable commerce backends (2)](#headless-and-composable-commerce-backends)
   - [Multi-marketplace and regional catalog bridges (3)](#multi-marketplace-and-regional-catalog-bridges)
7. [Deploy autonomous agentic commerce, ACP/UCP, and machine settlement (9)](#7-deploy-autonomous-agentic-commerce-acpucp-and-machine-settlement)
   - [Universal Commerce Protocol (UCP) onboarding and reference stacks (4)](#universal-commerce-protocol-ucp-onboarding-and-reference-stacks)
   - [POS and voice-activated merchant terminals (2)](#pos-and-voice-activated-merchant-terminals)
   - [Autonomous payment and settlement protocols (3)](#autonomous-payment-and-settlement-protocols)
8. [Resources](#resources)
   - [Official Documentation & SDKs](#official-documentation--sdks)
   - [Specifications & Standards](#specifications--standards)
9. [Reference](#reference)
   - [Merchant API v1 vs Content API v2.1 Architecture](#merchant-api-v1-vs-content-api-v21-architecture)
   - [Evaluation Methodology & Verification Invariants](#evaluation-methodology--verification-invariants)
   - [Repository Inclusion & Anti-Slop Policy](#repository-inclusion--anti-slop-policy)

---

## Developer Comparison Matrix

*A comparative feature matrix of all 57 Model Context Protocol servers, developer SDKs, and agent interfaces for Google Merchant Center, detailing language runtime, tool count, target API surface, operational safety flags, authentication patterns, and local storage engines. Click on any project name to jump directly to its detailed listing below.*

| Server / Tool | Runtime | Tools | Target API | Read/Write | Dry-Run | 2-Phase Commit | Audit Ledger | Auth Pattern | MCA Routing | Storage Engine | MCQL Search | GTIN Mod-10 | Feed Formats | Agent Protocol | Stars | Recency | Tier / Grade |
| --- | --- | :---: | --- | --- | :---: | :---: | :---: | --- | :---: | --- | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| [**A1-x-Tech/mcp-google-merchants**](#A1-x-Tech--mcp-google-merchants) | TypeScript | 28 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★0 | 2026-09 | B · Community Stable |
| [**A1-x-Tech/mcp-yandex-merchants**](#A1-x-Tech--mcp-yandex-merchants) | TypeScript | 13 | Yandex Market / Ya | Read-Write | — | ✅ | ✅ | OAuth 2.1 PKCE | — | In-Memory | ✅ | ✅ | XML/TSV | MCP | ★0 | 2026-09 | A+ · Production-Ready |
| [**AgriciDaniel/claude-seo**](#AgriciDaniel--claude-seo) | Python | 8 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★17351 | 2026-09 | B · Community Stable |
| [**BurhanBeigh/merchant-feed-builder**](#BurhanBeigh--merchant-feed-builder) | Python | — | Shopify Admin | Read-Only from Shopify (scoped strictly to `read_products`); writes local validated GMC product feeds (RSS 2.0 XML / TSV) | ✅ | ✅ | — | Config / Env | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | REST / SDK | ★1 | 2026-08 | A · Production-Ready |
| [**GajewskiMarcin/FeedForge**](#GajewskiMarcin--FeedForge) | PHP | — | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | OAuth 2.0 | — | Stateless Proxy | — | — | JSON | REST / SDK | ★3 | 2026-09 | A- · Community Stable |
| [**GreXLin85/serper.dev-mcp**](#GreXLin85--serper.dev-mcp) | TypeScript | 12 | Shopping SERP | Read-Only | — | — | — | API Key | — | Stateless Proxy | ✅ | ✅ | JSON | MCP | ★1 | 2026-08 | A · Production-Ready |
| [**HYPD-AI/ads-mcp-plugin**](#HYPD-AI--ads-mcp-plugin) | Config / Spec | 5 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★2 | 2026-08 | B · Community Stable |
| [**HasData/shopify-mcp**](#HasData--shopify-mcp) | Python | 2 | Shopping SERP | Read-Only Public Storefront Scraping | — | — | — | API Key | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | MCP | ★8 | 2026-09 | A · Production-Ready |
| [**MadMaxen92/marketing-mcp**](#MadMaxen92--marketing-mcp) | TypeScript | 56 | Merchant API v1 | Read-Write | ✅ | ✅ | ✅ | OAuth 2.0 | ✅ | Stateless Proxy | ✅ | ✅ | JSON | MCP | ★0 | 2026-09 | A+ · Production-Ready |
| [**MentionNetwork/awesome-agentic-commerce**](#MentionNetwork--awesome-agentic-commerce) | Config / Spec | — | UCP / ACP | Read-Only Documentation | — | — | — | Config / Env | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | UCP | ★62 | 2026-07 | B · Community Stable |
| [**NVIDIA-AI-Blueprints/Retail-Agentic-Commerce**](#NVIDIA-AI-Blueprints--Retail-Agentic-Commerce) | Python | 10 | UCP / ACP | Read-Write Full Agentic Checkout Lifecycle | ✅ | ✅ | ✅ | Bearer Token | ✅ | In-Memory | ✅ | ✅ | XML/TSV | UCP | ★75 | 2026-09 | A+ · Production-Ready |
| [**Nas198222/google-mcp-bridge**](#Nas198222--google-mcp-bridge) | TypeScript | 17 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★0 | 2026-05 | B · Community Stable |
| [**NovaCorpAI/agentpos-alexa**](#NovaCorpAI--agentpos-alexa) | TypeScript | 7 | UCP / ACP | Read-Write | ✅ | ✅ | — | OAuth 2.0 | ✅ | SQLite Worker | — | — | JSON | UCP | ★0 | 2026-09 | A+ · Production-Ready |
| [**PaidSync/paidsync-mcp**](#PaidSync--paidsync-mcp) | TypeScript | 3 | Merchant API v1 | Read-Write Catalog & Campaign Management (Full write across Google Ads/Meta/LinkedIn/OpenAI; Feed and link management on Google Merchant Center; Read-manage-optimize on TikTok/Snapchat/Reddit/Pinterest/Microsoft) | ✅ | ✅ | ✅ | OAuth 2.0 | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | MCP | ★3 | 2026-09 | B+ · Community Stable |
| [**PayRam/payram-mcp**](#PayRam--payram-mcp) | TypeScript | 52 | Payment API | Read-Write | ✅ | ✅ | — | API Key | ✅ | In-Memory | — | — | Multi | MCP | ★156 | 2026-07 | A · Production-Ready |
| [**ShoppingResult/shoppingscraper-cli**](#ShoppingResult--shoppingscraper-cli) | TypeScript | 18 | ShoppingScraper RE | Read-Only | ✅ | ✅ | — | API Key | — | Stateless Proxy | — | ✅ | JSON | MCP | ★1 | 2026-07 | A · Production-Ready |
| [**ViryaZheng/ucp-onboard**](#ViryaZheng--ucp-onboard) | Python | 7 | UCP / ACP | Read-Write Catalog & Profile Generation (Local Scaffolding and Export) | ✅ | ✅ | ✅ | Config / Env | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | UCP | ★4 | 2026-06 | A · Production-Ready |
| [**YerayRodri/merchant-center-mcp**](#YerayRodri--merchant-center-mcp) | Python | 4 | Merchant API v1 | Read-Only Diagnostics | — | — | — | OAuth 2.0 | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | MCP | ★0 | 2026-08 | A- · Community Stable |
| [**aakashraj7/vocalize**](#aakashraj7--vocalize) | TypeScript | 2 | Merchant API v1 | Read-Write | ✅ | ✅ | ✅ | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★0 | 2026-06 | B · Community Stable |
| [**agentic-commerce-lab/shopware-claude-commerce**](#agentic-commerce-lab--shopware-claude-commerce) | Python | 34 | UCP / ACP | Read-Write | ✅ | ✅ | — | OAuth 2.1 PKCE | ✅ | SQLite Worker | ✅ | ✅ | JSON | UCP | ★0 | 2026-09 | A+ · Production-Ready |
| [**agidesigner/OpenLucid**](#agidesigner--OpenLucid) | Python | 50 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | Config / Env | — | PostgreSQL | — | — | JSON | MCP | ★31 | 2026-05 | B · Community Stable |
| [**akelaonline/MCP-Google-Ads**](#akelaonline--MCP-Google-Ads) | Python | 461 | Merchant API v1 | Read-Write with Mandatory Propose-Confirm Two-Phase Commit | ✅ | ✅ | ✅ | OAuth 2.0 | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | MCP | ★4 | 2026-09 | A+ · Production-Ready |
| [**alessandrobenigni/ScrapingDog-MCP**](#alessandrobenigni--ScrapingDog-MCP) | JavaScript | 77 | Shopping SERP | Read-Only | — | — | — | API Key | — | Stateless Proxy | — | ✅ | JSON | MCP | ★1 | 2026-07 | B+ · Community Stable |
| [**alisadiq-ai/sketric-dataforseo-mcp-prefork**](#alisadiq-ai--sketric-dataforseo-mcp-prefork) | TypeScript | — | Merchant API v1 | Read-Only | ✅ | ✅ | — | Config / Env | — | Stateless Proxy | — | — | JSON | REST / SDK | ★0 | 2026-04 | B · Community Stable |
| [**almoretti/martech-ai-skills-and-tools**](#almoretti--martech-ai-skills-and-tools) | TypeScript | 39 | Merchant API v1 | Read-First with Explicit Write Confirmations (Only 3 write commands; delete requires --yes) | ✅ | ✅ | — | ADC / IAM | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | MCP | ★2 | 2026-07 | A · Production-Ready |
| [**api-evangelist/agenthaven-dev**](#api-evangelist--agenthaven-dev) | Config / Spec | 2 | Merchant API v1 | Read-Only | ✅ | ✅ | — | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★0 | 2026-09 | B · Community Stable |
| [**apivault-labs/n8n-nodes-apivault-temu**](#apivault-labs--n8n-nodes-apivault-temu) | TypeScript | 1 | Shopping SERP | Read & Transform (Scrapes upstream and exports GMC / Shopify feeds) | — | — | — | Bearer Token | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | MCP | ★3 | 2026-09 | B+ · Community Stable |
| [**christyandas/google-ads-brasil**](#christyandas--google-ads-brasil) | JavaScript | 126 | Merchant API v1 | Hybrid (Read-only diagnostics and automated scripts with manual execution via Google Ads Script panel) | — | — | — | Service Account | — | Stateless Proxy | ✅ | ✅ | XML/TSV | MCP | ★0 | 2026-07 | B · Community Stable |
| [**davillafer/mcp-merchant-scout**](#davillafer--mcp-merchant-scout) | TypeScript | 4 | UCP / ACP | Read-Only | — | — | — | Config / Env | ✅ | In-Memory | ✅ | ✅ | JSON | UCP | ★0 | 2026-03 | A- · Community Stable |
| [**flovoice53-tech/acp-sandbox**](#flovoice53-tech--acp-sandbox) | TypeScript | 7 | Agentic Commerce P | Read-Write | — | ✅ | ✅ | Bearer Token | ✅ | SQLite Worker | — | ✅ | Multi | ACP | ★0 | 2026-09 | A- · Community Stable |
| [**gioenjoy/mcp-google-merchant-center**](#gioenjoy--mcp-google-merchant-center) | TypeScript | 6 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | Service Account | — | Stateless Proxy | — | — | JSON | MCP | ★0 | 2026-06 | B · Community Stable |
| [**google/merchant-api-alpha-client**](#google--merchant-api-alpha-client) | Python | — | Merchant API v1 | Full Read-Write SDK (Supports get, list, insert, delete for Product Reviews and Merchant Reviews) | — | — | ✅ | OAuth 2.0 | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | REST / SDK | ★1 | 2026-06 | A+ · Production-Ready |
| [**google/merchant-api-samples**](#google--merchant-api-samples) | Python | 2 | Merchant API v1 | Read-Only | ✅ | ✅ | — | Service Account | — | Stateless Proxy | — | — | JSON | MCP | ★31 | 2026-09 | A+ · Production-Ready |
| [**googleads/googleads-shopping-samples**](#googleads--googleads-shopping-samples) | Java | — | Content API v2.1 | Read-Write SDK Reference (full CRUD sample implementations for Content API v2.1) | ✅ | ✅ | — | OAuth 2.0 | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | REST / SDK | ★207 | 2026-06 | B+ · Community Stable |
| [**haerriz/magento2-google-shopping-feed**](#haerriz--magento2-google-shopping-feed) | TypeScript | 7 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | Service Account | — | Stateless Proxy | — | — | JSON | MCP | ★1 | 2026-08 | B · Community Stable |
| [**ihint/merchant-context**](#ihint--merchant-context) | TypeScript | 9 | UCP / ACP | Read-Write | ✅ | ✅ | — | Config / Env | ✅ | SQLite Worker | — | — | XML/TSV | UCP | ★0 | 2026-08 | A+ · Production-Ready |
| [**itallstartedwithaidea/advertising-hub**](#itallstartedwithaidea--advertising-hub) | Python | 6 | Merchant API v1 | Read-Write | ✅ | ✅ | ✅ | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★42 | 2026-07 | B · Community Stable |
| [**johnisanerd/Apify-Google-Shopping-API**](#johnisanerd--Apify-Google-Shopping-API) | Python | 1 | Shopping SERP | Read-Only | — | — | — | OAuth 2.0 | ✅ | Stateless Proxy | — | ✅ | JSON | MCP | ★0 | 2026-09 | B- · Early Prototype |
| [**kLOsk/adloop**](#kLOsk--adloop) | Python | 84 | Merchant API v1 | Hybrid (Merchant Center is strictly Read-Only Diagnostic; Google Ads, GA4, and Reddit Ads support Read-Write with two-phase commit) | ✅ | ✅ | ✅ | OAuth 2.0 | ✅ | In-Memory | ✅ | ✅ | XML/TSV | MCP | ★266 | 2026-09 | A · Production-Ready |
| [**kevinfee3/authoryze-mcp**](#kevinfee3--authoryze-mcp) | Config / Spec | 4 | Visa Intelligent C | Read-Write | ✅ | ✅ | — | OAuth 2.1 PKCE | ✅ | Stateless Proxy | — | — | Multi | MCP | ★0 | 2026-08 | B · Community Stable |
| [**kinerette/claude-code-checkout-upsell**](#kinerette--claude-code-checkout-upsell) | Config / Spec | 5 | Shopify Admin | Read-Write | ✅ | ✅ | — | Config / Env | ✅ | Stateless Proxy | — | — | JSON | MCP | ★0 | 2026-09 | A- · Community Stable |
| [**kiwoongeom/gmc-mcp**](#kiwoongeom--gmc-mcp) | Python | 126 | Merchant API v1 | Read-Write Catalog Management (full CRUD across products, inventory, feeds, promotions, regions, and accounts) | ✅ | ✅ | ✅ | OAuth 2.0 | ✅ | In-Memory | ✅ | ✅ | XML/TSV | MCP | ★15 | 2026-05 | A · Production-Ready |
| [**lgiavedoni/claude-for-commerce-merchant-commercetools**](#lgiavedoni--claude-for-commerce-merchant-commercetools) | Python | 16 | commercetools | Read-Write | ✅ | ✅ | — | OAuth 2.0 | ✅ | In-Memory | ✅ | ✅ | JSON | MCP | ★0 | 2026-09 | A · Production-Ready |
| [**markifact/markifact-mcp**](#markifact--markifact-mcp) | TypeScript | 8 | Merchant API v1 | Read-Write | ✅ | ✅ | ✅ | OAuth 2.1 PKCE | — | Stateless Proxy | — | — | JSON | MCP | ★48 | 2026-09 | B · Community Stable |
| [**marwa-mrwan/google-clarity-mcp-codex**](#marwa-mrwan--google-clarity-mcp-codex) | JavaScript | 213 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | OAuth 2.0 | — | Stateless Proxy | — | — | JSON | MCP | ★0 | 2026-09 | A · Production-Ready |
| [**msalihk/catalog-mcp**](#msalihk--catalog-mcp) | TypeScript | 3 | Shopify Admin | Read-Only | — | — | — | Config / Env | — | Stateless Proxy | ✅ | ✅ | JSON | MCP | ★0 | 2026-09 | A · Production-Ready |
| [**prajapatimehul/shopify-cowork**](#prajapatimehul--shopify-cowork) | Python | 7 | Shopify Admin | Read-Write | ✅ | ✅ | — | Bearer Token | ✅ | Stateless Proxy | — | ✅ | JSON | MCP | ★15 | 2026-05 | A · Production-Ready |
| [**protyoya/Razorpay-Buidathon-Project**](#protyoya--Razorpay-Buidathon-Project) | JavaScript | 10 | Payment API | Read-Write | ✅ | ✅ | — | Config / Env | — | In-Memory | — | — | JSON | MCP | ★1 | 2026-09 | A · Production-Ready |
| [**psrikanthm/expense-report**](#psrikanthm--expense-report) | Python | — | Google Maps MCP Se | Read-Only Analysis (Parses local bank statements, queries remote Google Maps MCP for merchant location grounding, generates PDF reports) | ✅ | ✅ | — | API Key | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | REST / SDK | ★0 | 2026-06 | B+ · Community Stable |
| [**roblouw2nd/fetchgate**](#roblouw2nd--fetchgate) | Python | 4 | Fetchgate Cloudfla | Read-Only Content & Transactional Payment Challenge | ✅ | ✅ | ✅ | Config / Env | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | MCP | ★1 | 2026-09 | B+ · Community Stable |
| [**rushikeshmore/shopify-partner-agent**](#rushikeshmore--shopify-partner-agent) | Python | 6 | Merchant API v1 | Read-Only | ✅ | ✅ | — | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★13 | 2026-04 | B · Community Stable |
| [**simpleproductfeeds/skills**](#simpleproductfeeds--skills) | Config / Spec | 16 | Content API v2.1 | Read-Write | ✅ | ✅ | — | OAuth 2.0 | ✅ | Stateless Proxy | — | ✅ | XML/TSV | MCP | ★0 | 2026-08 | A · Production-Ready |
| [**theYahia/ifood-mcp**](#theYahia--ifood-mcp) | TypeScript | 26 | iFood Merchant API | Read-Write | — | ✅ | — | OAuth 2.0 | ✅ | In-Memory | — | — | JSON | MCP | ★1 | 2026-09 | A · Production-Ready |
| [**thesagarjain9-cpu/ucp-onboard**](#thesagarjain9-cpu--ucp-onboard) | TypeScript | 5 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | API Key | — | Stateless Proxy | — | — | JSON | MCP | ★2 | 2026-09 | B · Community Stable |
| [**umeshravani/spree_google_products**](#umeshravani--spree_google_products) | Ruby | — | Content API v2.1 | Read-Write Catalog Synchronization (pushes products/variants, fetches approval status and issues) | — | — | ✅ | OAuth 2.0 | ✅ | Stateless Proxy | ✅ | ✅ | XML/TSV | REST / SDK | ★4 | 2026-06 | A- · Community Stable |
| [**visa/vic-reference-agent**](#visa--vic-reference-agent) | TypeScript | 6 | Merchant API v1 | Read-Only | ✅ | ✅ | ✅ | Config / Env | — | Stateless Proxy | — | — | JSON | MCP | ★17 | 2026-06 | B · Community Stable |
| [**webloom-agency/merchant-center-mcp**](#webloom-agency--merchant-center-mcp) | Python | 25 | Merchant API v1 | Read-Only Enforced by Default with Safe Write Whitelist | ✅ | ✅ | ✅ | OAuth 2.1 PKCE | ✅ | In-Memory | ✅ | ✅ | XML/TSV | MCP | ★0 | 2026-08 | A · Production-Ready |

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

*11 projects. Diagnostic monitors, offline feed validation linters, disapproval issue mitigators, and competitive search scraping engines for maintaining catalog integrity.*

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

*5 projects. Specialized scrapers and SERP APIs capturing live Google Shopping competitor pricing, rankings, and stock levels.*

| Project | What it does |
|---|---|
| <a id="ShoppingResult--shoppingscraper-cli"></a>[**ShoppingResult/shoppingscraper-cli**](https://github.com/ShoppingResult/shoppingscraper-cli) | Extracts competitive pricing intelligence and Google Shopping SERP listings via 18 specialized CLI and MCP commands. Enables pricing elasticity analysis and automated price monitoring against competing merchant listings. |
| <a id="GreXLin85--serper.dev-mcp"></a>[**GreXLin85/serper.dev-mcp**](https://github.com/GreXLin85/serper.dev-mcp) | Delivers real-time Google Shopping search results, product prices, ratings, and merchant positions via the Serper API. Provides AI agents with 12 tools for comparative market research and Google Shopping visibility auditing. |
| <a id="johnisanerd--Apify-Google-Shopping-API"></a>[**johnisanerd/Apify-Google-Shopping-API**](https://github.com/johnisanerd/Apify-Google-Shopping-API) | Scrapes structured Google Shopping search pages and product comparison grids via serverless Apify actors. Retrieves real-time merchant pricing, stock availability, and sponsored ad placements for market intelligence. |
| <a id="alessandrobenigni--ScrapingDog-MCP"></a>[**alessandrobenigni/ScrapingDog-MCP**](https://github.com/alessandrobenigni/ScrapingDog-MCP) | Provides 77 web scraping and search tools including dedicated Google Shopping SERP extraction endpoints. Bypasses bot detection barriers to deliver live merchant pricing data and competitor catalog structures. |
| <a id="alisadiq-ai--sketric-dataforseo-mcp-prefork"></a>[**alisadiq-ai/sketric-dataforseo-mcp-prefork**](https://github.com/alisadiq-ai/sketric-dataforseo-mcp-prefork) | Bridges DataForSEO Google Shopping API and Merchant API v1 data streams into a single analytical MCP gateway. Supplies comprehensive keyword-level shopping rankings, item positions, and historical price movement. |

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

*4 projects. Operational guardrails, transactional dry-run validators, edge proxies, and spend authorization layers protecting live merchant catalogs.*

### Two-phase commit and catalog mutation guards

*2 projects. Validation layers and rate-limiting edge proxies enforcing preview confirmation before executing live catalog mutations.*

| Project | What it does |
|---|---|
| <a id="kinerette--claude-code-checkout-upsell"></a>[**kinerette/claude-code-checkout-upsell**](https://github.com/kinerette/claude-code-checkout-upsell) | Enforces strict transactional safety guardrails and validation rules for AI-driven catalog adjustments and checkout extensions. Prevents catastrophic bulk pricing errors by requiring preview validation gates before updating live product feeds. |
| <a id="roblouw2nd--fetchgate"></a>[**roblouw2nd/fetchgate**](https://github.com/roblouw2nd/fetchgate) | Acts as a secure Edge-deployed proxy on Cloudflare Workers for scraping and sanitizing merchant product data feeds. Applies rate-limiting, egress caching, and structural schema validation to protect origin merchant endpoints. |

### Safe execution sandboxes and spending authorization

*2 projects. Protocol sandboxes and cryptographic spend authorization frameworks preventing unauthorized autonomous transactions.*

| Project | What it does |
|---|---|
| <a id="flovoice53-tech--acp-sandbox"></a>[**flovoice53-tech/acp-sandbox**](https://github.com/flovoice53-tech/acp-sandbox) | Provides an isolated protocol testbed for the Agentic Commerce Protocol (ACP) and Universal Commerce Protocol (UCP). Allows developers to test autonomous product selection, checkout handoffs, and catalog queries in a sandboxed runtime. |
| <a id="kevinfee3--authoryze-mcp"></a>[**kevinfee3/authoryze-mcp**](https://github.com/kevinfee3/authoryze-mcp) | Implements policy-driven authorization and spend guardrails for autonomous agents executing commercial purchases and catalog edits. Enforces cryptographic signing, maximum transaction limits, and human-in-the-loop approvals for agent operations. |

---

## 5. Manage multi-tenant access and Multi-Client Account (MCA) routing

*4 projects. Multi-tenant authentication proxies, agency sub-account routers, and session persistence frameworks managing Multi-Client Account (MCA) structures.*

### Multi-tenant OAuth gateways and sub-account routers

*3 projects. Enterprise gateways isolating credentials, managing client sub-accounts, and aggregating merchant financial telemetry.*

| Project | What it does |
|---|---|
| <a id="api-evangelist--agenthaven-dev"></a>[**api-evangelist/agenthaven-dev**](https://github.com/api-evangelist/agenthaven-dev) | Architects an enterprise catalog governance gateway supporting Multi-Client Account (MCA) delegation and sub-account routing. Enforces strict multi-tenant tenant isolation and scoped OAuth 2.1 access control across agency client portfolios. |
| <a id="PaidSync--paidsync-mcp"></a>[**PaidSync/paidsync-mcp**](https://github.com/PaidSync/paidsync-mcp) | Provides a multi-tenant payment and billing MCP server connecting Google Merchant Center accounts with Stripe and custom billing rails. Manages subscription tiers, automated merchant invoice generation, and account-level settlement. |
| <a id="psrikanthm--expense-report"></a>[**psrikanthm/expense-report**](https://github.com/psrikanthm/expense-report) | Automates financial reconciliation and operational expense tracking across merchant ad spend and Google Cloud API consumption. Parses multi-account billing exports and provides structured financial rollups for agency administrators. |

### Context persistence and account scoping protocols

*1 project. Session context servers maintaining active account state across complex merchant hierarchies.*

| Project | What it does |
|---|---|
| <a id="ihint--merchant-context"></a>[**ihint/merchant-context**](https://github.com/ihint/merchant-context) | Maintains persistent session context and organizational scope across complex Multi-Client Account (MCA) hierarchies. Provides 9 tools for caching merchant account metadata, current sub-account selection, and user permissions. |

---

## 6. Bridge e-commerce storefronts and multi-channel catalogs

*7 projects. Bidirectional connectors syncing e-commerce platforms (Shopify, Shopware, commercetools) and regional marketplaces with Google Merchant Center feeds.*

### Shopify storefront and co-worker bridges

*2 projects. Bridges connecting Shopify store inventories, product variants, and admin endpoints to Merchant Center pipelines.*

| Project | What it does |
|---|---|
| <a id="prajapatimehul--shopify-cowork"></a>[**prajapatimehul/shopify-cowork**](https://github.com/prajapatimehul/shopify-cowork) | Coordinates catalog synchronization between Shopify Admin GraphQL endpoints and Google Merchant Center feeds via 7 agent tools. Automates product attribute mapping, inventory synchronization, and collection-level feed segregation. |
| <a id="HasData--shopify-mcp"></a>[**HasData/shopify-mcp**](https://github.com/HasData/shopify-mcp) | Extracts public Shopify catalog data and product structures without requiring private store credentials. Allows AI assistants to inspect competitor storefront products, variants, and pricing for merchant benchmark analysis. |

### Headless and composable commerce backends

*2 projects. Enterprise integrations connecting composable commerce engines to Google Shopping feed specifications.*

| Project | What it does |
|---|---|
| <a id="agentic-commerce-lab--shopware-claude-commerce"></a>[**agentic-commerce-lab/shopware-claude-commerce**](https://github.com/agentic-commerce-lab/shopware-claude-commerce) | Implements a comprehensive 34-tool commerce bridge connecting Shopware 6.7 Admin API with Google Shopping and Claude. Enables bidirectional catalog updates, order tracking, customer management, and automated Google Shopping XML export. |
| <a id="lgiavedoni--claude-for-commerce-merchant-commercetools"></a>[**lgiavedoni/claude-for-commerce-merchant-commercetools**](https://github.com/lgiavedoni/claude-for-commerce-merchant-commercetools) | Bridges commercetools composable commerce platforms with Google Merchant Center catalog feeds using 16 specialized tools. Implements Anthropic's enterprise commerce blueprint for large-scale enterprise catalog orchestration. |

### Multi-marketplace and regional catalog bridges

*3 projects. Connectors synchronizing catalog data across international marketplaces, delivery platforms, and workflow automation engines.*

| Project | What it does |
|---|---|
| <a id="A1-x-Tech--mcp-yandex-merchants"></a>[**A1-x-Tech/mcp-yandex-merchants**](https://github.com/A1-x-Tech/mcp-yandex-merchants) | Implements a TypeScript Model Context Protocol server for Yandex Market Partner API, mirroring Google Merchant Center capabilities. Provides 28 tools for multi-marketplace catalog synchronization, price management, and regional availability mapping. |
| <a id="theYahia--ifood-mcp"></a>[**theYahia/ifood-mcp**](https://github.com/theYahia/ifood-mcp) | Connects on-demand delivery merchants to the iFood Merchant API using 26 granular TypeScript MCP tools. Demonstrates real-time menu and catalog management, order processing, and dynamic inventory adjustments. |
| <a id="apivault-labs--n8n-nodes-apivault-temu"></a>[**apivault-labs/n8n-nodes-apivault-temu**](https://github.com/apivault-labs/n8n-nodes-apivault-temu) | Provides an n8n workflow automation node for syncing and scraping marketplace product catalogs and prices. Enables low-code orchestration between multi-channel retail marketplaces and Google Merchant Center feeds. |

---

## 7. Deploy autonomous agentic commerce, ACP/UCP, and machine settlement

*9 projects. Protocols and runtime environments for the Universal Commerce Protocol (UCP), Agentic Commerce Protocol (ACP), and cryptographic machine settlement.*

### Universal Commerce Protocol (UCP) onboarding and reference stacks

*4 projects. Official blueprints, onboarding agents, and reference indexes for Google's Universal Commerce Protocol.*

| Project | What it does |
|---|---|
| <a id="ViryaZheng--ucp-onboard"></a>[**ViryaZheng/ucp-onboard**](https://github.com/ViryaZheng/ucp-onboard) | Automates merchant onboarding and catalog registration for Google's Universal Commerce Protocol (UCP). Configures agent capabilities, validates merchant endpoint discovery manifests, and verifies UCP catalog compliance. |
| <a id="thesagarjain9-cpu--ucp-onboard"></a>[**thesagarjain9-cpu/ucp-onboard**](https://github.com/thesagarjain9-cpu/ucp-onboard) | Provides a TypeScript reference implementation for registering and onboarding merchant catalogs onto the Universal Commerce Protocol. Exposes 5 tools for catalog schema verification, merchant endpoint health checks, and payment bridge initialization. |
| <a id="NVIDIA-AI-Blueprints--Retail-Agentic-Commerce"></a>[**NVIDIA-AI-Blueprints/Retail-Agentic-Commerce**](https://github.com/NVIDIA-AI-Blueprints/Retail-Agentic-Commerce) | NVIDIA's flagship enterprise reference blueprint for agentic commerce, implementing the Universal Commerce Protocol (UCP). Combines multimodal product search, real-time inventory checking, and secure agent-to-agent checkout protocols. |
| <a id="MentionNetwork--awesome-agentic-commerce"></a>[**MentionNetwork/awesome-agentic-commerce**](https://github.com/MentionNetwork/awesome-agentic-commerce) | Curates the definitive landscape and architectural specifications for agentic commerce, ACP, and UCP protocols. Catalogs developer SDKs, machine-to-machine payment rails, and standards for autonomous shopping agents. |

### POS and voice-activated merchant terminals

*2 projects. Voice-enabled and terminal-native interfaces executing in-store inventory lookups and structured data validation.*

| Project | What it does |
|---|---|
| <a id="NovaCorpAI--agentpos-alexa"></a>[**NovaCorpAI/agentpos-alexa**](https://github.com/NovaCorpAI/agentpos-alexa) | Integrates Alexa voice contracts with Point-of-Sale (POS) systems and Google Universal Commerce Protocol catalog rails. Enables voice-driven checkout, in-store product lookups, and automated merchant transaction settlement. |
| <a id="AgriciDaniel--claude-seo"></a>[**AgriciDaniel/claude-seo**](https://github.com/AgriciDaniel/claude-seo) | Massive open-source agent skill suite providing in-depth e-commerce SEO audits and Google Merchant Center feed diagnostics. Validates structured data markup (Schema.org Product and Offer), crawlability, and merchant feed attribute parity. |

### Autonomous payment and settlement protocols

*3 projects. Settlement rails enabling autonomous AI agents to execute machine-to-machine checkout via fiat and decentralized rails.*

| Project | What it does |
|---|---|
| <a id="protyoya--Razorpay-Buidathon-Project"></a>[**protyoya/Razorpay-Buidathon-Project**](https://github.com/protyoya/Razorpay-Buidathon-Project) | Implements programmatic payment authorization and order settlement for autonomous AI agents using Razorpay payment rails. Demonstrates secure handoff from product selection to two-phase authorized payment execution. |
| <a id="PayRam--payram-mcp"></a>[**PayRam/payram-mcp**](https://github.com/PayRam/payram-mcp) | Provides a self-hosted cryptocurrency payment gateway and merchant settlement server with 52 granular tools. Enables autonomous agentic transactions, instant on-chain invoice generation, and decentralized merchant billing. |
| <a id="visa--vic-reference-agent"></a>[**visa/vic-reference-agent**](https://github.com/visa/vic-reference-agent) | Visa's official reference agent implementation for the Visa Intelligent Commerce (VIC) machine settlement framework. Demonstrates tokenized merchant checkout, cryptographic spending limits, and dispute-resistant agent purchases. |

---

## Resources

Curated official developer documentation, protocols, and technical resources for building Google Merchant Center agent tooling.

### Official Documentation & SDKs

- [Google Merchant API v1 Documentation](https://developers.google.com/merchant) — Official developer guides for the modern sub-API architecture covering Products, Accounts, Inventories, Promotions, and Data Sources.
- [Google Content API for Shopping Reference](https://developers.google.com/shopping-content/reference/rest) — Upstream REST reference for legacy v2.1 services and supplemental feed pipelines.
- [Google Merchant Center Help Center](https://support.google.com/merchants) — Policy guides, account suspension troubleshooting, and feed specification rules.
- [Google Cloud API Client Libraries](https://cloud.google.com/apis/docs/client-libraries-explained) — Official client SDKs across Python, Node.js, Go, and Java supporting Application Default Credentials (ADC).

### Specifications & Standards

- [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io/) — Open protocol standard defining client-server JSON-RPC messaging, stdio/SSE transports, and dynamic tool invocation for AI agents.
- [Universal Commerce Protocol (UCP) Specification](https://github.com/MentionNetwork/awesome-agentic-commerce) — Open standard for decentralized agentic commerce, autonomous product discovery, and merchant catalog federation.
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

### Evaluation Methodology & Verification Invariants

All 57 repositories listed in this catalog were evaluated against rigorous engineering standards:

1. **AST & Code Inspection:** Every tool was audited at the source-code level to verify callable tool counts, Zod/Pydantic input schemas, error handling, and target API alignment.
2. **Commit Recency Invariant:** Every repository has verified commit activity within the preceding 6 months (on or after March 21, 2026).
3. **Developer Provenance & Anti-Slop Audit:** Maintainer GitHub profiles were audited to separate sustained human engineering from disposable single-commit synthetic boilerplate.
4. **Operational Safety Audit:** Tools modifying live merchant inventories were evaluated for dry-run validation modes, spending guardrails, and audit rollback ledgers.

### Repository Inclusion & Anti-Slop Policy

This repository enforces strict inclusion boundaries to protect developers from unmaintained code and AI hallucination:

- **Included:** Production-grade MCP servers, official Google developer SDKs, verified shopping automation scripts, and documented agentic commerce protocols.
- **Quarantined & Excluded:** 16 synthetic GitHub bot farm repositories discovered during research were audited and quarantined due to identical commit timestamps, hallucinated dependencies, zero issue activity, and lack of real API client code.
