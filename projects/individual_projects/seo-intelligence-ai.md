# seo-intelligence-ai

**Overview:** Autonomous SEO audit platform - 100-point scoring engine, 31 rules across 6 families, SSRF-guarded crawler, 13-page Streamlit UI, JSON/CSV/PDF reports, Gemini + PageSpeed integrations

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/seo-intelligence-ai](https://github.com/hamids-ai-automations/seo-intelligence-ai) |
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
| Size | 3262 KB |
| Topics | - |

## Objectives

---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_eb52be59e9fa11f1961f525400f8a581
    ReservedCode1: U9cxipT1hjvnawc2nfjaVyBInAkedlz5U2B6SyNpX0/uH7ZqbKWCN5XsOR50hXavweEpmjYh/2nYFSQERE63rkSbeTzgydV4wARL6VQL+LI/9+xezeQiJx31yDJ+vfKhY/ULNB+qgWdTDxs/BsQ62uKwGM/kcNDhJk68/N//NEuigjPryZZnIEhe4/A=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_eb52be59e9fa11f1961f525400f8a581
    ReservedCode2: U9cxipT1hjvnawc2nfjaVyBInAkedlz5U2B6SyNpX0/uH7ZqbKWCN5XsOR50hXavweEpmjYh/2nYFSQERE63

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, .streamlit, app_pages, assets, database, docs, modules, scripts, tests, ui
- **Total files (tracked in default branch):** 68
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 6

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 307862 |

**Frameworks / libraries detected:** BeautifulSoup, NumPy, Streamlit, pandas, pytest, requests

**Dependencies:** altair, beautifulsoup4, numpy, pandas, pydantic, reportlab, requests, streamlit

## Important source files

- `app.py`
- `pyproject.toml`
- `requirements.txt`

## Installation and setup

No installation instructions found in the README.

## Deployment

No deployment configuration detected.

## Documentation links

- https://hamid-seo-intelligence-ai.streamlit.app
- http://localhost:8501

## Development status

Active — last push 2026-11-27

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/marvis-streamlit-dashboard
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/seo-intelligence-ai/blob/main/README.md

```markdown
---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_eb52be59e9fa11f1961f525400f8a581
    ReservedCode1: U9cxipT1hjvnawc2nfjaVyBInAkedlz5U2B6SyNpX0/uH7ZqbKWCN5XsOR50hXavweEpmjYh/2nYFSQERE63rkSbeTzgydV4wARL6VQL+LI/9+xezeQiJx31yDJ+vfKhY/ULNB+qgWdTDxs/BsQ62uKwGM/kcNDhJk68/N//NEuigjPryZZnIEhe4/A=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_eb52be59e9fa11f1961f525400f8a581
    ReservedCode2: U9cxipT1hjvnawc2nfjaVyBInAkedlz5U2B6SyNpX0/uH7ZqbKWCN5XsOR50hXavweEpmjYh/2nYFSQERE63rkSbeTzgydV4wARL6VQL+LI/9+xezeQiJx31yDJ+vfKhY/ULNB+qgWdTDxs/BsQ62uKwGM/kcNDhJk68/N//NEuigjPryZZnIEhe4/A=
---

# SEO Intelligence AI

[![Live demo](https://img.shields.io/badge/live%20demo-hamid--seo--intelligence--ai.streamlit.app-FF4B4B?logo=streamlit&logoColor=white)](https://hamid-seo-intelligence-ai.streamlit.app/)

**▶ Live demo — <https://hamid-seo-intelligence-ai.streamlit.app/>**
Hosted on Streamlit Community Cloud. No install, no API keys, no sign-in: the app opens on the Overview page.

> AI-powered website audit & growth intelligence — an offline-first Streamlit workspace by Muhammad Hamid.

SEO Intelligence AI audits a public page against a **31-rule, 100-point SEO rubric**, explains every point
it deducted, and then carries the same audit into performance, keyword, content, competitor and backlink
workflows. Every number the app shows is labelled with its provenance: a real fetch, a bundled sample, a
deterministic model, or a measured PageSpeed Insights call.

The app is designed to be **fully demonstrable with no API keys and no network**: three bundled sample
sites ship with the repo, and every modelled data source is tagged as modelled instead of pretending to be
measured.

---

## Status

| | |
|---|---|
| **Repository** | [hamids-ai-automations/seo-intelligence-ai](https://github.com/hamids-ai-automations/seo-intelligence-ai) — public, first commit `0cc3aaa` |
| **CI** | Green — `.github/workflows/ci.yml` runs `ruff check`, `pytest` (95 tests) and a headless render gate over all 13 pages |
| **Hosted demo** | **Live** — <https://hamid-seo-intelligence-ai.streamlit.app/> on Streamlit Community Cloud (repo `hamids-ai-automations/seo-intelligence-ai`, branch `main`, entrypoint `app.py`; Python 3.14.10, streamlit 1.67.0) |
| **Hosted data** | The cloud instance starts on a **fresh, empty SQLite database**; the numbers you see there come from the bundled sample audit. Local `data/` is git-ignored and is never uploaded |
| **App root** | `/` — the Overview page is the default route, so `/overview` returns 404 by design (see `PROJECT_PROGRESS.md` §5.9) |

The screenshots below were captured from a local run and match the hosted layout. The deployment details,
build log and operational caveats live in [`DEPLOYMENT_STATUS.md`](https://github.com/hamids-ai-automations/seo-intelligence-ai/blob/main/DEPLOYMENT_STATUS.md).

---

## Table of contents

- [What this is (and what it is not)](#what-this-is-and-what-it-is-not)
- [Feature overview](#feature-overview)
- [Scoring model](#scoring-model)
- [Architecture](#architecture)
- [Local setup](#local-setup)
- [Running the checks](#running-the-checks)
- [Optional API keys](#optional-api-keys)
- [Data, storage and privacy](#data-storage-and-privacy)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Project documentation](#project-documentation)
- [Tech stack](#tech-stack)
- [License](#license)

---

## What this is (and what it is not)

**Is**

- A deterministic SEO audit engine: 31 explicit rules across 6 categories, each rule declaring its own point
  value, severity, recommendation and reference.
- A multi-page analysis workspace: audit, Core Web Vitals, keyword planning, content analysis, competitor
  comparison, backlink profiling, an assistant, a report exporter and a settings surface.
- Offline-first. Sample sites, modelled keyword demand, modelled backlink
  profiles and an offline assistant playbook all work with no keys and no internet.
- Local by default. History lives in a single SQLite file; nothing is uploaded anywhere.

**Is not**

- **Not a rank tracker.** No Google Search Console, Google Analytics or Google Ads integration is
  implemented. No ranking positions, impressions or ad data are read or stored.
- **Not a crawler.** It audits **one URL per run** (plus `robots.txt` and `/sitemap.xml` probes). There is no
  site-wide crawl, no sitemap fan-out, no JavaScript rendering.
- **Not a keyword-volume provider.** Difficulty, volume bands, CPC bands and opportunity scores are computed
  deterministically from the seed text (`source: modelled`). No third-party keyword API is bundled.
- **Not a backlink database.** Referring domains, authority score and anchor mixes are deterministic models
  derived from the domain string. The Backlink page says so on every surface.
- **Not a hosted service.** It is a Streamlit app you run yourself.

---

## Feature overview

Navigation is declared once in `app.py` with `st.navigation` — 13 pages in 5 groups.

### Audit

| Page | Route | What it does |
|---|---|---|
| **Overview** | `/overview` | Score, grade, failed-check and critical counts for the active audit; "do these three first" priority queue; audit provenance; score-history line chart; recent audits table; quick-audit form (URL + keyword, or a bundled sample). |
| **SEO Auditor** | `/auditor` | The rulebook surface: run an audit (live crawl or sample, mobile/desktop strategy, optional PageSpeed), then inspect results as **Cards** (failed checks with fix text), **Table** (all findings), **All rules** (pass/warn/fail/skip per rule) and **Page facts** (final URL, status, HTML size, title, description, H1s, canonical, robots meta, lang, viewport, images, links, word count). Exports JSON/CSV in place. |
| **Technical SEO Analyzer** | `/technical` | The technical family in isolation: the six technical checks (HTTPS, canonical, robots meta, viewport, structured data, language) worth 25 points, with a technical-weight gauge, earned-vs-available points per check, the crawler's observed signals (final URL, status, HTML size, canonical, robots meta, viewport, lang, JSON-LD and social-tag counts), robots.txt/sitemap state, and the same run-audit form as the auditor. |
| **On-Page SEO Analyzer** | `/on-page` | The on-page family in isolation: the seven on-page checks worth 25 points, a rendered SERP-snippet preview built from the crawled title and description, a field-length table against the configured title/meta targets, the heading outline, and the four `content_keyword_*` placements for the target keyword. |
| **PageSpeed & Performance** | `/pagespeed` | Core Web Vitals for the active audit (LCP, CLS, INP, FCP, TTFB, TBT) with the threshold each metric is judged against, "what to fix, in order", a re-measure control (mobile/desktop), and performance-category findings. Without an API key the numbers are the documented offline heuristic and are labelled as such. |

### Growth intelligence

| Page | Route | What it does |
|---|---|---|
| **Keyword Intelligence** | `/keywords` | Seed → prioritised plan: intent, cluster, difficulty, volume band, CPC band, opportunity score and a written rationale per keyword. Market/language/idea-count controls, intent mix pie, cluster rollup, difficulty-vs-opportunity bars, secondary keywords, CSV export, plan persistence, and a hand-off button that sends the keyword to the Content page. |
| **Content Intelligence** | `/content` | Two tabs. **Analyse draft**: word count vs the 600-word baseline, Flesch reading ease, keyword density band, title/description length checks, heading-outline issues. **Build brief**: suggested title/meta/outline/talking points/internal-link ideas, Markdown + JSON preview and Markdown download. |
| **Competitor Analysis** | `/competitors` | Scores up to a handful of public pages on the **same 100-point rubric**, then reports field average, leader,
```
