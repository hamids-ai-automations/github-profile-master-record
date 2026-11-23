# shopify-growth-mcp

**Overview:** Production-grade Shopify Growth MCP Server: 61 MCP tools for AI store operations, SEO audits, GEO readiness, deterministic analytics, inventory intelligence, feed quality and safe marketing workflows. Model Context Protocol for Claude, Cursor, VS Code, Codex. TypeScript, MIT.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/shopify-growth-mcp](https://github.com/hamids-ai-automations/shopify-growth-mcp) |
| Live website | https://marvis.web.app/ |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-28 |
| Last update | 2026-11-20 |
| Last push | 2026-11-23 |
| Default branch | main |
| License | MIT |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 1 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 2 |
| Size | 150 KB |
| Topics | ai, analytics, claude, cursor, digital-marketing, ecommerce, geo, graphql, inventory, llm, mcp, mcp-server, model-context-protocol, seo, shopify, shopify-api, typescript, ai-agents, approval-workflow |

## Objectives

---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_6fc44ac2d27f11f196c5525400248c00
    ReservedCode1: Ms0XkeFrR7dbnIUJDH7Za5ErwbcaOgxsDCu7djCtv5/ImJ0CLsCcutypQRUaR9Jje3M7wrn05kZ/3fpjC+TDxc44qLdP2G+oc9ciNFxXW5eK42wyCXNXF1ywPniW72FazYkwVBmTTv+ZWf5w3iZVQTEmJHUCWZXNeVFkEDS2Kndl6IoPHbC7SS1FU0g=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_6fc44ac2d27f11f196c5525400248c00
    ReservedCode2: Ms0XkeFrR7dbnIUJDH7Za5ErwbcaOgxsDCu7djCtv5/ImJ0CLsCcutypQRUaR9Jje3M7wrn05kZ/3fpjC+TD

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, docs, research, src, tests
- **Total files (tracked in default branch):** 67
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 8

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 263040 |
| Dockerfile | 693 |
| JavaScript | 605 |

**Frameworks / libraries detected:** MCP

**Dependencies:** @eslint/js, @modelcontextprotocol/sdk, @types/node, dotenv, eslint, graphql, graphql-request, prettier, rimraf, tsx, typescript, typescript-eslint, vitest, zod

## Important source files

- `docker-compose.yml`
- `package.json`
- `tsconfig.json`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app/

## Documentation links

- https://marvis.web.app
- https://m8ven.ai/badge/mcp/hamid-digitalmarketer-shopify-growth-mcp-14q9ul?v=109ce7f30ab56045601044f15dae2367
- https://m8ven.ai/mcp/hamid-digitalmarketer-shopify-growth-mcp-14q9ul?s=readme

## Development status

Active — last push 2026-11-23

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/ghl-devops-toolkit
- hamids-ai-automations/nexgen-financial-experts
- hamids-ai-automations/firebase-ai-starter-kit
- hamids-ai-automations/Go-High-Level-MCP-2026-Complete
- hamids-ai-automations/cli

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

See [research/roadmap.md](https://github.com/hamids-ai-automations/shopify-growth-mcp/blob/main/research/roadmap.md). Near-term priorities:

1. Google Search Console integration for indexability evidence.
2. Google Analytics 4 + Google Ads / Meta Ads connectors (authorized APIs only).
3. Scheduled audits and report exports (client-ready deliverables for agencies).
4. Streamable HTTP transport for remote deployments.
5. Web dashboard for visual reports.

---

## README source

Full README: https://github.com/hamids-ai-automations/shopify-growth-mcp/blob/main/README.md

```markdown
---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_6fc44ac2d27f11f196c5525400248c00
    ReservedCode1: Ms0XkeFrR7dbnIUJDH7Za5ErwbcaOgxsDCu7djCtv5/ImJ0CLsCcutypQRUaR9Jje3M7wrn05kZ/3fpjC+TDxc44qLdP2G+oc9ciNFxXW5eK42wyCXNXF1ywPniW72FazYkwVBmTTv+ZWf5w3iZVQTEmJHUCWZXNeVFkEDS2Kndl6IoPHbC7SS1FU0g=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_6fc44ac2d27f11f196c5525400248c00
    ReservedCode2: Ms0XkeFrR7dbnIUJDH7Za5ErwbcaOgxsDCu7djCtv5/ImJ0CLsCcutypQRUaR9Jje3M7wrn05kZ/3fpjC+TDxc44qLdP2G+oc9ciNFxXW5eK42wyCXNXF1ywPniW72FazYkwVBmTTv+ZWf5w3iZVQTEmJHUCWZXNeVFkEDS2Kndl6IoPHbC7SS1FU0g=
---

# Shopify Growth MCP — AI Store Operations, SEO & Analytics

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Node](https://img.shields.io/badge/node-20%2B-brightgreen)](package.json)
[![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178c6)](tsconfig.json)
[![Tools](https://img.shields.io/badge/tools-61-blue)](docs/tools.md)
[![Tests](https://img.shields.io/badge/tests-64%20passing-brightgreen)](tests)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF)](.github/workflows/ci.yml)

A **production-grade Model Context Protocol (MCP) server for Shopify** that lets AI assistants like **Claude, Cursor, ChatGPT, VS Code and Codex** operate your store through natural language — while giving merchants, agencies and SEO professionals actionable growth workflows built on real store data.

**Stop juggling 20 tabs in Shopify Admin. Ask your AI assistant to find low-stock products, audit SEO metadata, summarize sales trends, or draft marketing copy — and get structured, safe, reviewable results.**

- **61 MCP tools** across products, orders, customers, collections, inventory, metafields, tags, SEO, GEO, analytics, feeds and marketing.
- **Read-only by default**, with plan previews, bound approvals and audit logging for every write.
- **Runs with zero configuration** in demo mode (fictional store data) — no Shopify credentials required to explore.
- **Deterministic core**: Shopify connectivity and analytics never require an LLM API key.

---

## Why Shopify Growth MCP?

Most Shopify MCP servers are thin API wrappers: they expose a CRUD surface but don't help you *decide* what to do next. Shopify Growth MCP combines reliable store operations with a growth layer that turns raw Shopify data into prioritized, explainable recommendations:

| Problem merchants face | What this server does |
| --- | --- |
| Products missing titles, descriptions or alt text | `seo_audit` finds gaps with severity + evidence + suggested fix |
| Low stock and stale listings cause lost sales | `inventory_intelligence` flags thresholds, stale products and reorder priorities |
| Hard to see how the store is actually performing | `analytics_summary` computes sales, AOV, best sellers and trends from real orders |
| Feed data quality breaks ad campaigns | `feed_quality_audit` + `feed_export` validate and export product feeds |
| AI search engines can't understand the store | `geo_ai_readiness` audits content clarity, structured data and machine readability |
| Writes are risky | Plan → preview → bound approval → apply, with a full audit trail |

---

## Feature Highlights

### Core store operations (61 tools)

- **Products** — list, search, create, update, archive, delete, media, variants, metafields, tags.
- **Orders** — list, get, update, cancel, draft orders, customer order history.
- **Customers** — list, search, get, create, update, addresses, order summaries (privacy-minimized).
- **Collections** — list, get, create, update, membership management, uncategorized-product detection.
- **Inventory** — levels, locations, set quantities, low-stock alerts.
- **Metafields & tags** — list, set, delete, add/remove tags with namespace/key validation.

### Growth differentiators

- **SEO audit** (`seo_audit`) — scans products and collections for missing titles, weak descriptions, duplicate content, missing alt text, metadata gaps; returns severity, evidence and estimated effort.
- **AI-assisted SEO proposals** (`seo_proposals`, `seo_proposals_apply`) — generates reviewable title/description/metadata proposals in bulk; optional LLM provider for richer drafts (template fallback included).
- **GEO / AI-search readiness** (`geo_ai_readiness`) — evidence-based audit of content clarity, naming consistency, structured data and machine readability. No ranking guarantees, ever.
- **Store analytics** (`analytics_*`) — sales totals, order counts, AOV, best sellers, sales trends, discounts, refunds, inventory exposure, product comparisons. Deterministic formulas documented.
- **Product feed quality** (`feed_quality_audit`, `feed_export`) — validates data against marketing-readiness criteria and exports structured feeds.
- **Inventory intelligence** (`inventory_intelligence`) — configurable low-stock thresholds, stale-product detection, reorder suggestions, variant inconsistencies.
- **Marketing preparation** (`marketing_*`) — ad copy drafts, campaign briefs, campaign naming, product grouping by category/priority.

### Safety first

- **Read-only by default**: every tool declares a risk tier (`READ` / `WRITE` / `DESTRUCTIVE`).
- **Plan-and-apply workflow**: bulk writes produce a preview (IDs, current values, proposed values, affected counts, warnings); an approval token is bound to the exact plan hash — changed parameters require a new approval.
- **Audit logging**: every operation is recorded with redacted secrets.
- **Least-privilege guidance**: setup docs show the minimal Admin API scopes.
- **No silent writes, no fabricated results, no fake "approved by Google/Meta" claims.**

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│  MCP clients: Claude Desktop · Claude Code · Cursor · VS Code · Codex │
└──────────────────────────────────────────┬───────────────────────────┘
                                           │ Model Context Protocol (stdio)
┌──────────────────────────────────────────▼───────────────────────────┐
│                       shopify-growth-mcp (this repo)                 │
│  ┌───────────────┐  ┌──────────────┐  ┌───────────────────────────┐  │
│  │ Tool registry │  │ Policy engine│  │ Audit log / approvals     │  │
│  │ 61 tools      │  │ READ/WRITE/  │  │ previews, bound tokens,   │  │
│  │ risk-tiered   │  │ DESTRUCTIVE  │  │ redaction                 │  │
│  └──────┬────────┘  └──────┬───────┘  └───────────────────────────┘  │
│         │                  │                                         │
│  ┌──────▼──────────────────▼──────────────────────────────────────┐  │
│  │ Shopify GraphQL client: pagination · retries · rate limits ·   │  │
│  │ timeouts · cost awareness · API version pinning (2025-10)      │  │
│  └──────────────────────────────┬────────────────────────────────┘  │
└─────────────────────────────────┼───────────────────────────────────┘
                                  │ Shopify Admin GraphQL API
                        ┌─────────▼─────────┐
                        │  Your Shopify store│
                        └───────────────────┘
```

Modules: `src/server` (lifecycle/transport) · `src/tools` (registry) · `src/shopify` (GraphQL client, operations, pagination) · `src/auth` (token lifecycle) · `src/security` (policy, approvals, previews, audit, redaction) · `src/seo` (audits, GEO, proposals, feed quality) · `src/analytics` (metrics) · `src/workflows` (inventory intelligence, marketing, store ops, plan) · `src/demo` (fictional demo data) · `src/config` (env validation) · `src/errors` (normalized errors) · `src/utils`.

See [docs/architecture.md](https://github.com/hamids-ai-automations/shopify-growth-mcp/blob/main/docs/architecture.md) for the full design, data-flow and decision log.

---

## Quick Start

### Prerequisites

- Node.js **22.12+** (tested on Node 24).
- No Shop
```
