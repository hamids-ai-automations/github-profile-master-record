# OpnForm

**Overview:** Beautiful Open-Source Form Builder

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/OpnForm](https://github.com/hamids-ai-automations/OpnForm) |
| Live website | https://opnform.com |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-11-15 |
| Default branch | main |
| License | NOASSERTION |
| Primary language | PHP |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 35 |
| Size | 60356 KB |
| Topics | - |

## Objectives

# OpnForm

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .agents, .codex, .cursor, .github, api, client, deploy, docker, docs, plugins, scripts, tests
- **Total files (tracked in default branch):** 2380
- **CI workflows:** .github/workflows/ci-cd.yml, .github/workflows/dependency-security.yml, .github/workflows/discord-notifications.yml, .github/workflows/scaleway-deployment.yml, .github/workflows/scaleway-validation.yml
- **Test files detected:** 400

## Languages and technologies

| Language | Bytes |
| --- | --- |
| PHP | 4442667 |
| Vue | 1956772 |
| TypeScript | 615203 |
| Python | 68019 |
| JavaScript | 67072 |
| Shell | 57711 |
| Blade | 53443 |

**Frameworks / libraries detected:** none detected from dependency files

**Dependencies:** none detected

## Important source files

- `client/api/index.js`
- `client/composables/index.js`
- `client/lib/formulas/functions/index.js`
- `client/lib/formulas/index.js`
- `client/lib/sdk/index.js`
- `client/package.json`
- `client/server/tsconfig.json`
- `client/tsconfig.json`
- `docker-compose.yml`

## Installation and setup

The easiest way to get started with OpnForm is through our [official managed service in the Cloud](https://opnform.com/).

For self-hosted installations, please refer to our [Deployment Guides](https://docs.opnform.com/deployment). For local development, we provide a minimal Docker-based setup - check out our [Docker Development Guide](https://docs.opnform.com/deployment/docker-development).

The client `npm run build` also checks the public form bundle size and eager dependencies. This check reads `.nuxt/dist/client/_nuxt`, independently of Nitro's deployment output directory (including AWS Amplify's `.amplify-hosting`). Run its regression tests from `client/` with `node --test scripts/check-public-form-bundle.test.mjs`.

The public form budget is **425 KiB gzip**. On 25 October 2026, the integrations-content update brought the unchanged `main` build to 419.3 KiB, still within the old 420 KiB limit. The combined security fixes measured 421.7 KiB: an additional 2.4 KiB (about 0.6%). The previous baseline used 416.4 KiB of a 420 KiB budget. The new limit accepts this measured increase and restores comparable headroom without changing the forbidden eager-dependency checks. Regression fixtures verify that a route around 424 KiB passes and one around 426 KiB fails.

## Deployment

Firebase/other hosting declared via homepage field: https://opnform.com

## Documentation links

- https://opnform.com
- https://hub.docker.com/r/jhumanj/opnform-api
- https://feedback.opnform.com
- https://discord.gg/YTSjU2a9TS
- https://docs.opnform.com/deployment/cloud-vs-self-hosting
- https://opnform.com/pricing
- https://docs.opnform.com
- https://docs.opnform.com/integrations/mcp
- https://docs.opnform.com/deployment
- https://docs.opnform.com/deployment/docker-development
- https://help.opnform.com
- https://opnform.com/terms-conditions

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/dynamic-schema-generator
- hamids-ai-automations/gohighlevel-php-sdk

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/OpnForm/blob/main/README.md

```markdown
# OpnForm

<p align="center">
<img src="https://github.com/OpnForm/OpnForm/blob/main/client/public/img/social-preview.jpg?raw=true">
</p>

<p align="center">
<a href="https://github.com/OpnForm/OpnForm/stargazers"><img src="https://img.shields.io/github/stars/OpnForm/OpnForm" alt="Github Stars"></a>
</a>
<a href="https://github.com/OpnForm/OpnForm/pulse"><img src="https://img.shields.io/github/commit-activity/m/OpnForm/OpnForm" alt="Commits per month"></a>
<a href="https://hub.docker.com/r/jhumanj/opnform-api">
<img src="https://img.shields.io/docker/pulls/jhumanj/opnform-api">
</a>
<a href="https://github.com/OpnForm/OpnForm/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-AGPLv3-purple" alt="License">
<a href="https://github.com/OpnForm/OpnForm/issues/new"><img src="https://img.shields.io/badge/Report a bug-Github-%231F80C0" alt="Report a bug"></a>
<a href="https://github.com/OpnForm/OpnForm/discussions/new?category=q-a"><img src="https://img.shields.io/badge/Ask a question-Github-%231F80C0" alt="Ask a question"></a>
<a href="https://feedback.opnform.com"><img src="https://img.shields.io/badge/Feature request-Featurebase-%231F80C0" alt="Ask a question"></a>
<a href="https://discord.gg/YTSjU2a9TS"><img src="https://img.shields.io/badge/OpnForm-Discord-%235865F2.svg" alt="Ask a question"></a>
</p>

OpnForm is an open-source form builder.

## Get Started

The easiest way to get started with OpnForm is to sign up for our [managed service in the Cloud](https://opnform.com/). You get support, backups, upgrades, and more. Your data is safe and secure, and you don't need to worry about maintenance or infrastructure. Check out our quick overview of [cloud vs self-hosting](https://docs.opnform.com/deployment/cloud-vs-self-hosting).

The cloud [pricing page](https://opnform.com/pricing) shows monthly equivalents for yearly billing by default. The Monthly / Yearly selector updates both the plan cards and the feature comparison table; yearly plans are billed annually.

## Key Features

-   🚀 No-code builder with unlimited forms & submissions
-   📝 Various input types: Text, Date, URL, File uploads & much more
-   🌐 Embed anywhere
-   📧 Email notifications
-   💬 Integrations (Slack, Webhooks, Discord)
-   🧠 Form logic & customization
-   🛡️ Captcha protection
-   📊 Form analytics

For a complete list of features and detailed documentation, visit our [Technical Documentation](https://docs.opnform.com).

## AI agents and MCP

OpnForm's remote MCP server lets AI agents create and preview a private form draft without requiring a login. OAuth adds workspace-aware form management and read-only submission search, statistics, and exports. The installable portable and native plugin package lives in [`plugins/opnform/`](https://github.com/hamids-ai-automations/OpnForm/blob/main/plugins/opnform). See the [MCP integration guide](https://docs.opnform.com/integrations/mcp).

## Quick Start

The easiest way to get started with OpnForm is through our [official managed service in the Cloud](https://opnform.com/).

For self-hosted installations, please refer to our [Deployment Guides](https://docs.opnform.com/deployment). For local development, we provide a minimal Docker-based setup - check out our [Docker Development Guide](https://docs.opnform.com/deployment/docker-development).

The client `npm run build` also checks the public form bundle size and eager dependencies. This check reads `.nuxt/dist/client/_nuxt`, independently of Nitro's deployment output directory (including AWS Amplify's `.amplify-hosting`). Run its regression tests from `client/` with `node --test scripts/check-public-form-bundle.test.mjs`.

The public form budget is **425 KiB gzip**. On 25 October 2026, the integrations-content update brought the unchanged `main` build to 419.3 KiB, still within the old 420 KiB limit. The combined security fixes measured 421.7 KiB: an additional 2.4 KiB (about 0.6%). The previous baseline used 416.4 KiB of a 420 KiB budget. The new limit accepts this measured increase and restores comparable headroom without changing the forbidden eager-dependency checks. Regression fixtures verify that a route around 424 KiB passes and one around 426 KiB fails.

## Form list performance

The dashboard fetches lightweight summaries in batches of 50. The API keeps its default page size of 10 and its maximum of 100 for other callers. It paginates forms before loading view and completed-submission counts for the returned IDs. Historical views use an index on `form_statistics.form_id`, and the aggregate is explicitly aliased as `total_views_count` so the model uses the preloaded value.

The index migration runs outside a transaction and uses `CREATE INDEX CONCURRENTLY` on PostgreSQL to keep writes available. It also recovers an invalid index left by an interrupted build. Run this migration through Laravel normally; do not wrap it in an external transaction. MySQL and SQLite use the standard schema index migration.

## Codex worktrees

Codex creates an isolated local environment for each worktree. It uses a dedicated PostgreSQL Docker volume and local Laravel/Nuxt processes, so sibling worktrees do not share ports, data, or API configuration.

Use the Codex `Start app`, `Reset DB`, and `Stop app` actions when available. You can also run the scripts directly:

```bash
./scripts/codex-worktree-setup.sh
./scripts/codex-worktree-up.sh
```

The startup command prints the worktree-specific URL. Opening its root URL automatically signs in the local Codex admin (`e2e@example.test` / `Abcd@1234`). The seed also creates three forms, including five completed submissions across two public forms, so the dashboard and submission screens are immediately useful. Reset only the current worktree database with:

```bash
./scripts/codex-worktree-reset-db.sh
```

Run the browser suite against the running worktree with:

```bash
./scripts/codex-worktree-test-e2e.sh
```

## Dependency security

The API resolves dependencies for PHP 8.3.36; use a patched PHP 8.3 or 8.4 runtime compatible with the lock and run `composer check-platform-reqs`. The client requires Node `^22.22.3 || ^24.15.0 || >=26`; CI and Docker use 24.22.1, also recorded in `client/.nvmrc`.

Nuxt Content uses the native `node:sqlite` connector, including on Amplify's Node 24 runtime. Its Zod dependency is pinned to the patched v4 line through a scoped npm override; keep that override until Nuxt Content updates its dependency range.

The executable npm audit policy is in [scripts/npm-exceptions.json](https://github.com/hamids-ai-automations/OpnForm/blob/main/scripts/npm-exceptions.json). Dependabot checks Composer, client npm packages, and GitHub Actions weekly, with up to three open version-update PRs per ecosystem. Compatible application updates are grouped; major application dependency updates remain separate except for the coordinated VueUse packages. GitHub Actions updates are grouped together. Security update handling is unchanged.

The lock requires node-forge 1.4.1 or newer. Its former RSA-verification exception has been removed; dated exceptions for other packages remain enforced.

## Date fields

Clearing a date with a click, Enter, or Space keeps the calendar closed. Reopen it to choose another date.

## Editor history

The form editor shows whether changes are saved. For an existing form, **Save Changes** saves both its design and settings; changes to a published form take effect immediately. In **Settings**, use **Save and close** to save directly, or **Close** to return to the editor with your changes still pending. While saving, Settings cannot be edited or dismissed. Failed saves preserve the pending edits for retry, and validation errors lead to the relevant field editor. For a new form, **Done** applies settings without creating or publishing it. Leaving the editor with unsaved changes asks for confirmation.

Clearing editor history uses the currently loaded form as the undo baseline and discards pending history updat
```
