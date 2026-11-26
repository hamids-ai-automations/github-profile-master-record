# mcp-memory-service

**Overview:** Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/mcp-memory-service](https://github.com/hamids-ai-automations/mcp-memory-service) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-01 |
| Last update | 2026-11-01 |
| Last push | 2026-11-04 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 123 |
| Size | 82491 KB |
| Topics | - |

## Objectives

# mcp-memory-service

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude, .claude-plugin, .github, .pyscn, agents, changelog.d, claude-hooks, claude_commands, codex, docs, examples, instincts, opencode, scripts, site, specs, spike, src, tests, tools, video
- **Total files (tracked in default branch):** 1633
- **CI workflows:** .github/workflows/changelog.yml, .github/workflows/ci.yml, .github/workflows/claim-check.yml, .github/workflows/claim-pending.yml, .github/workflows/cleanup-images.yml, .github/workflows/codeql.yml, .github/workflows/deploy-site.yml, .github/workflows/links.yml, .github/workflows/release.yml, .github/workflows/triage-digest.yml
- **Test files detected:** 617

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 9837742 |
| JavaScript | 2058925 |
| HTML | 1874129 |
| Shell | 494076 |
| CSS | 140641 |
| TypeScript | 129345 |
| PowerShell | 84992 |
| Dockerfile | 5064 |
| Slim | 4424 |
| Batchfile | 4164 |

**Frameworks / libraries detected:** FastAPI, MCP, Next.js, NumPy, pytest, requests

**Dependencies:** none detected

## Important source files

- `examples/plugin-audit-log/pyproject.toml`
- `examples/plugin-smart-tagger/pyproject.toml`
- `pyproject.toml`
- `src/mcp_memory_service/cli/main.py`
- `src/mcp_memory_service/web/api/manage.py`
- `src/mcp_memory_service/web/app.py`
- `tests/bridge/package.json`
- `tests/integration/package.json`
- `tools/docker/docker-compose.yml`
- `tools/pypi-placeholders/agent-memory-service/pyproject.toml`
- `tools/pypi-placeholders/ai-memory-service/pyproject.toml`
- `tools/pypi-placeholders/memory-for-agents/pyproject.toml`
- `video/package.json`
- `video/tsconfig.json`

## Installation and setup

No installation instructions found in the README.

## Deployment

No deployment configuration detected.

## Documentation links

- http://localhost:8000
- http://localhost:8000`
- https://mcpmemory.services
- https://opensource.org/licenses/Apache-2.0
- https://pypi.org/project/mcp-memory-service
- https://deepwiki.com/badge.svg
- https://deepwiki.com/doobidoo/mcp-memory-service
- https://mcpmemory.services/assets/videos/knowledge-graph-3d.mp4
- https://mcpmemory.services/assets/images/knowledge-graph-3d-poster.png
- https://mcpmemory.services/assets/images/knowledge-graph-3d.png
- https://mcpmemory.services/blog/remote-mcp-tutorial.html
- https://youtu.be/W34r8VFoSdQ
- https://glama.ai/mcp/servers/doobidoo/mcp-memory-service
- https://spark.entire.vc/mcps/vb-mcp-memory-service
- https://discord.gg/zrsNMEzmCj

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

Full README: https://github.com/hamids-ai-automations/mcp-memory-service/blob/main/README.md

```markdown
# mcp-memory-service

## Persistent Shared Memory for AI Agent Pipelines

Open-source memory backend for AI agents — **REST API, MCP, OAuth, CLI, dashboard**. One self-hosted service, every transport.
Agents store decisions, share causal knowledge graphs, and retrieve
context in 5ms — without cloud lock-in or API costs.

**Works with LangGraph · CrewAI · AutoGen · any HTTP client · Claude Desktop · OpenCode**

---

[![Website](https://img.shields.io/badge/Website-mcpmemory.services-00e5ff?logo=cloudflare&logoColor=white)](https://mcpmemory.services)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI version](https://img.shields.io/pypi/v/mcp-memory-service?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/mcp-memory-service/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-memory-service?logo=python&logoColor=white)](https://pypi.org/project/mcp-memory-service/)
[![GitHub stars](https://img.shields.io/github/stars/doobidoo/mcp-memory-service?logo=github&label=stars)](https://github.com/doobidoo/mcp-memory-service)
[![Remote MCP](https://img.shields.io/badge/MCP-Remote%20Support-blue?logo=anthropic)](https://github.com/doobidoo/mcp-memory-service/blob/main/docs/remote-mcp-setup.md)
[![OAuth 2.0](https://img.shields.io/badge/Auth-OAuth%202.0%20%2B%20DCR-green)](https://github.com/doobidoo/mcp-memory-service/blob/main/docs/oauth-setup.md)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/doobidoo/mcp-memory-service)

---

<div align="center">
  <video src="https://mcpmemory.services/assets/videos/knowledge-graph-3d.mp4" poster="https://mcpmemory.services/assets/images/knowledge-graph-3d-poster.png" width="820" autoplay loop muted playsinline controls>
    <a href="https://mcpmemory.services/"><img src="https://mcpmemory.services/assets/images/knowledge-graph-3d.png" alt="3D knowledge graph — memories as a glowing, interactive galaxy" width="820"></a>
  </video>
  <p><em>▶ <a href="https://mcpmemory.services/">The 3D knowledge graph in motion</a></em> — every memory a glowing node, every relationship a curved edge.</p>
</div>

---

## Why Agents Need This

Your AI assistant forgets everything when you start a new chat. You spend 10 minutes re-explaining your architecture. **Again.** MCP Memory Service captures project context, architecture decisions, and code patterns automatically — new sessions start with everything already known.

| Without mcp-memory-service | With mcp-memory-service |
|---|---|
| Each agent run starts from zero | Agents retrieve prior decisions in 5ms |
| Memory is local to one graph/run | Memory is shared across all agents and runs |
| You manage Redis + Pinecone + glue code | One self-hosted service, zero cloud cost |
| No causal relationships between facts | Knowledge graph with typed edges (causes, fixes, contradicts) |
| Context window limits create amnesia | Autonomous consolidation compresses old memories |

**Key capabilities for agent pipelines:**
- **Framework-agnostic REST API** — no MCP client library needed; the live endpoint list is at `/api/docs`
- **Knowledge graph** — agents share causal chains, not just facts
- **`X-Agent-ID` header** — auto-tag memories by agent identity for scoped retrieval
- **`conversation_id`** — bypass deduplication for incremental conversation storage
- **SSE events** — real-time notifications when any agent stores or deletes a memory
- **Embeddings run locally via ONNX** — memory never leaves your infrastructure

---

## 🚀 Get Started in 60 Seconds

> Not sure which setup fits? The **[Setup Guide](https://github.com/doobidoo/mcp-memory-service/blob/main/docs/setup-guide.md)** walks you to the right path in under a minute.

**1. Install:**

```bash
pip install mcp-memory-service
```

**2. Configure your AI client:**

<details open>
<summary><strong>Claude Desktop</strong></summary>

Add to your config file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "memory": {
      "command": "memory",
      "args": ["server"]
    }
  }
}
```

Restart Claude Desktop. Your AI now remembers everything across sessions.

</details>

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude mcp add memory -- memory server
```

Restart Claude Code. Memory tools will appear automatically.

</details>

<details>
<summary><strong>Agent pipelines (REST API — LangGraph, CrewAI, AutoGen, any HTTP client)</strong></summary>

```bash
MCP_ALLOW_ANONYMOUS_ACCESS=true memory server --http
# REST API running at http://localhost:8000
```

Store a memory with `POST /api/memories`, search with `POST /api/search`, retrieve by tag
with `POST /api/search/by-tag`. Send `X-Agent-ID: <id>` on a store request and the server
tags the memory `agent:<id>`, which a tag search then scopes retrieval by.

Worked examples per framework, the tag conventions and the async patterns:
**[docs/agents/](https://github.com/doobidoo/mcp-memory-service/tree/main/docs/agents)**

</details>

<details>
<summary><strong>OpenCode</strong></summary>

```bash
MCP_ALLOW_ANONYMOUS_ACCESS=true memory server --http
```

The plugin ships as repository files for the local plugin directory, so clone the
repository once even if you installed from PyPI. Install steps, the `/memory` slash
command and the endpoint override:
**[opencode/README.md](https://github.com/doobidoo/mcp-memory-service/blob/main/opencode/README.md)**

</details>

<details>
<summary><strong>Codex (automatic memory hooks)</strong></summary>

Start the Memory Service HTTP API, then install the hooks from this repository:

```bash
python3 codex/install_hooks.py
```

Restart Codex and review the hooks with `/hooks`. They retrieve project context,
capture new learnings, and checkpoint outcomes before compaction and at session end.
See [Codex hook setup](https://github.com/hamids-ai-automations/mcp-memory-service/blob/main/codex/README.md) for prerequisites, authentication, and project-local installation.

</details>

<details>
<summary><strong>claude.ai and ChatGPT (browser — Remote MCP)</strong></summary>

Remote MCP puts persistent memory in the browser on any device, no desktop app required:
OAuth 2.0 over HTTPS, self-hosted or cloud-hosted. Both claude.ai and ChatGPT
(Developer Mode) connect to the same endpoint.

Cloudflare Tunnel quick start, Let's Encrypt, nginx, Caddy and Docker production setups:
**[Remote MCP Setup](https://github.com/doobidoo/mcp-memory-service/blob/main/docs/remote-mcp-setup.md)** ·
[5-minute tutorial](https://mcpmemory.services/blog/remote-mcp-tutorial.html)

</details>

<details>
<summary><strong>Advanced: custom backends and team setup</strong></summary>

```bash
git clone https://github.com/doobidoo/mcp-memory-service.git
cd mcp-memory-service
python scripts/installation/install.py
```

Choose from **SQLite** (local, fast, single-user), **Cloudflare** (cloud, multi-device
sync), **Hybrid** (5ms local reads with background cloud sync — recommended for
production) or **Milvus** (dedicated vector DB: Lite file, self-hosted, or Zilliz Cloud).
For self-hosted team setups, the Hybrid backend can sync to another **HTTP MCP Memory Service** 
instead of Cloudflare using `MCP_HYBRID_SECONDARY_BACKEND=http`.

For long-lived services, prefer Docker Milvus or Zilliz Cloud over Milvus Lite —
[why](https://github.com/doobidoo/mcp-memory-service/blob/main/docs/milvus-backend.md#which-uri-to-use).

</details>

---

## ⚡ Works With Your Favorite AI Tools

- **Agent frameworks (REST):** LangGraph · CrewAI · AutoGen · OpenClaw/Nanobot · any HTTP client
- **CLI and terminal (MCP):** Claude Code · Gemini CLI · OpenCode · Codex CLI · Goose · Aider · Amp
- **Desktop and IDE (MCP):** Claude Desktop · VS Code · Cursor · Windsurf · Raycast · JetBrains · Zed
- **Chat (
```
