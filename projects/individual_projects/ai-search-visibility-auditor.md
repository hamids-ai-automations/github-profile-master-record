# ai-search-visibility-auditor

**Overview:** GEO toolkit: validate AI crawler access in robots.txt, generate and lint llms.txt, check AI-citation readiness of web content. Python, Streamlit.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/ai-search-visibility-auditor](https://github.com/hamids-ai-automations/ai-search-visibility-auditor) |
| Live website | https://marvis.web.app/ |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-17 |
| Last update | 2026-11-20 |
| Last push | 2026-10-17 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 24 KB |
| Topics | ai-search, digital-marketing, generative-engine-optimization, geo, llms-txt, python, seo, streamlit |

## Objectives

# AI Search Visibility Auditor

## Features

- **AI crawler access audit** — parses `robots.txt` with standard longest-match precedence, flags crawlers that are disallowed from key paths, distinguishes Google-Extended (Gemini training) from AI Overviews indexing.
- **llms.txt detection, validation and generation** — parses existing files, flags missing titles / duplicate URLs / non-absolute links, and generates a ready-to-publish `llms.txt` from your pages.
- **On-page AI-citation readiness audit** — detects direct answer blocks in the first ~100 words, question-based headings, FAQPage / Article / Organization / Person schema (including `@graph`), author & date signals, and structured body content (lists, tables).
- **Streamlit dashboard** — enter a URL, run the audit, see a prioritized issue list (critical / warning / info), crawler access table, suggested `llms.txt`, and CSV export.
- **Zero heavy dependencies** — stdlib-only analysis engine (urllib + html.parser); Streamlit is the only runtime dependency for the dashboard.
- **Polite fetching** — custom user-agent, timeouts, size limits, small crawl delay.

## Technical architecture

- **Top-level directories:** .github, geo_audit, tests
- **Total files (tracked in default branch):** 16
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 3

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 35876 |

**Frameworks / libraries detected:** Streamlit

**Dependencies:** streamlit

## Important source files

- `app.py`
- `requirements.txt`

## Installation and setup

```bash
git clone https://github.com/hamid-digitalmarketer/ai-search-visibility-auditor.git
cd ai-search-visibility-auditor
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501, enter a URL (e.g. `https://your-site.com`) and hit **Run audit**.

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app/

## Documentation links

- https://marvis.web.app
- http://localhost:8501
- https://your-site.com`
- https://example.com/robots.txt
- https://example.com/llms.txt
- https://example.com

## Development status

Active — last push 2026-10-17

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

- [ ] Multi-page crawl (audit an entire site, not just one page)
- [ ] AI citation monitor (lightweight answer-engine mention tracking)
- [ ] Schema validation details (JSON-LD syntax errors)
- [ ] llms.txt diff/versioning suggestions
- [ ] Sitemap-aware llms.txt generation

## README source

Full README: https://github.com/hamids-ai-automations/ai-search-visibility-auditor/blob/main/README.md

```markdown
# AI Search Visibility Auditor

Open-source **GEO (Generative Engine Optimization)** toolkit. In 2026, zero-click searches have reached ~68% and AI Overviews cut click-through rates on top organic positions by ~34%. Ranking #1 is no longer enough — brands must be **cited by AI answer engines**. This tool audits whether your website is ready for that world.

It answers three questions:
1. **Are AI crawlers allowed in?** — robots.txt checks for GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended and more.
2. **Do you speak the llms.txt standard?** — detects, validates and generates `/llms.txt` so AI crawlers know what to prioritize.
3. **Is your content structured for AI citation?** — audits answer blocks, question-based headings, FAQ/Article schema and E-E-A-T signals (author, dates, structured body).

Built as a free, open-source alternative to paid AI-visibility tools (SE Ranking ~$129/mo, Semrush ~$139–299/mo, Otterly.AI, Promptwatch).

---

## Features

- **AI crawler access audit** — parses `robots.txt` with standard longest-match precedence, flags crawlers that are disallowed from key paths, distinguishes Google-Extended (Gemini training) from AI Overviews indexing.
- **llms.txt detection, validation and generation** — parses existing files, flags missing titles / duplicate URLs / non-absolute links, and generates a ready-to-publish `llms.txt` from your pages.
- **On-page AI-citation readiness audit** — detects direct answer blocks in the first ~100 words, question-based headings, FAQPage / Article / Organization / Person schema (including `@graph`), author & date signals, and structured body content (lists, tables).
- **Streamlit dashboard** — enter a URL, run the audit, see a prioritized issue list (critical / warning / info), crawler access table, suggested `llms.txt`, and CSV export.
- **Zero heavy dependencies** — stdlib-only analysis engine (urllib + html.parser); Streamlit is the only runtime dependency for the dashboard.
- **Polite fetching** — custom user-agent, timeouts, size limits, small crawl delay.

## Quick start

```bash
git clone https://github.com/hamid-digitalmarketer/ai-search-visibility-auditor.git
cd ai-search-visibility-auditor
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501, enter a URL (e.g. `https://your-site.com`) and hit **Run audit**.

## CLI usage (library)

```python
from geo_audit import fetcher, report

status, robots = fetcher.polite_fetch("https://example.com/robots.txt")
_, llms = fetcher.polite_fetch("https://example.com/llms.txt")
_, html = fetcher.polite_fetch("https://example.com/")

audit = report.run_audit(
    domain="https://example.com",
    robots_text=robots if status == 200 else None,
    robots_status=status,
    llms_text=llms,
    llms_status=200,
    html=html,
)
for issue in audit.sorted_issues():
    print(issue["severity"], issue["code"], "-", issue["message"])
```

## What each check means

| Check | Why it matters in 2026 |
|---|---|
| GPTBot / ClaudeBot / PerplexityBot blocked | AI answer engines can't cite what they can't crawl. |
| Google-Extended blocked | Controls Gemini training only; doesn't block AI Overviews. Blocking by reflex hides content from model training pipelines. |
| `llms.txt` missing | The emerging standard that explicitly guides AI crawlers to priority content (adoption accelerating across major sites). |
| No direct answer block | AI extractors often stop at the first clean answer; burying it costs citations. |
| No FAQ/Article schema | FAQ schema feeds structured Q&A pairs straight into knowledge graphs — one of the highest-impact citation signals. |
| No author / no dates (E-E-A-T) | Anonymous, undated content fails AI quality filters. |

## Project structure

```
geo_audit/
  fetcher.py           # polite HTTP fetching (timeout, size limit, delay)
  robots_analyzer.py   # robots.txt parsing + AI crawler access checks
  llms_analyzer.py     # llms.txt parse / validate / generate
  content_analyzer.py  # on-page citation readiness signals
  report.py            # audit orchestration + prioritized issues
app.py                 # Streamlit dashboard
tests/                 # unit tests (unittest)
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Deployment (optional)

The app is a standard Streamlit app and deploys to **Streamlit Community Cloud** or any container host. For a zero-server demo, host the generated `llms.txt` and audit report as static files on GitHub Pages.

## Roadmap

- [ ] Multi-page crawl (audit an entire site, not just one page)
- [ ] AI citation monitor (lightweight answer-engine mention tracking)
- [ ] Schema validation details (JSON-LD syntax errors)
- [ ] llms.txt diff/versioning suggestions
- [ ] Sitemap-aware llms.txt generation

## License

MIT © Muhammad Hamid

## Feedback

Issues and pull requests welcome. Built as part of the [digital marketing portfolio](https://github.com/hamid-digitalmarketer).

```
