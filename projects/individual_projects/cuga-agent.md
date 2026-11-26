# cuga-agent

**Overview:** CUGA is an open-source generalist agent harness for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/cuga-agent](https://github.com/hamids-ai-automations/cuga-agent) |
| Live website | https://cuga.dev |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-10-28 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 34 |
| Size | 157580 KB |
| Topics | - |

## Objectives

<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/images/readme/hero-mobile.svg">
    <img src="docs/images/readme/hero.svg" alt="CUGA — Enterprise automation. Under your control. Sovereign deployment, execution policies, and efficient inference." width="100%">
  </picture>
</p>

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .bob, .claude, .cra, .cursor, .github, .run, .vscode, deployment, docs, events, scripts, src, tests
- **Total files (tracked in default branch):** 2044
- **CI workflows:** .github/workflows/dco.yml, .github/workflows/deploy-image-ghcr.yml, .github/workflows/deploy-image.yml, .github/workflows/external-fork-tests.yml, .github/workflows/fix-issues-with-bob.yml, .github/workflows/fix-pr-reviews-with-bob.yml, .github/workflows/licenses.yml, .github/workflows/release-pr.yml, .github/workflows/release.yml, .github/workflows/run-pr-eval.yml, .github/workflows/smoke-pip-install.yml, .github/workflows/stability-tests.yml, .github/workflows/tests.yml
- **Test files detected:** 611

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 10445122 |
| TypeScript | 1707154 |
| CSS | 207008 |
| Shell | 203063 |
| Jinja | 143662 |
| HTML | 69585 |
| JavaScript | 43750 |
| Makefile | 23582 |
| SCSS | 22929 |
| Slim | 8343 |
| Go Template | 2078 |
| Dockerfile | 1556 |

**Frameworks / libraries detected:** Anthropic API, BeautifulSoup, Django, FastAPI, Flask, LangChain, MCP, OpenAI API, Playwright, pandas, pytest, requests

**Dependencies:** none detected

## Important source files

- `deployment/docker-compose/openlit/docker-compose.yml`
- `docs/examples/agent_with_public_mcp/main.py`
- `docs/examples/cuga_as_mcp/main.py`
- `docs/examples/cuga_as_mcp/pyproject.toml`
- `docs/examples/cuga_with_runtime_tools/main.py`
- `docs/examples/cuga_with_runtime_tools/pyproject.toml`
- `docs/examples/demo_apps/setup/pyproject.toml`
- `docs/examples/digital_sales_openapi/main.py`
- `docs/examples/hello_tools/main.py`
- `docs/examples/knowledge_demo/main.py`
- `docs/examples/knowledge_demo/pyproject.toml`
- `docs/examples/travel_agent/main.py`
- `pyproject.toml`
- `src/cuga/backend/events/app.py`
- `src/cuga/backend/server/main.py`
- `src/cuga/cli/main.py`
- `src/cuga/demo_tools/crm/crm_api/main.py`
- `src/frontend_workspaces/agentic_chat/package.json`
- `src/frontend_workspaces/agentic_chat/tsconfig.json`
- `src/frontend_workspaces/extension/package.json`
- `src/frontend_workspaces/extension/tsconfig.json`
- `src/frontend_workspaces/frontend/package.json`
- `src/frontend_workspaces/frontend/tsconfig.json`
- `src/frontend_workspaces/package.json`
- `src/frontend_workspaces/runtime/package.json`
- `src/frontend_workspaces/runtime/tsconfig.json`
- `src/frontend_workspaces/shared/package.json`
- `src/frontend_workspaces/shared/tsconfig.json`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://cuga.dev

## Documentation links

- https://docs.astral.sh/uv/getting-started/installation
- https://cuga.dev
- https://docs.cuga.dev
- https://discord.gg/PN3Zdq4dEd
- https://docs.cuga.dev/docs/build/cuga-supervisor
- https://docs.astral.sh/uv/guides/projects/#running-commands
- http://your-inference-service:8000/v1
- https://docs.cuga.dev/docs/build/policies
- https://arxiv.org/html/2510.23856v1
- https://docs.cuga.dev/docs/build/cuga-agent

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

Full README: https://github.com/hamids-ai-automations/cuga-agent/blob/main/README.md

```markdown
<p align="center">
  <picture>
    <source media="(max-width: 640px)" srcset="docs/images/readme/hero-mobile.svg">
    <img src="docs/images/readme/hero.svg" alt="CUGA — Enterprise automation. Under your control. Sovereign deployment, execution policies, and efficient inference." width="100%">
  </picture>
</p>

# CUGA

**The enterprise agent harness for sovereign, policy-controlled automation.**

CUGA turns business requests into actions across your applications, APIs, and documents. Deploy in your private cloud or prepare an air-gapped environment, enforce fine-grained execution policies, and use open models on infrastructure you control. Connect your tools, configure your workflows, and optimize inference for your workload.

**[Get started](#quick-install)** · **[Documentation](https://docs.cuga.dev)** · **[Python SDK](#build-with-the-python-sdk)** · **[Deploy on Kubernetes](https://github.com/hamids-ai-automations/cuga-agent/blob/main/deployment/README.md)**

**[CUGA Apps](https://github.com/cuga-project/cuga-apps)** · **[CUGA Harness Kit](https://github.com/cuga-project/cuga-harness-kit)** · **[Discord](https://discord.gg/PN3Zdq4dEd)**

[Apache 2.0](https://github.com/hamids-ai-automations/cuga-agent/blob/main/LICENSE) · Configurable Generalist Agent · Built with IBM SiL

---

## Quick install

Use **Python 3.12** and [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
git clone https://github.com/cuga-project/cuga-agent.git
cd cuga-agent
uv sync --python 3.12
test -f .env || cp .env.example .env
```

<a id="llm-configuration---advanced-options"></a>

Set your provider, model, and credentials in `.env`. See [model configuration](https://github.com/hamids-ai-automations/cuga-agent/blob/main/docs/readme/configuration-guide.md#supported-platforms) for supported providers.

```bash
uv run cuga start manager --crm
```

Open `/manage` at the local URL printed by the CLI. Try the CRM tools, configure policies, and test a draft before publishing. [More source and demo options](#develop-from-source).

## Automate enterprise work. Keep control.

| Your priority | What CUGA gives you |
| --- | --- |
| **Sovereignty** | Run the harness in your environment. Connect privately hosted models and tools. Preload supporting model artifacts for disconnected deployments. |
| **Execution policies** | Block disallowed intents, require approval for selected tools, guide workflows with playbooks, and configure tool-level guards. |
| **Inference efficiency** | Choose open models, tune reasoning modes, shortlist relevant tools, set tool-call budgets, and inspect token usage with per-run receipts. |
| **Faster delivery** | Connect MCP servers, OpenAPI services, and Python tools. Configure and test an agent in the UI before publishing a version. |
| **Recurring automation** | Use the separate events service to run agents on schedules, webhooks, and application events, with run history in Events Studio. |
| **Reusable experience** | Load task-specific skills and use a configured Evolve integration to retrieve relevant guidance and user preferences. |

## See what you can build

Configure tools and policies beside a draft chat, then publish a version for users.

![Current CUGA manager UI showing connected CRM and Workspace tools, three policies, draft chat, and Publish](https://raw.githubusercontent.com/hamids-ai-automations/cuga-agent/main/docs/images/readme/manager.jpg)

*Current UI, captured from this repository with illustrative Revenue Operations configuration data. Internal endpoints and version labels are examples.*

| Set approval policies | Manage specialized agents |
| --- | --- |
| ![Tool Approval configuration requiring human approval for CRM account updates](https://raw.githubusercontent.com/hamids-ai-automations/cuga-agent/main/docs/images/readme/policies.jpg) | ![Agent dashboard with Revenue Operations, Knowledge Assistant, and Operations Supervisor examples](https://raw.githubusercontent.com/hamids-ai-automations/cuga-agent/main/docs/images/readme/agents.jpg) |
| Choose which tools need approval and show the proposed code before execution. | Configure individual agents and supervisors for different business workflows. |

### Watch the product tour

https://github.com/user-attachments/assets/cb21fd61-b04b-4188-8f3e-e33197df1b9e

*Visual tour of the current UI with sample configuration, flows, run history, and memory records. It does not show a live agent run. [Media details](https://github.com/hamids-ai-automations/cuga-agent/blob/main/docs/readme/media.md).*

## From a business request to a completed workflow

| Workflow | What an agent can do with the right tools and policies |
| --- | --- |
| **Revenue operations** | Match a contact list against CRM, join account data, calculate revenue percentiles, and draft a report. Gate account updates with Tool Approval. |
| **Knowledge assistance** | Search company documents, answer with citations, and combine shared reference material with documents uploaded to a conversation. |
| **Cross-application operations** | Use CugaSupervisor to coordinate specialized agents, each with its own tools and instructions, and prepare results for review. |
| **Browser and API automation** | Combine structured API calls with browser interactions for workflows spanning services and web interfaces. |
| **Recurring operations** | Schedule a weekday report or react to a new document through the events service, then deliver the result to a configured channel. |

Start with the [CRM demo](#develop-from-source), the [knowledge walkthrough](https://github.com/hamids-ai-automations/cuga-agent/blob/main/docs/examples/knowledge_demo/README.md), or the [multi-agent examples](https://github.com/hamids-ai-automations/cuga-agent/blob/main/docs/readme/configuration-guide.md#cugasupervisor-multi-agent).

### Build agents around your team's expertise

| Capability | What it enables |
| --- | --- |
| **Multi-agent coordination** | Give specialists focused tools and instructions, then route work through [CugaSupervisor](https://docs.cuga.dev/docs/build/cuga-supervisor/). |
| **Knowledge with citations** | Combine shared company documents with conversation uploads and inspect cited sources. [Knowledge walkthrough](https://github.com/hamids-ai-automations/cuga-agent/blob/main/docs/examples/knowledge_demo/README.md). |
| **Reusable agent skills** | Package procedures in `SKILL.md` files and load the relevant instructions when a task needs them. [Skills guide](https://github.com/hamids-ai-automations/cuga-agent/blob/main/docs/readme/configuration-guide.md#agent-skills). |
| **Execution visibility** | Inspect trajectories with `cuga viz` and enable per-run receipts for token usage, model calls, tool calls, and elapsed time. [Run receipts](https://github.com/hamids-ai-automations/cuga-agent/blob/main/docs/readme/configuration-guide.md#run-receipt). |
| **Access control** | Configure OIDC sign-in and enable separate chat and management role checks. [Authentication setup](https://github.com/hamids-ai-automations/cuga-agent/blob/main/docs/readme/configuration-guide.md#authentication-and-access-control). |

## Develop from source

<details>
<summary>Clone the repository and run with uv</summary>

Use **Python 3.12** and [uv](https://docs.astral.sh/uv/getting-started/installation/). [uv manages the project environment automatically](https://docs.astral.sh/uv/guides/projects/#running-commands), so you can run commands with `uv run` without creating or activating an environment manually.

```bash
git clone https://github.com/cuga-project/cuga-agent.git
cd cuga-agent
uv sync --python 3.12
test -f .env || cp .env.example .env
```

Edit `.env` to choose a model provider and set its credentials. For an OpenAI endpoint:

```dotenv
AGENT_SETTING_CONFIG=settings.openai.toml
OPENAI_API_KEY=your-api-key
MODEL_NAME=your-model-name
```

```bash
uv run cuga start demo_crm --read-only
```

Open the local URL printed by the CLI. Try:

> from contacts.txt sho
```
