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
| Last push | 2026-11-26 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 57 KB |
| Topics | adtech, google-ads, n-gram, negative-keywords, ppc, python, sem, streamlit |

## Objectives

# AdWaste Intelligence

## Features

| | Feature | Why it matters |
|---|---|---|
| 1 | **Bulletproof Google Ads ingestion** | Handles 2-row metadata headers, `Total:` rows, UTF-16, tab delimiters, `$` / `AED` / `PKR` / `€` currencies, `--` and `< 10%` placeholders, and variant column names. Falls back to a manual column-mapping UI when a required column is missing. |
| 2 | **One-click demo account** | 1,500 realistic search terms (~$30k spend, deliberate waste clusters) so visitors experience full value in 2 seconds — no CSV needed. |
| 3 | **Vectorized 1–4 gram engine** | Cost / clicks / conversions / CPA / ROAS per n-gram with **zero double-counting** inside a single query. 50,000-row stress test analyzes in seconds. |
| 4 | **Configurable waste rules** | Target CPA (auto-initialized to account average), CPA bleeder multiplier, zero-conversion spend threshold, min-clicks gating, brand-term whitelist, bundled stopword handling, and 4 preset negative-intent dictionaries (Job Seekers, Free/Cheap/Piracy, DIY/Academic, Support). |
| 5 | **Executive dashboard** | 5 KPI cards (total spend, flagged waste $ and %, projected annualized savings, wasted terms, wasted n-grams), spend-allocation donut, top-15 wasted n-grams bar, campaign-level waste breakdown. |
| 6 | **N-gram explorer with drill-down** | Filter by campaign / match type / flagged-only / min spend / text search, check rows into a staging list, and inspect every raw search term behind any n-gram. |
| 7 | **Conflict guard (the differentiator)** | Cross-checks every staged negative (Exact / Phrase / Broad semantics) against all **converting** search terms, shows the conversions + revenue you would block, and removes conflicts with one click. |
| 8 | **3 export channels** | Copy-paste block for Google Ads UI, Google Ads Editor CSV (`Campaign, Ad group, Keyword, Criterion Type`), and a branded multi-tab Excel client audit report. |
| 9 | **Optional AI intent audit (BYOK)** | Paste a Gemini API key (or set `GEMINI_API_KEY` in secrets) to classify your top 100 non-converting terms into High Commercial Intent / Informational / Competitor / Job / Irrelevant. The app is fully functional without it. |

## Technical architecture

- **Top-level directories:** .github, .streamlit, src, tests
- **Total files (tracked in default branch):** 20
- **CI workflows:** .github/workflows/tests.yml
- **Test files detected:** 6

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 146481 |

**Frameworks / libraries detected:** NumPy, Streamlit, pandas, pytest

**Dependencies:** google-genai, numpy, openpyxl, pandas, plotly, streamlit

## Important source files

- `app.py`
- `requirements.txt`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://adwaste-intelligence.streamlit.app

## Documentation links

- https://wa.me/923167417135
- https://share.streamlit.io
- https://adwaste-intelligence.streamlit.app
- https://www.python.org
- https:

## Development status

Active — last push 2026-11-26

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

