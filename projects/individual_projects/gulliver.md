# Gulliver

**Overview:** Test on tiny data before you run on giant data. MCP server + CLI that gives AI agents a dress rehearsal for SQL: cost preflight, scale lint with auto-fix, rehearse on 1% → 10%, predict 100%, run only within budget. DuckDB, Postgres, BigQuery, Snowflake. Local-first, MIT.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/Gulliver](https://github.com/hamids-ai-automations/Gulliver) |
| Live website | https://laaielichter.github.io/Gulliver/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-09 |
| Last update | 2026-11-09 |
| Last push | 2026-11-09 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 13 |
| Size | 1102 KB |
| Topics | - |

## Objectives

<!-- mcp-name: io.github.laaielichter/gulliver -->

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude-plugin, .github, docs, npm, skills, src, tests
- **Total files (tracked in default branch):** 121
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/codeql.yml, .github/workflows/release.yml
- **Test files detected:** 25

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 1077421 |
| JavaScript | 2484 |

**Frameworks / libraries detected:** MCP, pytest

**Dependencies:** none detected

## Important source files

- `npm/package.json`
- `pyproject.toml`

## Installation and setup

```bash
pip install gulliver-mcp
gulliver demo                       # creates gulliver_demo.duckdb with 5M events
export GULLIVER_DSN=gulliver_demo.duckdb

gulliver inspect
gulliver preflight "select country, count(*) from events e join users u on e.user_id = u.user_id group by 1"
gulliver lint "select * from events e, users u"           # GV003: join without a condition -> blocked
gulliver preflight "select * from read_csv('/etc/passwd')" # GS004: a file outside the allowed folders -> blocked
gulliver rehearse "select a.event_id, b.event_id from events a join events b on a.user_id = b.user_id"
```

The last one is the classic agent mistake: a self-join on a non-unique key. The rehearsal predicts the full
result (about 255 million rows from a 5-million-row table) and warns that the query multiplies rows, before you run it.

```
| Sample | Runtime  | Output rows |

## Deployment

Firebase/other hosting declared via homepage field: https://laaielichter.github.io/Gulliver/

## Documentation links

- https://docs.astral.sh/uv
- https://laaielichter.github.io/Gulliver
- https://raw.githubusercontent.com/laaielichter/Gulliver/main/docs/assets/social.jpg
- https://pypi.org/project/gulliver-mcp
- https://www.npmjs.com/package/gulliver-mcp
- https://raw.githubusercontent.com/laaielichter/Gulliver/main/docs/demo.svg
- http://127.0.0.1:8765/mcp`
- https://pypi.org/project/cost-guard-mcp/0.5.0
- https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp
- https://dbhub.ai/blog/postgres-mcp-server-review-dbhub
- https://supabase.com/docs/guides/ai-tools/mcp
- https://supabase.com/blog/defense-in-depth-mcp
- https://squawkhq.com/docs/rules
- https://pypi.org/project/dbt-costgate/1.0.5
- https://docs.datafold.com/reference/open_source
- https://contrib.rocks/image?repo=laaielichter/Gulliver

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

Ideas for what comes next, not promises. Each one is open for help:

- Live tests for BigQuery and Snowflake, so they can leave beta. The new query tags, history reads for
  `gulliver top` and review cost estimates on those engines are also tested only against fakes so far.
- GS005: look up the user functions a Postgres query calls in `pg_proc`, and block those in untrusted languages or
  with `SECURITY DEFINER`. It needs a live-server test setup.
- More same-rows rewrites in `gulliver_fix`, and more `--verify` coverage (window functions with ties are skipped today).
- Stopping the engine job when a rehearsal is cancelled from the MCP client.
- Databricks and ClickHouse engines.

Have a case where an agent's SQL went wrong at scale? [Open an issue](https://github.com/laaielichter/Gulliver/issues/new/choose).
Real examples shape the next lint rules.

## README source

Full README: https://github.com/hamids-ai-automations/Gulliver/blob/main/README.md

```markdown
<!-- mcp-name: io.github.laaielichter/gulliver -->

<p align="center">
  <a href="https://laaielichter.github.io/Gulliver/"><img src="https://raw.githubusercontent.com/laaielichter/Gulliver/main/docs/assets/social.jpg" alt="Gulliver: test on tiny data before you run on giant data. A rehearsal on 1%, 3% and 10% predicts the full run." width="760"></a>
</p>

<h1 align="center">Gulliver</h1>
<p align="center"><img src="docs/logo.svg" alt="Gulliver compass icon" width="56" height="56"></p>

<p align="center"><b>Test on tiny data before you run on giant data.</b><br>
An open-source MCP server and CLI that gives AI agents a dress rehearsal for SQL: estimate the cost, fix the slow parts, rehearse on 1% → 3% → 10% of the data, predict what 100% will do, and only run the full query inside a budget.</p>

<p align="center">
  <a href="https://github.com/laaielichter/Gulliver/actions/workflows/ci.yml"><img src="https://github.com/laaielichter/Gulliver/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pypi.org/project/gulliver-mcp/"><img src="https://img.shields.io/pypi/v/gulliver-mcp?label=pypi" alt="PyPI version"></a>
  <a href="https://www.npmjs.com/package/gulliver-mcp"><img src="https://img.shields.io/npm/v/gulliver-mcp?label=npm" alt="npm version"></a>
  <img src="https://img.shields.io/badge/python-3.10%20%E2%80%93%203.13-blue" alt="Python 3.10 to 3.13">
  <a href="https://github.com/laaielichter/Gulliver/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
  <a href="https://github.com/laaielichter/Gulliver/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22"><img src="https://img.shields.io/github/issues/laaielichter/Gulliver/good%20first%20issue?label=good%20first%20issues&color=7057ff" alt="Good first issues"></a>
</p>

<p align="center">
  <a href="https://laaielichter.github.io/Gulliver/">Website</a> ·
  <a href="#quick-start-2-minutes-no-warehouse-needed">Quick start</a> ·
  <a href="#install-the-mcp-server">Install</a> ·
  <a href="#auto-fix">Auto-fix</a> ·
  <a href="#guards-for-agents">Guards</a> ·
  <a href="#in-ci-and-on-pull-requests">CI</a> ·
  <a href="#how-it-compares">Compare</a> ·
  <a href="#faq">FAQ</a> ·
  <a href="#roadmap">Roadmap</a>
</p>

<p align="center">Works with <b>Claude Code</b>, <b>Codex</b>, <b>Cursor</b>, <b>Gemini CLI</b>, Claude Desktop, VS Code, Windsurf and any MCP client, on <b>DuckDB</b>, <b>Postgres</b>, <b>BigQuery</b> and <b>Snowflake</b>.</p>

> **New in 0.3.0:** a read-only gate that also blocks side-effect functions, SQL hidden in strings and file
> access, with DuckDB sandboxed in the engine. A result guard for personal data and prompt injection in rows. A
> runaway guard for loops and per-agent budgets. Lint for CI (SARIF, pre-commit), `gulliver fix --verify`,
> `gulliver top`, and `gulliver review` with a GitHub Action. **One breaking change:** DuckDB can no longer read
> files outside the database folder and the current folder unless you allow them
> ([details](#safety-model)). See the [changelog](https://github.com/laaielichter/Gulliver/blob/main/CHANGELOG.md).

![Gulliver rehearses a self-join on 1%, 3% and 10% of a 5-million-row table, predicts the size of the full result, then rewrites a date filter with the same rows](https://raw.githubusercontent.com/laaielichter/Gulliver/main/docs/demo.svg)

<sub>A real recording of the CLI on the demo database (script: [docs/demo.sh](https://github.com/laaielichter/Gulliver/blob/main/docs/demo.sh)).</sub>

> In *Gulliver's Travels*, Gulliver visits Lilliput, a land of tiny people, and Brobdingnag, a land of giants.
> Gulliver does the same with your data: it tries your query in Lilliput first, and only walks into Brobdingnag
> when it knows what will happen there.

## Why

Agents write SQL that works on a small table and breaks on a big one. They do not know that `events` has
5 billion rows, that a join multiplies rows, or that a forgotten partition filter scans every day since 2019.
Benchmarks score agents on *is the answer right*, never on *what did it cost* or *does it still work at 100x*.
One unlucky query can burn a monthly budget.

Gulliver sits between the agent and the warehouse:

| Step | Tool | What happens |
|---|---|---|
| 1 | `gulliver_inspect` | Which tables are big? Rows, bytes, partitions, columns. Metadata only, free. |
| 2 | `gulliver_preflight` | Bytes, rows and money **before** running, plus **scale lint** (15 rules), the read-only gate and the budget gate. When a safe rewrite exists, the answer already contains the fixed SQL (`autofix`). |
| 3 | `gulliver_rehearse` | Runs the query on 1%, 3% and 10% samples, fits a growth curve and **predicts the full run** with a confidence range. Catches joins that multiply rows. |
| 4 | `gulliver_run` | Runs the full query only inside the budget. Otherwise answers `needs_rehearsal` or `needs_approval`. The rows come back marked as untrusted data, with secrets masked and personal data flagged. |
| 5 | `gulliver_receipt` | Markdown proof for the human: what was estimated, rehearsed, approved and run, and predicted vs actual. |

Every answer has a `status` and a `next_step`, so even small models know what to do next.

Gulliver does not only say no. `gulliver_fix` **rewrites the SQL for the agent** and labels every change.
`same` (exactly the same rows) is only claimed when Gulliver has checked the column types on the connection;
everything else (`assumes`, `nulls`, `changes`) needs `mode=all` and says what may differ. With a connection it
estimates the old and the new query side by side, so nobody has to trust the saving blindly. With `--verify` it
also tests every rewrite on generated edge-case data and shows a counterexample when the rows differ.

Agents also fail in ways that have nothing to do with size. Gulliver guards those too (details in
[Guards for agents](#guards-for-agents)):

| Guard | Problem it solves |
|---|---|
| Read-only gate | "Only SELECT" is not read-only: a SELECT can stop sessions, run SQL hidden in a string, or read `~/.aws/credentials`. Refused with codes GS001-GS004; DuckDB is also sandboxed in the engine. |
| Result guard | Rows with emails, card numbers or API keys land in the model's context, and text in a row can carry instructions. Secrets are masked, personal data is flagged, rows are marked `untrusted: true`. |
| Runaway guard | An agent re-runs the same expensive query in a loop, or one agent spends the team's daily budget. Loops are stopped, and each agent and session can get its own budget. |

And for the pipeline around the query (details in [Pipeline tools](#pipeline-tools) and
[In CI and on pull requests](#in-ci-and-on-pull-requests)):

| Tool | Problem it solves |
|---|---|
| `gulliver_impact` | "If I change or drop this column, what breaks?" Column-level lineage over SQL models or a dbt manifest. |
| `gulliver_drift` | Schema changed under you: columns removed, retyped or added since the last snapshot, plus the models they break. |
| `gulliver_diff` | "Does my refactored / migrated / incremental model return the same rows?" Key-based data diff inside the engine, also across engines. |
| `gulliver_translate` | SQL between DuckDB, Postgres, BigQuery and Snowflake, with warnings and an optional preflight on the target. |
| `gulliver_incremental` | A model rebuilds everything every run. Is incremental safe, what is the SQL / dbt config, and how many rows does it skip? |
| `gulliver_check` | Data quality in one cheap scan: unique keys, not null, accepted values, ranges, freshness, row-count jumps. |
| `gulliver_top` | "Which repeated queries cost the most, and how do I fix them?" Query history grouped by shape, with same-rows fixes priced per month. |
| `gulliver_review` | "Is this pull request safe to merge?" New lint, breaking changes, downstream impact and cost per month of the changed models. |

## Quick start (2 minutes, no warehouse needed)

```bash
pip install gulliver-mcp
gulliver demo        
```
