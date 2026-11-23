# pyrite

**Overview:** A second brain for you, your agents, and your teams. Knowledge-as-Code: markdown + YAML in git, schema-validated, with semantic search and a three-tier MCP server. CLI, REST API, web UI, and plugin system. Zero running cost locally.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/pyrite](https://github.com/hamids-ai-automations/pyrite) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-01 |
| Last update | 2026-11-01 |
| Last push | 2026-11-01 |
| Default branch | dev |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 38 |
| Size | 14083 KB |
| Topics | - |

## Objectives

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo/pyrite-mark.svg">
    <img src="docs/assets/logo/pyrite-mark-light.svg" alt="Pyrite logo: an isometric cube inside a hexagonal frame, drawn as a graph of nodes and edges" width="120">
  </picture>
</p>

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude, .claude-plugin, .github, benchmarks, changelog.d, deploy, docs, extensions, feedback, kb, pyrite, pyrite-mcp, scripts, tests, web
- **Total files (tracked in default branch):** 2376
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/cleanup-stale-queue.yml, .github/workflows/publish.yml, .github/workflows/refresh-test-durations.yml
- **Test files detected:** 852

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 12483549 |
| TypeScript | 617989 |
| Svelte | 433394 |
| Shell | 37350 |
| CSS | 7081 |
| Dockerfile | 2249 |
| JavaScript | 1261 |
| HTML | 757 |
| Mako | 635 |

**Frameworks / libraries detected:** Anthropic API, FastAPI, MCP, OpenAI API, SQLAlchemy, Svelte, pytest

**Dependencies:** none detected

## Important source files

- `deploy/demo/docker-compose.yml`
- `deploy/ink/docker-compose.yml`
- `deploy/journalists/docker-compose.yml`
- `deploy/selfhost/docker-compose.yml`
- `docker-compose.yml`
- `extensions/encyclopedia/pyproject.toml`
- `extensions/journalism-investigation/pyproject.toml`
- `extensions/social/pyproject.toml`
- `extensions/software-kb/pyproject.toml`
- `extensions/zettelkasten/pyproject.toml`
- `pyproject.toml`
- `pyrite-mcp/pyproject.toml`
- `web/package.json`
- `web/tsconfig.json`

## Installation and setup

```bash

## Deployment

No deployment configuration detected.

## Documentation links

- https://railway.com/button.svg
- https://railway.com/template/new?repo=pyrite-wiki/pyrite&referralCode=pyrite
- https://render.com/images/deploy-to-render-button.svg
- https://render.com/deploy?repo=https://github.com/pyrite-wiki/pyrite
- http://localhost:8088
- https://pyrite.wiki
- https://transparencycascade.org

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine
- hamids-ai-automations/gemini-agent-reliability-kit
- hamids-ai-automations/envscope
- hamids-ai-automations/searchpulse-ai

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/pyrite/blob/dev/README.md

```markdown
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo/pyrite-mark.svg">
    <img src="docs/assets/logo/pyrite-mark-light.svg" alt="Pyrite logo: an isometric cube inside a hexagonal frame, drawn as a graph of nodes and edges" width="120">
  </picture>
</p>

# Pyrite

**A second brain for you, your agents, and your teams.**

Knowledge-as-Code — structured knowledge in markdown files with YAML frontmatter, schema-validated, versioned in git, searchable by any AI through MCP.

Your AI agents have no memory. Your knowledge is trapped in platform silos. Every new chat starts from zero. Pyrite gives you structured, validated, git-versioned knowledge bases that any AI can read and write through a built-in MCP server. One brain, every AI, persistent memory that compounds over time.

**Why Pyrite instead of vectors-in-Postgres or Notion+AI?**

- **Typed entries with schema validation** — not flat vector blobs. Define `person`, `decision`, `event`, `component` types with validated fields. Query structurally, not just by vibes.
- **Git-native** — every change is a file you commit to git (`git commit` or `pyrite kb commit`), not a database mutation. Branch, diff, review, rollback. Your knowledge has a full audit trail. In 0.26, **Your files, exactly** means an edit changes only what you asked; hand-maintained comments, order and quoting survive. See [how Pyrite edits your files](https://github.com/hamids-ai-automations/pyrite/blob/dev/docs/how-pyrite-edits-your-files.md).
- **MCP server with three-tier access control** — read/write/admin tiers. Give untrusted agents read-only access. Give your own agents write access. Keep admin for yourself.
- **Semantic + structured search** — find by meaning (vector embeddings) AND by type, tag, date range, or relationship. Both at once in hybrid mode.
- **Plugin system with 19 extension points** — custom entry types, MCP tools, CLI commands, validators, lifecycle hooks, relationship semantics, schema migrations.
- **Zero running cost locally** — markdown files + SQLite index on your disk. No cloud dependency, no subscription, no vendor lock-in. Your data is plain text files you can read in any editor.

> **Multi-user is experimental. Here be dragons.** Pyrite is solid for one person, their agents, and a team that trusts each other. Accounts and per-KB permissions work, and each release closes more gaps, but they have not had the review a system holding other people's private data needs. Don't put knowledge on a shared or internet-facing instance that you couldn't live with every user of that instance reading. See [SECURITY.md](https://github.com/hamids-ai-automations/pyrite/blob/dev/SECURITY.md#multi-user-is-experimental).

## Quick Start

```bash
# Install (no PyPI wheel yet -- from source). Needs Python 3.11+.
git clone https://github.com/pyrite-wiki/pyrite.git && cd pyrite
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[all]"

# Initialize a knowledge base outside the clone
pyrite init --template research --path ~/my-kb

# Create some entries
pyrite create -k my-kb --type person --title "Sarah Chen" \
  --body "Engineering lead. Considering move to consulting." --tags "team,engineering"

pyrite create -k my-kb --type note --title "Switch to async standups" \
  --body "Decided 2026-03-01. Reduces meeting load by 3hrs/week." --tags "process"

# Search (keyword, semantic, or hybrid)
pyrite search "consulting" -k my-kb
pyrite search "career transition" -k my-kb --mode=semantic  # keyword mode finds exact words only
# The first semantic search downloads the embedding model (~90 MB, one time).
# Writes never wait on that download: an entry is keyword-searchable the
# moment it is written, and gets its embedding on the next `pyrite index
# embed` / `index sync` (or, on a server, at startup). Run `pyrite index
# embed` to fetch the model and catch up on demand.

# Connect to Claude Code and Claude Desktop (every client it finds; restart it after)
pyrite mcp-setup                  # write tier; --tier read|admin, --client, --project
```

`pyrite mcp-setup` points a `pyrite` server entry at this install where each
client reads it: `claude mcp add -s user` for Claude Code (or `./.mcp.json`
with `--project`), and Claude Desktop's own `claude_desktop_config.json`. Run it
again any time. An entry that already points here is not rewritten; one that
points elsewhere gets its command path changed (and its tier, if you pass
`--tier`), and keeps its `env`, extra arguments and other keys. Other servers
are never touched. Each client is all or nothing: one it cannot change safely
is left as it was with the reason, while another may still be changed, and
the exit code is 1 unless every client ended up pointing here. The JSON report
names each client and what changed, says what the file holds when a change
could not be finished, and names a `pyrite` entry in another Claude Code scope
(one project's, from `claude mcp add` without `-s user`) that would be used
instead of this one.
[Getting started](https://github.com/hamids-ai-automations/pyrite/blob/dev/docs/getting-started.md#connect-an-ai-via-mcp) lists the
cases.

Or add it by hand to any MCP client's config:

```json
{
  "mcpServers": {
    "pyrite": {
      "command": "/absolute/path/to/.venv/bin/pyrite",
      "args": ["mcp", "--tier", "write"]
    }
  }
}
```

Use the absolute path (`which pyrite`): Claude Desktop does not see your shell's
PATH or an activated venv.

Now any AI that speaks MCP can search, read, and write your knowledge base.

## How It Works

Markdown files with YAML frontmatter in git are the source of truth. Pyrite builds a SQLite FTS5 index (with optional vector embeddings) on top of the files for fast search. The MCP server, CLI, and REST API all read from and write to the same files. Rebuild the index from files at any time with `pyrite index build`.

You define domain-specific entry types and field schemas in a `kb.yaml` file. Pyrite validates entries on every write, indexes them, and exposes them through all interfaces. A plugin protocol lets you extend entry types, add MCP tools, define relationship semantics, and hook into lifecycle events.

```
Your files (git)  →  SQLite index (derived)  →  MCP server / CLI / REST API / Web UI
                                               ↑
                                          Any AI connects here
```

## MCP Server

Three permission tiers. Each tier includes the tools from lower tiers. Counts below are the core `kb_*`/`task_*` tools only; installed plugins add more per tier (e.g. software-kb adds `sw_adrs`, `sw_backlog`, `sw_create_adr`) — run `pyrite mcp --help` for the live total including plugin tools, generated from the tool registry so it can't drift from what a running server exposes.

| Tier | Core tools |
|------|-------|
| **read** (29) | `kb_list`, `kb_search`, `kb_get`, `kb_timeline`, `kb_tags`, `kb_backlinks`, `kb_stats`, `kb_schema`, `kb_orient`, `kb_batch_read`, `kb_batch_suggest`, `kb_discover_neighbors`, `kb_list_entries`, `kb_recent`, `kb_qa_validate`, `kb_qa_status`, `kb_read_body`, `kb_find_by_status`, `kb_find_by_assignee`, `kb_find_by_location`, `kb_find_overdue`, `kb_index_job_status`, `list_edge_types`, `task_list`, `task_status`, `task_ancestors`, `task_blocked_by`, `task_critical_path`, `task_subtree` |
| **write** (+11) | read + `kb_create`, `kb_bulk_create`, `kb_update`, `kb_delete`, `kb_link`, `kb_qa_assess`, `task_create`, `task_update`, `task_claim`, `task_checkpoint`, `task_decompose` |
| **admin** (+8) | write + `kb_index_sync`, `kb_manage`, `kb_commit`, `kb_push`, `kb_registry_add`, `kb_registry_remove`, `kb_registry_reindex`, `kb_registry_health` |

Pagination and totals differ by tool and by transport (CLI/MCP/REST) — see `docs/json-contracts.md` for the measured shape of each, rather than assuming a uniform `has_more`/`total` contract. `kb_bulk_create` handles up to 50 entries per call. After parameter validation,
```
