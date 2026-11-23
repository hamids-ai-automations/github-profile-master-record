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

<p align="center">
  <a href="https://vibgrate.com"><img src="https://vibgrate.com/img/vibgrate-logo-512.png" alt="Vibgrate" width="96" height="96" /></a>
</p>

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

Paste this into your AI coding tool (Claude, Cursor, Copilot, Gemini CLI, …):

```
Set up Vibgrate for local codebase intelligence:
1. Install: npm install -g @vibgrate/cli@latest
2. Build the graph: vg build
3. Wire your assistant: vg install
4. Ask: vg ask "what are the main entry points?"
Then explain the architecture and my top 3 upgrade priorities.
```

See [docs/QUICKSTART-PROMPT.md](https://github.com/hamids-ai-automations/cli/blob/main/docs/QUICKSTART-PROMPT.md) for the full prompt.

---

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

```markdown
<p align="center">
  <a href="https://vibgrate.com"><img src="https://vibgrate.com/img/vibgrate-logo-512.png" alt="Vibgrate" width="96" height="96" /></a>
</p>

<p align="center">
  <strong>@vibgrate/cli</strong>
  <br />
  Local codebase intelligence for AI coding agents — graph, drift, and version-correct docs on your machine
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@vibgrate/cli"><img src="https://img.shields.io/npm/v/@vibgrate/cli?color=blue&label=npm" alt="npm version" /></a>
  <a href="https://dash.vibgrate.com/badges/driftscore/vibgrate/cli"><img src="https://badges.vibgrate.com/vibgrate/cli" alt="Vibgrate DriftScore" /></a>
  <a href="https://dash.vibgrate.com/badges/riskscore/vibgrate/cli"><img src="https://badges.vibgrate.com/riskscore/vibgrate/cli" alt="Vibgrate RiskScore" /></a>
  <a href="https://dash.vibgrate.com/badges/driftrisk/vibgrate/cli"><img src="https://badges.vibgrate.com/driftrisk/vibgrate/cli" alt="Vibgrate DriftRisk" /></a>
  <a href="https://vibgrate.com/cli"><img src="https://img.shields.io/badge/live%20demo-vibgrate.com%2Fcli-3FB0A4" alt="live demo" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="Apache 2.0" /></a>
  <img src="https://img.shields.io/badge/node-%3E%3D24-brightgreen" alt="node 24+" />
</p>

Want to help? See [CONTRIBUTING.md](https://github.com/hamids-ai-automations/cli/blob/main/CONTRIBUTING.md) and [good first issues](https://github.com/vibgrate/cli/labels/good%20first%20issue).

```bash
npx @vibgrate/cli scan          # drift score + upgrade priorities
npm install -D @vibgrate/cli   # install for repeat runs
```

`vg` answers three questions for any repo:

1. **What is this codebase?** — A deterministic [code graph](https://vibgrate.com/graph): call trees, import paths, impact surfaces, dependency facts.
2. **How far behind is it?** — A ranked **[DriftScore](https://vibgrate.com/driftscore)** (0–100) with runtime/framework lag, dependency age and EOL proximity, and a prioritized fix list. Exposure is scored separately as a **[RiskScore](https://vibgrate.com/riskscore)**; the two together are the **[DriftRisk Index](https://vibgrate.com/driftrisk)**. The full methodology — formulas, sources, and limitations — is published as a [whitepaper](https://vibgrate.com/whitepapers/software-risk-and-drift-scoring-methodology) under CC BY 4.0 (DOI [10.5281/zenodo.21336304](https://doi.org/10.5281/zenodo.21336304)).
3. **Can we fix it here?** — [**VG Code**](#vg-code--write-the-change-not-just-the-report), a coding agent whose search tool is the code graph, not a grep — in your terminal as `vg code` and as the VG Code panel in [Vibgrate for VS Code](https://vibgrate.com/vscode) — plus `vg fix`, ranked upgrade plans it can apply.

Everything runs **on your machine**. No API key, no network call, no data leaving your repo unless you explicitly push. The `vibgrate` command is an alias for `vg` — they are interchangeable.

---

## See it run

<p align="center">
  <a href="https://vibgrate.com/cli">
    <img src="docs/demo/cli-demo.svg" alt="Animated terminal replay: npx @vibgrate/cli scan produces a 74/100 drift score, a score breakdown, and ranked upgrade priorities." width="620" />
  </a>
</p>

<p align="center">
  <sub>A real <code>vg scan</code> replay — drift score, breakdown, and ranked priorities in one command. Animation plays right here on GitHub; nothing runs in your browser.</sub>
</p>

<p align="center">
  <a href="https://vibgrate.com/cli"><strong>▶ Try the live, interactive CLI simulator →</strong></a><br />
  <sub>Step through every command (<code>scan</code>, <code>build</code>, <code>ask</code>, <code>why</code>, …) against real sample repos.</sub>
</p>

---

## Try it in 10 seconds

No install, no signup:

```bash
npx @vibgrate/cli scan          # drift score + upgrade priorities
npx @vibgrate/cli build         # build the code graph
npx @vibgrate/cli ask "what does AuthService do?"
npx @vibgrate/cli code          # a coding agent — it asks before every edit
```

Install for repeat runs:

```bash
npm install -D @vibgrate/cli
npx vg scan                     # vg is the primary command; vibgrate is an alias
```

> Local binaries live in `node_modules/.bin` — use `npx vg` (or an npm script) unless you install globally.

---

## Windows installation

Windows is supported with Node.js 24 or newer. PowerShell is the preferred shell for the Windows installer:

```powershell
irm https://vibgrate.com/install.ps1 | iex
```

If you prefer npm, install the CLI globally:

```powershell
npm install -g @vibgrate/cli
```

For a one-off run without changing PATH, use:

```powershell
npx @vibgrate/cli scan
```

A global npm install places the `vg.cmd` and `vibgrate.cmd` shims in npm's global prefix. Check the exact location with `npm config get prefix`; if `vg` is not found, add that directory to your user `PATH`, then open a new PowerShell window. Verify the installation with:

```powershell
vg --help
vg doctor
```

`vg doctor` is a read-only diagnostic command. If `vg` conflicts with another command on your system, use the identical `vibgrate` command instead. Command examples elsewhere in this README use POSIX path syntax; adapt paths to PowerShell on Windows.

---

## Use it with your AI assistant

`vg serve` starts **[Vibgrate AI Context](https://vibgrate.com/library)** — a local-first [MCP](https://vibgrate.com/glossary/model-context-protocol) server that
gives any MCP-compatible assistant (Claude, Cursor, Windsurf, Copilot, Gemini
CLI, …) your code map, **offline drift**, local models, and **version-correct
library docs**, all from your machine (no account, nothing uploaded; thin
local docs fall through to the hosted catalog unless you pass `--local`). No
context-window stuffing, no hallucinated APIs. The map **keeps itself fresh**:
when files change — including edits the assistant itself just made — the next
tool call rebuilds it incrementally before answering, with no watcher or
daemon involved.

<p align="center">
  <a href="https://vibgrate.com/cli">
    <img src="https://vibgrate.com/img/cli-scenarios/node-turborepo/serve.gif" alt="Recorded node-turborepo/serve replay of the real Vibgrate CLI" width="620" />
  </a>
</p>
<p align="center"><sub><code>node-turborepo/serve</code> — <code>vg serve --http</code> starts Vibgrate AI Context. <a href="https://vibgrate.com/cli">Live simulator</a>.</sub></p>

Wire it up in one command:

```bash
vg install                      # interactive: pick your assistant(s) and done
vg install --all                # install for every detected assistant at once
```

This writes the MCP config for your chosen tool(s) and installs a skill that teaches the assistant how to query the graph. After reloading your assistant you get graph-aware answers: call trees, impact analysis, drift findings, version-correct library docs — all from local data. The token savings are measured and published, methodology included, at [vibgrate.com/cli/benchmarks/token-savings](https://vibgrate.com/cli/benchmarks/token-savings).

Browse all 21+ supported assistants and their skill descriptions at **[vibgrate.com/skills](https://vibgrate.com/skills)**.

## Cut what your assistant re-reads: context compression

Every turn, your AI assistant re-sends the whole conversation — including the
20,000-line test log, the 400-row JSON payload, and the grep output it has
already acted on. You pay for that context again on every step. Vibgrate CLI
compresses tool output and older turns **before** they reach the model, keeps
the originals retrievable on your machine, and reports what it saved.

```bash
vg install claude --compress    # point Claude Code at the listener and start it (undo with `vg uninstall claude`)
vg savings                      # tokens and estimated dollars saved, today / 7 days / 30 days
```

There is no separate command to learn: compression is a mode of the server you
already run and a flag on the installer you already 
```
