# sentryward

**Overview:** Self-hosted AI code reviewer with automated reviews, inline suggestions, and flexible support for cloud and local models.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/sentryward](https://github.com/hamids-ai-automations/sentryward) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-01 |
| Last update | 2026-11-01 |
| Last push | 2026-11-06 |
| Default branch | main |
| License | MIT |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 6 |
| Size | 3403 KB |
| Topics | - |

## Objectives

<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="client/public/sentryward-logo-dark.png">
    <img src="client/public/sentryward-logo-light.png" alt="Sentryward" width="360">
  </picture>
</h1>

## Features

- **Self-hosted, bring your own model:** Anthropic, OpenAI, Google, a compatible
  proxy on a [custom host](#llm-connections-and-custom-endpoints), or a local
  [Ollama](#ollama) model.
- **GitHub and GitLab:** a GitHub App, plus GitLab.com or self-hosted GitLab.
- **Reviews where you work:** inline findings with suggestions, one summary
  comment, and a `sentryward/review` commit status.
- **Manual or automatic:** submit a PR/MR URL, review on webhooks, or comment
  `/sentryward review`.
- **Per-repository config:** dashboard settings, overridable by a
  [`.sentryward.yaml`](#review-configuration) in the repository.
- **Findings across runs:** a later run never posts the same finding twice.
  Ignore findings as false positives, intentional, or fix later, and track the
  false-positive rate on the dashboard, broken down by category, severity and
  model with a pointer to the setting that would quiet the noisiest ones.
- **Teams:** share connections, repositories, reviews and model keys in team
  workspaces, with owner, admin and member roles and one-time invite links,
  managed from **Team settings** in the workspace switcher.

## Technical architecture

- **Top-level directories:** .github, client, docker, docs, server
- **Total files (tracked in default branch):** 746
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/codeql.yml, .github/workflows/release-image.yml
- **Test files detected:** 119

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 3360367 |
| Python | 6683 |
| CSS | 5853 |
| Go | 3709 |
| Dockerfile | 2267 |
| Shell | 961 |
| HTML | 661 |

**Frameworks / libraries detected:** Anthropic API, OpenAI API

**Dependencies:** none detected

## Important source files

- `client/package.json`
- `client/tsconfig.json`
- `docker-compose.yml`
- `server/evals/cases/go-clean-loopvar/after/go.mod`
- `server/evals/cases/go-clean-loopvar/before/go.mod`
- `server/package.json`
- `server/tsconfig.json`

## Installation and setup

```sh
git clone https://github.com/rdlugs/sentryward.git && cd sentryward
cp .env.example .env

## Deployment

No deployment configuration detected.

## Documentation links

- http://localhost:5173
- http://localhost:4000/api
- http://localhost:4000/api/health
- https://`
- http://localhost:5173/api/connections/gitlab/oauth/callback`
- http://localhost:5173/api/connections/github/callback`
- https://sentryward.example.com/reviews
- http://host.docker.internal:11434/v1`
- https://sentryward.example.com/api/reviews

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/servicenow-ultimate-mcp
- hamids-ai-automations/shopify-growth-mcp
- hamids-ai-automations/ghl-devops-toolkit
- hamids-ai-automations/nexgen-financial-experts
- hamids-ai-automations/firebase-ai-starter-kit

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/sentryward/blob/main/README.md

```markdown
<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="client/public/sentryward-logo-dark.png">
    <img src="client/public/sentryward-logo-light.png" alt="Sentryward" width="360">
  </picture>
</h1>

<p align="center">
  <b>Self-hosted AI code review for GitHub pull requests and GitLab merge requests.</b>
</p>

<p align="center">
  <a href="https://github.com/rdlugs/sentryward/actions/workflows/ci.yml"><img src="https://github.com/rdlugs/sentryward/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/rdlugs/sentryward/releases"><img src="https://img.shields.io/github/v/release/rdlugs/sentryward?label=release" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#review-configuration">Configuration</a> ·
  <a href="CHANGELOG.md">Changelog</a> ·
  <a href="https://github.com/rdlugs/sentryward/discussions">Discussions</a>
</p>

Sentryward is an AI code reviewer for GitHub pull requests and GitLab merge requests.
Connect repositories, choose a model provider or Ollama, and run manual or
automatic reviews with inline findings, walkthroughs, and commit statuses. The
dashboard tracks reviews and findings across runs.

> [!WARNING]
> Sentryward is pre-1.0: minor releases may include breaking changes. AI findings
> need human verification and can miss problems or report false positives.
> `docker-compose.yml` is for development; to host an instance, see [Deploying](#deploying).

## Contents

- [Highlights](#highlights)
- [Quick start](#quick-start)
- [How it works](#how-it-works)
- [Getting started](#getting-started): [runtime environment](#docker-runtime-environment), [users and invites](#users-and-invites), [workspaces and teams](#workspaces-and-teams), [first review](#run-your-first-review), [troubleshooting](#troubleshooting)
- [Deploying](#deploying)
- [Forge connections](#forge-connections), [publishing](#publishing-to-the-forge), [automatic reviews](#automatic-reviews), [notifications](#notifications)
- [Review configuration](#review-configuration): [LLM connections](#llm-connections-and-custom-endpoints), [Ollama](#ollama), [`.sentryward.yaml`](#sentrywardyaml-reference), [review rules](#review-rules)
- [Privacy and data](#privacy-and-data): [what is stored](#what-is-stored), [what leaves the server](#what-leaves-the-server), [retention](#retention), [provider restrictions](#provider-and-host-restrictions), [audit log](#audit-log)
- [API](#api)
- [Development](#development)
- [Contributing and license](#contributing-and-license)

## Highlights

- **Self-hosted, bring your own model:** Anthropic, OpenAI, Google, a compatible
  proxy on a [custom host](#llm-connections-and-custom-endpoints), or a local
  [Ollama](#ollama) model.
- **GitHub and GitLab:** a GitHub App, plus GitLab.com or self-hosted GitLab.
- **Reviews where you work:** inline findings with suggestions, one summary
  comment, and a `sentryward/review` commit status.
- **Manual or automatic:** submit a PR/MR URL, review on webhooks, or comment
  `/sentryward review`.
- **Per-repository config:** dashboard settings, overridable by a
  [`.sentryward.yaml`](#review-configuration) in the repository.
- **Findings across runs:** a later run never posts the same finding twice.
  Ignore findings as false positives, intentional, or fix later, and track the
  false-positive rate on the dashboard, broken down by category, severity and
  model with a pointer to the setting that would quiet the noisiest ones.
- **Teams:** share connections, repositories, reviews and model keys in team
  workspaces, with owner, admin and member roles and one-time invite links,
  managed from **Team settings** in the workspace switcher.

## Quick start

```sh
git clone https://github.com/rdlugs/sentryward.git && cd sentryward
cp .env.example .env
# set JWT_SECRET and ENCRYPTION_KEY in .env, each with: openssl rand -hex 32
docker compose up --build
```

Open http://localhost:5173, register, then follow
[Run your first review](#run-your-first-review). The full setup is in
[Getting started](#getting-started).

## How it works

The `worker` container runs review jobs: it fetches the PR/MR, resolves the review configuration, sends the diff to the configured model in one or more passes (plus an optional walkthrough), validates the findings, re-checks blocking ones with a second model call (`review.verify`; `llm.walkthrough_model` and `llm.verify_model` can point those two calls at a different model than the review passes) and stores the result on the job. Model keys come from `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` or `GOOGLE_GENERATIVE_AI_API_KEY`, unless the repository's workspace has stored its own. The worker polls the `review_jobs` table (claimed with `FOR UPDATE SKIP LOCKED`, so several workers can run side by side); tune it with `WORKER_POLL_INTERVAL_MS`, `WORKER_CONCURRENCY`, `WORKER_LOCK_TIMEOUT_MS`, `WORKER_MAX_ATTEMPTS`, `WORKER_HEARTBEAT_INTERVAL_MS` and `WORKER_MAX_RUN_MS`. While a job runs the worker refreshes its lock every `WORKER_HEARTBEAT_INTERVAL_MS` (default 60s, keep it well below `WORKER_LOCK_TIMEOUT_MS`), so a long-but-healthy review is not reclaimed as a dead worker (the server refuses to start otherwise). `WORKER_MAX_RUN_MS` (default 30m) is the longest a review may take: a run past it is failed, healthy or not, and its slot freed, so raise it for repositories with very large reviews. A run that loses its job this way, or to stale-lock recovery, stops and publishes nothing more.

`REVIEW_RETENTION_DAYS` bounds how long reviews keep their bulky data (unset, the default, keeps everything). Once an hour the worker deletes superseded, skipped and cancelled reviews that finished more than that many days ago, and clears the stored result, resolved configuration and publication record of older completed, partial and failed ones. Those keep their row, status, verdict and summary, so the reviews list, stats and findings list are unaffected, while the review page says the full result has expired and its markdown export answers `410`. The newest completed or partial review of each change is never cleared, however old, so its findings keep their full details, replies on their inline threads can still be answered and the next push still gets an incremental review. A finding last reported by an older, cleared review (for example one ignored a while ago) keeps its row but loses its full details. Failed reviews that stored nothing are left as they are, so they still show their error. Pruning works in batches of 500 rows so it never holds long locks. Because cancelled reviews are deleted, a change cancelled or closed more than the window ago and later reopened at the same commit is reviewed again. An instance admin can set the period from the dashboard instead, which takes precedence over the environment variable, and each workspace can shorten it; see [Retention](#retention).

## Getting started

Requires Docker with Compose.

```sh
cp .env.example .env
# set JWT_SECRET and ENCRYPTION_KEY, each with: openssl rand -hex 32
# keep NODE_ENV=development for the local HTTP setup
docker compose up --build
```

The initial command builds the client and server dependency images. For subsequent
starts, use `docker compose up`. Source changes are bind-mounted into the containers
and picked up by the development watchers without rebuilding. Rebuild the images
when either `package.json` or `package-lock.json` changes.

- Web client: http://localhost:5173 (`CLIENT_HOST_PORT`)
- API: http://localhost:4000/api (`API_HOST_PORT`); the client proxies `/api` to it
- Postgres: localhost:5433 (`DB_HOST_PORT`)

If you change `CLIENT_HOST_PORT`, update `CLIENT_ORIGIN` to match.

Migrations are applied automatically when the `server` container starts.

Check startup without opening a
```
