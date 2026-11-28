# open-resource-broker

**Overview:** A unified API for orchestrating and provisioning compute capacity. Define what you need in a template, request it, track it and return it through a CLI, REST API, MCP server or native SDKs.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/open-resource-broker](https://github.com/hamids-ai-automations/open-resource-broker) |
| Live website | https://finos.github.io/open-resource-broker/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-30 |
| Last update | 2026-10-30 |
| Last push | 2026-11-10 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 16 |
| Size | 63316 KB |
| Topics | - |

## Objectives

[![FINOS - Incubating](https://cdn.jsdelivr.net/gh/finos/contrib-toolbox@master/images/badge-incubating.svg)](https://community.finos.org/docs/governance/Software-Projects/stages/incubating)

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .githooks, .github, assets, config, deployment, dev-tools, docs, examples, k8s-legacy, makefiles, sdk, src, tests
- **Total files (tracked in default branch):** 3105
- **CI workflows:** .github/workflows/changelog-validation.yml, .github/workflows/ci-quality.yml, .github/workflows/ci-tests.yml, .github/workflows/container-cleanup-dev.yml, .github/workflows/container-cleanup-on-release.yml, .github/workflows/dev-containers.yml, .github/workflows/dev-pypi.yml, .github/workflows/dev-sdk.yml, .github/workflows/docs.yml, .github/workflows/fuzz.yml, .github/workflows/labels.yml, .github/workflows/package-testing.yml, .github/workflows/pr-sdk-dryrun.yml, .github/workflows/prod-release.yml, .github/workflows/reusable-sdk-publish.yml, .github/workflows/reusable-security.yml, .github/workflows/reusable-test.yml, .github/workflows/scorecard.yml, .github/workflows/sdk.yml, .github/workflows/security-code.yml
- **Test files detected:** 1399

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 20413787 |
| Java | 221431 |
| Go | 192353 |
| C# | 173468 |
| Kotlin | 165084 |
| Shell | 164256 |
| TypeScript | 148320 |
| Makefile | 92335 |
| Dockerfile | 7065 |
| Batchfile | 5693 |
| Nix | 1784 |
| Go Template | 1582 |
| Mako | 1365 |
| JavaScript | 697 |

**Frameworks / libraries detected:** FastAPI, MCP, Next.js, React, SQLAlchemy, pytest, requests

**Dependencies:** none detected

## Important source files

- `deployment/docker/docker-compose.yml`
- `dev-tools/analysis/visualise/requirements.txt`
- `go.mod`
- `pyproject.toml`
- `sdk/go/go.mod`
- `sdk/java/build.gradle`
- `sdk/typescript/package.json`
- `sdk/typescript/tsconfig.json`
- `src/orb/cli/main.py`
- `src/orb/ui/app.py`
- `tests/e2e/microvm/worker/app.py`

## Installation and setup

```bash
pip install orb-py
orb init
orb templates generate
```

## Deployment

Firebase/other hosting declared via homepage field: https://finos.github.io/open-resource-broker/

## Documentation links

- https://finos.github.io/open-resource-broker
- https://cdn.jsdelivr.net/gh/finos/contrib-toolbox@master/images/badge-incubating.svg
- https://community.finos.org/docs/governance/Software-Projects/stages/incubating
- https://raw.githubusercontent.com/finos/open-resource-broker/main/docs/assets/orb-logo-horizontal-dark.svg
- https://raw.githubusercontent.com/finos/open-resource-broker/main/docs/assets/orb-logo-horizontal.svg
- https://pypi.org/project/orb-py
- https://deepwiki.com/finos/open-resource-broker
- https://scorecard.dev/viewer/?uri=github.com/finos/open-resource-broker
- https://api.securityscorecards.dev/projects/github.com/finos/open-resource-broker/badge
- https://www.bestpractices.dev/projects/13611
- https://www.bestpractices.dev/projects/13611/badge
- http://localhost:8000/api/v1/templates
- http://localhost:8000/api/v1/requests
- http://localhost:8000/api/v1/requests/req-12345
- http://localhost:8000/health

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

Full README: https://github.com/hamids-ai-automations/open-resource-broker/blob/main/README.md

```markdown
[![FINOS - Incubating](https://cdn.jsdelivr.net/gh/finos/contrib-toolbox@master/images/badge-incubating.svg)](https://community.finos.org/docs/governance/Software-Projects/stages/incubating)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/finos/open-resource-broker/main/docs/assets/orb-logo-horizontal-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/finos/open-resource-broker/main/docs/assets/orb-logo-horizontal.svg">
    <img alt="Open Resource Broker" src="https://raw.githubusercontent.com/finos/open-resource-broker/main/docs/assets/orb-logo-horizontal.svg" width="520">
  </picture>
</p>

<p align="center">
  <strong>Unified API for orchestrating and provisioning compute capacity</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/finos/open-resource-broker" alt="License"></a>
  <a href="https://pypi.org/project/orb-py/"><img src="https://img.shields.io/pypi/v/orb-py" alt="PyPI Version"></a>
  <a href="https://github.com/finos/open-resource-broker/releases"><img src="https://img.shields.io/github/v/release/finos/open-resource-broker" alt="Latest Release"></a>
  <a href="https://pypi.org/project/orb-py/"><img src="https://img.shields.io/pypi/pyversions/orb-py" alt="Python Versions"></a>
  <a href="https://deepwiki.com/finos/open-resource-broker"><img src="https://img.shields.io/badge/Ask-DeepWiki-blue" alt="Ask DeepWiki"></a>
  <br>
  <a href="https://github.com/finos/open-resource-broker/actions/workflows/ci-tests.yml"><img src="https://github.com/finos/open-resource-broker/actions/workflows/ci-tests.yml/badge.svg" alt="Unit Tests"></a>
  <a href="https://github.com/finos/open-resource-broker/actions/workflows/ci-quality.yml"><img src="https://github.com/finos/open-resource-broker/actions/workflows/ci-quality.yml/badge.svg" alt="Quality Checks"></a>
  <a href="https://github.com/finos/open-resource-broker/actions/workflows/security-code.yml"><img src="https://github.com/finos/open-resource-broker/actions/workflows/security-code.yml/badge.svg" alt="Security Scanning"></a>
  <a href="https://github.com/finos/open-resource-broker/actions/workflows/docs.yml"><img src="https://github.com/finos/open-resource-broker/actions/workflows/docs.yml/badge.svg" alt="Documentation"></a>
  <br>
  <a href="https://codecov.io/gh/finos/open-resource-broker"><img src="https://codecov.io/gh/finos/open-resource-broker/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/finos/open-resource-broker"><img src="https://api.securityscorecards.dev/projects/github.com/finos/open-resource-broker/badge" alt="OpenSSF Scorecard"></a>
  <a href="https://www.bestpractices.dev/projects/13611"><img src="https://www.bestpractices.dev/projects/13611/badge" alt="OpenSSF Best Practices"></a>
</p>

---

**Open Resource Broker (ORB)** is a unified API for orchestrating and provisioning compute capacity programmatically. Define what you need in a template, request it, track it, return it — through a CLI, REST API, MCP server, or native SDKs for Python, Go, TypeScript, Java, Kotlin, and .NET.

ORB includes provider backends for AWS, Azure, Google Cloud, and Kubernetes, plus an extensible provider system for adding new backends.

**Provider support:**
- **AWS** — EC2 RunInstances, EC2Fleet, SpotFleet, Auto Scaling Groups, Lambda MicroVMs (built in; see [AWS Provider Setup](#setup) below)
- **Azure** — VM Scale Sets, single VMs, CycleCloud cluster nodes (`pip install "orb-py[azure]"`; see [Azure Provider Guide](https://github.com/hamids-ai-automations/open-resource-broker/blob/main/docs/root/providers/azure/index.md))
- **Google Cloud** — Managed Instance Groups, single Compute Engine VMs (`pip install "orb-py[gcp]"`; see [Google Cloud Provider Guide](https://github.com/hamids-ai-automations/open-resource-broker/blob/main/docs/root/providers/gcp/index.md))
- **Kubernetes** — Pod, Deployment, StatefulSet, Job (`pip install "orb-py[k8s]"`; see [Kubernetes provider docs](https://github.com/hamids-ai-automations/open-resource-broker/blob/main/docs/root/providers/k8s/index.md))
- **OCI** - Compute instances, Flex and bare-metal shapes, preemptible capacity, and instance-principal authentication ([setup guide](https://github.com/hamids-ai-automations/open-resource-broker/blob/main/docs/root/deployment/oci-integration.md))
- **Custom** — extensible via [provider registry](https://github.com/hamids-ai-automations/open-resource-broker/blob/main/docs/root/developer_guide/architecture.md) and the [`orb.providers` entry-point group](https://github.com/hamids-ai-automations/open-resource-broker/blob/main/docs/root/providers/k8s/plugin-authoring.md)

**Scheduler support:**
- **Default** — direct usage without an external scheduler, via ORB's native request/machine API
- **IBM Spectrum Symphony (HostFactory)** — see [HostFactory Integration](#hostfactory-integration)
- **Slurm Workload Manager by SchedMD** — integrates via ResumeProgram/SuspendProgram power hooks; see [Slurm Integration Guide](https://github.com/hamids-ai-automations/open-resource-broker/blob/main/docs/root/slurm/integration_guide.md)
- **HTC-Grid** and **OpenGRIS Scaler** — these grid schedulers consume ORB through the default scheduler's native API rather than a dedicated ORB scheduler strategy; see [HTC-Grid](https://github.com/finos/htc-grid) and [OpenGRIS Scaler](https://github.com/finos/opengris-scaler)

![ORB](https://raw.githubusercontent.com/hamids-ai-automations/open-resource-broker/main/ORB.gif)

## Quick Start

```bash
pip install orb-py
orb init
orb templates generate
```

### 1. Pick a template

```bash
orb templates list
```

### 2. Request machines

```bash
orb machines request <template-id> 3
```

### 3. Check status

```bash
orb requests status <request-id>
```

### 4. Return machines when done

```bash
orb machines return <machine-id-1> <machine-id-2> ...
```

### 5. Check the return status

`machines return` prints a return-request id; check it the same way as step 3:

```bash
orb requests status <return-request-id>
```

## Setup

Get ORB installed and configured for your environment.

<details>
<summary>Installation</summary>

### Standard install (core + AWS provider)

```bash
pip install orb-py
```

`boto3`/`botocore` are core dependencies, so the base install already includes the AWS provider. `pip install "orb-py[aws]"` installs the same packages — it is an explicit, forward-compatible alias for operators who prefer to name providers by extra. Azure, Google Cloud, and Kubernetes each need their own extra below.

ORB still boots cleanly when no provider is configured in `config.json`: commands that need a provider return a clear "no providers configured" error rather than an ImportError.

### Per-provider install

```bash
pip install "orb-py[aws]"          # AWS provider — same deps as the base install, explicit opt-in
pip install "orb-py[azure]"        # Azure provider (azure-identity, azure-mgmt-compute, ...)
pip install "orb-py[gcp]"          # Google Cloud provider (google-cloud-compute)
pip install "orb-py[k8s]"   # Kubernetes provider (kubernetes SDK)
pip install "orb-py[aws,cli]"      # AWS provider + colored CLI output
pip install "orb-py[aws,api]"      # AWS provider + REST API server
pip install "orb-py[monitoring-aws]"  # AWS provider + full monitoring stack
pip install "orb-py[all]"          # All providers + all features
```

### Provider extras matrix

| Use case | Install command |
|----------|----------------|
| Core (includes AWS provider) | `pip install orb-py` |
| AWS operator (explicit extra) | `pip install "orb-py[aws]"` |
| Azure operator | `pip install "orb-py[azure]"` |
| Google Cloud operator | `pip install "orb-py[gcp]"` |
| Kubernetes operator | `pip install "orb-py[k8s]"` |
| AWS + Kubernetes | `pip install "orb-py[aws,k8s]"` |
| AWS + colored CLI | `pip install "orb-py[aws,c
```
