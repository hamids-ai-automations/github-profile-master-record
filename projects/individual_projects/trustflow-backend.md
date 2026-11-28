# trustflow-backend

**Overview:** _No repository description provided._

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/trustflow-backend](https://github.com/hamids-ai-automations/trustflow-backend) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-31 |
| Last update | 2026-10-31 |
| Last push | 2026-11-01 |
| Default branch | main |
| License | none declared |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 88 |
| Size | 3095 KB |
| Topics | - |

## Objectives

# 🔧 TrustFlow Core — Backend API

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, .vscode, backend, docs
- **Total files (tracked in default branch):** 443
- **CI workflows:** .github/workflows/README.md, .github/workflows/backend-ci.yml, .github/workflows/scheduled-backups.yml
- **Test files detected:** 149

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 1895457 |
| Shell | 33587 |
| JavaScript | 8813 |
| Dockerfile | 1093 |

**Frameworks / libraries detected:** none detected from dependency files

**Dependencies:** none detected

## Important source files

- `backend/package.json`
- `backend/tsconfig.json`
- `docker-compose.yml`
- `package.json`

## Installation and setup

```bash
npm install
```

## Deployment

No deployment configuration detected.

## Documentation links

- https://opensource.org/licenses/MIT
- https://soroban-testnet.stellar.org
- https://horizon-testnet.stellar.org
- http://localhost:3001/api/docs`
- http://localhost:3001/api/docs-json`
- http://localhost:3001/auth/challenge?address=GXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- http://localhost:3001/auth/verify
- http://localhost:3001/escrows
- https://docs.trustflow.xyz
- https://stellar.org/community

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/marvis-portfolio
- hamids-ai-automations/firebase-ai-starter-kit
- hamids-ai-automations/ghl-servicepro-theme
- hamids-ai-automations/servicenow-ultimate-mcp
- hamids-ai-automations/shopify-growth-mcp

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/trustflow-backend/blob/main/README.md

```markdown
# 🔧 TrustFlow Core — Backend API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **The off-chain backbone of the TrustFlow Protocol.**

TrustFlow Core is the backend API service that powers off-chain logic for the TrustFlow gig-economy platform. Built with NestJS and TypeScript, it bridges the Stellar/Soroban blockchain with real-world application features — handling authentication, escrow state management, webhook delivery, and Prometheus-grade observability.

---

## ✨ Core Features.

- 🔐 **JWT Authentication with Wallet Signatures**: Secure wallet-based auth using Stellar signature verification. Users authenticate by signing a cryptographic challenge with their Freighter wallet, proving ownership without exposing private keys.
- 💼 **Escrow Management**: Full CRUD API for escrow entities — creation, funding, milestone tracking.
- 🌐 **Stellar Integration**: Native Horizon and Soroban RPC helpers for on-chain reads and writes.
- 🔔 **Webhook Engine**: Event-driven webhook dispatch with automatic retry logic.
- 📊 **Monitoring & Metrics**: Built-in Prometheus metrics, health checks, and alerting helpers.
- 🛡️ **Distributed Rate Limiting**: Redis-backed per-IP and per-wallet token buckets with sliding-window abuse detection and temporary lockouts.

---

## 🗂️ Project Structure

```
backend/
└── src/
    ├── admin/                  # Read-only protocol analytics dashboard (admin-only)
    ├── auth/                   # Wallet-signature JWT auth — challenge/verify, nonce store, guard
    ├── common/                 # Cross-cutting: rate limiting, Redis client, idempotency, pagination, logging, DB, filters
    ├── config/                 # Zod-validated env config, .env loading
    ├── deliverable/            # Gig deliverable submission and review
    ├── dispute/                # Dispute resolution saga (juror voting, resolution)
    ├── escrow/                 # Escrow vault CRUD, milestone release, disputes
    ├── escrow-reconciliation/  # Reconciles off-chain escrow state against on-chain Soroban state
    ├── escrow-write/           # Builds unsigned Soroban release transactions for client signing
    ├── event-ingestion/        # Polls Soroban RPC for contract events, feeds the outbox
    ├── gig/                    # Gig solicitation postings — accept/cancel, auto-expiry sweep
    ├── ipfs-pinning/           # Multi-provider IPFS pinning (Pinata/Web3.Storage/Infura) with failover
    ├── migration/              # Schema migration registry/runner (admin-triggered run/rollback)
    ├── milestone-notifications/# WebSocket gateway for milestone/escrow event notifications
    ├── monitoring/             # Health checks (`/health`) and Prometheus metrics (`/metrics`)
    ├── notification/           # Shared notification dispatch types/service
    ├── outbox/                 # Transactional outbox relay to WebSocket/webhooks/workers
    ├── reputation/             # Wallet reputation scoring with time decay
    ├── sentry/                 # Sentry error-monitoring integration
    ├── soroban-event-indexer/  # Indexes raw Soroban events into Redis for `/events/soroban`
    ├── stellar/                # Horizon/Soroban RPC clients, failover, network config
    ├── testing/                # Shared test doubles (fake Redis client)
    ├── user-profile/           # Wallet-linked user profiles — search, ratings, verification
    ├── webhook/                # Webhook registration/dispatch, HMAC signing, Discord notifications
    └── main.ts                 # App entry point
```

---

## 🚀 Getting Started

### Prerequisites

- Node.js >= 20
- A Stellar RPC endpoint (testnet or mainnet)
- Freighter wallet (for client-side wallet signature testing)

### Installation

```bash
npm install
```

### Environment Setup

Copy the example env file into `backend/` (where the app looks for it) and fill in your values:

```bash
cd backend
cp ../.env.example .env
```

Key variables:

```env
JWT_SECRET=your-secret
SOROBAN_RPC_URL=https://soroban-testnet.stellar.org
STELLAR_HORIZON_URL=https://horizon-testnet.stellar.org
REDIS_URL=redis://localhost:6379
RATE_LIMIT_ABUSE_WINDOW_SECONDS=300
RATE_LIMIT_ABUSE_THRESHOLD=5
RATE_LIMIT_LOCKOUT_SECONDS=900
# allow (fail open, default) or deny (503 + Retry-After) when Redis is down; /auth/* always denies
RATE_LIMIT_ON_REDIS_ERROR=allow
REDIS_COMMAND_TIMEOUT_MS=1000
```

See [`.env.example`](https://github.com/hamids-ai-automations/trustflow-backend/blob/main/.env.example) for the full list of variables, including optional IPFS, database, and admin settings.

**What dependencies are required?** See [Runtime Dependencies](https://github.com/hamids-ai-automations/trustflow-backend/blob/main/docs/runtime-dependencies.md) for a detailed breakdown of each external service (Redis, PostgreSQL, Stellar, IPFS, etc.), what happens when they're unset or down, and which are mandatory for production.

### Running

```bash
# Development
cd backend
npm run dev

# Production
npm run build && npm start

# Run tests
npm test

# Run CI checks locally
./scripts/ci-check.sh
```

See [Backend Setup Instructions](https://github.com/hamids-ai-automations/trustflow-backend/blob/main/backend/SETUP_INSTRUCTIONS.md) for detailed development workflow.

---

## 📖 API Modules

### 📚 Interactive API Documentation

**Swagger UI**: `http://localhost:3001/api/docs`  
**OpenAPI JSON**: `http://localhost:3001/api/docs-json`
(Disabled in production unless `SWAGGER_ENABLED=true`; protect with `SWAGGER_USER`/`SWAGGER_PASSWORD`.)

Full guide: [API Documentation](https://github.com/hamids-ai-automations/trustflow-backend/blob/main/backend/API_DOCUMENTATION.md)

### 🗂️ Off-Chain State Model

[docs/state-model.md](https://github.com/hamids-ai-automations/trustflow-backend/blob/main/docs/state-model.md) — Reference for the Escrow, Gig, and DisputeSaga state
machines: which transitions are driven by API calls, on-chain Soroban events, or background workers,
plus a catalogue of known deviations from the intended model.

### All Route Prefixes

| Controller path | Auth required | Swagger tag |
| --- | --- | --- |
| `/auth` | No (issues the JWT) | Authentication |
| `/escrows` | No (IP rate-limited only) | Escrow |
| `/webhooks` | No (IP rate-limited only) | Webhooks |
| `/health`, `/metrics` | No | Monitoring |
| `/gigs` | Partial — reads public, writes require JWT | Gigs |
| `/profiles` | Partial — reads public (never include the email address), writes and `GET /profiles/me` require JWT | User Profiles |
| `/deliverables` | Yes (JWT) | Deliverables |
| `/dispute` | Yes (JWT) | Dispute Resolution |
| `/reputation` | No | Reputation |
| `/ipfs/pins` | Yes (JWT) | IPFS Pinning |
| `/outbox` | Yes (JWT) | Outbox |
| `/escrow-reconciliation` | Yes (JWT) | Escrow Reconciliation |
| `/event-ingestion` | No | Event Ingestion |
| `/events/soroban` | No | Soroban Events |
| `/stellar` | No | Stellar |
| `/rpc-status` | Yes (JWT) | RPC Status |
| `/migrations` | Yes (JWT + admin allow-list) | Schema Migrations |
| `/admin/analytics` | Yes (JWT + admin allow-list) | Admin |

### Auth (`/auth`)

- **`GET /auth/challenge`** — Get authentication challenge for wallet signing
- **`POST /auth/verify`** — Verify wallet signature, returns JWT
- JWT Guard protects downstream routes that require it (see table above — several routes are intentionally public and rely on IP-scoped rate limiting instead).

#### Authentication Flow

1. **Request Challenge**: Client requests a cryptographic challenge for their wallet address
2. **Sign Challenge**: User signs the challenge with their Freighter wallet
3. **Verify & Get Token**: Client sends the signature to verify and receive a JWT token
4. **Use Token**: Include JWT in Authorization header for authenticated requests

#### Example Usage

```bash
# 1. Get challenge
curl "http://localhost:3001/auth/challenge?address=GXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# 2. Sign challenge with Freighter wa
```
