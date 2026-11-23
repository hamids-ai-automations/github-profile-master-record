# algen-agent-runtime

**Overview:** Provider-neutral Python runtime for governed AI agents: approvals, policies, budgets, tenant isolation, audit and OpenTelemetry in the execution path. Works alongside LangGraph and the OpenAI Agents SDK.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/algen-agent-runtime](https://github.com/hamids-ai-automations/algen-agent-runtime) |
| Live website | https://algenai.github.io/algen-agent-runtime/ |
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
| Contributors | 3 |
| Size | 3217 KB |
| Topics | - |

## Objectives

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/brand/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/brand/banner-light.svg">
  <img alt="Algen Agent Runtime — Build governed agents. Own the runtime." src="https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/brand/banner-light.svg">
</picture>

## Features

| Capability | Included |
| --- | --- |
| Execution | Checkpointed state machine, retries, cancellation, timeouts, resumability |
| Models | Capability-aware routing and ordered or balanced fallback across OpenAI, Azure OpenAI, Anthropic, Gemini, xAI, Groq, Mistral, DeepSeek, Hugging Face Inference, Ollama, any OpenAI-compatible endpoint and local transformers; prompt caching; recoverable malformed tool calls |
| File attachments | Images and PDFs passed by reference to scanned artifacts, read natively by models that support them, on runs, conversations and workflows ([guide](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/attachments.md)) |
| Tools | Typed schemas, permissions, idempotency, approvals enforced at execution, call guards, caller credentials, execution ledger with reconciliation of unknown outcomes |
| MCP | Managed client for stdio, streamable HTTP and SSE servers with per-tenant or per-user OAuth, DNS-pinned egress, secret references, and governance mapping |
| Context management | [Working state](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/context-management.md), [progressive skills](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/skills.md), [learned memory](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/learned-memory.md), [compaction/offloading](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/artifacts.md), and [evaluations/diagnostics](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/context-evaluation.md) |
| Retrieval | Keyword, vector, and hybrid retrieval with citation verification |
| Governance | Policies at every boundary with explicit fail modes, signed policy bundles, budgets, PII and secret redaction, prompt-injection screening, human-in-the-loop decisions and an approval inbox |
| Security and operations | OIDC or JWT authentication with scopes and token revocation, egress proxy and mTLS, sandboxed subprocesses, signed plugins, per-run limits, per-tenant storage quotas and retention, readiness and graceful drain |
| Conversations | Durable messages, feedback, follow-ups, SSE, rich response blocks |
| Analytics | Typed analytical DAGs, application-registered nodes, secret-safe query sources, semantic layers, governance and evaluation gates |
| Multi-agent workflows | Validated manifests, dependency scheduling, dynamic fan-out, bounded repair, exact-version child composition, durable clarification and approval pause/resume, explicit crash recovery, typed resources, correlation, and lifecycle events |
| Observability | Structured logs, OpenTelemetry, optional Traccia integration |
| Frameworks | Optional LangGraph, OpenAI Agents, AutoGen, and CrewAI adapters |

## Technical architecture

- **Top-level directories:** .agents, .github, docs, examples, scripts, src, tests
- **Total files (tracked in default branch):** 658
- **CI workflows:** .github/workflows/auto-release.yml, .github/workflows/dco.yml, .github/workflows/docs.yml, .github/workflows/quality.yml, .github/workflows/release.yml, .github/workflows/security.yml
- **Test files detected:** 176

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 3609494 |
| PLpgSQL | 11027 |
| Shell | 3170 |
| Dockerfile | 586 |
| Makefile | 165 |

**Frameworks / libraries detected:** FastAPI, MCP, NumPy, OpenAI API, pytest

**Dependencies:** none detected

## Important source files

- `docker-compose.yml`
- `examples/case_study_responsible_hiring/app.py`
- `examples/case_study_teaching_assistant/app.py`
- `examples/pattern_approval_workflow/app.py`
- `examples/pattern_child_workflow/app.py`
- `examples/pattern_evaluation_gate/app.py`
- `examples/pattern_governed_research/app.py`
- `examples/pattern_guarded_tools/app.py`
- `examples/pattern_langgraph_governance/app.py`
- `examples/pattern_mcp_governance/app.py`
- `examples/pattern_multi_agent_fanout/app.py`
- `examples/pattern_openai_agents_integration/app.py`
- `examples/pattern_provider_fallback/app.py`
- `examples/pattern_secured_api/app.py`
- `examples/pattern_side_effect_reconciliation/app.py`
- `examples/pattern_text_to_sql/advanced/app.py`
- `examples/pattern_text_to_sql/app.py`
- `examples/pattern_text_to_sql/schema.sql`
- `examples/quickstart_agent_tool/app.py`
- `examples/quickstart_approval/app.py`
- `examples/quickstart_cloud_chat/app.py`
- `examples/quickstart_conversation/app.py`
- `examples/quickstart_local_chat/app.py`
- `examples/quickstart_rag/app.py`
- `examples/quickstart_tool/app.py`
- `examples/reference_customer_support/app.py`
- `examples/reference_incident_response/app.py`
- `examples/reference_invoice_exceptions/app.py`
- `pyproject.toml`
- `src/algen_agent_runtime/api/app.py`

## Installation and setup

Install the latest package from PyPI:

```bash
python -m pip install algen-agent-runtime

## Deployment

Firebase/other hosting declared via homepage field: https://algenai.github.io/algen-agent-runtime/

## Documentation links

- https://www.python.org/downloads
- https://algenai.github.io/algen-agent-runtime
- https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/brand/banner-dark.svg
- https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/brand/banner-light.svg
- https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/demo/approval.gif
- http://127.0.0.1:8000/v1/runs
- http://127.0.0.1:8000/agent-ui`

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine
- hamids-ai-automations/gemini-agent-reliability-kit
- hamids-ai-automations/envscope

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/README.md

```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/brand/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/brand/banner-light.svg">
  <img alt="Algen Agent Runtime — Build governed agents. Own the runtime." src="https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/brand/banner-light.svg">
</picture>

# Algen Agent Runtime

[![Quality](https://github.com/AlgenAI/algen-agent-runtime/actions/workflows/quality.yml/badge.svg)](https://github.com/AlgenAI/algen-agent-runtime/actions/workflows/quality.yml)
[![Security](https://github.com/AlgenAI/algen-agent-runtime/actions/workflows/security.yml/badge.svg)](https://github.com/AlgenAI/algen-agent-runtime/actions/workflows/security.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Algen Agent Runtime is a typed, provider-neutral Python runtime for building governed AI agents. It provides deterministic execution state, model routing, tool controls, human approvals, retrieval, verification, durable stores, streaming events, and OpenTelemetry instrumentation without binding applications to one model vendor or agent framework.

> [!IMPORTANT]
> `0.1.0a21` is a pre-release, single-node foundation. The repository is suitable for evaluation and contribution, but it is not yet presented as a production distributed control plane. Review the [known production gaps](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/production-readiness.md), [threat model](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/threat-model.md), and [security policy](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/SECURITY.md) before deployment.

**[Documentation](https://algenai.github.io/algen-agent-runtime/)** · [Why use it](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/why-algen-agent-runtime.md) · [Examples](#importable-examples) · [Changelog](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/CHANGELOG.md)

## See it in one minute

No API key and no network: the built-in mock provider stands in for the model.

```bash
python -m pip install --pre algen-agent-runtime
python -m examples.quickstart_approval.app
```

The workflow proposes a change, then pauses at an approval node and asks `Approve or reject?`.
Approve it and the change is applied once, under an idempotency key; reject it and nothing is
written. The final state records the decision, who made it, and the key:

<img alt="Terminal recording: the approval quickstart pauses, the user types approve, and the run prints the approval decision and the applied result with its idempotency key" src="https://raw.githubusercontent.com/AlgenAI/algen-agent-runtime/refs/heads/main/docs/assets/demo/approval.gif" width="720">

The approval is part of the Runtime's execution path, not an instruction in the prompt, so the model
cannot skip it. Pass `--approve-all` or `--reject-all` to run it without a prompt.

## Why Algen Agent Runtime?

- **Provider-neutral execution:** route across local and hosted model providers through typed contracts.
- **Governance in the execution path:** enforce policies, approvals, budgets, verification, and tenant boundaries around every run.
- **Durable and observable:** persist agent and multi-agent workflow checkpoints, events, conversations, approvals, artifacts, and tool-execution records with optional PostgreSQL and Redis adapters.
- **Governed artifact inputs:** stage tenant-scoped files with checksums, scan/quarantine state,
  expiry, metadata-only listing, and bounded retention before attaching them to a run. Agents that
  opt in read attached images and PDFs natively, passed by reference and never stored inline.
- **Application-friendly:** use the same runtime as an embedded Python library or through its FastAPI REST/SSE service.
- **Runtime-owned multi-agent DAGs:** declare JSON-Schema inputs/outputs, agent, dynamic map-agent, deterministic-handler,
  predicate, and join nodes with conditions, bounded loops and repairs, clarification limits, and
  lifecycle events; compose exact-version child workflows without duplicating their topology.
- **Ready-made connectors:** email (SMTP, Gmail, Outlook), messaging, databases, documents, GitHub
  and more ship as governed toolkits in
  [algen-agent-tools](https://github.com/AlgenAI/algen-agent-tools), which builds on this runtime.
- **Typed System One decisions:** use the optional TypeSafe Jev client for fast Choice, Score, and
  Noul routing gates while keeping generative work in model providers and deterministic work in code.
- **Extensible by design:** add model providers, tools, planners, context builders, verifiers, stores, and external-framework adapters without changing the state machine.
- **Offline-testable:** the deterministic mock provider supports tests without credentials, network access, or paid model calls.

## The Algen agent lifecycle

Runtime is the open-source execution foundation in a three-product lifecycle:

| Product | Role | Boundary |
| --- | --- | --- |
| **Algen Agent Runtime** | Build and execute portable, governed agents and multi-agent DAGs | Open-source Python library and service; owns execution contracts and semantics |
| **Algen Agent Studio** | Low-code build, test, evaluate, publish, and deploy workbench | Private product; consumes Runtime without redefining its workflow dialect |
| **Algen Agent Marketplace** | Discover, distribute, license, and import versioned agents | Public/private and free/paid catalog; packages agents but does not execute them |

An agent can be built directly with Runtime or visually in Studio. Studio validates and evaluates the
same Runtime project, publishes a versioned package to Marketplace, and deploys it with
environment-specific credentials. Marketplace consumers import that package into Studio before
configuration and deployment. Secrets and live environment values never belong in a marketplace
artifact.

Typed workflows can reference staged file IDs rather than embedding bytes. See the
[artifact lifecycle](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/artifacts.md) for upload, checksum, quarantine, retention, and storage
boundaries.

Workflows can also call exact, trusted child workflow versions through a `WorkflowRegistry`; Runtime
preserves correlation, lineage, checkpoints, pause/approval propagation, and recovery. See
[multi-agent workflows](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/multi-agent-workflows.md) and the importable
`examples/pattern_child_workflow`. For governed outbound messages, see [email](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/email.md).

## Status and support

| Area | Status |
| --- | --- |
| Python | 3.12 and 3.13 |
| Package maturity | Pre-alpha (`0.1.0a21`) |
| Core execution | Available and covered by deterministic tests |
| HTTP API | Available; secure deployment configuration is operator-owned |
| Persistence | In-memory, PostgreSQL, and Redis adapters |
| Artifact storage | Memory, PostgreSQL, and encrypted S3-compatible object storage |
| Distributed execution | Experimental; see the production-readiness roadmap |
| Public API compatibility | Experimental during `0.x`; see the [API stability policy](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/docs/api-stability.md) |
| Community support | Best effort; see [SUPPORT.md](https://github.com/hamids-ai-automations/algen-agent-runtime/blob/main/SUPPORT.md) |

## Install

Install the latest package from PyPI:

```bash
python -m
```
