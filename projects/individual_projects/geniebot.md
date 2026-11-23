# geniebot

**Overview:** RAG + vision Telegram bot: document Q&A and image captioning via OpenRouter free-tier LLMs, with SQLite vector storage.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/geniebot](https://github.com/hamids-ai-automations/geniebot) |
| Live website | https://geniebot-s98h.onrender.com/health |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-11-11 |
| Default branch | main |
| License | none declared |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 2652 KB |
| Topics | - |

## Objectives

# GenieBot - RAG + Vision Telegram Assistant

## Features

- RAG retrieval with persistent embeddings in SQLite
- Query and embedding caches in RAM for fast repeated calls
- Vision pipeline for image caption + tags (via a hosted vision model, no local weights)
- User memory that keeps the last 3 interactions per user
- Health/status page at `/` and `/health`

## Technical architecture

- **Top-level directories:** .github, bot, data, docs, media, rag, scripts, tests, utils, vision
- **Total files (tracked in default branch):** 48
- **CI workflows:** .github/workflows/tests.yml
- **Test files detected:** 10

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 114529 |
| Dockerfile | 185 |

**Frameworks / libraries detected:** NumPy, requests

**Dependencies:** Pillow, fastembed, numpy, python-dotenv, python-telegram-bot, requests

## Important source files

- `app.py`
- `requirements.txt`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://geniebot-s98h.onrender.com/health

## Documentation links

- https://geniebot-s98h.onrender.com/health
- https://t.me/Hello_Genie_Bot
- https://openrouter.ai/models?max_price=0
- https://render.com

## Development status

Fork of another project; see upstream for original authorship.

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

Full README: https://github.com/hamids-ai-automations/geniebot/blob/main/README.md

```markdown
# GenieBot - RAG + Vision Telegram Assistant

[![Tests](https://github.com/iamvisheshsrivastava/geniebot/actions/workflows/tests.yml/badge.svg)](https://github.com/iamvisheshsrivastava/geniebot/actions/workflows/tests.yml)

GenieBot is a Telegram bot that answers questions against a small local document set (RAG), captions and tags photos, and can summarize your last chat or image interaction. I built it to run entirely on free tiers - OpenRouter for the LLM/vision calls, fastembed for embeddings (no torch, no GPU), and SQLite for the vector store - so it comfortably fits on Render's free instance.

## Quick Access

- Telegram bot: [@Hello_Genie_Bot](https://t.me/Hello_Genie_Bot)
- Service check: [https://geniebot-s98h.onrender.com/health](https://geniebot-s98h.onrender.com/health) to confirm whether the bot service is running
- Hosted on Render's free tier (see **Deploy (free tier)** below); the previous DigitalOcean droplet deployment has been retired

## Highlights

- RAG retrieval with persistent embeddings in SQLite
- Query and embedding caches in RAM for fast repeated calls
- Vision pipeline for image caption + tags (via a hosted vision model, no local weights)
- User memory that keeps the last 3 interactions per user
- Health/status page at `/` and `/health`

## Tech Stack

- Python 3.10+
- python-telegram-bot
- OpenRouter (`z-ai/glm-4.6` for chat, `z-ai/glm-4.6v` for vision) is the default and what's actually deployed on Render. `LLM_PROVIDER=ollama` still works for local dev if you'd rather point at a model running on your own machine, but the vision pipeline always goes through OpenRouter regardless of that setting.
- fastembed / sentence-transformers/all-MiniLM-L6-v2 (embeddings, ONNX-based, no torch)
- SQLite (`data/rag_embeddings.db`)

## Current Runtime Settings

- retrieval top_k: 2
- chunk_size: 200
- max_tokens: 800 for `/ask` and `/summarize`, 400 for image captioning (higher than you'd expect for a 2-4 sentence answer, because GLM-4.6 is a reasoning model and spends part of that budget on hidden reasoning before it writes the visible response — too low and you get an empty reply)
- user history: last 3 interactions per user

## Project Structure

```text
app.py                    # Bot bootstrap + status server
bot/handlers.py           # Telegram command handlers
rag/system.py             # Chunking, embedding, retrieval, SQLite persistence
rag/qa.py                 # QA orchestration and prompt flow
rag/llm.py                # OpenRouter + Ollama clients with model fallback handling
rag/embeddings.py         # fastembed wrapper (no torch dependency)
vision/processor.py       # Image captioning via a hosted OpenRouter vision model
utils/cache.py            # QueryCache + EmbeddingCache (RAM)
utils/memory.py           # Per-user short history (RAM)
utils/logger.py           # File + console logging
data/                     # Knowledge documents + SQLite DB file
media/                    # Assignment screenshots used below
docs/diagrams/system-design.mmd
```

## Setup and Run (local)

### 1) Create and activate virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Configure environment

Create `.env` from `.env.example`. By default `LLM_PROVIDER=openrouter`, which needs no local model server:

```env
TELEGRAM_BOT_TOKEN=your_token_here
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=z-ai/glm-4.6
OPENROUTER_VISION_MODEL=z-ai/glm-4.6v
LOG_LEVEL=INFO
PORT=8080
```

A word of caution on `OPENROUTER_MODEL`/`OPENROUTER_VISION_MODEL`: these are free-tier model IDs, and OpenRouter does retire them from time to time (that's what happened to the model this bot originally shipped with - see closed issue [#8](https://github.com/iamvisheshsrivastava/geniebot/issues/8)). If `/ask` or `/summarize` start failing in production, check https://openrouter.ai/models?max_price=0 for what's still free before assuming it's a code problem.

To use a local Ollama server instead, set `LLM_PROVIDER=ollama` and configure `OLLAMA_BASE_URL` / `OLLAMA_MODEL` (see `.env.example`); note the vision pipeline always calls OpenRouter regardless of `LLM_PROVIDER`.

### 4) Optional: prebuild the embedding DB

```bash
python scripts/build_vector_db.py --data-dir data --db-path data/rag_embeddings.db --chunk-size 200 --chunk-overlap 50
```

### 5) Run the bot

```bash
python app.py
```

## Testing

There's a pytest suite (47 tests, runs in CI on every push/PR via `.github/workflows/tests.yml`) covering the parts that would actually leak memory, misrank retrieval, or break silently on a model outage:

- `RateLimiter`, `UserMemory`, and the two RAM caches (`EmbeddingCache`, `QueryCache`)
- `rag/system.py` - document chunking/overlap, the SQLite index-signature invalidation logic, and cosine-similarity retrieval ranking
- `rag/llm.py` - the Ollama/OpenRouter fallback-model chains and the retry-on-error heuristics, fully mocked (no live Ollama/OpenRouter calls)

```bash
pip install -r requirements-dev.txt
pytest tests/
```

It still doesn't touch the Telegram handlers themselves - those depend on `python-telegram-bot`'s update objects and would need a different mocking approach.

## Deploy (free tier)

This repo includes a `Dockerfile` and `render.yaml` for a one-click Render deployment:

1. On [Render](https://render.com), choose **New > Blueprint** and point it at this repo (`render.yaml` will be picked up automatically).
2. Set the required secrets in the Render dashboard: `TELEGRAM_BOT_TOKEN` and `OPENROUTER_API_KEY`.
3. Deploy. Render auto-redeploys on every push to `main` (`autoDeployTrigger: commit`).
4. Confirm it's running via `<your-render-url>/health`.

The bot itself doesn't need inbound HTTP (it long-polls Telegram), the status server just satisfies Render's free-tier requirement that the service bind to `$PORT`.

## Bot Commands

- `/start` - quick intro and commands
- `/help` - usage guidance
- `/ask <question>` - document-grounded answer
- `/image` - upload image for caption + tags
- `/summarize [chat|image]` - summarize latest interaction
- `/export` - download your saved conversation history as a file
- `/stats` - see your saved history and rate-limit status
- `/clear` - clear your saved conversation history

## Demo Screenshots

### Start
![Start](https://raw.githubusercontent.com/hamids-ai-automations/geniebot/main/media/start.png)

### Ask
![Ask](https://raw.githubusercontent.com/hamids-ai-automations/geniebot/main/media/ask.png)

These are example `/ask` queries that fetch information from your loaded documents and then answer:
- `/ask What is the return policy?`
- `/ask What are the pricing plans and included features?`
- `/ask What are the support hours and escalation process?`
- `/ask How do I reset my account password?`
- `/ask What are the main security/compliance points?`

### Image
![Image](https://raw.githubusercontent.com/hamids-ai-automations/geniebot/main/media/image.png)

### Summarize
![Summarize](https://raw.githubusercontent.com/hamids-ai-automations/geniebot/main/media/summarize.png)

## Architecture Diagram

Source: `docs/diagrams/system-design.mmd`

```mermaid
flowchart TD
    U[Telegram User] --> TG[Telegram API]
    TG --> APP["app.py - Bot Runtime"]
    WEB[Browser / Render Ping] --> STATUS["Status endpoints: / and /health"]
    STATUS --> APP

    APP --> H["bot/handlers.py - Command Handlers"]
    H --> MEM["utils/memory.py - Last 3 interactions per user"]
    H --> QA["rag/qa.py - RAG QA Orchestrator"]
    H --> VISION["vision/processor.py - Vision Caption + Tags"]

    QA --> RAG["rag/system.py - RAG Retrieval"]
    QA --> LLM["rag/llm.py - OpenRouter/Ollama LLM + Fallback"]
    QA --> QCACHE["utils/cache.py - QueryCache (RAM only)"]

    RAG --> DOCS["Knowledge Documents (md txt file
```
