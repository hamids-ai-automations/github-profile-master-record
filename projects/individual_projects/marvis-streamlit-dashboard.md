# marvis-streamlit-dashboard

**Overview:** MARVIS - GitHub Profile & Professional Work Intelligence Dashboard powered by github-profile-master-record

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/marvis-streamlit-dashboard](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-11-28 |
| Last update | 2026-11-28 |
| Last push | 2026-11-28 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 363 KB |
| Topics | - |

## Objectives

# MARVIS — GitHub Profile & Professional Work Intelligence Dashboard

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, .streamlit, app_pages, assets, docs, src, tests
- **Total files (tracked in default branch):** 58
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 15

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 256715 |

**Frameworks / libraries detected:** Streamlit, pandas, pytest, requests

**Dependencies:** google-genai, pandas, pillow, pydantic, reportlab, requests, streamlit

## Important source files

- `pyproject.toml`
- `requirements.txt`

## Installation and setup

No installation instructions found in the README.

## Deployment

No deployment configuration detected.

## Documentation links

- https://marvis.web.app
- https://wa.me/923167417135
- https://www.python.org/downloads
- https://streamlit.io
- https://share.streamlit.io

## Development status

Active — last push 2026-11-28

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/README.md

```markdown
# MARVIS — GitHub Profile & Professional Work Intelligence Dashboard

[![CI](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit 1.67+](https://img.shields.io/badge/streamlit-1.67%2B-FF4B4B.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**MARVIS** is a read-only, live-synchronized Streamlit intelligence hub and public portfolio for **Muhammad Hamid** (`@hamids-ai-automations`), powered directly by the canonical GitHub master record repository [`hamids-ai-automations/github-profile-master-record`](https://github.com/hamids-ai-automations/github-profile-master-record).

> **Public Portfolio:** [marvis.web.app](https://marvis.web.app/) · **GitHub:** [@hamids-ai-automations](https://github.com/hamids-ai-automations) · **WhatsApp:** [+92 316 7417135](https://wa.me/923167417135)

---

## What MARVIS Does

Instead of maintaining a static, manually edited portfolio, MARVIS fetches, validates, normalizes, and visualizes Muhammad Hamid's canonical GitHub database (`MASTER_DATABASE.json`) and supplemental index documents in real time:

1. **Executive Dashboard** — Live dynamically computed KPIs (total, owned, forked, archived repositories, live websites, contributions, commits, pull requests, releases), pinned flagships, language breakdown, and recently updated repositories.
2. **Repository Explorer** — Searchable, filterable, sortable, paginated explorer across all 101+ repositories (zero omitted), with rich detail views and on-demand loading of individual `projects/individual_projects/<slug>.md` dossiers.
3. **Project Portfolio & Case Studies** — Domain-organized portfolio (MCP Servers, AI Agents & LLM Automation, AI Security & DevSecOps, GoHighLevel & CRM, E-Commerce & Shopify, SEO & Search Intelligence, AdTech & Marketing Analytics, Websites & SaaS) with strictly factual case-study breakdowns.
4. **Development Activity & Timeline** — Daily & monthly contribution trends, commit counts by repository, authored pull requests & issues, software releases, sync change logs, and explicit disclosure of historical gaps.
5. **Skills & Technology Intelligence** — Clearly separates **profile-documented capabilities** (from GitHub Profile README) from **repository-inferred technologies** (languages, frameworks, dependencies, CI/test tooling).
6. **Websites & External Work Directory** — Filterable directory of live sites, documentation, APIs, and business profiles linked back to owning repositories, with opt-in, SSRF-guarded reachability verification.
7. **Achievements & Professional History** — Chronological milestones, releases, merged upstream PRs, and honest `unverified`/`unavailable` badge status tracking.
8. **AI Career & Project Analyst** — Runs 100% deterministically without an API key (citation-backed queries, CV draft, monthly report, gap audit) and supports optional live synthesis via Google Gemini (`google-genai`, `gemini-3.8-flash`) configured via Streamlit Secrets.
9. **Synchronization & Data Health Center** — Displays master commit SHA, dual timestamps (`source_synced_at` vs `app_fetched_at`), cache TTL, schema/URL audits, cross-document consistency checks, manual refresh trigger, and full JSON/CSV/Markdown/PDF export downloads.

---

## Architecture & Data Sources

```
github-profile-master-record (Read-Only Source of Truth)
  ├── MASTER_DATABASE.json          (Canonical machine-readable DB)
  ├── projects/projects_index.json  (Project docs & live URL mapping)
  ├── repositories/repositories_index.json
  ├── README.md, SYNC_STATUS.md, MASTER_PROFILE.md, AI_AGENT_CONTEXT.md
  └── projects/individual_projects/<slug>.md (Fetched lazily on demand)
          │
          ▼ HTTPS GET (retries + timeout + @st.cache_data(ttl=300))
marvis-streamlit-dashboard
  ├── streamlit_app.py              (st.navigation entrypoint + sidebar controls)
  ├── app_pages/                    (9 flat Streamlit page scripts)
  ├── src/marvis/                   (Pure domain logic, Pydantic v2, analytics, exports, AI)
  └── tests/                        (Offline unit tests + AppTest UI smoke suite)
```

Read deeper documentation in [`docs/`](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/docs/):
- [`docs/ARCHITECTURE.md`](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/docs/ARCHITECTURE.md)
- [`docs/DATA_MAPPING.md`](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/docs/DATA_MAPPING.md)
- [`docs/DATA_DICTIONARY.md`](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/docs/DATA_DICTIONARY.md)
- [`docs/SYNCHRONIZATION.md`](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/docs/SYNCHRONIZATION.md)
- [`docs/SECURITY.md`](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/docs/SECURITY.md)
- [`docs/DEPLOYMENT.md`](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/docs/DEPLOYMENT.md)
- [`docs/DEVELOPMENT_GUIDE.md`](https://github.com/hamids-ai-automations/marvis-streamlit-dashboard/blob/main/docs/DEVELOPMENT_GUIDE.md)

---

## Synchronization Mechanism

- **Code sync:** Pushing updates to `hamids-ai-automations/marvis-streamlit-dashboard` (`main`) triggers Streamlit Community Cloud to redeploy application code.
- **Data sync:** When `github-profile-master-record` receives automated hourly/daily/weekly commits, MARVIS automatically refreshes from raw GitHub URLs after the `300`-second `@st.cache_data` TTL expires—or immediately when clicking **Refresh master data** in the sidebar or Sync & Data Health page—with no app redeployment required.
- **Resilience:** Each successful load is stored in `st.session_state["last_good_snapshot"]`. If GitHub is temporarily unreachable, MARVIS continues serving the last valid snapshot with an explicit stale-fallback warning.

---

## Local Installation & Running

```bash
git clone https://github.com/hamids-ai-automations/marvis-streamlit-dashboard.git
cd marvis-streamlit-dashboard

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

Run tests, linting, and type-checking:

```bash
python -m pip install -r requirements-dev.txt
pytest
ruff check .
ty check
```

---

## Optional Gemini & GitHub Configuration

MARVIS works out-of-the-box with **zero secrets**. To enable live Gemini conversational analysis or higher GitHub REST API rate limits, configure Streamlit Secrets locally in `.streamlit/secrets.toml` (never commit!) or in Streamlit Community Cloud **App Settings → Secrets**:

```toml
# Optional: unlocks Google Gemini synthesis in AI Career Analyst
GEMINI_API_KEY = "your-gemini-api-key"

# Optional: raises GitHub REST API rate limit from 60/hr to 5,000/hr for commit SHA display
GITHUB_TOKEN = "your-read-only-github-pat"
```

Environment variable overrides (`.env.example`) are also supported (`MARVIS_CACHE_TTL_SECONDS`, `MARVIS_GEMINI_MODEL`, `MARVIS_MASTER_OWNER`, `MARVIS_MASTER_REPO`, `MARVIS_MASTER_BRANCH`).

---

## Streamlit Community Cloud Deployment

Select these exact settings when creating the app on [share.streamlit.io](https://share.streamlit.io/):

| Setting | Value |
| --- | --- |
| **Repository** | `hamids-ai-automations/marvis-streamlit-dashboard` |
| **Branch** | `main` |
| **Main file path** | `streamlit_app.py` |
| **Suggested App URL** | `marvis-work-hub` |

---

## Security & GitHub Actions

- Strictly read-only: never modifies `github-profile-master-record` or `marvis.web.app`.
- No hardcoded secrets; `.gitignore` excludes `.env`, `.env.*`, and `.streamlit/secrets.toml`.
- Hop-by-hop SSRF validation
```
