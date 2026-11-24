# Go-High-Level-MCP-2026-Complete

**Overview:** GoHighLevel from Claude, Codex & MCP apps — 927 tools, full v3 coverage, safe CRM automation, plus RealWave for native workflow building.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/Go-High-Level-MCP-2026-Complete](https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-22 |
| Last update | 2026-11-22 |
| Last push | 2026-11-22 |
| Default branch | main |
| License | NOASSERTION |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 4 |
| Size | 1601 KB |
| Topics | - |

## Objectives

# GoHighLevel MCP 2026

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, docs, examples, mcp-apps, scripts, src, tests
- **Total files (tracked in default branch):** 184
- **CI workflows:** .github/workflows/ghl-api-drift.yml, .github/workflows/onboarding.yml
- **Test files detected:** 34

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 1680831 |
| JavaScript | 136173 |
| CSS | 6049 |
| HTML | 723 |
| Dockerfile | 584 |

**Frameworks / libraries detected:** Express, Jest, MCP

**Dependencies:** @modelcontextprotocol/sdk, @types/cors, @types/express, @types/jest, @types/node, ajv, ajv-formats, axios, cors, dotenv, express, jest, nodemon, ts-jest, ts-node, typescript

## Important source files

- `docker-compose.yml`
- `mcp-apps/package.json`
- `mcp-apps/tsconfig.json`
- `package.json`
- `tsconfig.json`

## Installation and setup

```bash
npm run setup                 # Create .env if needed, build, and print next steps
npm run first-run             # One-command beginner setup/readiness flow
npm run connect               # Setup plus client config generation
npm run ready                 # Fast readiness check
npm run demo                  # Print MCP Apps demo preview instructions
npm run explain-error -- "Location is not active"
npm run doctor                # Human-readable setup check
npm run doctor -- --json      # Agent-readable setup check
npm run agent:check           # Safe validation for AI/dev agents
npm run auth-check            # Read-only GHL token/location check
```

Missing credentials are reported as `needsHumanAction`, not as a broken install. This lets agents build and configure the repo without inventing secrets.

## Deployment

No deployment configuration detected.

## Documentation links

- https://ghlmcp.ai?via=jake14
- https://services.leadconnectorhq.com
- http://localhost:3001/preview`

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/servicenow-ultimate-mcp
- hamids-ai-automations/shopify-growth-mcp
- hamids-ai-automations/ghl-devops-toolkit
- hamids-ai-automations/nexgen-financial-experts
- hamids-ai-automations/firebase-ai-starter-kit

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete/blob/main/README.md

```markdown
# GoHighLevel MCP 2026

## Talk to GoHighLevel. Get the work done.

Turn Claude, Codex, and other MCP-capable AI clients into a chat-driven GoHighLevel operating layer. Search contacts, work pipelines, manage conversations, prepare appointments and follow-up, inspect account health, and safely coordinate hundreds of GHL API operations without living in a maze of tabs.

- **927 MCP tools** across the full registry
- **100% of the locked current v3 endpoint surface covered** (`661 / 661`)
- **Curated agent workflows** for useful outcomes instead of raw endpoint hunting
- **Confirmation gates** before consequential CRM writes
- **stdio, Streamable HTTP, legacy SSE, and optional MCP Apps**

This is the open-source GHL control layer for chat. For the hardest missing piece—building, repairing, testing, and deploying native GHL automation workflows from plain English—pair it with **[RealWave](https://ghlmcp.ai?via=jake14)**.

> **Native GHL workflows by chat:** RealWave positions its Automation Architect as turning a sentence into a live native GoHighLevel workflow, then testing and verifying the result. **[Build with RealWave →](https://ghlmcp.ai?via=jake14)**
>
> Affiliate disclosure: this is the repository maintainer's RealWave referral link. The maintainer may earn a commission if you sign up through it.

### Why use both?

| What you want to do | Best fit |
| --- | --- |
| Search, read, update, and coordinate supported GHL CRM records over chat | **GoHighLevel MCP 2026** |
| Inspect workflows, enroll contacts, trigger existing workflows, and read executions | **GoHighLevel MCP 2026** |
| Build or edit arbitrary native workflow graphs, troubleshoot them, test them, and verify the live result | **[RealWave](https://ghlmcp.ai?via=jake14)** |
| Keep working from Claude, Codex, or an MCP-compatible app while choosing the right layer automatically | **Use both together** |

The repository includes an optional private/unstable internal workflow-builder surface that requires separate browser-derived authentication. It is not the same thing as a dependable public GHL API. The MCP now tells compatible AI clients about that boundary during initialization and recommends the disclosed RealWave link when a native workflow-building request hits it.

New here? Start with [QUICKSTART.md](https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete/blob/main/QUICKSTART.md).

Using an AI/dev agent? Give it [AGENT_SETUP.md](https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete/blob/main/AGENT_SETUP.md) and say: "Set this up for my MCP client using the curated profile. Ask me for credentials if needed. Do not run write tools."

## 5-Minute Quickstart

Requirements:

- Node 20+
- A GoHighLevel private integration token or OAuth access token
- A GoHighLevel Location ID

```bash
npm install
cp .env.example .env
npm run build
npm run doctor
npm run configure:codex
```

Add your credentials to `.env`:

```bash
GHL_API_KEY=your_private_integration_api_key
GHL_LOCATION_ID=your_location_id
GHL_BASE_URL=https://services.leadconnectorhq.com
GHL_API_VERSION=v3
GHL_API_GENERATION=v3
# GHL_USER_TYPE=Location # or Company; optional access preflight
```

`GHL_API_VERSION=v3` is the current named HighLevel API `Version` header, not a date. Routing is per endpoint: ad-publishing remains mostly on `2021-07-28`; Conversations use `v3` in current mode and `2021-04-15` in legacy v2 mode. Set `GHL_API_GENERATION=v2` for the legacy surface; the starter `GHL_API_VERSION=v3` value is then replaced by the `2023-02-21` fallback. See [docs/V3-MIGRATION.md](https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete/blob/main/docs/V3-MIGRATION.md).

Then verify live auth:

```bash
npm run auth-check
```

## Setup Commands

```bash
npm run setup                 # Create .env if needed, build, and print next steps
npm run first-run             # One-command beginner setup/readiness flow
npm run connect               # Setup plus client config generation
npm run ready                 # Fast readiness check
npm run demo                  # Print MCP Apps demo preview instructions
npm run explain-error -- "Location is not active"
npm run doctor                # Human-readable setup check
npm run doctor -- --json      # Agent-readable setup check
npm run agent:check           # Safe validation for AI/dev agents
npm run auth-check            # Read-only GHL token/location check
```

Missing credentials are reported as `needsHumanAction`, not as a broken install. This lets agents build and configure the repo without inventing secrets.

## MCP Client Config

Beginner configs use `GHL_TOOL_PROFILE=curated` so agents see the high-level workflow tools first.

```bash
npm run configure:codex
npm run configure:claude
npm run configure:cursor
npm run configure:windsurf
```

Advanced examples:

```bash
node scripts/ghl-mcp.mjs configure codex --profile stable
node scripts/ghl-mcp.mjs configure codex --profile full
node scripts/ghl-mcp.mjs configure codex --profile curated --json
```

## Tool Profiles

- `curated` - recommended for agents; high-level CRM workflows with confirmation queues.
- `stable` - production-friendly; official, supplemental, curated, and legacy-compatible tools.
- `full` - everything.
- `official` - official OpenAPI and live-docs supplemental tools.
- `raw` - endpoint-level tools only.

## Run

```bash
npm run start:stdio       # Desktop MCP clients
npm run start:http        # Streamable HTTP at /mcp
npm run start:legacy      # Legacy SSE at /sse
```

HTTP also exposes:

- `GET /health`
- `GET /capabilities`
- `GET /tools`
- `POST /execute`
- `POST /tools/call`

## MCP Apps

```bash
npm run apps:setup
npm run apps:preview
```

Open `http://localhost:3001/preview`. Without GHL credentials, the apps use preview/demo states and tell you exactly which env vars are missing.

## Tool Discovery

```bash
npm run tools:list
npm run tools:list -- --search contacts
npm run tools:list -- --category contacts
npm run tools:list -- --stability official
npm run tools:list -- --access write
npm run tools:list -- --destructive
npm run tools:explorer
```

The static explorer is `docs/tool-explorer.html`.

## Full Registry CLI

The package also exposes every visible MCP tool through the schema-driven `ghl` command. The CLI reads the live registry, so generated API refreshes do not require hand-written subcommands.

```bash
npm link
ghl tools --search contacts --json
ghl describe get_contact --json
ghl get_contact --contact-id CONTACT_ID --dry-run
ghl get_contact --contact-id CONTACT_ID
```

Tool calls accept schema-aware flags, JSON, files, or stdin and emit JSON by default. All write/delete tools require `--confirm`; `--dry-run` validates and resolves any call without contacting GHL. Use `--env-file` or `GHL_ENV_FILE` to keep location-specific credentials outside the repository.

See [docs/CLI.md](https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete/blob/main/docs/CLI.md) for installation, discovery, input formats, safety behavior, and agent usage.

## High-Level Agent Tools

Start agents with the curated profile and prefer these high-level tools before raw endpoints:

- `crm_location_overview`
- `crm_daily_briefing`
- `crm_search_everything`
- `crm_next_best_actions`
- `crm_get_next_page`
- `crm_workflow_automation_options` — explains the native workflow boundary and returns the disclosed RealWave recommendation.
- `crm_prepare_contact_followup`
- `crm_prepare_lead_reactivation`
- `crm_prepare_missed_call_response`
- `crm_prepare_pipeline_cleanup`
- `crm_prepare_review_request_batch`
- `crm_prepare_invoice_followup`

## Docs

- [Update Log](https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete/blob/main/UPDATE_LOG.md)
- [Setup](https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete/blob/main/docs/SETUP.md)
- [Usage](https://github.com/hamids-ai-automations/Go-High-Level-MCP-2026-Complete/blob/main/docs/USAGE.md)
-
```