The full product spec, phased development roadmap and launch checklist live
in [`SPEC.md`](https://github.com/hamids-ai-automations/adwaste-intelligence/blob/main/SPEC.md). This app is the web SaaS companion to the
*Google Ads Waste Detector* Chrome extension and doubles as a lead-magnet
audit tool for paid-ads agencies and PPC clients.

## README source

Full README: https://github.com/hamids-ai-automations/adwaste-intelligence/blob/main/README.md

```markdown
# AdWaste Intelligence

**Google Ads Waste Detector — N-Gram Audit Engine**

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-059669?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-app-FF4B4B?logo=streamlit&logoColor=white)](https://adwaste-intelligence.streamlit.app)
[![Tests](https://img.shields.io/badge/pytest-passing-059669)](#testing)
[![License: MIT](https://img.shields.io/badge/license-MIT-0F172A)](LICENSE)

> Companion web app to the **Google Ads Waste Detector** Chrome extension.
> Upload a Search Terms report (or load the demo account), get a full 1–4 gram
> waste audit, build conflict-safe negative keyword lists, and export
> client-ready Excel audit reports — in under 60 seconds.
>
> **Privacy-first: 100% in-memory processing. Client CSV data is never saved or logged.**

---

## What it does

| | Feature | Why it matters |
|---|---|---|
| 1 | **Bulletproof Google Ads ingestion** | Handles 2-row metadata headers, `Total:` rows, UTF-16, tab delimiters, `$` / `AED` / `PKR` / `€` currencies, `--` and `< 10%` placeholders, and variant column names. Falls back to a manual column-mapping UI when a required column is missing. |
| 2 | **One-click demo account** | 1,500 realistic search terms (~$30k spend, deliberate waste clusters) so visitors experience full value in 2 seconds — no CSV needed. |
| 3 | **Vectorized 1–4 gram engine** | Cost / clicks / conversions / CPA / ROAS per n-gram with **zero double-counting** inside a single query. 50,000-row stress test analyzes in seconds. |
| 4 | **Configurable waste rules** | Target CPA (auto-initialized to account average), CPA bleeder multiplier, zero-conversion spend threshold, min-clicks gating, brand-term whitelist, bundled stopword handling, and 4 preset negative-intent dictionaries (Job Seekers, Free/Cheap/Piracy, DIY/Academic, Support). |
| 5 | **Executive dashboard** | 5 KPI cards (total spend, flagged waste $ and %, projected annualized savings, wasted terms, wasted n-grams), spend-allocation donut, top-15 wasted n-grams bar, campaign-level waste breakdown. |
| 6 | **N-gram explorer with drill-down** | Filter by campaign / match type / flagged-only / min spend / text search, check rows into a staging list, and inspect every raw search term behind any n-gram. |
| 7 | **Conflict guard (the differentiator)** | Cross-checks every staged negative (Exact / Phrase / Broad semantics) against all **converting** search terms, shows the conversions + revenue you would block, and removes conflicts with one click. |
| 8 | **3 export channels** | Copy-paste block for Google Ads UI, Google Ads Editor CSV (`Campaign, Ad group, Keyword, Criterion Type`), and a branded multi-tab Excel client audit report. |
| 9 | **Optional AI intent audit (BYOK)** | Paste a Gemini API key (or set `GEMINI_API_KEY` in secrets) to classify your top 100 non-converting terms into High Commercial Intent / Informational / Competitor / Job / Irrelevant. The app is fully functional without it. |

## Screenshots

> TODO after first deploy: add a 20-second screen-recording GIF of
> *upload CSV → flagged n-grams → conflict checker → export* at the top of
> this README (see the launch checklist in `SPEC.md`).

## Quickstart (local)

```bash
git clone https://github.com/hamids-ai-automations/adwaste-intelligence.git
cd adwaste-intelligence

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

streamlit run app.py
```

Then click **Load Demo Account (1,500 Search Terms)** — no report needed.

### Testing

```bash
pip install pytest
python -m pytest tests/ -v
```

The suite covers messy Google Ads CSVs (metadata rows, totals, UTF-16,
currencies, placeholders), n-gram math (dedup, stopwords, roll-ups), waste
rules (bleeders, high CPA, presets, brand whitelist), the conflict guard's
match-type semantics, all three export formats, and a 50,000-row performance
guard.

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub (e.g. `hamids-ai-automations/adwaste-intelligence`).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. **New app** → pick the repo → branch `main` → main file path **`app.py`**.
4. Choose **Python 3.11+** and click **Deploy**. That's it — `requirements.txt`
   is already Streamlit-Cloud-ready (no `packages.txt` needed).

### Optional secrets

In the app's **Settings → Secrets** panel:

```toml
GEMINI_API_KEY = "your-key"              # enables the AI intent audit
CHROME_EXTENSION_URL = "https://..."     # live Chrome Web Store listing
```

Both are optional — the app works 100% offline/free without them.

## Project structure

```text
adwaste-intelligence/
├── app.py                        # Streamlit entry point: tabs, session state
├── requirements.txt              # Pinned lightweight deps for streamlit.io
├── .streamlit/config.toml        # Clean SaaS theme
├── src/
│   ├── constants.py              # Bundled stopwords & preset dictionaries
│   ├── ingestion.py              # Bulletproof CSV/XLSX parser
│   ├── sample_data.py            # Deterministic 1,500-row demo generator
│   ├── ngram_engine.py           # Vectorized 1-4 gram aggregation
│   ├── waste_detector.py         # Waste rules, conflict guard, Gemini audit
│   ├── exporter.py               # Copy-paste / Editor CSV / Excel builder
│   └── ui_components.py          # KPI cards, Plotly charts, CTA banners
└── tests/                        # pytest suite (ingestion, ngrams, exports)
```

## How wasted spend is calculated

A search term or n-gram is flagged when any rule matches **and** it is not
protected by your brand whitelist:

| Rule | Condition | Wasted spend counted |
|---|---|---|
| Zero-Conv Bleeder | `Conversions = 0` AND `Cost ≥ threshold` AND `Clicks ≥ min` | 100% of cost |
| High CPA | `CPA ≥ Target CPA × multiplier` | Cost above the Target-CPA budget (`cost − target_cpa × conversions`) |
| Preset Intent | matches an enabled dictionary AND `Conversions = 0` | 100% of cost |

**Projected Annualized Savings** = flagged wasted spend ÷ days-in-report × 365
(date range parsed from the export header; 30 days assumed when absent).

The **Priority Score (0–100)** ranks flagged items by wasted-spend impact so
the biggest budget leaks always appear at the top.

## Privacy

* All parsing and analysis runs in-memory per browser session.
* Uploaded files are never written to disk, logged, or shared.
* The optional Gemini audit sends only the search-term strings you choose to
  classify, using your own API key.

## Roadmap & background

The full product spec, phased development roadmap and launch checklist live
in [`SPEC.md`](https://github.com/hamids-ai-automations/adwaste-intelligence/blob/main/SPEC.md). This app is the web SaaS companion to the
*Google Ads Waste Detector* Chrome extension and doubles as a lead-magnet
audit tool for paid-ads agencies and PPC clients.

## Author

**Muhammad Hamid** — Google Ads waste elimination & AI automation.

* WhatsApp (free 15-minute account waste audit): [wa.me/923167417135](https://wa.me/923167417135)
* GitHub: [github.com/hamids-ai-automations](https://github.com/hamids-ai-automations)

## License

[MIT](https://github.com/hamids-ai-automations/adwaste-intelligence/blob/main/LICENSE) © Muhammad Hamid

```
