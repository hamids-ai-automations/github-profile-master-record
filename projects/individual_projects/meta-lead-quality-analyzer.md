# meta-lead-quality-analyzer

**Overview:** Open-source lead quality scoring & CRM revenue feedback engine for Meta Ads. Detects fake leads, disposable emails, bot form fatigue, and optimizes Cost-Per-Qualified-Lead (CPQL).

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/meta-lead-quality-analyzer](https://github.com/hamids-ai-automations/meta-lead-quality-analyzer) |
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
| Size | 600 KB |
| Topics | adtech, b2b-marketing, bot-detection, conversions-api, crm-integration, facebook-leads, hubspot, lead-generation, lead-quality, lead-scoring, meta-ads, offline-conversions, performance-marketing, python, salesforce, fake-leads |

## Objectives

# Meta Lead Quality Analyzer 🎯📋

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, data, docs, reports, src, tests
- **Total files (tracked in default branch):** 42
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 5

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 56097 |
| HTML | 8325 |

**Frameworks / libraries detected:** FastAPI, pandas, pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

pip install -e ".[dev]"
```

---

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app/

## Documentation links

- https://marvis.web.app
- https://abouthamid.web.app
- https://www.python.org/downloads
- https://www.linkedin.com/in/muhammad-hamid-digital-marketing
- http://mypy-lang.org
- https://opensource.org/licenses/MIT
- http://localhost:8000`

## Development status

Active — last push 2026-10-12

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

Full README: https://github.com/hamids-ai-automations/meta-lead-quality-analyzer/blob/main/README.md

```markdown
# Meta Lead Quality Analyzer 🎯📋

[![CI](https://github.com/hamid-digitalmarketer/meta-lead-quality-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/hamid-digitalmarketer/meta-lead-quality-analyzer/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](http://mypy-lang.org/)
[![Hire Me: Lead Gen Audits](https://img.shields.io/badge/Hire%20Me-Lead%20Gen%20Audits%20%26%20CAPI-2ea44f?style=flat-square&logo=googlechrome&logoColor=white)](https://abouthamid.web.app/)
[![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Muhammad%20Hamid-0077b5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammad-hamid-digital-marketing/)
[![Direct Email](https://img.shields.io/badge/Email-mhamidlad%40gmail.com-red?style=flat-square&logo=gmail&logoColor=white)](mailto:mhamidlad@gmail.com)

> **Diagnostic and quality audit engine for Meta Lead Ads (Instant Forms) and CRM pipelines.**  
> Detects disposable burner emails, fake telephone numbers, sub-5-second speed-clickers, and computes true **Cost-Per-Qualified-Lead (CPQL)** vs vanity front-end **Cost-Per-Lead (CPL)**. Generates automated **Meta Conversions API (CAPI) offline event payloads** for value optimization and custom audience exclusion lists.

---

![Meta Lead Quality Analyzer Audit Preview](https://raw.githubusercontent.com/hamids-ai-automations/meta-lead-quality-analyzer/main/docs/report_preview.png)

---

## ⚡ The Problem: Cheap Meta Leads That Never Close

Meta Lead Ads (Instant Forms) deliver extraordinary lead volume at low apparent front-end Cost-Per-Lead ($15–$30 CPL). However, sales and revenue teams frequently encounter severe drop-off:

1. **Auto-Fill Mis-clicks & Speed Bots**: Meta pre-populates lead forms with user profile data. Users scrolling Instagram Reels tap the ad, accidentally confirm the pre-filled form, and submit in $<5$ seconds without reading the offer.
2. **Burner Disposable Emails**: Users seeking downloadable PDFs or price sheets use throwaway temporary inboxes (`@mailinator.com`, `@tempmail.com`, `@guerrillamail.com`).
3. **Fictional Phone Numbers**: Users bypass mandatory phone fields with repeated digits (`5555555555`, `1234567890`) or reserved dummy prefixes.
4. **The CPL vs. CPQL Illusion**: While marketing celebrates a $25.00 CPL, sales only qualifies 1 in 8 leads, making the true Cost-Per-Qualified-Lead (CPQL) $200.00+. Meta's algorithm continues optimizing for cheap, low-intent volume because down-funnel sales qualification signals are never fed back.

**Meta Lead Quality Analyzer** audits your lead flow, calculates real acquisition economics, and automates closed-loop feedback to train Meta's algorithms on qualified pipeline.

---

## 🚀 Key Features

- 🔍 **5 Specialized Quality Analyzers**:
  - `DisposableEmailAnalyzer`: Flags temporary inboxes, throwaway domain providers, and dummy addresses.
  - `PhoneValidator`: Detects repeated digit spam, sequential keyboard inputs, and invalid formats.
  - `CompletionSpeedAnalyzer`: Flags sub-5-second submissions indicating auto-fill mis-clicks or bot scrapers.
  - `CustomQuestionAnalyzer`: Evaluates user answers to custom qualification questions for gibberish (`asdf`, `none`, `test`).
  - `CRMStageMatchAnalyzer`: Cross-references leads against CRM deal stages (`Qualified`, `Disqualified_Bad_Info`, `Won`), calculating true CPQL and junk lead percentage.
- 🔄 **Meta CAPI Offline Event Exporter**:
  - Generates ready-to-upload JSON payloads with SHA-256 normalized user matching (`QualifiedLead`, `WonDeal`) to feed back into Meta Advantage+ value optimization.
- 📋 **CRM Disqualification & Suppression List**:
  - Exports flagged leads to CSV for bulk CRM cleanup and Meta Custom Audience negative targeting.
- 📊 **Executive & Engineering Reports**:
  - **Interactive Tailwind CSS Dashboard**: Visual cards showing CPL vs True CPQL divergence, lead quality score, and filterable finding cards.
  - **JSON & Flat CSV Exports**: Machine-readable logs for data pipelines.
  - **SQLite Database Persistence**: Full audit history stored in `reports/lead_quality.sqlite`.
- 🔒 **100% Privacy & Local Execution**: Runs locally without transmitting sensitive CRM customer data externally.

---

## 📦 Installation

```bash
git clone https://github.com/hamid-digitalmarketer/meta-lead-quality-analyzer.git
cd meta-lead-quality-analyzer

# Install package in editable mode with development tools
pip install -e ".[dev]"
```

---

## 🛠️ Quick Start

### 1. Run Audit with Built-in Datasets
Test the diagnostic engine immediately using realistic synthetic multi-campaign datasets:

```bash
meta-lead audit
```

To automatically launch the interactive HTML report in your browser:
```bash
meta-lead audit --open-browser
```

### 2. Audit Your Own Meta Leads & CRM Data
Pass your Meta Lead Ads export CSV and CRM deal stages export CSV:

```bash
meta-lead audit \
  --leads path/to/meta_instant_leads.csv \
  --crm path/to/crm_lead_stages.csv \
  --out-dir ./reports \
  --open-browser
```

### 3. Quick Single Lead Verification
Validate contact information and form completion duration:

```bash
meta-lead validate-lead --email "user@tempmail.com" --phone "5555555555" --duration 2.5
```

### 4. Serve the Web Dashboard Locally
```bash
meta-lead serve --port 8000
```
Browse your latest audit at `http://localhost:8000`.

---

## 💻 Programmatic Python API

```python
from pathlib import Path
from meta_lead_quality_analyzer.data.loader import load_crm_deals, load_meta_leads
from meta_lead_quality_analyzer.analyzers import (
    DisposableEmailAnalyzer,
    PhoneValidator,
    CompletionSpeedAnalyzer,
    CRMStageMatchAnalyzer,
)
from meta_lead_quality_analyzer.report import ReportGenerator

# Load CSV data
leads = load_meta_leads("data/sample_data/meta_instant_leads.csv")
crm = load_crm_deals("data/sample_data/crm_lead_stages.csv")

# Run quality checks
findings = []
findings.extend(DisposableEmailAnalyzer().analyze(leads))
findings.extend(PhoneValidator().analyze(leads))
findings.extend(CompletionSpeedAnalyzer().analyze(leads))

crm_findings, total_spend, fe_cpl, qual_count, true_cpql, junk_count, junk_pct, crm_disq = (
    CRMStageMatchAnalyzer().analyze(leads, crm)
)
findings.extend(crm_findings)

print(f"Front-End CPL: ${fe_cpl:.2f} | True CPQL: ${true_cpql:.2f} | Junk Rate: {junk_pct}%")
```

---

## 📁 Repository Structure

```
meta-lead-quality-analyzer/
├── .github/
│   ├── ISSUE_TEMPLATE/        # Bug report and feature request templates
│   ├── workflows/ci.yml       # GitHub Actions CI matrix (Python 3.11, 3.12)
│   └── pull_request_template.md
├── data/
│   ├── loader.py              # Ingestion utilities
│   └── sample_data/           # Synthetic real-world test datasets
│       ├── meta_instant_leads.csv
│       └── crm_lead_stages.csv
├── docs/
│   ├── architecture.md        # Technical pipeline architecture
│   ├── lead_quality_guide.md  # Failure taxonomy & remediation
│   ├── usage.md               # CLI & API guide
│   └── report_preview.png     # Dashboard screenshot
├── reports/                   # Audit outputs (.html, .json, .csv, .sqlite)
├── src/meta_lead_quality_analyzer/
│   ├── analyzers/             # 5 Quality diagnostic engines
│   │   ├── disposable_email.py
│   │   ├── phone_validator.py
│   │   ├── completion_speed.py
│   │   ├── custom_question_analyzer.py
│   │   └── crm_stage_match.py
│   ├── exporters/             # CAPI offline and CRM suppression exporters
│   │   ├── meta_capi_offline.py
│   │   └── crm_disqualification_list.py
│   ├── templates/             # Jinja2 Tailwind CSS report template
│   │   └── report.html
│ 
```
