# ai-marketing-shared

**Overview:** Shared Python foundation for AI agents: Pydantic v2 schemas, LLM provider abstraction, tracing, cost controls and an eval harness.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/ai-marketing-shared](https://github.com/hamids-ai-automations/ai-marketing-shared) |
| Live website | https://marvis.web.app/ |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-15 |
| Last update | 2026-11-20 |
| Last push | 2026-10-16 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 1 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 31 KB |
| Topics | automation, data-schemas, digital-marketing, marketing, martech, open-source, pydantic, python, shared-library, eval-harness, llm, pydantic-v2 |

## Objectives

# AI Marketing Shared

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, agents, data, docs, evaluation, infra, src, tests, tools
- **Total files (tracked in default branch):** 37
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 9

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 47842 |
| Dockerfile | 709 |

**Frameworks / libraries detected:** Anthropic API, MCP, OpenAI API, pytest

**Dependencies:** none detected

## Important source files

- `infra/docker-compose.yml`
- `pyproject.toml`

## Installation and setup

```bash
pip install -e .
pytest                       # unit + evaluation suites, coverage gate ≥ 90%
```

Run a 10-line demo that produces evidence-backed recommendations with the **mock provider**:

```python
from ai_marketing_shared.fallback import build_default_engine

engine = build_default_engine()
facts = {"campaign": "Summer_Sale", "spend": 9000, "cpa": 115.0, "target_cpa": 50.0, "ctr": 0.008}
for rec in engine.evaluate(facts):
    print(rec.agent, "|", rec.issue, "| confidence", rec.confidence)
```

Expected output (deterministic, zero cost):

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app/

## Documentation links

- https://marvis.web.app
- https://python.org
- https://docs.pydantic.dev

## Development status

Active — last push 2026-10-16

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

- [x] **0.1.0** — schemas, tools, tracing, cost, fallback, eval harness, providers, CI, docs
- [ ] **0.2.0** — MCP reference client example, structured output helpers for agents
- [ ] **0.3.0** — provider cost optimization hints and multi-model routing

---

## README source

Full README: https://github.com/hamids-ai-automations/ai-marketing-shared/blob/main/README.md

```markdown
# AI Marketing Shared

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-92004C?style=for-the-badge&logo=pydantic)](https://docs.pydantic.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![CI](https://img.shields.io/badge/CI-Lint%20%2F%20Type%20%2F%20Test%20%2F%20Build-emerald?style=for-the-badge&logo=githubactions)](.github/workflows/ci.yml)

> **Shared foundation for the AI Marketing Engineer portfolio.** One importable Python package —
> schemas, tooling, observability, cost controls, evaluation, and provider abstraction — reused by
> every repository in the portfolio.

Built by **Muhammad Hamid** to make every downstream AI marketing repo coherent: same Pydantic
schemas, same tool permission model, same tracing, same evaluation harness, same zero-cost demo mode.

---

## Why This Exists

Every repo in the portfolio must produce **evidence-backed recommendations**, use **tools safely**,
enforce **human approval**, expose **observability**, and run with **zero API keys**. Without a shared
foundation, 17 repos would drift into 17 incompatible conventions. `ai-marketing-shared` defines those
conventions **once**:

1. **Structured outputs** — Pydantic v2 schemas with field names matching the master prompt exactly.
2. **Safe tools** — a `Tool` base class with explicit permission levels (`read` / `write` / `external`)
   and a registry that rejects calls below the required permission.
3. **Provider-agnostic** — OpenAI, Anthropic, local HTTP endpoints, and a deterministic mock provider
   (default) so every demo runs at `$0.00`.
4. **Observability** — every run is traced with inputs, tool calls, outputs, cost, latency.
5. **Cost controls** — model pricing tables, ledgers, and budget caps.
6. **Evaluation** — a harness with dataset loaders and metric reporters, wired into CI.

---

## Repository Layout

```
ai-marketing-shared/
├── src/ai_marketing_shared/   # The importable package
│   ├── schemas.py             # Pydantic v2 schemas (Recommendation, Evidence, ...)
│   ├── tools.py               # Tool base class, permissions, ToolRegistry, MCP adapter
│   ├── tracing.py             # Tracer, spans, logging utilities
│   ├── cost.py                # Model pricing, cost accounting, cost caps
│   ├── fallback.py            # Rule-based fallback engine (demo mode)
│   ├── eval.py                # Eval harness: dataset loaders + metric reporters
│   └── providers.py           # OpenAI / Anthropic / local / mock provider abstraction
├── agents/                    # Conventions for agents built on top of this package
├── tools/                     # Conventions for tools built on top of this package
├── data/sample_data/          # Sample facts + example run fixtures
├── evaluation/                # Labeled datasets + pytest evaluation suite
├── tests/                     # Unit tests (>90% coverage on core modules)
├── infra/                     # Dockerfile + docker-compose
├── docs/                      # api.md, architecture.md, evaluation.md, cost-controls.md
└── .github/workflows/ci.yml   # lint → type-check → test → build
```

---

## Quick Start (Zero API Keys)

```bash
pip install -e .
pytest                       # unit + evaluation suites, coverage gate ≥ 90%
```

Run a 10-line demo that produces evidence-backed recommendations with the **mock provider**:

```python
from ai_marketing_shared.fallback import build_default_engine

engine = build_default_engine()
facts = {"campaign": "Summer_Sale", "spend": 9000, "cpa": 115.0, "target_cpa": 50.0, "ctr": 0.008}
for rec in engine.evaluate(facts):
    print(rec.agent, "|", rec.issue, "| confidence", rec.confidence)
```

Expected output (deterministic, zero cost):

```
spend-waste-rule | High CPA (115.0) vs target (50.0): pause or reallocate spend on Summer_Sale | confidence 0.9
ctr-rule | CTR (0.008) is well below 0.01 benchmark: refresh ad creative and A/B test headlines | confidence 0.75
```

---

## Install

```bash
# from a downstream repo (git install)
pip install "ai-marketing-shared @ git+https://github.com/hamid-digitalmarketer/ai-marketing-shared.git"

# locally for development
pip install -e ".[dev]"
```

Optional extras: `.[openai]`, `.[anthropic]` for real provider SDKs.

---

## Using the Mock Provider (Default)

`ProviderFactory.get_provider()` returns `MockProvider` unless `AI_MARKETING_PROVIDER` is set:

```python
from ai_marketing_shared.providers import ProviderFactory

provider = ProviderFactory.get_provider()          # mock, no keys needed
resp = provider.complete("Tell me about the brand")
print(resp.text, resp.api_cost, resp.latency_ms)   # cost is 0.0
```

Never hardcode keys. Real providers read `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` from the environment
and raise `MissingApiKeyError` when absent — so CI and demos stay green without secrets.

---

## Evaluation Summary

The repo ships a labeled evaluation dataset (`evaluation/datasets/recommendation_eval.jsonl`) and a
pytest suite that runs the rule-based engine against it, reporting **accuracy / precision / recall /
F1 / tool-use success / latency / cost**. Current results are tracked in
[docs/evaluation.md](https://github.com/hamids-ai-automations/ai-marketing-shared/blob/main/docs/evaluation.md) and reproduced in CI.

---

## Roadmap

- [x] **0.1.0** — schemas, tools, tracing, cost, fallback, eval harness, providers, CI, docs
- [ ] **0.2.0** — MCP reference client example, structured output helpers for agents
- [ ] **0.3.0** — provider cost optimization hints and multi-model routing

---

## Contributing

See [CONTRIBUTING.md](https://github.com/hamids-ai-automations/ai-marketing-shared/blob/main/CONTRIBUTING.md).

## License

MIT — see [LICENSE](https://github.com/hamids-ai-automations/ai-marketing-shared/blob/main/LICENSE).

```
