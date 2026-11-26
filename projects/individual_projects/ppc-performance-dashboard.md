# ppc-performance-dashboard

**Overview:** Interactive PPC performance dashboard: normalize and visualize multi-channel ad spend, ROAS, CPA, conversion trends, and period-over-period comparisons.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/ppc-performance-dashboard](https://github.com/hamids-ai-automations/ppc-performance-dashboard) |
| Live website | https://marvis.web.app/ |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-12 |
| Last update | 2026-11-20 |
| Last push | 2026-10-18 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 1 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 19 KB |
| Topics | ad-reporting, data-visualization, google-ads, marketing-dashboard, meta-ads, performance-marketing, python, streamlit, ppc-dashboard |

## Objectives

# PPC Performance Dashboard

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, tests
- **Total files (tracked in default branch):** 9
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 1

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 12350 |

**Frameworks / libraries detected:** Streamlit, pandas, pytest

**Dependencies:** openpyxl, pandas, plotly, pytest, streamlit

## Important source files

- `app.py`
- `requirements.txt`

## Installation and setup

```bash
python -m venv venv

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app/

## Documentation links

- https://marvis.web.app
- https://wa.me/923167417135
- https://hamid-resume.web.app
- https://www.linkedin.com/in/muhammad-hamid-digital-marketing

## Development status

Active — last push 2026-10-18

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

- The comparison assumes calendar-aligned equal-length periods
- Real exports vary by ad platform; unknown columns are ignored (no guessing)
- No multi-touch attribution or incrementality modeling — the dashboard reports platform-reported metrics as-is

## Future development opportunities

- Budget pacing / burn-rate alerts
- Multi-platform data merge (Google Ads + Meta + Bing)
- Forecasts using simple time-series models
- Scheduled email delivery of the report

## README source

Full README: https://github.com/hamids-ai-automations/ppc-performance-dashboard/blob/main/README.md

```markdown
# PPC Performance Dashboard

An interactive paid-media performance dashboard built with Python, Pandas, Plotly, and Streamlit. Upload a Google Ads / Meta Ads / Bing Ads export, and get normalized KPIs, filters, trend charts, campaign and ad group breakdowns, period-over-period comparison, and CSV export — all in one page.

## Problem it solves

Marketers waste hours stitching CSV exports into Excel to answer simple questions: *"How did CTR change this month?"*, *"Which ad group has the lowest cost per conversion?"* This dashboard answers those questions instantly with consistent KPI definitions (CTR, CPC, CPA, conversion rate) and honest, clearly-labeled derived metrics.

## Key features

- Upload CSV or XLSX exports; column names are normalized automatically (date, campaign, ad group, impressions, clicks, spend, conversions)
- Automatic KPI calculation: CTR, CPC, Cost/Conversion, conversion rate
- Sidebar filters: date range, campaign, ad group
- Trend chart for clicks and conversions over time
- Performance tables and charts by campaign and by ad group
- Period-over-period comparison with absolute and percentage deltas
- Download summarized results as CSV
- Bundled synthetic sample data for an instant demo

## Data expectations

The dashboard expects at least a date column and one or more of: impressions, clicks, spend, conversions. Recognized date column names include `date`, `day`, `Date`. Campaign and ad group columns are optional but recommended. Any numeric column that is missing is treated as zero; derived metrics are never invented — they are computed from the columns actually present.

## Technology stack

- Python 3.11
- Pandas (data processing)
- Plotly (interactive charts)
- Streamlit (web UI)
- openpyxl (XLSX upload support)

## Folder structure

```
ppc-performance-dashboard/
├── app.py                  # Streamlit application
├── data_processor.py       # Normalization, KPI, filter, aggregation, comparison engine
├── tests/
│   └── test_data_processor.py
├── sample_data.csv         # Synthetic demo data (4 weeks, 4 campaigns)
├── requirements.txt
└── .gitignore
```

## Installation

```bash
python -m venv venv
# Windows: venv\Scripts\activate  |  macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Choose **Use bundled sample data** for an instant demo, or upload your own campaign export.

## Testing

```bash
pytest -q
```

Tests cover column normalization, KPI math, campaign filters, date-range filters, aggregation, and period comparison.

## Limitations and known issues

- The comparison assumes calendar-aligned equal-length periods
- Real exports vary by ad platform; unknown columns are ignored (no guessing)
- No multi-touch attribution or incrementality modeling — the dashboard reports platform-reported metrics as-is

## Future improvements

- Budget pacing / burn-rate alerts
- Multi-platform data merge (Google Ads + Meta + Bing)
- Forecasts using simple time-series models
- Scheduled email delivery of the report

## Related projects

- [ppc-waste-detector](https://github.com/hamid-digitalmarketer/ppc-waste-detector) — forensic detection of wasted ad spend and exclusion list generation
- [conversion-tracking-doctor](https://github.com/hamid-digitalmarketer/conversion-tracking-doctor) — diagnostics and fixes for broken conversion tracking

## License

MIT — see [LICENSE](https://github.com/hamids-ai-automations/ppc-performance-dashboard/blob/main/LICENSE).

---

**Developed by Muhammad Hamid**

Digital Marketing | SEO | Performance Marketing | E-commerce | Web Development

- Portfolio: [https://hamid-resume.web.app/](https://hamid-resume.web.app/)
- LinkedIn: [https://www.linkedin.com/in/muhammad-hamid-digital-marketing/](https://www.linkedin.com/in/muhammad-hamid-digital-marketing/)
- WhatsApp: [https://wa.me/923167417135](https://wa.me/923167417135)

Have a project, job opportunity, or collaboration in mind? [Contact Muhammad Hamid on WhatsApp](https://wa.me/923167417135).

```
