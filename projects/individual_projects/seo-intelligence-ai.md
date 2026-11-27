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
| Size | 3251 KB |
| Topics | - |

## Objectives

# SEO Intelligence AI

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
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/seo-intelligence-ai/blob/main/README.md

```markdown
# SEO Intelligence AI

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
| **Hosted demo** | **Not deployed yet.** Streamlit Community Cloud needs an interactive GitHub OAuth login, which has not been completed. Run it locally: see [Local setup](#local-setup) |
| **App root** | `/` — the Overview page is the default route, so `/overview` returns 404 by design (see `PROJECT_PROGRESS.md` §5.9) |

Nothing in this repository is a live service; the screenshots below were taken from a local run.

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
| **Competitor Analysis** | `/competitors` | Scores up to a handful of public pages on the **same 100-point rubric**, then reports field average, leader, your gap to the leader, category gap table, radar comparison, side-by-side table and takeaways. Live fetch is a toggle; off means deterministic modelled snapshots. |
| **Backlink & Authority** | `/backlinks` | Builds a modelled authority profile from a domain: authority score, referring domains, total backlinks, dofollow ratio, monthly referring-domain trend, anchor-text mix, top referring domains and an outreach playbook. Saved profiles are listed. |

### Assist & deliver

| Page | Route | What it does |
|---|---|---|
| **AI SEO Assistant** | `/assistant` | Chat over the active audit. With a Gemini key, answers come from the model; without one, a built-in offline SEO playbook answers with concrete steps. "Ground the answer in the active audit" passes a trimmed finding summary as context — raw HTML is never sent. |
| **Reports** | `/reports` | Rebuilds any stored audit from its payload and exports it: **PDF** (ReportLab A4), **CSV** (UTF-8 with BOM) and **JSON**, plus "write all three to disk" into `reports/` and a payload preview. |

### Configure

| Page | Route | What it does |
|---|---|---|
| **Settings & Integrations** | `/settings` | Integration status for `GEMINI_API_KEY`, `PAGESPEED_API_KEY`, `OPENAI_API_KEY` (present/absent, source, masked value); default outbound-HTTP toggle; SQLite table counts and file size; "delete all stored data" danger zone; app/site/app-version metadata. |

### About

| Page | Route | What it does |
|---|---|---|
| **About Developer** 
```
