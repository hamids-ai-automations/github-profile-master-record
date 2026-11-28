# meho

**Overview:** Governance backplane for AI agents acting on infrastructure — policy-gated, audit-grade, MCP-native. Apache 2.0.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/meho](https://github.com/hamids-ai-automations/meho) |
| Live website | https://evoila.github.io/meho/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-01 |
| Last update | 2026-11-01 |
| Last push | 2026-11-01 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 12 |
| Size | 63344 KB |
| Topics | - |

## Objectives

# MEHO

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude-plugin, .github, .oss-scanner, backend, ci, cli, clients, deploy, docs, docs-site, examples, scripts
- **Total files (tracked in default branch):** 4511
- **CI workflows:** .github/workflows/chart.yml, .github/workflows/ci.yml, .github/workflows/cli-release.yml, .github/workflows/connector-overlay.yml, .github/workflows/consumer-tool-name-check.yml, .github/workflows/dependency-license-check.yml, .github/workflows/docs-site.yml, .github/workflows/eval-gate.yml, .github/workflows/image.yml, .github/workflows/linux-download.yml, .github/workflows/linux-server-test.yml, .github/workflows/mcpb-bundle.yml, .github/workflows/merge-queue-cleanup.yml, .github/workflows/migration-compat.yml, .github/workflows/migration-heads.yml, .github/workflows/plugin-test.yml, .github/workflows/plugin-version-check.yml, .github/workflows/pr-smoke.yml, .github/workflows/quality-gate.yml, .github/workflows/readme-version-check.yml
- **Test files detected:** 1677

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 55398602 |
| Go | 5601381 |
| HTML | 1255289 |
| Shell | 381289 |
| JavaScript | 255497 |
| Dockerfile | 36418 |
| Go Template | 34421 |
| CSS | 23941 |
| Makefile | 6315 |
| HCL | 5902 |
| PLpgSQL | 3479 |
| Jinja | 2927 |
| Mako | 693 |

**Frameworks / libraries detected:** Next.js

**Dependencies:** none detected

## Important source files

- `backend/pyproject.toml`
- `backend/src/meho_backplane/main.py`
- `cli/go.mod`
- `clients/claude-code-plugin/package.json`
- `clients/claude-desktop-mcpb/package.json`
- `deploy/connector-overlay/example/pyproject.toml`
- `pyproject.toml`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://evoila.github.io/meho/

## Documentation links

- https://evoila.github.io/meho
- https://meho.example.com/mcp
- https://meho.example.com`
- https://raw.githubusercontent.com/evoila/meho/main/deploy/values-examples/values-kind.yaml
- https://github\.com/evoila/meho/\.github/workflows/image\.yml@refs/(heads/main|tags/v.+
- https://token.actions.githubusercontent.com
- https://github\.com/evoila/meho/\.github/workflows/chart\.yml@refs/(heads/main|tags/v.+
- https://github\.com/evoila/meho/\.github/workflows/cli-release\.yml@refs/tags/v.+$
- https://keepachangelog.com/en/1.1.0

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/marvis-streamlit-dashboard
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/adwaste-intelligence

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/meho/blob/main/README.md

```markdown
# MEHO

> Governance backplane for AI agents acting on infrastructure —
> policy-gated, audit-grade, MCP-native. Apache 2.0.

[![Release](https://img.shields.io/github/v/release/evoila/meho)](https://github.com/evoila/meho/releases)
[![CI](https://github.com/evoila/meho/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/evoila/meho/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](./LICENSE)
[![OSS](https://img.shields.io/badge/OSS-public%20from%20day%201-success.svg)](./CONTRIBUTING.md#public-from-day-1-deliberately)

**Status:** Released — see the release badge above for the current version.
The backplane image, Helm chart, and operator CLI are all shipped and cosign-signed.

**Documentation:** <https://evoila.github.io/meho/> — the published,
versioned docs site (install, client setup, task guides) and the primary
entry point for operators. It builds from `docs-site/`; the `docs/` tree
in this repo is separate, contributor-facing material.

## The problem

AI agents are getting good enough to *do* infrastructure work — roll a
credential, drain a node, restart a service — not just describe it. But
handing an agent a long-lived admin token and a shell is how you get an
un-auditable, over-privileged actor loose in production. The moment an
agent can act, you need the same controls you'd demand of any operator:
who is allowed to do what, with credentials that expire, against which
targets, with every action recorded and reviewable.

Today that control plane doesn't exist. Each team bolts ad-hoc wrappers
around an MCP server, or trusts the agent runtime to behave. MEHO is the
missing layer.

## What MEHO is

MEHO is the layer that turns **"any MCP client"** into **"any MCP client
*operating against real infrastructure under audit*."**

It sits between AI agents (Claude Code, Cursor, Cline, Continue, custom
MCP clients) and the infrastructure they operate against (Kubernetes,
vCenter / VCF, NSX, public cloud, network appliances, secrets stores).
Every operation passes through a single governed seam before it touches
anything real.

The agent runtime is *not* part of MEHO. **Bring your own agent** — MEHO
governs what it's allowed to do.

### What it guarantees

Every interaction through MEHO is:

- **Policy-gated** — operations are authorised against the caller's role
  and per-target grants before they execute.
- **Credential-federated** — the agent never holds a backend credential;
  a short-lived Keycloak OIDC token is exchanged with Vault for a
  just-in-time backend credential per operation.
- **Server-reduced** — results are reduced server-side, so the agent
  sees a compact, relevant view instead of raw firehose output.
- **Broadcast** — every action is published to a real-time activity feed
  other agents and humans can watch.
- **Audited** — every interaction lands as an immutable audit row in
  PostgreSQL, attributed to the calling principal.
- **Tenant-scoped & version-aware** — every context lookup is scoped to
  the caller's tenant and aware of resource versions.

## Why MEHO

A governance seam in front of an MCP server is reproducible. What is not
reproducible is **operating knowledge of the on-prem stack** the agent is
acting on. MEHO's moat is the two together: a policy/credential/audit
layer **and** connectors that encode how VCF, NSX, and vSphere are
actually operated — not just thin API passthrough.

The VMware/VCF surface is the clearest example. Under
[`backend/src/meho_backplane/connectors/`](https://github.com/hamids-ai-automations/meho/blob/main/backend/src/meho_backplane/connectors/)
the connectors are not 1:1 HTTP wrappers:

- **`vmware_rest` composites** encode real operational sequences as single
  governed operations — `host.evacuate` (which orchestrates `vm.migrate`
  under the hood), `cluster.drs_recommendations`, `vm.snapshot.revert`,
  `host.detach_from_vds`, `cluster.patch` — each with pre-flight checks,
  not a raw vCenter call the agent has to chain by hand.
- **`nsx`** speaks the Policy API directly — Tier-0/Tier-1 gateways,
  segments, and domain security-policies — the objects an NSX operator
  reasons about, not bare REST paths.
- **`vcf_operations`, `vcf_fleet`, `vcf_logs`, `vcf_automation`,
  `sddc_manager`** cover the VCF management plane an operator lives in:
  Operations alerts/symptoms/recommendations, SDDC Manager
  domains/clusters/bundles, fleet and log surfaces.

Public-cloud and Kubernetes connectors exist too, but they are
commodity — many tools cover them. The defensible part is the deep VCF /
on-prem operator fluency baked into the connectors, governed by the same
policy + audit seam as everything else. That combination is the moat.

### How MEHO compares

| | MEHO | Teleport / StrongDM | Raw MCP gateway | `kubectl` / vCenter by hand |
| --- | --- | --- | --- | --- |
| **Built for AI agents acting on infra** | Yes — MCP-native, agent is the first-class caller | No — human-session access (SSH/DB/k8s) | Partial — transport only, no policy/audit semantics | No — human at a terminal |
| **VCF / NSX / vSphere operator depth** | Yes — connectors encode operational sequences (host evacuation, DRS, NSX policy) | No — protocol-level access, no domain ops | No — passthrough to whatever the upstream MCP exposes | Only what the operator knows + types |
| **Per-action policy gate + immutable audit** | Yes — every `tools/call` authorised + audited per principal | Session-level audit, not per-agent-action semantics | No — you build it | No structured audit by default |
| **Just-in-time backend credentials** | Yes — Keycloak→Vault token exchange, agent never holds a secret | Yes (its own broker) | No — you wire your own secret handling | No — long-lived admin creds |
| **Bring-your-own agent runtime** | Yes — governs any MCP client, runs no model | N/A | Yes | N/A |

## See it work

The [`examples/r4-local-claude/`](https://github.com/hamids-ai-automations/meho/blob/main/examples/r4-local-claude/) reference
pattern wires your local Claude Code to a MEHO backplane under your own
Keycloak identity. The full walkthrough is in
[`GUIDE.md`](https://github.com/hamids-ai-automations/meho/blob/main/examples/r4-local-claude/GUIDE.md); the shape of one
audited round-trip is below.

**1. Point your MCP client at MEHO.** Drop this into your repo as
`.mcp.json` (full example, including the `mcp-remote` stdio variant, in
[`mcp.json.example`](https://github.com/hamids-ai-automations/meho/blob/main/examples/r4-local-claude/mcp.json.example)):

```json
{
  "mcpServers": {
    "meho": {
      "type": "http",
      "url": "https://meho.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${MEHO_MCP_TOKEN}"
      }
    }
  }
}
```

The token comes from `meho login https://meho.example.com` (Keycloak
device-code flow) — the agent never sees a backend credential.

**2. Ask the agent to do something.** In your Claude Code session:

> what's interesting on the MEHO backplane right now?

The session calls the `search_memory` tool over MCP. MEHO authorises the
call against your role, executes it under a just-in-time credential, and
reduces the result before the agent ever sees it.

**3. The operation leaves an audit trail.** Every `tools/call` lands one
immutable audit row, attributed to *your* Keycloak `sub` — and emits a
broadcast event other watchers can see:

```bash
meho audit query --op-id search_memory --limit 1 --json \
  | jq '.rows[0] | {principal_sub, op_id, occurred_at}'
# -> {"principal_sub": "<your-keycloak-sub>", "op_id": "search_memory", ...}
```

The same identity model, RBAC, and audit trail apply whether the caller
is your local Claude session or a 24/7 hosted triage agent — there are
no parallel auth boundaries to learn.

## Architecture

```mermaid
flowchart LR
    A["MCP clients<br/>(Claude Code · Cursor · Cline · custom)"]
    subgraph MEHO["MEHO backplane"]
        direction TB
        P["policy gate"]
        T["token exchange<br/>(Key
```
