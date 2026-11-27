# agentshield-ai

**Overview:** AI agent security scanner and governance console - prompt-injection analysis, telemetry dashboard, risk scoring, PDF/JSON/CSV reports, built with Streamlit

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/agentshield-ai](https://github.com/hamids-ai-automations/agentshield-ai) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-11-26 |
| Last update | 2026-11-26 |
| Last push | 2026-11-27 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 1000 KB |
| Topics | - |

## Objectives

# AgentShield AI

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, .streamlit, app_pages, assets, database, modules, scripts, tests, ui
- **Total files (tracked in default branch):** 48
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 6

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 250234 |

**Frameworks / libraries detected:** NumPy, Streamlit, pandas, pytest, requests

**Dependencies:** PyYAML, altair, numpy, pandas, reportlab, requests, streamlit

## Important source files

- `app.py`
- `pyproject.toml`
- `requirements.txt`

## Installation and setup

```bash
git clone https://github.com/hamids-ai-automations/agentshield-ai.git
cd agentshield-ai

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

The app opens on <http://localhost:8501>. Use **Load demo workspace** in the sidebar (or the
Dashboard button) to populate it with sample scans, prompts and telemetry.

## Deployment

No deployment configuration detected.

## Documentation links

- https://marvis.web.app
- https://www.python.org/downloads
- https://streamlit.io
- https://share.streamlit.io
- http://localhost:8501

## Development status

Active — last push 2026-11-27

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

- [ ] SARIF export for GitHub code scanning
- [ ] Configurable rule packs (per-framework templates for LangChain / CrewAI / MCP)
- [ ] Diff view: posture delta between two scans of the same agent
- [ ] Multi-tenant PostgreSQL backend
- [ ] Scheduled re-scans with regression alerts

---

## README source

Full README: https://github.com/hamids-ai-automations/agentshield-ai/blob/main/README.md

```markdown
# AgentShield AI

**AI security scanning & governance console for agentic systems — built with Python and Streamlit.**

AgentShield AI statically analyses AI agent configurations, detects leaked credentials and
over-permissive tool grants, scores prompt-injection risk, tracks runtime telemetry, and
produces audit-ready reports. Every check runs locally: uploaded configurations are parsed as
inert text and are never executed, and secrets are redacted before they reach the UI or disk.

[![CI](https://github.com/hamids-ai-automations/agentshield-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/hamids-ai-automations/agentshield-ai/actions/workflows/ci.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Streamlit 1.67](https://img.shields.io/badge/streamlit-1.67-FF4B4B.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Status

| | |
|---|---|
| **Repository** | [hamids-ai-automations/agentshield-ai](https://github.com/hamids-ai-automations/agentshield-ai) — public, `658ca9b` |
| **CI** | Green on `52d211a` — `.github/workflows/ci.yml` runs `ruff check`, `pytest` (34 tests with coverage), a headless `AppTest` render pass over all six pages, `pip-audit` and a committed-secrets guard |
| **Hosted demo** | **Not deployed yet.** Streamlit Community Cloud requires an interactive GitHub OAuth login, which has not been completed — run it locally, see [Getting started](#getting-started) |
| **Data** | SQLite under `data/` (git-ignored); a fresh clone starts empty, use **Load demo workspace** |

Nothing here is a live service. The screenshots below were captured from a local run.

---

## Screenshots

Six full-page captures from the running app (Chromium, viewport 1600×1000, full-page, light theme) against a
local database holding three saved scans and 22 findings, so charts and KPI strips show real data rather than
mocks. Files live in `assets/screenshots/`.

**Dashboard** — portfolio posture, severity mix, findings trend, category heat and recent activity.
![Dashboard](https://raw.githubusercontent.com/hamids-ai-automations/agentshield-ai/main/assets/screenshots/01-dashboard.png)

**Security scanner** — grade, severity filter and per-finding evidence/remediation from a static config scan.
![Security scanner](https://raw.githubusercontent.com/hamids-ai-automations/agentshield-ai/main/assets/screenshots/02-scanner.png)

**Prompt analyzer** — risk band, matched injection families and a defanged preview safe to paste into a ticket.
![Prompt analyzer](https://raw.githubusercontent.com/hamids-ai-automations/agentshield-ai/main/assets/screenshots/03-prompts.png)

**Agent monitoring** — KPI strip plus volume/spend, failure-rate, latency and token-mix charts over real telemetry.
![Agent monitoring](https://raw.githubusercontent.com/hamids-ai-automations/agentshield-ai/main/assets/screenshots/04-monitoring.png)

**AI assistant** — grounded chat; without a key it answers from the offline knowledge base.
![AI assistant](https://raw.githubusercontent.com/hamids-ai-automations/agentshield-ai/main/assets/screenshots/05-assistant.png)

**Reports** — executive summary, fix-first priorities and PDF/JSON/CSV export.
![Reports](https://raw.githubusercontent.com/hamids-ai-automations/agentshield-ai/main/assets/screenshots/06-reports.png)

---

## Why this project exists

Agentic systems fail differently from traditional apps. The blast radius is defined by three
things that are almost never reviewed: **what the agent can call** (tool grants), **what it can
read** (secrets and scopes), and **what it will obey** (prompt handling). AgentShield AI turns
those three questions into a repeatable, scored review that a security team can run before an
agent reaches production — and re-run after every configuration change.

---

## Features

### 1. Security Scanner (`/scanner`)
- Accepts agent configurations as **JSON / YAML / TOML / .env / plain text**, via upload, paste,
  or bundled reference samples.
- **Static analysis only** — content is parsed with safe loaders; nothing is imported, evaluated
  or executed. Files above 512 KB are refused.
- Detects: wildcard tool grants, dangerous tool families (shell, filesystem write, browser,
  payment), unbounded autonomy/recursion, missing human approval, disabled logging, exposed
  system prompts, and unguarded PII handling.
- **Secrets detector** with provider-aware patterns (OpenAI, Anthropic, Google, AWS, GitHub,
  Slack, Stripe, private keys, JWTs) plus entropy heuristics and `.env`-style assignments.
  Evidence is truncated and masked (`sk-live…9f2a`), never printed in full.
- Findings carry severity, category, evidence excerpt, remediation and an OWASP LLM Top 10
  reference.

### 2. Prompt Analyzer (`/prompts`)
- Scores a single prompt or a batch of prompts against 16 rule-based injection families:
  instruction override, role hijack, jailbreak personas, policy-bypass requests, system-prompt
  extraction, indirect injection (markup/template payloads), shell invocation, credential
  exfiltration, concealment ("do not tell the user"), social pressure, unbounded recursion,
  leetspeak obfuscation, base64/hex payloads, invisible/bidi characters and oversize prompts.
- Weighted 0–100 risk score with banding (safe / low / medium / high / critical) and
  per-signal remediation guidance.
- Produces a **defanged preview** (zero-width and control characters stripped, truncation) that is
  safe to paste into a ticket.

### 3. Agent Monitoring (`/monitoring`)
- Ingests agent run telemetry: model, tokens in/out, latency, cost, status, error type.
- KPI strip (runs, tokens, spend, error rate) plus Altair charts for volume/spend, failure rate,
  p95 latency and token mix — all timezone-safe and filtered by window/model/status.
- Manual event entry and full event log for triage.

### 4. AI Assistant (`/assistant`)
- Gemini / OpenAI-compatible chat that explains findings, prioritises fixes and drafts hardened
  configuration snippets.
- **Works fully offline**: without an API key it answers from a deterministic knowledge base
  built on the same rule catalogue, so the app is always demo-able.
- API keys are read from `st.secrets` / environment variables, held in memory only, never logged
  or rendered.
- Export the whole conversation or a generated remediation plan as Markdown.

### 5. Reports (`/reports`)
- Rehydrates saved scans and renders a Markdown executive summary.
- One-click **PDF** (ReportLab, severity colour-coding, fix-first table), **JSON** and **CSV**
  exports with timestamped, filesystem-safe filenames.
- Fix-first prioritisation groups findings into actions so a reviewer knows what to do next.

### 6. Dashboard (`/dashboard`)
- Portfolio posture: average and worst score, severity mix, findings trend, category heat, recent
  activity feed and latest prompt-risk readings.
- One-click **demo workspace** seeding (3 sample configs, 3 prompt analyses, 14 days of telemetry)
  and a guarded "clear all data" action.

---

## Scoring model

The posture score starts at 100 and deducts per finding, with **diminishing returns for repeats**
of the same severity so a single noisy rule cannot dominate:

| Severity | Deduction | Grade band |
|---|---|---|
| Critical | 22 | **A** ≥ 90 · hardened |
| High | 11 | **B** ≥ 80 · solid, minor gaps |
| Medium | 5 | **C** ≥ 70 · internal pilots only |
| Low | 2 | **D** ≥ 60 · restrict autonomy |
| Info | 0 | **F** < 60 · do not deploy |

Prompt risk uses additive signal weights, capped at 100:
`critical ≥ 70 · high ≥ 45 · medium ≥ 25 · low ≥ 1 · safe = 0`.

---

## Architecture

```
agentshield-ai/
├── app.py                      # entry point: st.navigation + sidebar + demo/clear actions
├── app_pages/                  # one module per route (content only, no config)
│   ├── 1_Dashboard.py
│   ├── 2_Security_Scanner.py
│   ├── 3_Prompt_Analyzer.py
│   ├── 4_Agent_Monitoring.py
│   ├
```
