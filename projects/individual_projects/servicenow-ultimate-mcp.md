# servicenow-ultimate-mcp

**Overview:** Enterprise operations console and reference control plane for the ServiceNow Ultimate MCP server - ITSM, CMDB, workflows, analytics and an LLM-powered natural-language query console.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/servicenow-ultimate-mcp](https://github.com/hamids-ai-automations/servicenow-ultimate-mcp) |
| Live website | https://marvis.web.app |
| Visibility | public |
| Status | active |
| Creation date | 2026-11-24 |
| Last update | 2026-11-25 |
| Last push | 2026-11-24 |
| Default branch | main |
| License | MIT |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 1 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 1 |
| Contributors | 1 |
| Size | 228 KB |
| Topics | ai-agents, automation, cmdb, itsm, llm, mcp, model-context-protocol, nextjs, servicenow, typescript |

## Objectives

# ServiceNow Ultimate MCP — Enterprise AI Operations Platform

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, QA, examples, prisma, public, src, tests
- **Total files (tracked in default branch):** 114
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 7

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 363385 |
| CSS | 5376 |
| JavaScript | 1728 |

**Frameworks / libraries detected:** MCP, Next.js, React, Tailwind CSS

**Dependencies:** @dnd-kit/core, @dnd-kit/sortable, @dnd-kit/utilities, @hookform/resolvers, @prisma/client, @radix-ui/react-accordion, @radix-ui/react-alert-dialog, @radix-ui/react-aspect-ratio, @radix-ui/react-avatar, @radix-ui/react-checkbox, @radix-ui/react-collapsible, @radix-ui/react-context-menu, @radix-ui/react-dialog, @radix-ui/react-dropdown-menu, @radix-ui/react-hover-card, @radix-ui/react-label, @radix-ui/react-menubar, @radix-ui/react-navigation-menu, @radix-ui/react-popover, @radix-ui/react-progress, @radix-ui/react-radio-group, @radix-ui/react-scroll-area, @radix-ui/react-select, @radix-ui/react-separator, @radix-ui/react-slider, @radix-ui/react-slot, @radix-ui/react-switch, @radix-ui/react-tabs, @radix-ui/react-toast, @radix-ui/react-toggle, @radix-ui/react-toggle-group, @radix-ui/react-tooltip, @reactuses/core, @tailwindcss/postcss, @tanstack/react-query, @tanstack/react-table, @types/react, @types/react-dom, @vitest/coverage-v8, bun-types, class-variance-authority, clsx, cmdk, date-fns, embla-carousel-react, eslint, eslint-config-next, framer-motion, input-otp, lucide-react, next, next-auth, next-intl, next-themes, prisma, react, react-day-picker, react-dom, react-hook-form, react-markdown

## Important source files

- `package.json`
- `tsconfig.json`

## Installation and setup

```bash
git clone https://github.com/hamids-ai-automations/servicenow-ultimate-mcp.git
cd servicenow-ultimate-mcp

npm install

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app

## Documentation links

- https://marvis.web.app
- https://wa.me/923167417135
- http://localhost:3000
- https://nextjs.org
- https://www.typescriptlang.org
- https://modelcontextprotocol.io
- https://your-instance.service-now.com

## Development status

Active — last push 2026-11-24

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 1

## Related projects

- hamids-ai-automations/marvis-portfolio
- hamids-ai-automations/ghl-servicepro-theme
- hamids-ai-automations/shopify-growth-mcp
- hamids-ai-automations/ghl-devops-toolkit
- hamids-ai-automations/nexgen-financial-experts

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

An 8-phase delivery timeline from core server through hardening.

---

## README source

Full README: https://github.com/hamids-ai-automations/servicenow-ultimate-mcp/blob/main/README.md

```markdown
# ServiceNow Ultimate MCP — Enterprise AI Operations Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Next.js](https://img.shields.io/badge/Next.js-16-black.svg)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue.svg)](https://www.typescriptlang.org)
[![MCP](https://img.shields.io/badge/MCP-2025.1-teal.svg)](https://modelcontextprotocol.io)

> The bridge between AI agents and ServiceNow — an enterprise-grade Model
> Context Protocol server that gives AI agents comprehensive access to
> ServiceNow: ITSM, ITOM, ITAM, CMDB, HR, CSM, workflows, automation,
> reporting, and administration.

This repository contains the **operations dashboard and reference web
application** for the ServiceNow Ultimate MCP server. It is a production-grade
Next.js 16 control plane that visualises the MCP tool registry, ServiceNow
modules, automation workflows, live operations analytics, and an interactive
natural-language query console powered by a large language model.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [The NL Query Console](#the-nl-query-console)
- [MCP Tools & Resources](#mcp-tools--resources)
- [Configuration](#configuration)
- [Available Scripts](#available-scripts)
- [Testing & QA](#testing--qa)
- [Roadmap](#roadmap)
- [Security](#security)
- [Developer & Contact](#developer--contact)
- [License](#license)

---

## Overview

ServiceNow Ultimate MCP exposes ServiceNow's ITSM, ITOM, ITAM, CMDB, HR, and
CSM capabilities to AI agents through the Model Context Protocol. AI clients
(Claude Desktop, Cursor, Cline, VS Code MCP, Gemini agents, custom Python
agents) connect over STDIO or Streamable HTTP and invoke **40+ validated
tools** across **20 categories**, read **16 URI-addressable resources**, and
execute **multi-step automation workflows** — all with strict security
safeguards.

This web application is the **management and demonstration plane** for that
server: a real-time operations dashboard, a tools/resources explorer, a
ServiceNow records browser, and an interactive natural-language console.

> **Note:** This web app uses mock ServiceNow data for demonstration. The
> natural-language query console uses a real LLM (via `z-ai-web-dev-sdk`) to
> translate plain English into validated ServiceNow encoded queries. To
> connect a real ServiceNow instance, point the backend API routes at the
> ServiceNow REST API and supply credentials via environment variables.

---

## Features

### Operations Dashboard
- 10 live KPIs (open incidents, critical, SLA breaches, problems, changes,
  CMDB CIs, health, avg resolution, first-contact resolution, approvals)
- Incident volume area chart (opened vs. resolved, 7 days)
- Priority distribution pie chart
- Assignment group performance bar chart
- SLA compliance trend line (6 weeks)
- Audited recent-activity feed

### ServiceNow Modules Browser
Tabbed records browser for Incidents, Problems, Changes, CMDB, Assets,
Knowledge, and SLA records with live filtering.

### MCP Tools Explorer
40 tools across 20 categories (Incident, Problem, Change, Request, CMDB,
Asset, User, Group, Knowledge, SLA, Reporting, Query, Script, Attachment,
Workflow, Approval, Instance, Audit, AI Analysis, Bulk). Each tool card
opens a detail dialog with the full input schema, output contract, permission
tier, safety flag, and an example JSON-RPC invocation.

### MCP Resources Browser
16 URI-addressable resources (`servicenow://incidents`, templates like
`servicenow://incidents/{number}`, schema endpoints, instance info, etc.).

### Natural Language Query Console
Type any operational request in plain English — e.g. *"Find all high-priority
incidents that have not been updated in seven days"* — and the LLM layer
returns:
- an `understood` flag and intent label
- the target ServiceNow table
- a validated encoded query (`priority=high^sys_updated_onONjavascript:gs.daysAgo(7)`)
- parsed filters
- a plain-English explanation
- an ordered list of planned MCP tool calls
- matching records (when not in dry-run mode)

### Automation Workflows
4 reusable multi-step workflows (Incident Resolution Assistant, Change Risk &
Conflict Review, Infrastructure Investigation, Duplicate Incident Triage) with
expandable step traces, safeguards, and estimated durations.

### Reports & Analytics
Avg resolution time by category, change success rate, and an exportable
reports list (JSON / CSV / Excel / HTML / Markdown).

### Architecture, Security & Multi-Instance
- 4-layer architecture diagram (AI Agent → MCP Protocol → Ultimate MCP →
  ServiceNow REST API)
- 6-pillar security framework (multi-auth, least-privilege, dry-run,
  explicit authorization, audit logging, no secret leakage)
- 4 permission tiers (read / write / admin / privileged)
- Multi-instance manager (Production, Development, Test, DR)
- Technology stack overview

### Roadmap
An 8-phase delivery timeline from core server through hardening.

---

## Tech Stack

| Layer | Technology |
| --- | --- |
| Framework | Next.js 16 (App Router) |
| Language | TypeScript 5 |
| Styling | Tailwind CSS 4 + shadcn/ui (New York) |
| Icons | Lucide React |
| Charts | Recharts |
| State | React hooks + lightweight fetch layer |
| AI / LLM | `z-ai-web-dev-sdk` (backend only) |
| Database | Prisma ORM (SQLite) — available for persistence |
| Linting | ESLint |

---

## Getting Started

### Prerequisites
- Node.js **20.9+** (required by Next.js 16) and npm 10+
- A terminal

### Installation

```bash
git clone https://github.com/hamids-ai-automations/servicenow-ultimate-mcp.git
cd servicenow-ultimate-mcp

npm install

# Optional for local UI work — the app runs on mock data without it
cp .env.example .env.local

# Optional persistence layer
npx prisma generate

npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Production Build

```bash
npm run build
npm run start
```

---

## Project Structure

```
servicenow-ultimate-mcp/
├── src/
│   ├── app/
│   │   ├── layout.tsx              # Root layout + theme provider
│   │   ├── page.tsx                # Single-page dashboard (10 sections)
│   │   ├── globals.css             # Dark-first emerald enterprise theme
│   │   └── api/
│   │       ├── dashboard/route.ts  # KPIs, trends, activity
│   │       ├── modules/route.ts    # ServiceNow records (7 modules)
│   │       ├── tools/route.ts      # MCP tool registry
│   │       ├── resources/route.ts  # MCP resource registry
│   │       ├── workflows/route.ts  # Automation workflows
│   │       ├── instances/route.ts  # Multi-instance manager
│   │       └── nlp-query/route.ts  # LLM-powered NL → ServiceNow query
│   ├── components/
│   │   ├── sections/               # Hero, Dashboard, Modules, Tools,
│   │   │                           # Resources, NlpConsole, Workflows,
│   │   │                           # Reports, Architecture, Roadmap
│   │   ├── ui/                     # shadcn/ui component set
│   │   ├── sidebar-nav.tsx
│   │   ├── section.tsx
│   │   ├── site-footer.tsx
│   │   ├── sn-badges.tsx           # Severity/state/permission badges
│   │   └── theme-provider.tsx
│   ├── hooks/
│   │   ├── use-api.ts              # Lightweight data-fetching hook
│   │   └── use-mobile.ts
│   └── lib/
│       ├── servicenow-data.ts      # Mock data + TypeScript types
│       ├── db.ts                   # Prisma client
│       └── utils.ts
├── prisma/
│   └── schema.prisma               # Database schema (SQLite)
├── public/                         # logo.svg, robots.txt
├── examples/                       # WebSocket reference demo
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── package.json
├── tsconfig.json
├── next.config.ts
├── tailwind.config.ts
├── postcss.config.mjs
├── eslint.config.mjs
└── components.json
```

---

## The NL Query Console

The console at `/api/nlp-query` u
```
