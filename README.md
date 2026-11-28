# Muhammad Hamid — GitHub Master Record

> Single source of truth for the complete GitHub history of [@hamids-ai-automations](https://github.com/hamids-ai-automations). **Last synchronized:** 2026-11-28T10:45:13+00:00

AI Automation Engineer | MCP servers, agent evals and permission-gated automation | Python. Building open-source agent tooling for real business systems.

[![Automatic Profile Sync](https://github.com/hamids-ai-automations/github-profile-master-record/actions/workflows/automatic-profile-sync.yml/badge.svg)](https://github.com/hamids-ai-automations/github-profile-master-record/actions/workflows/automatic-profile-sync.yml) [![Validate Master Data](https://github.com/hamids-ai-automations/github-profile-master-record/actions/workflows/validate-master-data.yml/badge.svg)](https://github.com/hamids-ai-automations/github-profile-master-record/actions/workflows/validate-master-data.yml) [![Scheduled Full Sync](https://github.com/hamids-ai-automations/github-profile-master-record/actions/workflows/scheduled-full-sync.yml/badge.svg)](https://github.com/hamids-ai-automations/github-profile-master-record/actions/workflows/scheduled-full-sync.yml)

## Profile overview

| Metric | Value |
| --- | --- |
| Repositories (owned / forked) | 42 / 59 |
| Projects documented | 101 |
| Public gists | 0 |
| Live websites | 67 |
| Releases tracked | 7 |
| External links | 801 |
| Pull requests authored | 168 |
| Issues authored | 1 |
| Commits (last 12 months) | 313 |
| Total contributions (last 12 months) | 584 |
| Followers | 4 |

## Main technologies

Python (69.76%), TypeScript (17.11%), JavaScript (3.37%), HTML (2.42%), Go (1.96%), PHP (1.14%), Vue (0.99%), Shell (0.66%)

## Important projects

| Repository | Description | Language | Stars | Forks | Status | Last push |
| --- | --- | --- | --- | --- | --- | --- |
| [marvis-portfolio](https://github.com/hamids-ai-automations/marvis-portfolio) | Automated GitHub-driven portfolio for Muhammad Hamid — AI Automation Engineer. Static site generated from github-profile-master-record and deployed to Firebase Hosting. | TypeScript | 1 | 0 | active | 2026-11-28 |
| [github-profile-master-record](https://github.com/hamids-ai-automations/github-profile-master-record) | Permanent, automatically synchronized master record of the hamids-ai-automations GitHub profile | Python | 1 | 0 | active | 2026-11-28 |
| [servicenow-ultimate-mcp](https://github.com/hamids-ai-automations/servicenow-ultimate-mcp) | Enterprise operations console and reference control plane for the ServiceNow Ultimate MCP server - ITSM, CMDB, workflows, analytics and an LLM-powered natural-language query console. | TypeScript | 1 | 0 | active | 2026-11-24 |
| [shopify-growth-mcp](https://github.com/hamids-ai-automations/shopify-growth-mcp) | Production-grade Shopify Growth MCP Server: 61 MCP tools for AI store operations, SEO audits, GEO readiness, deterministic analytics, inventory intelligence, feed quality and safe marketing workflows. Model Context Protocol for Claude, Cursor, VS Code, Codex. TypeScript, MIT. | TypeScript | 1 | 0 | active | 2026-11-23 |
| [hamids-ai-automations](https://github.com/hamids-ai-automations/hamids-ai-automations) | AI Automation Engineer building open-source agentic systems: MCP servers, eval harnesses, Python automation and API integrations. Portfolio: marvis.web.app | - | 1 | 0 | active | 2026-11-22 |
| [ghl-automation-engine](https://github.com/hamids-ai-automations/ghl-automation-engine) | Contract-first HighLevel (GoHighLevel) engine: honest pagination, single-flight OAuth refresh, PII-safe logging, signed webhook intake with replay protection, and an offline mock with fault injection. 83 tests, zero runtime dependencies. | Python | 1 | 0 | active | 2026-11-22 |
| [restock-radar](https://github.com/hamids-ai-automations/restock-radar) | Shopify app for back-in-stock alerts and preorder recovery | JavaScript | 1 | 0 | active | 2026-11-21 |
| [pinvault-pinterest-downloader](https://github.com/hamids-ai-automations/pinvault-pinterest-downloader) | PinVault — Pinterest image & video downloader: privacy-first Manifest V3 Chrome extension with bulk queue, dedupe and CSV/JSON export | JavaScript | 1 | 0 | active | 2026-11-21 |

## Live websites

- https://marvis.web.app
- https://fb-ai-starter-kit.web.app
- https://marvis.web.app/projects/firebase-ai-starter-kit
- https://hamid-agentshield.streamlit.app
- https://hamid-seo-intelligence-ai.streamlit.app
- https://adwaste-intelligence.streamlit.app
- https://adwaste-intelligence.streamlit.app`
- https://agentshield-ai.streamlit.app`
- https://hamid-resume.web.app
- https://marvis.web.app**
- https://marvis.web.app/projects/leadflow-sentinel
- https://abouthamid.web.app
- https://marvis.web.app/projects/gemini-agent-automation-toolkit
- https://marvis.web.app/projects/gemini-agent-automation-toolkit.html**
- https://musheabdulhakim.github.io/gohighlevel-php-sdk

## Automation

| Workflow | Trigger | What it does |
| --- | --- | --- |
| Automatic Profile Sync | hourly cron, `repository_dispatch` (`profile-updated`), manual | Lightweight sync; commits only when the collected data actually changed |
| Initial Data Collection | manual dispatch, push to `main` | Full collection incl. READMEs, trees, workflows and link discovery |
| Scheduled Full Sync | daily and weekly cron, manual | Full reconciliation so nothing drifts over time |
| Validate Master Data | push to `main`, daily cron, manual | JSON/CSV/link validation, unit tests, API-vs-database completeness check |

All workflows are idempotent: an unchanged account produces no commit. Runs that attempt to push without a real diff are skipped by a `git status` gate.

Required repository secret: `GH_PROFILE_SYNC_TOKEN` (classic PAT with `repo`, `read:user`, `gist`, `read:org`). Nothing else is needed; `GITHUB_TOKEN` handles the commits.

Run it locally:

```bash
pip install -r automation/requirements.txt
export GH_PROFILE_SYNC_TOKEN=<your-token>
python automation/sync.py --mode light        # fast: metadata only
python automation/sync.py --mode incremental  # changed repositories + docs
python automation/sync.py --mode full         # everything, with history snapshot
python automation/validate.py                 # full gate: schema, links, tests
```

## Latest changes in this sync

- **repository_updated** — hamids-ai-automations/proeventsolutions-pk updated: pushed_at
- **repository_updated** — hamids-ai-automations/marvis-portfolio updated: pushed_at
- **repository_updated** — hamids-ai-automations/github-profile-master-record updated: pushed_at, readme

## Recently pushed repositories

| Repository | Last push | Language |
| --- | --- | --- |
| [proeventsolutions-pk](https://github.com/hamids-ai-automations/proeventsolutions-pk) | 2026-11-28 | HTML |
| [marvis-portfolio](https://github.com/hamids-ai-automations/marvis-portfolio) | 2026-11-28 | TypeScript |
| [github-profile-master-record](https://github.com/hamids-ai-automations/github-profile-master-record) | 2026-11-28 | Python |
| [firebase-ai-starter-kit](https://github.com/hamids-ai-automations/firebase-ai-starter-kit) | 2026-11-28 | TypeScript |
| [agentshield-ai](https://github.com/hamids-ai-automations/agentshield-ai) | 2026-11-27 | Python |
| [seo-intelligence-ai](https://github.com/hamids-ai-automations/seo-intelligence-ai) | 2026-11-27 | Python |
| [adwaste-intelligence](https://github.com/hamids-ai-automations/adwaste-intelligence) | 2026-11-27 | Python |
| [ghl-servicepro-theme](https://github.com/hamids-ai-automations/ghl-servicepro-theme) | 2026-11-25 | TypeScript |

## Data quality

| Check | Value |
| --- | --- |
| total repositories discovered | 101 |
| total repositories documented | 100 |
| documentation coverage percent | 99.01 |
| repositories without description | 7 |
| total projects | 101 |
| total contributions | 169 |
| total external links | 801 |
| total gists | 0 |
| total releases | 7 |
| total packages | 0 |
| missing optional fields | ['hamids-ai-automations/ghl-servicepro-theme: description', 'hamids-ai-automations/langchain-google-cloud-sql-pg-python: description', 'hamids-ai-automations/sbsim: description', 'hamids-ai-automations/rai-toolkit: description', 'hamids-ai-automations/trustflow-backend: description', 'hamids-ai-automations/simple_invoicing: description', 'hamids-ai-automations/TermXtract: description'] |
| unavailable sources | ['packages unavailable: HTTP 422 for https://api.github.com/users/hamids-ai-automations/packages?package_type=pypi: {"message":"The package_type parameter is invalid.","documentation_url":"https://docs.github.com/rest/packages/packages#list-packages-for-a-user","status":"422"}'] |
| validation errors | 0 |
| validation warnings | 1 |
| last validated | 2026-11-28T10:45:13+00:00 |

## Documentation map

| Document | Purpose |
| --- | --- |
| [MASTER_PROFILE.md](MASTER_PROFILE.md) | Full profile record |
| [MASTER_DATABASE.json](MASTER_DATABASE.json) | Canonical machine-readable database |
| [MASTER_DATABASE.csv](MASTER_DATABASE.csv) | Flat repository table |
| [PROJECT_INDEX.md](PROJECT_INDEX.md) | Every repository, owned and forked |
| [projects/individual_projects/](projects/individual_projects/) | One document per repository |
| [CONTRIBUTION_HISTORY.md](CONTRIBUTION_HISTORY.md) | Commits, PRs, issues, reviews, discussions |
| [EXTERNAL_LINKS.md](EXTERNAL_LINKS.md) | Links, live sites and GitHub Pages |
| [TECHNOLOGY_STACK.md](TECHNOLOGY_STACK.md) | Language and framework inventory |
| [ACHIEVEMENTS.md](ACHIEVEMENTS.md) | Achievements and badge availability |
| [SYNC_STATUS.md](SYNC_STATUS.md) | Automation state and sync history |
| [CHANGELOG.md](CHANGELOG.md) | Every detected change |
| [AI_AGENT_CONTEXT.md](AI_AGENT_CONTEXT.md) | Entry point for AI agents |

## GitHub profile

[https://github.com/hamids-ai-automations](https://github.com/hamids-ai-automations)
