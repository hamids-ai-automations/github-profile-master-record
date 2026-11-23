# cli

**Overview:** Local codebase intelligence for AI coding agents and software teams, in the CLI and VS Code. Vibgrate builds a deterministic Code Graph, measures dependency and runtime drift with DriftScore, maps architecture and blast radius, analyses dependency and vulnerability risk, and generates SBOM/VEX.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/cli](https://github.com/hamids-ai-automations/cli) |
| Live website | https://vibgrate.com |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-29 |
| Last update | 2026-10-29 |
| Last push | 2026-11-14 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 10 |
| Size | 8353 KB |
| Topics | - |

## Objectives

Objectives are not documented in a README. Repository description: Local codebase intelligence for AI coding agents and software teams, in the CLI and VS Code. Vibgrate builds a deterministic Code Graph, measures dependency and runtime drift with DriftScore, maps architecture and blast radius, analyses dependency and vulnerability risk, and generates SBOM/VEX..

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude-plugin, .github, bench, charts, docs, examples, packages, packaging, plugins, releases, scripts, skills, src, test, vendor
- **Total files (tracked in default branch):** 1798
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/docker-hub-mirror.yml, .github/workflows/docker.yml, .github/workflows/helm.yml, .github/workflows/packaging.yml, .github/workflows/publish-action.yml, .github/workflows/release.yml
- **Test files detected:** 758

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 11539681 |
| JavaScript | 229889 |
| Python | 93596 |
| C# | 76326 |
| Java | 73926 |
| Go Template | 4802 |
| Dockerfile | 3514 |
| Ruby | 1659 |
| PowerShell | 1051 |
| Shell | 1007 |

**Frameworks / libraries detected:** MCP

**Dependencies:** @modelcontextprotocol/sdk, @noble/hashes, @tree-sitter-grammars/tree-sitter-hcl, @types/node, @types/semver, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, chalk, commander, eslint, fast-xml-parser, gpt-tokenizer, graphology, graphology-communities-louvain, graphology-metrics, graphology-shortest-path, graphology-traversal, graphology-types, ignore, msgpackr, semver, smol-toml, tinypool, tree-sitter-wasms, tsup, tsx, typescript, vitest, web-tree-sitter, yaml

## Important source files

- `examples/go-pseudo-versions/go.mod`
- `examples/semver-build-metadata/go/go.mod`
- `examples/semver-build-metadata/java-gradle/build.gradle`
- `examples/semver-build-metadata/java/pom.xml`
- `examples/semver-build-metadata/package.json`
- `examples/semver-build-metadata/python/requirements.txt`
- `package.json`
- `packages/test-solutions/java-spring/pom.xml`
- `packages/test-solutions/node-turborepo/apps/admin/package.json`
- `packages/test-solutions/node-turborepo/apps/admin/tsconfig.json`
- `packages/test-solutions/node-turborepo/apps/api/package.json`
- `packages/test-solutions/node-turborepo/apps/api/tsconfig.json`
- `packages/test-solutions/node-turborepo/apps/web/package.json`
- `packages/test-solutions/node-turborepo/apps/web/tsconfig.json`
- `packages/test-solutions/node-turborepo/package.json`
- `packages/test-solutions/node-turborepo/packages/config/package.json`
- `packages/test-solutions/node-turborepo/packages/database/package.json`
- `packages/test-solutions/node-turborepo/packages/types/package.json`
- `packages/test-solutions/node-turborepo/packages/ui/package.json`
- `packages/test-solutions/node-turborepo/packages/ui/tsconfig.json`
- `packages/test-solutions/node-turborepo/packages/utils/package.json`
- `packages/test-solutions/node-turborepo/tsconfig.json`
- `packages/test-solutions/package.json`
- `packages/test-solutions/python-fastapi/app/main.py`
- `packages/test-solutions/python-fastapi/pyproject.toml`
- `test/fixtures/go-unpinned-require/go.mod`
- `test/fixtures/gradle-scopes/build.gradle`
- `test/fixtures/maven-multi-module/app/pom.xml`
- `test/fixtures/maven-multi-module/pom.xml`
- `test/fixtures/maven-scopes/pom.xml`
- `test/fixtures/sample/svc/app.py`
- `tsconfig.json`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://vibgrate.com

## Documentation links

- https://vibgrate.com
- https://vibgrate.com/img/vibgrate-logo-512.png
- https://www.npmjs.com/package/@vibgrate/cli
- https://dash.vibgrate.com/badges/driftscore/vibgrate/cli
- https://badges.vibgrate.com/vibgrate/cli
- https://dash.vibgrate.com/badges/riskscore/vibgrate/cli
- https://badges.vibgrate.com/riskscore/vibgrate/cli
- https://dash.vibgrate.com/badges/driftrisk/vibgrate/cli
- https://badges.vibgrate.com/driftrisk/vibgrate/cli
- https://vibgrate.com/cli
- https://vibgrate.com/graph
- https://vibgrate.com/driftscore
- https://vibgrate.com/riskscore
- https://vibgrate.com/driftrisk
- https://vibgrate.com/whitepapers/software-risk-and-drift-scoring-methodology
- https://doi.org/10.5281/zenodo.21336304
- https://vibgrate.com/vscode
- https://vibgrate.com/install.ps1
- https://vibgrate.com/library
- https://vibgrate.com/glossary/model-context-protocol
- https://vibgrate.com/img/cli-scenarios/node-turborepo/serve.gif
- https://vibgrate.com/cli/benchmarks/token-savings
- https://vibgrate.com/skills
- https://vibgrate.com/mcp
- https://vibgrate.com/img/cli-scenarios/node-turborepo/build.gif
- https://vibgrate.com/img/cli-scenarios/node-turborepo/ask.gif
- https://vibgrate.com/img/cli-scenarios/node-turborepo/impact.gif
- https://vibgrate.com/relay
- https://vibgrate.com/img/cli-scenarios/calcom/scan.gif
- https://vibgrate.com/glossary/sbom

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/ghl-devops-toolkit
- hamids-ai-automations/nexgen-financial-experts
- hamids-ai-automations/shopify-growth-mcp
- hamids-ai-automations/firebase-ai-starter-kit
- hamids-ai-automations/Go-High-Level-MCP-2026-Complete

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/cli/blob/main/README.md
