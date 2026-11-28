# starlette

**Overview:** The little ASGI framework that shines. 🌟

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/starlette](https://github.com/hamids-ai-automations/starlette) |
| Live website | https://starlette.dev |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-29 |
| Last update | 2026-10-29 |
| Last push | 2026-10-29 |
| Default branch | main |
| License | BSD-3-Clause |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 349 |
| Size | 8656 KB |
| Topics | - |

## Objectives

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette_dark.svg" width="420px">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg" width="420px">
    <img alt="starlette-logo" src="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg">
  </picture>
</p>

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, benchmarks, docs, scripts, starlette, tests
- **Total files (tracked in default branch):** 151
- **CI workflows:** .github/workflows/benchmark.yml, .github/workflows/main.yml, .github/workflows/publish.yml, .github/workflows/zizmor.yml
- **Test files detected:** 41

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 812747 |
| Shell | 1161 |

**Frameworks / libraries detected:** pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

```shell
$ pip install starlette
```

You'll also want to install an ASGI server, such as [uvicorn](https://uvicorn.dev) or any of the [other ASGI server implementations](https://asgi.readthedocs.io/en/latest/implementations.html#servers).

```shell
$ pip install uvicorn
```

## Deployment

Firebase/other hosting declared via homepage field: https://starlette.dev

## Documentation links

- https://starlette.dev
- https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette_dark.svg
- https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg
- https://badge.fury.io/py/starlette.svg
- https://pypi.python.org/pypi/starlette
- https://pypi.org/project/starlette
- https://discord.gg/RxKUF5JuHs
- https://uvicorn.dev
- https://asgi.readthedocs.io/en/latest/implementations.html#servers
- http://127.0.0.1:8000
- https://asgi.readthedocs.io/en/latest
- https://pypi.org/project/httpx2
- https://jinja.palletsprojects.com
- https://opentelemetry.io/docs/languages/python/api
- https://multipart.fastapiexpert.com
- https://itsdangerous.palletsprojects.com
- https://www.sqlalchemy.org
- https://pyyaml.org/wiki/PyYAMLDocumentation

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/marvis-streamlit-dashboard
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/adwaste-intelligence

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/starlette/blob/main/README.md

```markdown
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette_dark.svg" width="420px">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg" width="420px">
    <img alt="starlette-logo" src="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg">
  </picture>
</p>

<p align="center">
    <em>✨ The little ASGI framework that shines. ✨</em>
</p>

---

[![Build Status](https://github.com/Kludex/starlette/workflows/Test%20Suite/badge.svg)](https://github.com/Kludex/starlette/actions)
[![Package version](https://badge.fury.io/py/starlette.svg)](https://pypi.python.org/pypi/starlette)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/starlette.svg?color=%2334D058)](https://pypi.org/project/starlette)
[![Discord](https://img.shields.io/discord/1051468649518616576?logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/RxKUF5JuHs)

---

**Documentation**: <a href="https://starlette.dev/" target="_blank">https://starlette.dev</a>

**Source Code**: <a href="https://github.com/Kludex/starlette" target="_blank">https://github.com/Kludex/starlette</a>

---

# Starlette

Starlette is a lightweight [ASGI][asgi] framework/toolkit,
which is ideal for building async web services in Python.

It is production-ready, and gives you the following:

* A lightweight, low-complexity HTTP web framework.
* WebSocket support.
* In-process background tasks.
* Startup and shutdown events.
* Test client built on `httpx2`.
* CORS, GZip, Static Files, Streaming responses.
* Session and Cookie support.
* 100% test coverage.
* 100% type annotated codebase.
* Few hard dependencies.
* Compatible with `asyncio` and `trio` backends.
* Great overall performance [against independent benchmarks][techempower].

## Installation

```shell
$ pip install starlette
```

You'll also want to install an ASGI server, such as [uvicorn](https://uvicorn.dev) or any of the [other ASGI server implementations](https://asgi.readthedocs.io/en/latest/implementations.html#servers).

```shell
$ pip install uvicorn
```

## Example

```python title="main.py"
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route("/", endpoint=homepage)
]

app = Starlette(debug=True, routes=routes)
```

Then run the application using Uvicorn:

```shell
$ uvicorn main:app
```

## Dependencies

Starlette only requires `anyio`, and the following are optional:

* [`httpx2`][httpx2] - Required if you want to use the `TestClient`.
* [`jinja2`][jinja2] - Required if you want to use `Jinja2Templates`.
* [`opentelemetry-api`][opentelemetry-api] - Required for `OpenTelemetryMiddleware`.
* [`python-multipart`][python-multipart] - Required if you want to support form parsing, with `request.form()`.
* [`itsdangerous`][itsdangerous] - Required for `SessionMiddleware` support.
* [`pyyaml`][pyyaml] - Required for `SchemaGenerator` support.

You can install all of these with `pip install starlette[full]`.

## Framework or Toolkit

Starlette is designed to be used either as a complete framework, or as
an ASGI toolkit. You can use any of its components independently.

```python
from starlette.responses import PlainTextResponse


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)
```

Run the `app` application in `example.py`:

```shell
$ uvicorn example:app
INFO: Started server process [11509]
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Run uvicorn with `--reload` to enable auto-reloading on code changes.

## Modularity

The modularity that Starlette is designed on promotes building reusable
components that can be shared between any ASGI framework. This should enable
an ecosystem of shared middleware and mountable applications.

The clean API separation also means it's easier to understand each component
in isolation.

---

<p align="center"><i>Starlette is <a href="https://github.com/Kludex/starlette/blob/main/LICENSE.md">BSD licensed</a> code.<br/>Designed & crafted with care.</i></br>&mdash; ⭐️ &mdash;</p>

[asgi]: https://asgi.readthedocs.io/en/latest/
[httpx2]: https://pypi.org/project/httpx2/
[jinja2]: https://jinja.palletsprojects.com/
[opentelemetry-api]: https://opentelemetry.io/docs/languages/python/api/
[python-multipart]: https://multipart.fastapiexpert.com/
[itsdangerous]: https://itsdangerous.palletsprojects.com/
[sqlalchemy]: https://www.sqlalchemy.org
[pyyaml]: https://pyyaml.org/wiki/PyYAMLDocumentation
[techempower]: https://github.com/TechEmpower/FrameworkBenchmarks

```
