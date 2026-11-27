# rag-docker

**Overview:** RAG creation as a docker instance.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/rag-docker](https://github.com/hamids-ai-automations/rag-docker) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-01 |
| Last update | 2026-11-01 |
| Last push | 2026-11-04 |
| Default branch | develop |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 3 |
| Size | 15866 KB |
| Topics | - |

## Objectives

# RAG Platform

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude, .github, api, exports, ingest-inbox, mcp, ollama, proxy, scripts, telemetry, ui
- **Total files (tracked in default branch):** 428
- **CI workflows:** .github/workflows/triage-label.yml, .github/workflows/verify.yml
- **Test files detected:** 191

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 2605915 |
| Shell | 330380 |
| JavaScript | 298690 |
| TypeScript | 161788 |
| Go Template | 6604 |
| Dockerfile | 3020 |
| HTML | 299 |
| CSS | 59 |

**Frameworks / libraries detected:** MCP

**Dependencies:** none detected

## Important source files

- `api/main.py`
- `api/requirements.txt`
- `docker-compose.yml`
- `mcp/requirements.txt`
- `ui/package.json`
- `ui/tsconfig.json`

## Installation and setup

```bash

## Deployment

No deployment configuration detected.

## Documentation links

- http://localhost:8080
- http://localhost:8080`
- https://docs.docker.com/get-docker
- https://docs.docker.com/engine/network/port-publishing/#publishing-ports
- http://localhost:8080/api/collections
- http://localhost:8080/api/auth/login
- http://localhost:8080/api/auth/logout
- https://office-mac.local/`
- https://office-mac.local:8443/`
- http://localhost:8080/api/health
- https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html
- http://localhost:8080/api/export
- http://localhost:8080/api/export/job
- http://localhost:8080/api/packages
- https://age-encryption.org
- http://localhost:8080/api/import
- http://localhost:8080/api/import/job
- http://localhost:8080/api/tune/rechunk
- http://localhost:8080/api/tune/reembed
- http://localhost:8080/api/tune/reindex
- https://registry-1.docker.io
- http://localhost:9090`
- http://localhost:8080/api/collections`
- http://localhost:8080/api/ingest/upload
- http://collector:4318`

## Development status

Fork of another project; see upstream for original authorship.

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

Full README: https://github.com/hamids-ai-automations/rag-docker/blob/develop/README.md

```markdown
# RAG Platform

[![Verify](https://github.com/mikesilvers/rag-docker/actions/workflows/verify.yml/badge.svg?branch=develop)](https://github.com/mikesilvers/rag-docker/actions/workflows/verify.yml)

A self-contained, Dockerized Retrieval-Augmented Generation (RAG) platform. Upload documents, ask questions, and generate evaluation datasets — all running locally with no external API keys required.

## What's included

| Component | Technology | Purpose |
|---|---|---|
| Vector store | Weaviate 1.40.2 | Stores and retrieves document chunks |
| LLM + embeddings | Ollama 0.3.14 | Runs phi3.5 (chat) and nomic-embed-text (embeddings) locally |
| API | FastAPI + Python 3.11 | RAG pipeline, ingest, gold standard generation |
| UI | React 18 + Vite + Tailwind | Web interface with login and three roles |
| Proxy | nginx 1.29 | Routes traffic; listens on port 80 in-container, published on host port 8080 |

## Prerequisites

- **Docker Desktop with Engine 28.0.0 or newer** (or Docker Engine 28.0.0+ with Compose v2) — [install](https://docs.docker.com/get-docker/)
- **12 GB RAM and 2 GB swap allocated to Docker** (Docker Desktop → Settings → Resources → Memory and Swap). phi3.5 alone is ~6 GB resident; at 10 GB, full verification runs still hit Ollama timeouts under memory pressure, and below that the model is repeatedly evicted and reloaded and queries time out. Swap turns a short spike into a slowdown instead of a failure. Leave macOS at least 4 GB: on a 16 GB Mac, 12 GB is the practical ceiling. `/health` reports what Docker actually has against this recommendation
- **20 GB disk minimum allocated to Docker, 32 GB recommended** — see [Storage requirements](#storage-requirements) below. Check your current limit before building — a small virtual disk (8 GB or so) cannot hold this stack, and the build fails partway through with a confusing error.
- Port **8080** free on the host — `docker-compose.yml` publishes the proxy as `127.0.0.1:8080:80`, bound to host loopback on supported engines

Check the daemon version with `docker version --format '{{.Server.Version}}'`. Docker documents that engines older than 28.0.0 allow same-network hosts to reach localhost-published ports; upgrade the engine before using this local workbench. See [Docker port publishing](https://docs.docker.com/engine/network/port-publishing/#publishing-ports). This default assumes Docker's standard bridge/NAT configuration; custom direct-routing settings are outside this local profile.

No API keys, no cloud accounts, no Python or Node installs required on your machine.

### Storage requirements

All of this lives inside Docker's virtual disk, not your host filesystem. Measured on a clean build (Apple Silicon, linux/arm64):

| What | Size | When |
|---|---|---|
| `ollama/ollama` image | 3.2 GB | first pull |
| `rag-docker-api` image | 2.8 GB | build |
| `rag-docker-ui` image | 149 MB | build |
| `weaviate` image | 200 MB | first pull |
| `nginx` image | 50 MB | first pull |
| **Images after a full build** | **~6.5 GB** | |
| Model weights (phi3.5 2.2 GB, nomic-embed-text 274 MB) | ~2.5 GB | first run, into the `ollama_models` volume |
| **Total steady state** | **~9.0 GB** | |

Build cache adds several GB on top, though much of it shares layers with the images rather than duplicating them. A rebuild also holds the old and new image layers at once until you prune.

**Allocate 20 GB minimum.** That covers the steady-state ~9.0 GB plus build cache and rebuild headroom. **32 GB is recommended** if you plan to ingest a meaningful document corpus, since the Weaviate index, the uploaded files and the retained originals all grow on top of everything above.

Three things scale with your corpus rather than with the stack:

- the **Weaviate index** and its vectors,
- **retained source documents** (`rag_sources`), which hold one copy of every ingested file so a collection can be exported at `with-sources` fidelity and re-chunked later,
- **export packages** in `./exports`, which live on the *host* filesystem rather than Docker's virtual disk. A package is roughly the size of the corpus it came from, and about 2.3 GB larger if exported with `include_models: true`.

So budget the figures above **plus the size of your document corpus** — counted twice if you keep exports of it alongside the live collections.

> The api image is 2.8 GB rather than 7.6 GB because `api/Dockerfile` installs CPU-only torch from the PyTorch CPU index before resolving `requirements.txt`. The default PyPI torch wheel drags in ~4.1 GB of NVIDIA CUDA and Triton packages that cannot execute without an NVIDIA GPU. See the comment in `api/Dockerfile` before changing those pins.

To change the disk allocation: **Docker Desktop → Settings → Resources → Virtual disk limit**, then apply and restart. On Docker Engine (Linux) there is no virtual disk — the limit is simply free space on `/var/lib/docker`.

Reclaim space at any time with `docker builder prune` (build cache only) or `docker system prune -a` (also removes unused images, forcing a full rebuild).

## Quick start

```bash
# 1. Clone and enter the project
git clone <repo-url> rag-docker
cd rag-docker

# 2. Start the stack
docker compose up -d

# 3. Watch Ollama download the models (first run only — ~5 minutes)
docker compose logs -f ollama

# 4. Create the first AI Engineer (first start only); it prints a one-time password
docker compose exec api python -m auth bootstrap <username>

# 5. Open the UI once all services are healthy, log in and choose a new password
open http://localhost:8080       # macOS
# or visit http://localhost:8080 in your browser
```

The stack is ready when `docker compose ps` shows **weaviate**, **ollama**, and **api** as healthy. The ui and proxy services have no healthcheck and show as running — wait an additional 10–15 seconds after api becomes healthy before opening the browser.

## First run timeline

Build times below are measured on Apple Silicon; download times are estimated
from transfer size at roughly 90 Mbps. Both downloads and pulls are
bandwidth-bound, so a slower link stretches them proportionally.

| Time | What happens |
|---|---|
| 0s | Docker starts pulling base images (~3.8 GB on disk: ollama 3.2 GB, weaviate 200 MB, python 158 MB, node 136 MB, nginx 50 MB) and building api and ui in parallel |
| ~1min | Weaviate starts — its image is only 120 MB, so it is ready well before the others |
| ~4min | api image finishes building. That build measures **~3 min from scratch**: apt 32s, pip install 97s, sentence-transformers pre-cache 19s. The ui image finishes sooner |
| ~5min | The 3.2 GB ollama image finishes pulling; the container starts and immediately begins downloading models |
| ~10min | phi3.5 (2.2 GB) and nomic-embed-text (274 MB) finish; ollama passes its healthcheck and api, ui and nginx start |

**Total first run: roughly 10–20 minutes**, dominated by downloads rather than CPU.
Note that nothing can pull models until the ollama image itself has downloaded,
so the model wait begins several minutes in — the stack is not stuck.

On subsequent starts everything is immediate: the images are built and the model weights are cached in the `ollama_models` Docker volume.

## Accounts and roles

Everyone logs in with their own account, and each account has one role (#25).
The API enforces the role on every request; the UI only hides what the role
can't use.

| Role | Access |
|---|---|
| **End User** | Q&A only |
| **Developer** | Q&A, Import, Chunking, Retrieval, Gold Standard, Transfer |
| **AI Engineer** | All of the above + Collections management (deleting collections) + Health dashboard + tuning + Users (account management) + Service keys (API keys for programs) + Audit (the audit log) |

Endpoint by endpoint (paths under `/api`):

| Needs | Endpoints |
|---|---|
| nothing | `GET /health`, `GET /auth/status`, `POST /auth/login` |
| any logged-in user | `GET /auth/me`, `POST /auth/logout`, `POST /auth/password` |
| End User | `GET /collections`, `
```
