# trafilatura

**Overview:** Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/trafilatura](https://github.com/hamids-ai-automations/trafilatura) |
| Live website | https://trafilatura.readthedocs.io |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-30 |
| Last update | 2026-10-30 |
| Last push | 2026-11-11 |
| Default branch | master |
| License | Apache-2.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 99 |
| Size | 35843 KB |
| Topics | - |

## Objectives

# Trafilatura: Discover Web Content, Extract Text and Metadata

## Features

- Advanced web crawling and text discovery:
  - Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)
  - Smart crawling and URL management (filtering and deduplication)

- Parallel processing of online and offline input:
  - Live URLs, efficient and polite processing of download queues
  - Previously downloaded HTML files and parsed HTML trees

- Robust and configurable extraction of key elements:
  - Main text (own rule-based extractor with jusText and readability-lxml as fallbacks)
  - Metadata (title, author, date, site name, categories and tags)
  - Formatting and structure: paragraphs, titles, lists, quotes, code, line breaks, in-line text formatting
  - Optional elements: comments, links, images, tables
  - Optional add-ons: language detection, speed optimizations

- Multiple output formats:
  - TXT and Markdown

## Technical architecture

- **Top-level directories:** .github, docs, tests, trafilatura
- **Total files (tracked in default branch):** 1173
- **CI workflows:** .github/workflows/codeql.yml, .github/workflows/tests.yml
- **Test files detected:** 1086

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 1069929 |

**Frameworks / libraries detected:** BeautifulSoup, pandas, pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://trafilatura.readthedocs.io

## Documentation links

- https://trafilatura.readthedocs.io
- https://raw.githubusercontent.com/adbar/trafilatura/master/docs/trafilatura-logo.png
- https://pypi.python.org/pypi/trafilatura
- https://readthedocs.org/projects/trafilatura/badge/?version=latest
- http://trafilatura.readthedocs.org/en/latest/?badge=latest
- https://static.pepy.tech/badge/trafilatura/month
- https://pepy.tech/project/trafilatura
- https://aclanthology.org/2021.acl-demo.15
- https://github.blog/2019-03-29-leader-spotlight-erin-spiceland
- https://trafilatura.readthedocs.io/en/latest/used-by.html
- https://tei-c.org
- https://trafilatura.readthedocs.io/en/latest/evaluation.html
- https://hal.archives-ouvertes.fr/hal-02768510v3/document
- https://webis.de/downloads/publications/papers/bevendorff_2023b.pdf
- https://trafilatura.readthedocs.io/en/latest/quickstart.html
- https://trafilatura.readthedocs.io/en/latest/installation.html
- https://trafilatura.readthedocs.io/en/latest/usage-cli.html
- https://trafilatura.readthedocs.io/en/latest/usage-python.html
- https://trafilatura.readthedocs.io/en/latest/usage-r.html
- https://trafilatura.readthedocs.io/en/latest/corefunctions.html
- https://trafilatura.readthedocs.io/en/latest/tutorials.html
- https://www.youtube.com/watch?v=8GkiOM17t0Q&list=PL-pKWbySIRGMgxXQOtGIz1-nbfYLvqrci
- https://www.apache.org/licenses/LICENSE-2.0.html
- https://ko-fi.com/adbarbaresi
- https://en.wikipedia.org/wiki/Wire_drawing
- https://adrien.barbaresi.eu
- https://hal.archives-ouvertes.fr/hal-02447264/document
- https://hal.archives-ouvertes.fr/hal-01371704v2/document
- https://www.sigwac.org.uk/wiki/WAC-X

## Development status

Fork of another project; see upstream for original authorship.

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

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/trafilatura/blob/master/README.md

