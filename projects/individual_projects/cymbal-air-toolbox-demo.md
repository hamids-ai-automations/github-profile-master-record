# cymbal-air-toolbox-demo

**Overview:** Demo of a customer service agent (Cymbal Air) using LangGraph, Tools, and RAG to interact with Google Cloud Databases via MCP Toolbox.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/cymbal-air-toolbox-demo](https://github.com/hamids-ai-automations/cymbal-air-toolbox-demo) |
| Live website | https://github.com/googleapis/genai-toolbox/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-21 |
| Last update | 2026-11-21 |
| Last push | 2026-11-21 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 18 |
| Size | 60597 KB |
| Topics | - |

## Objectives

# ![](https://raw.githubusercontent.com/hamids-ai-automations/cymbal-air-toolbox-demo/main/static/logo-header.png)

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, agent, data, docs, models, static, templates
- **Total files (tracked in default branch):** 52
- **CI workflows:** .github/workflows/labels.yaml, .github/workflows/lint.yml, .github/workflows/lint_fallback.yml, .github/workflows/release-please.yml
- **Test files detected:** 2

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 62431 |
| JavaScript | 13964 |
| CSS | 8971 |
| HTML | 5112 |
| Dockerfile | 1041 |

**Frameworks / libraries detected:** Express, FastAPI, LangChain, pandas

**Dependencies:** fastapi, google-auth, google-cloud-aiplatform, itsdangerous, jinja2, langchain, langchain-core, langchain-google-vertexai, langgraph, markdown, pandas, pandas-stubs, pydantic, python-multipart, pytz, toolbox-langchain, types-Markdown, types-pytz, uvicorn

## Important source files

- `app.py`
- `pyproject.toml`
- `requirements.txt`
- `static/index.js`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://github.com/googleapis/genai-toolbox/

## Documentation links

- https://github.com/googleapis/genai-toolbox
- https://forms.gle/dJUdMEbUu7k3TmT4A
- https://forms.gle/3AknwhhWv2pWw46Q8
- https://www.promptingguide.ai/techniques/rag
- https://www.promptingguide.ai/agents/introduction
- https://mcp-toolbox.dev/documentation/introduction
- https://mcp-toolbox.dev/documentation/introduction/#install-toolbox
- https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox
- https://mcp-toolbox.dev/documentation/introduction/#run-toolbox
- https://mcp-toolbox.dev/documentation/deploy-to/cloud-run
- https://mcp-toolbox.dev/documentation/getting-started
- https://mcp-toolbox.dev/documentation/configuration

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

Full README: https://github.com/hamids-ai-automations/cymbal-air-toolbox-demo/blob/main/README.md

```markdown
# ![](https://raw.githubusercontent.com/hamids-ai-automations/cymbal-air-toolbox-demo/main/static/logo-header.png)

> [!NOTE]
> This project is for demonstration only and is not an officially supported
> Google product.
>
> If you're a Googler using this demo, please fill up this
> [form](https://forms.gle/dJUdMEbUu7k3TmT4A). If you're interested in using our
> hosted version, please fill up this
> [form](https://forms.gle/3AknwhhWv2pWw46Q8).

## Introduction

This project provides a production-quality reference implementation for building
Agentic applications that use [Agents] and [Retrieval Augmented Generation
(RAG)][rag] to query and interact with data stored in Google Cloud Databases.

This demonstration features Cymbal Air, a fictional airline. The application
showcases a customer service assistant that helps travelers manage flights and
find information about San Francisco International Airport (SFO), Cymbal Air's
hub. The agent can answer questions like:

* *Are there any luxury shops in the terminal?*
* *Where can I get coffee near gate A6?*
* *I need to find a gift for my colleague.*
* *What flights are headed to NYC tomorrow?*

[rag]: https://www.promptingguide.ai/techniques/rag
[Agents]: https://www.promptingguide.ai/agents/introduction

## Table of Contents
<!-- TOC depthfrom:2 -->

- [Understanding the demo](#understanding-the-demo)
    - [Retrieval Augmented Generation RAG](#retrieval-augmented-generation-rag)
    - [Agent-based Orchestration](#agent-based-orchestration)
    - [Architecture](#architecture)
- [Deployment](#deployment)
    - [Before you begin](#before-you-begin)
    - [One-Time Database & Tool Configuration](#one-time-database--tool-configuration)
    - [Launch the Toolbox Server Choose One](#launch-the-toolbox-server-choose-one)
    - [Running the Agentic Application](#running-the-agentic-application)
    - [Clean Up](#clean-up)
- [Customizing Your Tools](#customizing-your-tools)

<!-- /TOC -->

## Understanding the demo

### Retrieval Augmented Generation (RAG)

One of the best tools for reducing hallucinations is to use Retrieval Augmented
Generation (RAG). RAG is the concept of retrieving some data or information,
augmenting your prompt to the agent, and allowing it to generate more accurate
responses based on the data included in the prompt. This grounds the model’s
response, making it less likely to hallucinate. This technique is also useful
for allowing the agent to access data it didn’t have when it was trained. And
unlike fine-tuning, the information retrieved for RAG does not alter the model
or otherwise leave the context of the request - making it more suitable for use
cases where information privacy and security are important.

Cloud databases provide a managed solution for storing and accessing data in a
scalable and a reliable way. By connecting an agent to a cloud database,
developers can give their applications access to a wider range of information
and reduce the risk of hallucinations.


### Agent-based Orchestration

This application uses an Agent-based orchestration model. Instead of a static
chain of calls, the LLM acts as an intelligent Agent that decides which tools to
use and in what order. It is given a set of available tools, each with a
specific function (e.g., `find_flights`, `list_amenities`). Based on the user's
query, the agent reasons about the best tool to use to find the answer. This
"thought process" allows the agent to handle a wider variety of queries and to
break down complex questions into smaller, manageable steps.

### Architecture

![Overview](https://raw.githubusercontent.com/hamids-ai-automations/cymbal-air-toolbox-demo/main/architecture.svg)

The architecture consists of three main components:
1. **Application** -- The user-facing agentic app that orchestrates the
   interaction between the user and the agent.
1. **MCP Toolbox** -- [MCP Toolbox](https://github.com/googleapis/genai-toolbox)
   is a middleware server that exposes the database operations as a set of
   tools. The LLM agent connects to the Toolbox to execute these tools. This
   provides a secure, scalable, and modular way to manage database interactions.
1. **Database** -- The database containing the data the agent can use to answer
   questions. For this application, the database used was intentionally designed
   to be interchangeable in order to make it easier to run this on your
   preferred database.

Using the Toolbox as an intermediary offers several advantages:

1. **Better Security** - The Toolbox handles authentication and authorization,
   preventing the agent from directly accessing the database and reducing the
   risk of security vulnerabilities.
1. **Better scalability** - Toolbox allows multiple different Agents to leverage
   it, as well as allowing it to scale independently. It allows for production
   best practices such as connection pooling or caching.
1. **Better recall** - Agents perform better when given smaller, discrete tasks
   they can use to accomplish larger goals. By mapping a specific action to a
   specific, pre-determined query, via tools, it significantly improves the
   agent's ability to leverage it successfully.

Head over to the official [MCP Toolbox
docs](https://mcp-toolbox.dev/documentation/introduction/)
for more details.

## Deployment

Deploying Cymbal Air app is a three-step process. You will first download the
necessary tools, then perform a one-time setup for your database and Toolbox
configuration, and finally launch the Toolbox server and the app.

### Before you begin

First, clone this repository and download the MCP Toolbox binary.

1.  **Clone the repository:**
      ```bash
      git clone https://github.com/GoogleCloudPlatform/cymbal-air-toolbox-demo.git
      cd cymbal-air-toolbox-demo
      ```
2.  **Download MCP Toolbox binary:**

      Follow [these
      steps](https://mcp-toolbox.dev/documentation/introduction/#install-toolbox)
      to download the binary. This involves running the following commands:
      ```bash
      # See the releases page for the latest version
      export VERSION=0.8.0
      curl -O https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox
      chmod +x toolbox
      ```

### One-Time Database & Tool Configuration

Next, you must perform a one-time setup to create your database instance,
populate it with data, and create the `tools.yaml` configuration file. This
process uses the Toolbox binary you just downloaded.

> [!IMPORTANT]
> For detailed, step-by-step instructions, follow the **[Database Setup
> Guide](https://github.com/hamids-ai-automations/cymbal-air-toolbox-demo/blob/main/docs/database_setup.md)**.

> [!NOTE]
> If you have already configured your own database, you can skip this section.

### Launch the Toolbox Server (Choose One)

After your database is initialized and your `tools.yaml` file is created, you
must run the Toolbox server so the agentic app can connect to it. You can either
run it locally for development or deploy it to Cloud Run for a more robust
setup.

#### **Option A:** Run Toolbox Locally

For local development and testing, you can run the Toolbox server directly from
your terminal. This is the quickest way to get started.

**For instructions, follow the [guide to running the Toolbox
locally](https://mcp-toolbox.dev/documentation/introduction/#run-toolbox).**

The basic command will be:
```bash
./toolbox --tools-file "tools.yaml"
```

#### **Option B:** Deploy Toolbox to Cloud Run

For a scalable and production-ready setup, you can deploy the Toolbox as a
service on Google Cloud Run. This provides a stable, shareable endpoint for your
application.

**For instructions, follow the [guide to deploying the Toolbox on Cloud
Run](https://mcp-toolbox.dev/documentation/deploy-to/cloud-run/)**.

### Running the Agentic Application

[Instructions for running app locally](https://github.com/hamids-ai-automations/cymbal-air-toolbox-demo/blob/main/docs/run_app.md)

### Clean Up

[Instruction
```
