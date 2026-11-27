# opencomplai

**Overview:** Code-First AI Compliance. The open-source regulatory engine for the EU AI Act. Automate your risk assessments directly within your CI/CD pipeline.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/opencomplai](https://github.com/hamids-ai-automations/opencomplai) |
| Live website | https://opencomplai.com/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-11-01 |
| Default branch | main |
| License | AGPL-3.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 8 |
| Size | 9995 KB |
| Topics | - |

## Objectives

# OpenComplAI: Compliance-as-Code for AI Pipelines

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, api, assets, docs, examples, infra, integrations, packages, packaging, scripts, services, sync, templates, tests, tools
- **Total files (tracked in default branch):** 1107
- **CI workflows:** .github/workflows/actionlint.yml, .github/workflows/ci-node.yml, .github/workflows/ci-python.yml, .github/workflows/codeql.yml, .github/workflows/dco.yml
- **Test files detected:** 474

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 4376907 |
| HTML | 176239 |
| TypeScript | 115869 |
| PowerShell | 46777 |
| Shell | 43199 |
| Dockerfile | 9293 |
| Ruby | 754 |
| JavaScript | 711 |

**Frameworks / libraries detected:** FastAPI, Jest, pytest

**Dependencies:** none detected

## Important source files

- `api/docs-gen/requirements.txt`
- `api/egress/requirements.txt`
- `api/evidence/requirements.txt`
- `api/gateway/tsconfig.json`
- `api/risk/requirements.txt`
- `docs/checker-widget/package.json`
- `docs/checker-widget/tsconfig.json`
- `examples/sample-system/under-declared-analytics/requirements.txt`
- `examples/sample-system/under-declared-chatbot/requirements.txt`
- `infra/compose/docker-compose.yml`
- `package.json`
- `packages/ai/pyproject.toml`
- `packages/cli/pyproject.toml`
- `packages/cli/src/opencomplai_cli/main.py`
- `packages/core/pyproject.toml`
- `packages/sdk-python/pyproject.toml`
- `pyproject.toml`
- `services/doc-generator/pyproject.toml`
- `services/doc-generator/src/opencomplai_doc_generator/main.py`
- `services/egress-proxy/pyproject.toml`
- `services/egress-proxy/src/opencomplai_egress_proxy/main.py`
- `services/evidence-vault/pyproject.toml`
- `services/evidence-vault/src/opencomplai_evidence_vault/main.py`
- `services/gateway-api/package.json`
- `services/gateway-api/tsconfig.json`
- `services/risk-engine/pyproject.toml`
- `services/risk-engine/src/opencomplai_risk_engine/main.py`
- `tests/fixtures/eu_ai_scan/requirements.txt`
- `tests/fixtures/eu_ai_scan/src/app.py`

## Installation and setup

Get your first compliance check running in **under 15 minutes**:

```bash
pip install opencomplai
```

This installs the CLI, core rule engine, and SDK with a stable API contract (see
[CHANGELOG](https://github.com/hamids-ai-automations/opencomplai/blob/main/CHANGELOG.md) for exit-code and artifact-schema guarantees).

```bash
opencomplai init --system-id my-model --intended-purpose "customer support chatbot"
opencomplai check
```

That's the local loop. For the full path — CI gate, optional dashboard push, pre-commit
hook, and self-hosted Docker Compose — see the
[Deployment Journey](https://github.com/hamids-ai-automations/opencomplai/blob/main/docs/src/getting-started/deployment-journey.md).

## Deployment

Firebase/other hosting declared via homepage field: https://opencomplai.com/

## Documentation links

- https://www.python.org
- https://opencomplai.com
- https://pypi.org/project/opencomplai
- https://nodejs.org
- https://docs.opencomplai.com/getting-started/scanner/#ocignore
- https://discord.gg/egjX5JgQJ
- https://www.linkedin.com/company/opencomplai
- https://www.reddit.com/user/akin_opencomplai/m/opencomplai_research
- https://docs.opencomplai.com/getting-started/eu-ai-act-checker

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/opencomplai/blob/main/README.md

```markdown
# OpenComplAI: Compliance-as-Code for AI Pipelines

**Stop manual audits → Start shipping.**

OpenComplAI brings AI compliance directly into your CI/CD pipeline, turning fragmented legal mandates into automated, machine-readable "Pre-Ship Checks." The EU AI Act is evaluated natively; NIST AI RMF 1.0 is derived from the same evidence.

[![CI (Python)](https://github.com/Opencomplai/opencomplai/actions/workflows/ci-python.yml/badge.svg?branch=main)](https://github.com/Opencomplai/opencomplai/actions/workflows/ci-python.yml) [![CI (Node)](https://github.com/Opencomplai/opencomplai/actions/workflows/ci-node.yml/badge.svg?branch=main)](https://github.com/Opencomplai/opencomplai/actions/workflows/ci-node.yml) [![PyPI](https://img.shields.io/pypi/v/opencomplai)](https://pypi.org/project/opencomplai/) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE) [![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/) [![Node.js 24+](https://img.shields.io/badge/node-24%2B-339933)](https://nodejs.org/)

### Demo

![OpenComplAI quickstart — opencomplai scan --quick in action](https://raw.githubusercontent.com/hamids-ai-automations/opencomplai/main/assets/opencomplai-quickstart.gif)

<video src="assets/opencomplai.mp4" controls width="100%">
  Your browser does not support the video tag.
</video>

[Watch the full narrated walkthrough (MP4)](https://github.com/hamids-ai-automations/opencomplai/blob/main/assets/opencomplai.mp4) — the GIF above is the
30-second zero-setup scan; the MP4 is the deeper narrated tour.

## Why OpenComplAI?

Traditional GRC tools are disconnected dashboards that create "velocity tax." We shift compliance left:

- **Prevent Non-Compliance:** Gate releases by blocking builds that violate safety rules.
- **Automated Evidence:** `opencomplai check` writes `compliance-artifact.json` with evidence hashes for every run; it is signed only when you pass `--sign` and a local signing key exists.
- **Frameworks Side by Side:** Assess one system against the EU AI Act and NIST AI RMF 1.0 side by side (`compliance_targets` in the manifest, or `opencomplai gaps --target EU_AI_ACT --target NIST_AI_RMF`). The EU AI Act is evaluated natively; NIST AI RMF is re-projected per subcategory from that same EU AI Act evidence through a built-in crosswalk, with no scanner of its own (see [NIST AI RMF](https://github.com/hamids-ai-automations/opencomplai/blob/main/docs/src/concepts/nist-ai-rmf.md)). ISO/IEC 42001 is a native pack of attestation rows that read Unverified until you record an attestation under `framework_inputs` (`--target ISO_IEC_42001`). DORA and EBA are mapped only: `gaps --map-to DORA|EBA` adds a low-confidence citation per EU AI Act article (see [Mapped regimes](https://github.com/hamids-ai-automations/opencomplai/blob/main/docs/src/concepts/mapped-regimes.md)). Standing line: EU AI Act evaluated; NIST AI RMF derived (partial, unreviewed); ISO 42001 native pack, attestation-led (partial, unreviewed); DORA and EBA mapped only. See [Frameworks](https://github.com/hamids-ai-automations/opencomplai/blob/main/docs/src/frameworks/index.md).

## Who it is for

Teams that build, fine-tune or substantially modify AI systems and need a per-release EU AI Act check in CI.
It is not a GRC platform or an eval tool; it runs beside them and stays offline unless you run `opencomplai push`.
See [Works alongside other tools](https://github.com/hamids-ai-automations/opencomplai/blob/main/docs/src/guides/works-alongside.md).

## How It Works (The 3-Minute Setup)

1. **Define:** Create a compliance manifest for your model.
2. **Integrate:** Copy the ready-made [GitHub Actions/GitLab CI workflow](https://github.com/hamids-ai-automations/opencomplai/blob/main/docs/src/guides/ci-integration.md) into your pipeline, or use the [GitHub Action](https://github.com/hamids-ai-automations/opencomplai/blob/main/integrations/github-action/README.md) for a sticky pull request comment.
3. **Ship:** Get an automated "Pass/Fail" result before your code ever hits production.

[**Check out our Dummy Repo (Sandbox)**](https://github.com/hamids-ai-automations/opencomplai/blob/main/examples/gate-demo/) – *Five fictional systems, one per gate outcome (exit codes 3, 4, 1, 1, 0). Illustrative sandbox, not legal advice. It does not scan code.*

## Core Components

- `opencomplai-core`: The rule engine that evaluates controls.
- `opencomplai-cli`: Run checks locally in your dev environment.
- `opencomplai`: The Python SDK for embedding compliance into your own tooling — and the
  package `pip install opencomplai` actually installs. It depends on `opencomplai-core` and
  `opencomplai-cli`, so a single `pip install opencomplai` pulls in the whole stack (rule
  engine, CLI, and SDK) in one go.

## Quick Start

Get your first compliance check running in **under 15 minutes**:

```bash
pip install opencomplai
```

This installs the CLI, core rule engine, and SDK with a stable API contract (see
[CHANGELOG](https://github.com/hamids-ai-automations/opencomplai/blob/main/CHANGELOG.md) for exit-code and artifact-schema guarantees).

```bash
opencomplai init --system-id my-model --intended-purpose "customer support chatbot"
opencomplai check
```

That's the local loop. For the full path — CI gate, optional dashboard push, pre-commit
hook, and self-hosted Docker Compose — see the
[Deployment Journey](https://github.com/hamids-ai-automations/opencomplai/blob/main/docs/src/getting-started/deployment-journey.md).

`opencomplai scan` inventories files via a repo-root `.ocignore` (not `.gitignore`),
bootstrapped once from `.gitignore` on first scan unless you pass
`--no-ocignore-bootstrap`. `opencomplai check --scan` bootstraps and uses it the same
way; plain `opencomplai check` never touches it. See
[`.ocignore` scan configuration](https://docs.opencomplai.com/getting-started/scanner/#ocignore).

## Community & Feedback

OpenComplAI is free to use today — `opencomplai scan --quick` and the EU AI Act Checker below
both work with zero setup. We're actively building with early adopters and want your feedback.

- **[Join our Developer Discord](https://discord.gg/egjX5JgQJ)** — discuss EU AI Act workflows, pipeline integration, and stress-test the engine with other MLOps engineers
- [Report a bug](https://github.com/Opencomplai/opencomplai/issues/new?template=bug-report.yml) · [Request a feature](https://github.com/Opencomplai/opencomplai/discussions/new?category=ideas)
- [LinkedIn](https://www.linkedin.com/company/opencomplai) · [Reddit research community](https://www.reddit.com/user/akin_opencomplai/m/opencomplai_research/)

## EU AI Act Checker

Not sure whether the EU AI Act applies to your system, or which obligations you carry as a provider versus a deployer? Use the interactive [EU AI Act Checker](https://docs.opencomplai.com/getting-started/eu-ai-act-checker/) — a browser-based wizard covering scope, high-risk classification, GPAI, and obligations. No account needed. Or run it locally:

```bash
opencomplai checker --web          # opens the hosted docs page
opencomplai checker --web --local  # serves a self-contained copy offline
```

## Persistent control register & honest Annex IV documentation

Beyond the per-run pass/fail gate, Opencomplai maintains a **persistent
control register** (requires an evidence vault): one control per EU AI Act
article, tracked across runs with an owner, an evidence-freshness TTL, and a
state (`satisfied` / `evidence_missing` / `evidence_stale` / `pending_review`
/ `waived`). `opencomplai controls status` gives you a CI-consumable summary
of exactly what's missing or gone stale.

The Annex IV dossier generated by `opencomplai docs generate` never claims
more than the code actually does: every field is either automated from your
manifest and risk classification, wired evidence loaded from a real scan/eval
report, or an explicit provider-attestation placeholder when nobody has
supplied it yet. Opencomplai assembles s
```