```markdown
# Trafilatura: Discover Web Content, Extract Text and Metadata

<br/>

<img alt="Trafilatura Logo" src="https://raw.githubusercontent.com/adbar/trafilatura/master/docs/trafilatura-logo.png" align="center" width="60%"/>

<br/>

[![Python package](https://img.shields.io/pypi/v/trafilatura.svg)](https://pypi.python.org/pypi/trafilatura)
[![Python versions](https://img.shields.io/pypi/pyversions/trafilatura.svg)](https://pypi.python.org/pypi/trafilatura)
[![Documentation Status](https://readthedocs.org/projects/trafilatura/badge/?version=latest)](http://trafilatura.readthedocs.org/en/latest/?badge=latest)
[![Code Coverage](https://img.shields.io/codecov/c/github/adbar/trafilatura.svg)](https://codecov.io/gh/adbar/trafilatura)
[![Downloads](https://static.pepy.tech/badge/trafilatura/month)](https://pepy.tech/project/trafilatura)
[![Reference DOI: 10.18653/v1/2021.acl-demo.15](https://img.shields.io/badge/DOI-10.18653%2Fv1%2F2021.acl--demo.15-blue)](https://aclanthology.org/2021.acl-demo.15/)


``` python
>>> from trafilatura import fetch_url, extract
>>> downloaded = fetch_url("https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/")
>>> extract(downloaded)
'Erin Spiceland is a software engineer and ...'
>>> extract(downloaded, output_format="json", with_metadata=True)
'{"title": "Leader spotlight: Erin Spiceland", "author": "Jessica Rudder", "text": "Erin Spiceland is a software engineer and ..."}'
```


## Introduction

Trafilatura is a comprehensive **Python package and command-line tool**
designed to **gather text from the Web and turn raw HTML into structured,
meaningful data**. It includes all necessary
discovery and text processing components to perform **web crawling,
downloads, scraping, and extraction** of main texts, metadata and
comments. It aims at staying **handy and modular**: no database is
required, the output can be converted to commonly used formats.

Going from raw HTML to essential parts, it **focuses on the actual
content**, **avoids noise** caused by recurring elements (headers,
footers, boilerplate), and **makes sense of the data and metadata**.
The extractor strikes a balance between limiting noise (precision) and
including all valid parts (recall). It is **robust and reasonably fast**.

Trafilatura is [widely used](https://trafilatura.readthedocs.io/en/latest/used-by.html)
across [thousands of projects](https://github.com/adbar/trafilatura/network/dependents),
including by HuggingFace, IBM, Microsoft Research, NVIDIA, the Allen Institute for AI, Stanford, and the Internet Archive.


### Features

- Advanced web crawling and text discovery:
  - Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)
  - Smart crawling and URL management (filtering and deduplication)

- Parallel processing of online and offline input:
  - Live URLs, efficient and polite processing of download queues
  - Previously downloaded HTML files and parsed HTML trees

- Robust and configurable extraction of key elements:
  - Main text (own rule-based extractor with jusText and readability-lxml as fallbacks)
  - Metadata (title, author, date, site name, categories and tags)
  - Formatting and structure: paragraphs, titles, lists, quotes, code, line breaks, in-line text formatting
  - Optional elements: comments, links, images, tables
  - Optional add-ons: language detection, speed optimizations

- Multiple output formats:
  - TXT and Markdown
  - CSV
  - JSON
  - HTML, XML and [XML-TEI](https://tei-c.org/)


### Evaluation

Trafilatura consistently outperforms other open-source libraries in text
extraction benchmarks. For more information see the
[benchmark section](https://trafilatura.readthedocs.io/en/latest/evaluation.html)
and the [evaluation readme](https://github.com/adbar/trafilatura/blob/master/tests/README.rst)
to run the evaluation with the latest data and packages.


#### Other evaluations

- Most efficient open-source library in *ScrapingHub*'s [article extraction benchmark](https://github.com/scrapinghub/article-extraction-benchmark)
- Best overall tool according to [Bien choisir son outil d'extraction de contenu à partir du Web](https://hal.archives-ouvertes.fr/hal-02768510v3/document)
  (Lejeune & Barbaresi 2020)
- Best single tool by ROUGE-LSum Mean F1 Page Scores in [An Empirical Comparison of Web Content Extraction Algorithms](https://webis.de/downloads/publications/papers/bevendorff_2023b.pdf)
  (Bevendorff et al. 2023)


## Documentation

[Getting started with Trafilatura](https://trafilatura.readthedocs.io/en/latest/quickstart.html)
is straightforward. For more information and detailed guides, visit
[Trafilatura's documentation](https://trafilatura.readthedocs.io/):

- [Installation](https://trafilatura.readthedocs.io/en/latest/installation.html)
- Usage:
  [On the command-line](https://trafilatura.readthedocs.io/en/latest/usage-cli.html),
  [With Python](https://trafilatura.readthedocs.io/en/latest/usage-python.html),
  [With R](https://trafilatura.readthedocs.io/en/latest/usage-r.html)
- [Core Python functions](https://trafilatura.readthedocs.io/en/latest/corefunctions.html)
- Interactive Python Notebook: [Trafilatura Overview](https://github.com/hamids-ai-automations/trafilatura/blob/master/docs/Trafilatura_Overview.ipynb) (in the repository)
- [Tutorials and use cases](https://trafilatura.readthedocs.io/en/latest/tutorials.html)

See the [video tutorials playlist](https://www.youtube.com/watch?v=8GkiOM17t0Q&list=PL-pKWbySIRGMgxXQOtGIz1-nbfYLvqrci) (multiple languages).


## License

This package is distributed under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

Versions prior to v1.8.0 are under GPLv3+ license.


## Contributing

Contributions of all kinds are welcome. Visit the [Contributing
page](https://github.com/adbar/trafilatura/blob/master/CONTRIBUTING.md)
for more information. Bug reports can be filed on the [dedicated issue
page](https://github.com/adbar/trafilatura/issues).

Many thanks to the
[contributors](https://github.com/adbar/trafilatura/graphs/contributors)
who extended the docs or submitted bug reports, features and bugfixes!


## Support

**If you value this software or depend on it for your product, consider
sponsoring it and contributing to its codebase.** Your support
[on GitHub](https://github.com/sponsors/adbar) or [ko-fi.com](https://ko-fi.com/adbarbaresi)
will help maintain and enhance this package.


## Context

This work started as a PhD project at the crossroads of linguistics and
NLP. This expertise has been instrumental in shaping Trafilatura over
the years. Initially launched to create text databases for research purposes
at the Berlin-Brandenburg Academy of Sciences (DWDS and ZDL units),
this package continues to be maintained and its future depends on community support.

*Trafilatura* is an Italian word for [wire
drawing](https://en.wikipedia.org/wiki/Wire_drawing) symbolizing the
refinement and conversion process. It is also the way shapes of pasta
are formed.

### Author

Reach out via the software repository or the [contact
page](https://adrien.barbaresi.eu/) for inquiries, collaborations, or
feedback. See also social networks for the latest updates.

-   Barbaresi, A. [Trafilatura: A Web Scraping Library and Command-Line
    Tool for Text Discovery and
    Extraction](https://aclanthology.org/2021.acl-demo.15/), Proceedings
    of ACL/IJCNLP 2021: System Demonstrations, 2021, p. 122-131.
-   Barbaresi, A. "[Generic Web Content Extraction with Open-Source
    Software](https://hal.archives-ouvertes.fr/hal-02447264/document)",
    Proceedings of KONVENS 2019, Kaleidoscope Abstracts, 2019.
-   Barbaresi, A. "[Efficient construction of metadata-enhanced web
    corpora](https://hal.archives-ouvertes.fr/hal-01371704v2/document)",
    Proceedings of the [10th Web as Corpus Workshop
    (WAC-X)](https://www.sigwac.org.uk/wiki/WAC-X), 2016.


### Citing Trafilatura

Trafilatura is widely used in the academic domain, chiefly for data
acquisition. Here is how t
```
