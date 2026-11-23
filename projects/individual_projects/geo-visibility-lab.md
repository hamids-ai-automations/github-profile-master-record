# geo-visibility-lab

**Overview:** Open-source Local SEO & Google Business Profile (GBP) proximity rank tracker. Audits 5x5 geo-grids, aggregator NAP citation drift, review velocity decay, and exports Schema.org JSON-LD.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/geo-visibility-lab](https://github.com/hamids-ai-automations/geo-visibility-lab) |
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
| Size | 601 KB |
| Topics | citation-audit, geo-grid, geojson, google-business-profile, json-ld, local-pack, local-search, local-seo, maps-seo, martech, nap-consistency, python, rank-tracker, schema-org, seo-audit, review-velocity |

## Objectives

# GeoVisibilityLab 🗺️

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
| Python | 58453 |
| HTML | 10736 |

**Frameworks / libraries detected:** FastAPI, pandas, pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

```bash

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app/

## Documentation links

- https://marvis.web.app
- https://abouthamid.web.app
- https://www.linkedin.com/in/muhammad-hamid-digital-marketing
- https://www.python.org
- http://mypy-lang.org
- https://www.apexdentalcare-example.com

## Development status

Active — last push 2026-10-12

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine
- hamids-ai-automations/gemini-agent-reliability-kit
- hamids-ai-automations/envscope

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/geo-visibility-lab/blob/main/README.md

```markdown
# GeoVisibilityLab 🗺️

[![CI](https://github.com/hamid-digitalmarketer/geo-visibility-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/hamid-digitalmarketer/geo-visibility-lab/actions/workflows/ci.yml)
[![Python 3.10 | 3.11 | 3.12](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](http://mypy-lang.org/)
[![Hire Me: Local SEO Audits](https://img.shields.io/badge/Hire%20Me-Local%20SEO%20%26%20GBP%20Audits-2ea44f?style=flat-square&logo=googlechrome&logoColor=white)](https://abouthamid.web.app/)
[![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Muhammad%20Hamid-0077b5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammad-hamid-digital-marketing/)
[![Direct Email](https://img.shields.io/badge/Email-mhamidlad%40gmail.com-red?style=flat-square&logo=gmail&logoColor=white)](mailto:mhamidlad@gmail.com)

> **Open-Source Local SEO Proximity Matrix, NAP Consistency & Review Velocity Engine.** Audit Google Business Profile ranking drop-offs across geographic coordinates, detect aggregator citation drift, forecast review velocity decay, and generate production-ready Schema.org JSON-LD and GeoJSON heatmaps.

---

## Visual Dashboard Preview

![GeoVisibilityLab Dashboard Preview](https://raw.githubusercontent.com/hamids-ai-automations/geo-visibility-lab/main/docs/report_preview.png)

*Interactive audit dashboard featuring a 5x5 proximity rank heatmap, citation consistency audit, review velocity trajectory, and LocalBusiness JSON-LD markup generator.*

---

## The Problem

Local SEO success hinges on geographical proximity, accurate citations across aggregators, and consistent review velocity. Yet marketing teams and multi-location agencies struggle with:

1. **Ranking Blindspots Beyond 2 Miles**: Traditional single-location rank trackers report one rank for an entire city, missing severe ranking drops just blocks away.
2. **Aggregator NAP Citation Drift**: Inconsistencies in Name, Address, or Phone across Yelp, Apple Maps, Bing, and Facebook quietly erode Google Local Pack trust signals.
3. **Review Velocity Decay & Drought**: Stalled customer reviews trigger algorithmic demotion in local search packs before business owners notice.
4. **Manual Schema & GIS Workflows**: Converting local performance into actionable Schema.org structured data or GIS heatmaps requires fragmented tools.

**GeoVisibilityLab** provides an automated, programmatic pipeline to evaluate proximity grids, audit aggregator citations, monitor review momentum, and export structured data.

---

## Core Capabilities

- **📍 Geo-Grid Proximity Ranking Analyzer**: Evaluates coordinate grids (e.g. 5x5 or 7x7) to calculate Average Rank Position (ARP), Share of Voice in the Top 3 Map Pack (SoV%), rank volatility, and maximum drop-off radius.
- **🏢 NAP Citation Consistency Engine**: Calculates Levenshtein string similarity against canonical business credentials across major directories (Google, Yelp, Bing, Apple Maps, YellowPages, Facebook). Flags critical mismatches that penalize local pack ranking.
- **⭐ Review Velocity & Reputation Decay Monitor**: Computes 30-day vs historical monthly review velocity, identifies review droughts (>14 days without a customer review), evaluates recent rating trends, and surfaces customer sentiment risks.
- **📄 LocalBusiness Schema.org JSON-LD Generator**: Instantly produces valid, search-engine-ready `DentalClinic`, `MedicalClinic`, `Restaurant`, `LegalService`, or generic `LocalBusiness` JSON-LD structured markup.
- **🗺️ GeoJSON Proximity Heatmap Exporter**: Exports RFC 7946 compliant GeoJSON FeatureCollections colored by ranking tier (Top 3 green, 4-10 yellow, 10+ red) for direct visualization in Kepler.gl, Mapbox, or QGIS.
- **📊 Modern Tailwind CSS Dashboard**: Zero-dependency standalone HTML audit report featuring interactive SVG proximity grids, severity breakdown pills, actionable recommendations, and multi-format exports (HTML, JSON, CSV).
- **🚀 Embedded Web Server**: Launch and inspect reports locally with `geo-lab serve`.

---

## Quickstart

### Installation

```bash
# Clone repository
git clone https://github.com/hamid-digitalmarketer/geo-visibility-lab.git
cd geo-visibility-lab

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```

### Run Audit via CLI

Run a comprehensive audit using included synthetic datasets:

```bash
# Run full local SEO audit and generate HTML, JSON, and CSV reports
geo-lab audit --out-dir reports

# View the generated dashboard in your browser
# reports/geo_audit_report.html
```

### Serve Local Dashboard

Launch the built-in FastAPI web server to inspect reports interactively:

```bash
geo-lab serve --report-dir reports --port 8000
```

### Generate LocalBusiness Schema.org Markup

```bash
geo-lab generate-schema \
  --name "Apex Dental Care" \
  --business-type "DentalClinic" \
  --address "1204 Market St, San Francisco, CA 94102" \
  --phone "+1 415-555-0192" \
  --url "https://www.apexdentalcare-example.com" \
  --out-file schema.json
```

---

## CLI Command Reference

| Command | Arguments | Description |
|---|---|---|
| `geo-lab audit` | `--grid-file`, `--citations-file`, `--reviews-file`, `--canonical-name`, `--canonical-phone`, `--canonical-address`, `--business-type`, `--out-dir` | Runs all 3 analyzers, generates summary scores, exports Schema & GeoJSON, and outputs HTML/JSON/CSV reports |
| `geo-lab generate-schema` | `--name`, `--business-type`, `--address`, `--phone`, `--url`, `--out-file` | Generates Google-compliant LocalBusiness Schema.org JSON-LD |
| `geo-lab serve` | `--report-dir`, `--port` | Serves generated audit reports locally via FastAPI/Uvicorn |
| `geo-lab version` | none | Displays installed GeoVisibilityLab version |

---

## Python API Usage

```python
from geo_visibility_lab import run_geo_audit
from geo_visibility_lab.data.loader import (
    load_sample_geo_grid,
    load_sample_citations,
    load_sample_review_log,
)

# Load dataframes or provide custom Pandas DataFrames
grid_df = load_sample_geo_grid()
citations_df = load_sample_citations()
reviews_df = load_sample_review_log()

# Execute audit pipeline
audit = run_geo_audit(
    grid_df=grid_df,
    nap_df=citations_df,
    review_df=reviews_df,
    canonical_name="Apex Dental Care",
    canonical_address="1204 Market St, San Francisco, CA 94102",
    canonical_phone="+1 415-555-0192",
    canonical_url="https://www.apexdentalcare-example.com",
    business_type="DentalClinic",
)

# Access summary metrics
print(f"Overall Health Score: {audit.summary.overall_health_score}/100")
print(f"Average Rank Position: {audit.summary.avg_rank_position:.2f}")
print(f"Top 3 Share of Voice:  {audit.summary.top3_share_of_voice:.1f}%")
print(f"NAP Consistency Score: {audit.summary.nap_consistency_score:.1f}%")
print(f"Review Velocity Ratio: {audit.summary.review_velocity_ratio:.2f}x")

# Inspect findings
for finding in audit.findings:
    print(f"[{finding.severity.upper()}] {finding.title}: {finding.recommendation}")
```

---

## Architecture

```mermaid
flowchart TD
    A[Inputs: CSV / DataFrames] --> B[Geo-Grid Coordinate Nodes]
    A --> C[Aggregator NAP Citations]
    A --> D[Customer Review Velocity Log]
    
    subgraph Engine [GeoVisibilityLab Engine]
        B --> E[GeoGridAnalyzer]
        C --> F[NAPConsistencyAnalyzer]
        D --> G[ReviewHealthAnalyzer]
        
        E --> H[Rank Metrics: ARP, SoV%, Dropoff Radius]
        F --> I[String Match & Directory Consistency]
        G --> J[Velocity Ratio & Drought Alerts]
        
        H --> K[SQLite Storage & GeoAuditResult Aggregator]
        I --> K
        J --> K
    end
    
    subgraph Expo
```
