# sample-aws-genai-db-modernizer

**Overview:** Assess a relational database for modernization on AWS. Analyzes your real schema and queries, scores each query pattern against purpose-built engines (DynamoDB, DocumentDB, Aurora, OpenSearch, ElastiCache), and produces schema designs, migration waves and cost estimates. Runs locally with Claude Code.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/sample-aws-genai-db-modernizer](https://github.com/hamids-ai-automations/sample-aws-genai-db-modernizer) |
| Live website | https://aws-samples.github.io/sample-aws-genai-db-modernizer/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-01 |
| Last update | 2026-11-01 |
| Last push | 2026-11-01 |
| Default branch | main |
| License | MIT-0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 23 |
| Size | 82956 KB |
| Topics | - |

## Objectives

# Database Modernizer Assessment

## Features

<!-- --8<-- [start:overview] -->
Moving off a monolithic relational database raises hard questions. Which queries belong in DynamoDB? Which need a document store? What stays relational? A wrong answer can force a redesign in the middle of the project.

**Database Modernizer Assessment answers these questions using your real workload.** It scores every query against the AWS purpose-built engines, places each query on its best-fit engine, checks that the resulting architecture holds together, and produces schema designs, a migration roadmap in waves and a cost projection you can implement. The engine placement is deterministic: the scores decide it, not a model, so it comes out the same on every run and can be audited. A model writes the schema designs and the executive summary.

- **Sources:** PostgreSQL, MySQL, MariaDB, SQL Server and Oracle. A SQL Server or Oracle source moves to whichever Aurora engine scores higher on its workload (Aurora PostgreSQL unless Aurora MySQL scores clearly higher), so wave 1 includes a schema and dialect conversion (the plan says that wave is not yet optimized for heterogeneous migrations).
- **Targets:** DynamoDB, DocumentDB, Aurora PostgreSQL and Aurora MySQL own queries; ElastiCache can sit in front as a cache, and OpenSearch can serve search as a read model.
- **Your data stays yours:** the collection scripts are read-only and never read table rows. They collect the schema, query shapes and counters; query text can still carry literal values.

## Technical architecture

- **Top-level directories:** .claude, .github, benchmarks, ci, contrib, docs, infrastructure, pipeline, scripts, src, tests
- **Total files (tracked in default branch):** 2840
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/contract-major-gate.yml, .github/workflows/docs.yml, .github/workflows/issue-assignment-gate.yml, .github/workflows/maintainer-decision-gate.yml, .github/workflows/pr-evidence.yml, .github/workflows/refresh-prices.yml, .github/workflows/release.yml
- **Test files detected:** 1713

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 20547886 |
| JavaScript | 1094136 |
| Shell | 155219 |
| Go | 73124 |
| Jinja | 26584 |
| TSQL | 23967 |
| CSS | 14768 |
| Dockerfile | 6048 |
| Makefile | 2627 |
| HTML | 1035 |

**Frameworks / libraries detected:** FastAPI, Playwright, pytest

**Dependencies:** none detected

## Important source files

- `contrib/cdc-elasticache-prototype/data-plane/bulk-loader/requirements.txt`
- `contrib/cdc-elasticache-prototype/data-plane/sink-worker-v3/requirements.txt`
- `contrib/cdc-elasticache-prototype/examples/my-pipeline/setup/schema.sql`
- `contrib/cdc-elasticache-prototype/tools/go-aggregator/go.mod`
- `contrib/cdc-elasticache-prototype/tools/go-gen/go.mod`
- `contrib/cdc-elasticache-prototype/tools/go-genenv/go.mod`
- `contrib/cdc-elasticache-prototype/tools/go-kafka/go.mod`
- `contrib/cdc-elasticache-prototype/tools/go-lat/go.mod`
- `contrib/cdc-elasticache-prototype/tools/go-loader/go.mod`
- `contrib/cdc-elasticache-prototype/tools/go-multi/go.mod`
- `contrib/cdc-elasticache-prototype/tools/go-sink/go.mod`
- `contrib/cdc-elasticache-prototype/tools/go-split/go.mod`
- `pyproject.toml`
- `src/api/main.py`
- `src/atx_orchestrator/app.py`
- `src/atx_orchestrator/requirements.txt`
- `src/ui/package.json`
- `src/ui/src/index.js`

## Installation and setup

<!-- --8<-- [start:quickstart] -->
You need Python 3.12+, [uv](https://docs.astral.sh/uv/) and [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Node 22 is optional: with it, a local UI opens next to the chat. No AWS account, API key or Docker is needed.

## Deployment

Firebase/other hosting declared via homepage field: https://aws-samples.github.io/sample-aws-genai-db-modernizer/

## Documentation links

- https://www.python.org/downloads
- https://docs.astral.sh/uv
- https://aws-samples.github.io/sample-aws-genai-db-modernizer
- https://docs.anthropic.com/en/docs/claude-code
- https://aws-samples.github.io/sample-aws-genai-db-modernizer/other-ways-to-run-it
- https://aws-samples.github.io/sample-aws-genai-db-modernizer/use-claude-code/#analyzing-your-own-database
- https://aws-samples.github.io/sample-aws-genai-db-modernizer/understand-the-results
- https://aws-samples.github.io/sample-aws-genai-db-modernizer/sample
- https://aws-samples.github.io/sample-aws-genai-db-modernizer/use-claude-code
- https://aws-samples.github.io/sample-aws-genai-db-modernizer/faq
- https://aws-samples.github.io/sample-aws-genai-db-modernizer/contribute
- https://aws.amazon.com/migration-evaluator

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

Full README: https://github.com/hamids-ai-automations/sample-aws-genai-db-modernizer/blob/main/README.md

```markdown
# Database Modernizer Assessment

[![CI](https://github.com/aws-samples/sample-aws-genai-db-modernizer/actions/workflows/ci.yml/badge.svg)](https://github.com/aws-samples/sample-aws-genai-db-modernizer/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-93%25-brightgreen.svg)](https://github.com/aws-samples/sample-aws-genai-db-modernizer/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT--0-green.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-help%20site-blue.svg)](https://aws-samples.github.io/sample-aws-genai-db-modernizer/)

Database Modernizer Assessment reads the schema and query statistics of a relational database and tells you which AWS purpose-built database should serve each query. It then designs the target schemas and writes an executive report, an engineering report and a cost projection, all from your real workload.

> **Disclaimer:** This is a sample project intended for educational and evaluation purposes. It requires proper review, testing, and modification before use in production environments. Use at your own risk.

![A time-lapsed /modernize run on the WordPress sample in a terminal, with the approval gate and the final summary held on screen, then the job's results and summary pages in the local UI and four pages of the executive report PDF](https://raw.githubusercontent.com/hamids-ai-automations/sample-aws-genai-db-modernizer/main/docs/assets/modernizer-demo.gif)

*A full `/modernize` run on the WordPress sample (about 7.5 minutes, time-lapsed to 78 seconds) with its one approval gate and final summary, then the job's results and summary pages in the local UI and four pages of the executive report PDF.*

## Quick start

<!-- --8<-- [start:quickstart] -->
You need Python 3.12+, [uv](https://docs.astral.sh/uv/) and [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Node 22 is optional: with it, a local UI opens next to the chat. No AWS account, API key or Docker is needed.

### 1. Install

```bash
git clone https://github.com/aws-samples/sample-aws-genai-db-modernizer.git
cd sample-aws-genai-db-modernizer
uv sync
```

### 2. Run the bundled sample

The repository ships a WordPress + WooCommerce sample (50 tables, 107 queries). Open the folder in Claude Code and run:

```
/modernize docs/examples/wordpress/wordpress-collection.json
```

The run takes about 8 minutes on the sample (the first one also builds the local UI) and stops once, after the engine assignment, for your approval. After you approve, it finishes on its own. Add `--mode chat` for a terminal-only run with no UI.

### 3. Read the results

The run writes its deliverables to <!-- deliverables-list -->`artifacts/<db>/<job>/deliverables/`: `executive-report.pdf` (executive report: a landscape briefing), `engineering-report.md` (engineering report), `assessment-data.json` (Assessment Data, JSON), `engineering-report-detailed.md` (detailed engineering report: the full routing detail, for auditing the result), and `index.md`, which lists who each file is for and the assignment version<!-- /deliverables-list -->. The chat also links the job's results page in the local UI, with the same assessment and a download button for each report.

### No Claude Code?

One command runs the whole pipeline with no model and no credentials, in seconds:

```bash
uv run python scripts/run_assessment.py --file docs/examples/wordpress/wordpress-collection.json --db wordpress --llm-mode none --all -y
```

It writes the same deliverables folder. Schema design is skipped and the executive summary is fixed text, because those two need a model. [Other ways to run it](https://aws-samples.github.io/sample-aws-genai-db-modernizer/other-ways-to-run-it/) covers this command, Amazon Bedrock, the Python library and the local UI on its own.
<!-- --8<-- [end:quickstart] -->

## Where to go next

The [help site](https://aws-samples.github.io/sample-aws-genai-db-modernizer/) has everything below:

- [Analyze your own database](https://aws-samples.github.io/sample-aws-genai-db-modernizer/use-claude-code/#analyzing-your-own-database): the read-only collection scripts, and how to limit the engines the plan may use.
- [Understand the results](https://aws-samples.github.io/sample-aws-genai-db-modernizer/understand-the-results/): what each deliverable shows and how to read an assignment.
- [Sample report](https://aws-samples.github.io/sample-aws-genai-db-modernizer/sample/): the deliverables of a real run, before you run anything.
- [Use Claude Code](https://aws-samples.github.io/sample-aws-genai-db-modernizer/use-claude-code/): every `/modernize` option and the one-phase-at-a-time commands.
- [FAQ](https://aws-samples.github.io/sample-aws-genai-db-modernizer/faq/): model access, permissions, the UI, collector grants.
- [Contribute](https://aws-samples.github.io/sample-aws-genai-db-modernizer/contribute/), [CONTRIBUTING.md](https://github.com/hamids-ai-automations/sample-aws-genai-db-modernizer/blob/main/CONTRIBUTING.md) and [AGENTS.md](https://github.com/hamids-ai-automations/sample-aws-genai-db-modernizer/blob/main/AGENTS.md): the architecture, the tests and the review process.

## What it does

<!-- --8<-- [start:overview] -->
Moving off a monolithic relational database raises hard questions. Which queries belong in DynamoDB? Which need a document store? What stays relational? A wrong answer can force a redesign in the middle of the project.

**Database Modernizer Assessment answers these questions using your real workload.** It scores every query against the AWS purpose-built engines, places each query on its best-fit engine, checks that the resulting architecture holds together, and produces schema designs, a migration roadmap in waves and a cost projection you can implement. The engine placement is deterministic: the scores decide it, not a model, so it comes out the same on every run and can be audited. A model writes the schema designs and the executive summary.

- **Sources:** PostgreSQL, MySQL, MariaDB, SQL Server and Oracle. A SQL Server or Oracle source moves to whichever Aurora engine scores higher on its workload (Aurora PostgreSQL unless Aurora MySQL scores clearly higher), so wave 1 includes a schema and dialect conversion (the plan says that wave is not yet optimized for heterogeneous migrations).
- **Targets:** DynamoDB, DocumentDB, Aurora PostgreSQL and Aurora MySQL own queries; ElastiCache can sit in front as a cache, and OpenSearch can serve search as a read model.
- **Your data stays yours:** the collection scripts are read-only and never read table rows. They collect the schema, query shapes and counters; query text can still carry literal values.

## Who is this for?

Teams that have **decided to refactor their application** to use purpose-built databases. It helps you figure out which queries go where and what the target schemas should look like.

## Who is this NOT for?

- **Lift-and-shift migrations**: If you're moving a database as-is to RDS or Aurora without changing the data model, you don't need this tool.
- **Tight deadline migrations**: This tool guides application refactoring, which takes time. If you need to migrate by next week, use AWS DMS for a straight move.
- **Teams that haven't committed to refactoring**: If you're still deciding whether to modernize, start with the [AWS Migration Evaluator](https://aws.amazon.com/migration-evaluator/) or a Well-Architected review first.
<!-- --8<-- [end:overview] -->

## Security

See [CONTRIBUTING](https://github.com/hamids-ai-automations/sample-aws-genai-db-modernizer/blob/main/CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the [LICENSE](https://github.com/hamids-ai-automations/sample-aws-genai-db-modernizer/blob/main/LICENSE) file.

```
