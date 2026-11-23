# ecommerce-seo-optimizer

**Overview:** Audit and optimize e-commerce product listings at scale. Validates titles, descriptions, pricing, image alt tags, and exports keyword-optimized catalogs.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/ecommerce-seo-optimizer](https://github.com/hamids-ai-automations/ecommerce-seo-optimizer) |
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
| Size | 12 KB |
| Topics | digital-marketing, e-commerce, ecommerce-seo, product-seo, python, seo-automation, shopify-seo, streamlit, catalog-optimization |

## Objectives

# E-commerce SEO Optimizer

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, tests
- **Total files (tracked in default branch):** 8
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 1

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 14285 |

**Frameworks / libraries detected:** Streamlit, pandas, pytest

**Dependencies:** openpyxl, pandas, pytest, streamlit

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

- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine
- hamids-ai-automations/gemini-agent-reliability-kit
- hamids-ai-automations/envscope

## Known issues and limitations

- Keyword extraction is heuristic (brand, category, top words); it is not a full SEO content service
- Title length guidance uses common best-practice ranges (20-70 title, 50-160 description) — tune the constants in `optimizer.py` to your vertical if needed
- No integration with platforms (Shopify, WooCommerce, etc.); export and import manually

## Future development opportunities

- Keyword density scoring and SERP snippet preview
- Competitor title analysis (from a comparison file)
- Shopify/WooCommerce export formats
- Batch apply via a reviewed CSV diff

## README source

Full README: https://github.com/hamids-ai-automations/ecommerce-seo-optimizer/blob/main/README.md

```markdown
# E-commerce SEO Optimizer

A practical tool for e-commerce teams and SEO specialists to audit and improve on-page product listings at scale. Built with Python, Pandas, and Streamlit: upload a product catalog, see every title/description/image/price issue, review keyword-aware suggestions, and export an optimized copy — original columns are always preserved.

## Problem it solves

E-commerce stores often have hundreds or thousands of thin product listings: short titles, missing descriptions, no keywords, broken image references. Fixing them manually in a spreadsheet is slow and error-prone. This tool surfaces the exact problems, proposes concrete title/description improvements using the product's own brand/category/keywords, and produces a safe export for review before applying changes upstream.

## Key features

- Upload CSV or XLSX product catalogs (title, description, price, category, brand, image columns recognized and normalized)
- Audit engine: empty/short/long titles, empty/short descriptions, missing prices, missing or malformed image URLs, duplicate titles
- Severity grading: critical / warning / info
- Suggestion engine: expands short titles with brand/category keywords, generates description copy, records reasons for every change
- Safe apply: writes `optimized_title`, `optimized_description`, `optimized` columns without overwriting originals
- Download the optimized catalog as CSV

## Data expectations

The tool looks for a title column (`title`, `name`, `product`, `product title`) and optional description, price, category, brand, image columns. Unknown columns are ignored. Missing values are flagged, never guessed.

## Technology stack

- Python 3.11
- Pandas (catalog processing)
- Streamlit (web UI)
- openpyxl (XLSX support)

## Folder structure

```
ecommerce-seo-optimizer/
├── app.py                  # Streamlit application
├── optimizer.py            # Validation, suggestion, and export engine
├── tests/
│   └── test_optimizer.py
├── requirements.txt
└── .gitignore
```

## Installation

```bash
python -m venv venv
# Windows: venv/Scripts/activate  |  macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Upload a catalog or use the bundled sample, review the issues and suggestions, then apply and download the optimized file.

## Testing

```bash
pytest -q
```

Tests cover issue detection, suggestion generation, missing-title handling, safe apply behavior, and CSV export.

## Limitations and known issues

- Keyword extraction is heuristic (brand, category, top words); it is not a full SEO content service
- Title length guidance uses common best-practice ranges (20-70 title, 50-160 description) — tune the constants in `optimizer.py` to your vertical if needed
- No integration with platforms (Shopify, WooCommerce, etc.); export and import manually

## Future improvements

- Keyword density scoring and SERP snippet preview
- Competitor title analysis (from a comparison file)
- Shopify/WooCommerce export formats
- Batch apply via a reviewed CSV diff

## Related projects

- [seo-doctor](https://github.com/hamid-digitalmarketer/seo-doctor) — automated technical SEO site crawler
- [seo-audit-tool](https://github.com/hamid-digitalmarketer/seo-audit-tool) — on-page SEO audit and website health checker

## License

MIT — see [LICENSE](https://github.com/hamids-ai-automations/ecommerce-seo-optimizer/blob/main/LICENSE).

---

**Developed by Muhammad Hamid**

Digital Marketing | SEO | Performance Marketing | E-commerce | Web Development

- Portfolio: [https://hamid-resume.web.app/](https://hamid-resume.web.app/)
- LinkedIn: [https://www.linkedin.com/in/muhammad-hamid-digital-marketing/](https://www.linkedin.com/in/muhammad-hamid-digital-marketing/)
- WhatsApp: [https://wa.me/923167417135](https://wa.me/923167417135)

Have a project, job opportunity, or collaboration in mind? [Contact Muhammad Hamid on WhatsApp](https://wa.me/923167417135).

```
