# seo-doctor

**Overview:** Open-source technical SEO crawler: broken links, canonical validation, crawl comparison and SEO health scoring. Python CLI.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/seo-doctor](https://github.com/hamids-ai-automations/seo-doctor) |
| Live website | https://marvis.web.app/ |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-12 |
| Last update | 2026-11-20 |
| Last push | 2026-10-12 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 1 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 578 KB |
| Topics | broken-link-checker, canonical-tags, cli, core-web-vitals, digital-marketing, on-page-seo, python, seo, seo-audit, seo-tools, site-crawler, technical-seo |

## Objectives

# SEO-Doctor 🩺

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, docs, examples, reports, src, tests
- **Total files (tracked in default branch):** 51
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 8

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 100750 |
| HTML | 16691 |

**Frameworks / libraries detected:** BeautifulSoup, FastAPI, pandas, pytest, requests

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app/

## Documentation links

- https://marvis.web.app
- https://www.python.org/downloads
- https://abouthamid.web.app
- https://www.linkedin.com/in/muhammad-hamid-digital-marketing
- http://localhost:8000
- https://example.com
- https://example.com/checkout
- https://example.com/pricing
- http://127.0.0.1:8000/index.html
- http://127.0.0.1:8000/sitemap.xml

## Development status

Active — last push 2026-10-12

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/seo-doctor/blob/main/README.md

```markdown
# SEO-Doctor 🩺

[![CI Pipeline](https://github.com/hamid-digitalmarketer/seo-doctor/actions/workflows/ci.yml/badge.svg)](https://github.com/hamid-digitalmarketer/seo-doctor/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests: 23/23 Passing](https://img.shields.io/badge/tests-23%2F23%20passed-success.svg)](tests/)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type Checked: Mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://github.com/python/mypy)
[![Hire Me: Technical SEO Audits](https://img.shields.io/badge/Hire%20Me-SEO%20Audits%20%26%20Consulting-2ea44f?style=flat-square&logo=googlechrome&logoColor=white)](https://abouthamid.web.app/)
[![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Muhammad%20Hamid-0077b5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammad-hamid-digital-marketing/)
[![Direct Email](https://img.shields.io/badge/Email-mhamidlad%40gmail.com-red?style=flat-square&logo=gmail&logoColor=white)](mailto:mhamidlad@gmail.com)
[![Cost: $0.00 Free](https://img.shields.io/badge/cost-%240.00%20free-brightgreen.svg)](#pricing--free-open-source)

A free, production-grade, open-source **technical SEO auditor, crawler, and site diagnostics engine**. Designed for business owners, SEO freelancers, marketing agencies, and web developers who need to identify indexing blockers, broken link equity, duplicate metadata, canonical tag conflicts, and crawl regressions—**without expensive monthly software subscriptions**.

---

## 📌 Executive Overview: Why Technical SEO Auditing Matters

Website owners frequently encounter discouraging organic search bottlenecks:
- *Why is my website not ranking on Google?*
- *Why are my newly published product pages not indexed?*
- *Which pages leak link equity through 404 dead ends or redirect chains?*
- *Did our recent staging deployment accidentally break canonical tags or introduce `noindex` directives?*

Most commercial tools (Screaming Frog, Ahrefs, Semrush) charge $120–$500/month or enforce strict URL caps. **SEO-Doctor** runs locally on your machine, respects target servers, detects technical search bottlenecks, prioritizes fixes into clear actionable tiers, and produces executive-ready **HTML, CSV, and JSON** audit reports.

---

## 📸 Interactive HTML Audit Dashboard

SEO-Doctor generates a standalone, responsive HTML report featuring a technical health score ring, critical blocker callouts, and filterable diagnostic tables:

![SEO-Doctor Report Preview](https://raw.githubusercontent.com/hamids-ai-automations/seo-doctor/main/docs/report_preview.png)

---

## ⚡ Key Capabilities & Diagnostic Checks

SEO-Doctor audits your website across 10 specialized technical disciplines:

| Diagnostic Check | Issues Detected | Impact Level |
| :--- | :--- | :---: |
| **1. Broken Links** | Internal 404s, 500 server crashes, and broken external links | `CRITICAL` / `MEDIUM` |
| **2. Redirects** | Multi-hop redirect chains (2+ hops), redirect loops, temporary 302s | `CRITICAL` / `HIGH` |
| **3. Metadata** | Missing `<title>`, duplicate titles, short/long titles, missing/duplicate meta descriptions | `CRITICAL` / `HIGH` |
| **4. Headings** | Missing `<h1>`, multiple conflicting `<h1>` tags, skipped hierarchy levels (e.g. H1 $\to$ H3) | `HIGH` / `LOW` |
| **5. Canonical Tags** | Missing canonicals, multiple canonical tags, canonicals pointing to 404s or redirects | `CRITICAL` / `HIGH` |
| **6. Robots Directives** | Meta robots `noindex`/`nofollow`, `X-Robots-Tag` headers, and `robots.txt` disallows | `CRITICAL` / `HIGH` |
| **7. Images** | Missing `alt` attributes, empty `alt` on content images, broken image sources | `HIGH` / `MEDIUM` |
| **8. XML Sitemaps** | Missing `sitemap.xml`, dead 404 URLs in sitemap, sitemap URLs redirecting or noindexed | `CRITICAL` / `HIGH` |
| **9. Orphan Pages** | URLs discoverable in sitemaps that have 0 internal inbound links across the site | `HIGH` |
| **10. Indexability** | HTTP 4xx/5xx responses, thin body content (< 100 words), connection timeouts | `CRITICAL` / `LOW` |

---

## 🔄 Crawl Comparison (Tracking Regressions & Fixes)

SEO-Doctor includes built-in comparison to track changes between two crawl runs:

```bash
seo-doctor compare reports/run-2026-01-01.json reports/run-2026-02-01.json
```

**Terminal Comparison Output:**
```text
+--------------------------------------------------------------------+
| [?] Crawl Comparison Audit                                         |
| Baseline:   https://example.com (2026-01-01T12:00:00)              |
| Comparison: https://example.com (2026-02-01T12:00:00)              |
+--------------------------------------------------------------------+
               Score & Issue Delta
+-----------------------------------------------+
| Metric        | Baseline | Comparison | Delta |
|---------------+----------+------------+-------|
| Health Score  | 70       | 85         | +15   |
| Total Issues  | 14       | 6          | -8    |
| Pages Crawled | 120      | 124        | +4    |
+-----------------------------------------------+

[+] Issues Fixed (8):
  + https://example.com/checkout - broken_internal_link
  + https://example.com/pricing  - missing_canonical

[!] Issues Introduced (0):
  (No new technical regressions detected)
```

---

## 🚀 Installation & Quickstart

### Prerequisites
- Python 3.11+
- Git

### 1. Installation
```bash
git clone https://github.com/hamid-digitalmarketer/seo-doctor.git
cd seo-doctor
pip install -e .
```

### 2. Run Your First Crawl
```bash
# Audit any website up to 50 pages
seo-doctor crawl https://example.com --max-pages 50
```

### 3. Generated Report Artifacts
Each audit automatically exports three structured files into `./reports`:
- `reports/crawl-<timestamp>.html` — Interactive visual dashboard for clients & executives.
- `reports/crawl-<timestamp>.csv` — Spreadsheet for development ticket backlogs.
- `reports/crawl-<timestamp>.json` — Machine-readable dataset for automated diffs and CI/CD.

### 4. Launch Local Web Viewer
Browse and inspect historical reports directly in your browser:
```bash
seo-doctor serve --port 8000
```
Visit **[http://localhost:8000](http://localhost:8000)**.

---

## 🧪 Testing with the Included Sample Site

SEO-Doctor includes a pre-configured sample site with intentional SEO defects (`examples/sample-site`):

```bash
# 1. Start local mock site
python -m http.server 8000 --directory examples/sample-site

# 2. In another terminal, run audit against the sample site
seo-doctor crawl http://127.0.0.1:8000/index.html --sitemap http://127.0.0.1:8000/sitemap.xml
```

The audit will immediately detect:
- Broken internal links pointing to `/dead-single-origin-404.html`
- Multiple `<h1>` headings on `about.html`
- Duplicate title and meta description between `index.html` and `duplicate-meta-page.html`
- Orphan page candidate `orphan-page.html` listed in sitemap but having 0 inbound links
- Conflicting canonical tags and image tags missing `alt` attributes

---

## 🛡️ Security, Politeness & Ethical Guidelines

- **Configurable Rate Limiting**: Defaults to `--delay 0.05` seconds between requests to avoid overloading origin servers.
- **`robots.txt` Compliance**: Reads and enforces `robots.txt` disallow rules by default (`--respect-robots-txt`).
- **No Private Data Storage**: Does not store customer personal data, login credentials, or ad tokens.
- **Non-Aggressive Footprint**: User-Agent header is configurable (`--user-agent`).
- **Deterministic**: Does not require external LLM APIs for core auditing, guaranteeing zero cloud token costs and reproducible output.

---

## 📂 Repository Structure

```
seo-doctor/
├── .github/
│   ├── workflows/ci.yml             # GitHub Actions CI (Ruff, Mypy, Pytest)
│   ├── ISSUE_TE
```
