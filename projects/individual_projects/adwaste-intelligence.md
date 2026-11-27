# adwaste-intelligence

**Overview:** Google Ads Waste Detector — N-Gram Audit Engine: 1-4 gram search-term waste analysis, converting-query conflict guard, and Excel/Ads Editor exports.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/adwaste-intelligence](https://github.com/hamids-ai-automations/adwaste-intelligence) |
| Live website | https://adwaste-intelligence.streamlit.app |
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
| Pull requests (open / merged) | 9 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 1253 KB |
| Topics | adtech, google-ads, n-gram, negative-keywords, ppc, python, sem, streamlit |

## Objectives

# AdWaste Intelligence

## Features

| | Feature | Why it matters |
|---|---|---|
| 1 | **Bulletproof Google Ads ingestion** | Handles 2-row metadata headers, `Total:` summary rows, UTF-16, tab/semicolon/comma delimiters, `$` / `AED` / `PKR` / `€` / `£` / `INR` currencies, `--` and `< 10%` placeholders, ragged rows, and variant column names. Falls back to a manual column-mapping UI if a required column is missing. |
| 2 | **One-click demo account** | Deterministic 1,500-term B2B SaaS + Home Services account (`$37,297.43` spend, deliberate waste clusters) so visitors experience every workflow in 2 seconds with zero file upload needed. |
| 3 | **Vectorized 1–4 gram engine** | Rolls up cost, impressions, clicks, conversions, CTR, CPC, Conv. Rate, CPA, and ROAS per n-gram with **zero intra-query double-counting**. Includes a 50,000-row performance benchmark guard in `tests/`. |
| 4 | **Configurable waste rules** | Auto-initialized Target CPA, CPA bleeder multiplier, zero-conversion spend threshold, min-clicks gating, brand-term whitelist protection, bundled stopword exclusion (1-grams only), and 4 preset negative-intent dictionaries (Job Seekers, Free/Cheap/Piracy, DIY/Academic, Existing Customer/Support). |
| 5 | **Executive dashboard** | 5 KPI cards (Total Spend Analyzed, Flagged Wasted Spend, Projected Annualized Savings, Wasted Search Terms, Wasted N-Grams), spend-allocation donut, top-15 wasted n-grams bar chart, and campaign-level waste breakdown. |
| 6 | **N-gram explorer with drill-down** | Filter by n-gram level (1–4), campaign, match type, flagged-only, min spend, and text search; stage rows via checkboxes; inspect every raw search term behind any n-gram. |
| 7 | **Conflict guard (key differentiator)** | Cross-checks every staged negative keyword (Exact / Phrase / Broad match semantics) against all **converting** search terms, quantifies blocked conversions and conversion value, and strips conflicts with one click. |
| 8 | **3 export channels** | Copy-paste block for Google Ads UI, Google Ads Editor CSV (`Campaign, Ad group, Keyword, Criterion Type`), and a formatted multi-tab Excel client audit workbook (`.xlsx` built in-memory). |
| 9 | **Optional AI intent audit (BYOK)** | Supply a `GEMINI_API_KEY` (runtime input, env var, or `st.secrets`) to classify up to 100 top non-converting terms into High Commercial Intent / Informational / Competitor / Job / Irrelevant. Works 100% offline/free without a key. |

---

## Technical architecture

- **Top-level directories:** .github, .streamlit, assets, docs, scripts, src, tests
- **Total files (tracked in default branch):** 43
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 6

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 153363 |

**Frameworks / libraries detected:** NumPy, Streamlit, pandas, pytest

**Dependencies:** google-genai, numpy, openpyxl, pandas, plotly, streamlit

## Important source files

- `app.py`
- `pyproject.toml`
- `requirements.txt`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://adwaste-intelligence.streamlit.app

## Documentation links

- https://marvis.web.app
- https://wa.me/923167417135
- https://adwaste-intelligence.streamlit.app
- https://adwaste-intelligence.streamlit.app`
- https://www.python.org/downloads
- https://streamlit.io
- https://share.streamlit.io
- http://localhost:8501`
- https:

## Development status

Active — last push 2026-11-27

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/adwaste-intelligence/blob/main/README.md

```markdown
# AdWaste Intelligence

**Google Ads Waste Detector — N-Gram Audit Engine**

[![CI](https://github.com/hamids-ai-automations/adwaste-intelligence/actions/workflows/ci.yml/badge.svg)](https://github.com/hamids-ai-automations/adwaste-intelligence/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-059669?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Streamlit 1.67+](https://img.shields.io/badge/streamlit-1.67%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/license-MIT-0F172A)](LICENSE)

> Companion web SaaS to the **Google Ads Waste Detector** Chrome extension.
> Upload any Google Ads Search Terms report (`.csv` or `.xlsx`) — or load the
> 1,500-term demo account — to run a full 1–4 gram waste audit, block conflicting
> negatives before they harm converting queries, and export ready-to-paste lists
> and client-ready Excel audit workbooks in under 60 seconds.
>
> **Privacy-first: 100% in-memory processing. Client CSV data is never written to disk, stored, or logged.**

---

## Status

| | |
|---|---|
| **Repository** | [hamids-ai-automations/adwaste-intelligence](https://github.com/hamids-ai-automations/adwaste-intelligence) — public |
| **CI** | `.github/workflows/ci.yml` runs `ruff check`, `pytest` (with `src/` coverage), headless `AppTest` smoke (`scripts/smoke_pages.py`), committed-secrets guard, `pip-audit`, and `gitleaks` across Python 3.11 & 3.12 |
| **Hosted demo** | Target URL: `https://adwaste-intelligence.streamlit.app` — **pending Streamlit Community Cloud interactive OAuth link** (see [Deployment status](https://github.com/hamids-ai-automations/adwaste-intelligence/blob/main/DEPLOYMENT_STATUS.md) and [Deploy on Streamlit Community Cloud](#deploy-on-streamlit-community-cloud)) |
| **Local run** | Fully verified with demo mode ($37,297.43 spend, 18.5% flagged waste, $81.2k projected annual savings) and messy Google Ads CSV/XLSX ingestion |

---

## Table of Contents

- [What it does](#what-it-does)
- [Screenshots](#screenshots)
- [Quickstart (local)](#quickstart-local)
- [Quality checks & testing](#quality-checks--testing)
- [Deploy on Streamlit Community Cloud](#deploy-on-streamlit-community-cloud)
- [Project structure & architecture](#project-structure--architecture)
- [How wasted spend is calculated](#how-wasted-spend-is-calculated)
- [Privacy & security](#privacy--security)
- [Documentation](#documentation)
- [Author](#author)
- [License](#license)

---

## What it does

| | Feature | Why it matters |
|---|---|---|
| 1 | **Bulletproof Google Ads ingestion** | Handles 2-row metadata headers, `Total:` summary rows, UTF-16, tab/semicolon/comma delimiters, `$` / `AED` / `PKR` / `€` / `£` / `INR` currencies, `--` and `< 10%` placeholders, ragged rows, and variant column names. Falls back to a manual column-mapping UI if a required column is missing. |
| 2 | **One-click demo account** | Deterministic 1,500-term B2B SaaS + Home Services account (`$37,297.43` spend, deliberate waste clusters) so visitors experience every workflow in 2 seconds with zero file upload needed. |
| 3 | **Vectorized 1–4 gram engine** | Rolls up cost, impressions, clicks, conversions, CTR, CPC, Conv. Rate, CPA, and ROAS per n-gram with **zero intra-query double-counting**. Includes a 50,000-row performance benchmark guard in `tests/`. |
| 4 | **Configurable waste rules** | Auto-initialized Target CPA, CPA bleeder multiplier, zero-conversion spend threshold, min-clicks gating, brand-term whitelist protection, bundled stopword exclusion (1-grams only), and 4 preset negative-intent dictionaries (Job Seekers, Free/Cheap/Piracy, DIY/Academic, Existing Customer/Support). |
| 5 | **Executive dashboard** | 5 KPI cards (Total Spend Analyzed, Flagged Wasted Spend, Projected Annualized Savings, Wasted Search Terms, Wasted N-Grams), spend-allocation donut, top-15 wasted n-grams bar chart, and campaign-level waste breakdown. |
| 6 | **N-gram explorer with drill-down** | Filter by n-gram level (1–4), campaign, match type, flagged-only, min spend, and text search; stage rows via checkboxes; inspect every raw search term behind any n-gram. |
| 7 | **Conflict guard (key differentiator)** | Cross-checks every staged negative keyword (Exact / Phrase / Broad match semantics) against all **converting** search terms, quantifies blocked conversions and conversion value, and strips conflicts with one click. |
| 8 | **3 export channels** | Copy-paste block for Google Ads UI, Google Ads Editor CSV (`Campaign, Ad group, Keyword, Criterion Type`), and a formatted multi-tab Excel client audit workbook (`.xlsx` built in-memory). |
| 9 | **Optional AI intent audit (BYOK)** | Supply a `GEMINI_API_KEY` (runtime input, env var, or `st.secrets`) to classify up to 100 top non-converting terms into High Commercial Intent / Informational / Competitor / Job / Irrelevant. Works 100% offline/free without a key. |

---

## Screenshots

Captured from a local run (`streamlit run app.py`, headless Chromium 1600px wide, light theme) using the built-in **1,500-term Demo Account**.

### 1 · Landing & Privacy-First Uploader
![Landing](https://raw.githubusercontent.com/hamids-ai-automations/adwaste-intelligence/main/assets/screenshots/01-landing.png)

### 2 · Tab 1 — Executive Waste Overview
![Executive Waste Overview](https://raw.githubusercontent.com/hamids-ai-automations/adwaste-intelligence/main/assets/screenshots/02-overview.png)

### 3 · Tab 2 — N-Gram Intelligence Explorer & Drill-Down
![N-Gram Intelligence Explorer](https://raw.githubusercontent.com/hamids-ai-automations/adwaste-intelligence/main/assets/screenshots/03-ngram-explorer.png)

### 4 · Tab 3 — Search Term Auditor & Optional Gemini AI Intent
![Search Term Auditor](https://raw.githubusercontent.com/hamids-ai-automations/adwaste-intelligence/main/assets/screenshots/04-term-auditor.png)

### 5 · Tab 4 — Negative Builder, Conflict Guard & Exports
![Negative Builder and Conflict Guard](https://raw.githubusercontent.com/hamids-ai-automations/adwaste-intelligence/main/assets/screenshots/05-negative-builder.png)

---

## Quickstart (local)

Requirements: **Python 3.11+**

```bash
git clone https://github.com/hamids-ai-automations/adwaste-intelligence.git
cd adwaste-intelligence

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501` and click **Load Demo Account (1,500 Search Terms)** — no CSV export required.

---

## Quality checks & testing

Install development tooling and run the exact gates enforced by CI:

```bash
pip install -r requirements-dev.txt
ruff check .
pytest --cov=src --cov-report=term-missing
python scripts/smoke_pages.py
```

The test suite covers messy Google Ads CSVs & XLSX roundtrips (metadata rows, ragged totals, UTF-16, currencies, placeholders, column aliases, manual mapping fallback), 1–4 gram aggregation invariants (intra-query deduplication, stopword handling, drill-down), waste rules & brand whitelist protection, match-type conflict detection, copy-paste/CSV/Excel exports, mocked Gemini audit parsing, UI helpers/charts, headless `AppTest` integration, and a 50,000-row performance benchmark.

---

## Deploy on Streamlit Community Cloud

1. Open [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
2. Click **New app** → **From existing repo** → select `hamids-ai-automations/adwaste-intelligence`.
3. Set branch to `main`, **Main file path** to **`app.py`**, and Python to **3.11** or **3.12**.
4. Click **Deploy** — `requirements.txt` needs no `packages.txt` OS binaries.

### Optional secrets

Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` locally (git-ignored) or add keys under **App settings → Secrets** in Streamlit Community Cloud:

```toml
GEMINI_API_KEY = "your-key"              # enables optional BYOK AI intent audit
CHROME_EXTENSION_URL = "ht
```
