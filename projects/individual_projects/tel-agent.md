# Tel-Agent

**Overview:** AI phone assistant | open-source 

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/Tel-Agent](https://github.com/hamids-ai-automations/Tel-Agent) |
| Live website | https://Tel-Agent.com |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-10-28 |
| Default branch | main |
| License | AGPL-3.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 11 |
| Size | 5532 KB |
| Topics | - |

## Objectives

<div align="center">

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude, .cursor, .github, agent, alembic, api, docker, docs, examples, locales, packaging, scripts, tests, web
- **Total files (tracked in default branch):** 814
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/release-drafter.yml, .github/workflows/release-images.yml, .github/workflows/release-packages.yml
- **Test files detected:** 90

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 2415145 |
| TypeScript | 1043703 |
| CSS | 16223 |
| JavaScript | 14216 |
| Shell | 10393 |
| PowerShell | 4631 |
| Inno Setup | 4096 |
| Dockerfile | 3973 |
| Batchfile | 1268 |
| Mako | 704 |

**Frameworks / libraries detected:** FastAPI, Next.js, SQLAlchemy, pytest

**Dependencies:** none detected

## Important source files

- `api/main.py`
- `docker-compose.yml`
- `pyproject.toml`
- `web/package.json`
- `web/tsconfig.json`

## Installation and setup

```bash
git clone https://github.com/Dpro-at/Tel-Agent.git
cd Tel-Agent
cp .env.example .env

## Deployment

Firebase/other hosting declared via homepage field: https://Tel-Agent.com

## Documentation links

- https://Tel-Agent.com
- https://dpro.at
- https://tel-agent.com/download
- http://localhost:38471**
- http://localhost:38472/docs
- https://www.star-history.com/?repos=dpro-at%2Ftel-agent&type=date&legend=top-left
- https://api.star-history.com/chart?repos=dpro-at/tel-agent&type=date&theme=dark&legend=top-left
- https://api.star-history.com/chart?repos=dpro-at/tel-agent&type=date&legend=top-left

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

Full README: https://github.com/hamids-ai-automations/Tel-Agent/blob/main/README.md

```markdown
<div align="center">

<img src="logo.png" alt="Tel-Agent" height="130">

# AI phone assistant

**Connect any phone line to any AI model. Self-hosted, bring your own keys.**

<!-- Two rows of marks. The first is the channels that ship today (call and
     landline are two drawings of the one phone channel); the second is the wave-2
     channels being added now, tracked in the issues labelled "channel". The rows are
     about recognition, not arithmetic. -->
<p>
  <img src="docs/brand/channels/call.svg" alt="Call" title="Call" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/landline.svg" alt="Landline" title="Landline" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/web-chat.svg" alt="Web chat" title="Web chat" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/sms.svg" alt="SMS" title="SMS" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/email.svg" alt="Email" title="Email" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/whatsapp.svg" alt="WhatsApp" title="WhatsApp" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/telegram.svg" alt="Telegram" title="Telegram" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/messenger.svg" alt="Messenger" title="Messenger" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/instagram.svg" alt="Instagram" title="Instagram" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/discord.svg" alt="Discord" title="Discord" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/slack.png" alt="Slack" title="Slack" height="26">
</p>
<p>
  <img src="docs/brand/channels/teams.svg" alt="Microsoft Teams" title="Microsoft Teams" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/signal.svg" alt="Signal" title="Signal" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/viber.svg" alt="Viber" title="Viber" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/google-chat.svg" alt="Google Chat" title="Google Chat" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/mattermost.svg" alt="Mattermost" title="Mattermost" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/matrix.svg" alt="Matrix" title="Matrix" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/irc.svg" alt="IRC" title="IRC" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/line.svg" alt="LINE" title="LINE" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/wechat.svg" alt="WeChat" title="WeChat" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/wecom.svg" alt="WeCom" title="WeCom" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/qq.svg" alt="QQ" title="QQ" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/dingtalk.svg" alt="DingTalk" title="DingTalk" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/feishu.svg" alt="Feishu / Lark" title="Feishu / Lark" height="26">
  &nbsp;&nbsp;
  <img src="docs/brand/channels/imessage.svg" alt="iMessage" title="iMessage" height="26">
</p>

<p>Connect them over MCP — and get full control.</p>

<!-- Thirteen logos, one file per theme. Seven of them are single-colour marks, so the
     strip is built twice rather than recoloured live. See docs/brand/models/README.md. -->
<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/brand/models/models-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/brand/models/models-light.svg">
  <img src="docs/brand/models/models-light.svg" alt="Works with OpenAI, Claude, Gemini, Mistral, Ollama, Perplexity, Copilot, Manus, DeepSeek, Grok, Qwen, Groq and OpenRouter" height="28">
</picture>
</p>

<!-- Two files, one seal. The wreath is single-colour artwork on a transparent
     background, so it needs dark ink on GitHub's light theme and white ink on the
     dark one; <picture> is what lets a README ship both. -->
<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/brand/awards/product-of-the-day-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/brand/awards/product-of-the-day-light.svg">
  <img src="docs/brand/awards/product-of-the-day-light.svg" alt="Product of the day - 1st" height="74">
</picture>
</p>

<p>
  <img src="docs/brand/compliance/gdpr-dsgvo.png" alt="DSGVO & GDPR compliant" height="34">
  <img src="docs/brand/compliance/eu-ai-act.png" alt="EU AI Act compliant" height="34">
</p>

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)
[![Status: alpha](https://img.shields.io/badge/status-alpha-blue.svg)](#project-status)
[![Release](https://img.shields.io/github/v/release/Dpro-at/Tel-Agent?label=release)](https://github.com/Dpro-at/Tel-Agent/releases/latest)

[tel-agent.com](https://tel-agent.com) · maintained by [Dpro GmbH](https://dpro.at), Vienna

</div>

---

## What it is

Tel-Agent is an open-source gateway that sits between a phone line and an AI agent.

A call arrives over SIP. Tel-Agent checks the caller against your routing rules and
either passes it through to a human, blocks it, or hands it to an AI agent. The agent
speaks with the caller in real time, can invoke tools — transfer the call, take a
message, check a calendar, call any HTTP endpoint — and every call is recorded,
transcribed, and searchable.

It runs on your own hardware, on your own LAN, with your own API keys.

The same agent handles phone calls and answers
on **web chat, SMS, email, WhatsApp, Telegram, Messenger, Instagram, Discord and
Slack** — connected with your own credentials from each platform, never a shared
application of ours. The official channel scope now covers **24 channels including the phone**, with additional channels built on the extension contract. A channel is a route a
customer uses to reach you; a system you run your own business on is an integration,
and those are reached through webhooks and the HTTP tool.

## What it is not

- **Not a PBX replacement.** It connects to your existing PBX (3CX, Asterisk, FreePBX)
  as an extension.
- **Not a workflow automation platform.** Webhooks and a generic HTTP tool reach n8n
  and Home Assistant, which do that job better. A *channel* is where the conversation
  happens; an *integration* is a system the agent acts on. We own the first and reach
  the second through the HTTP tool.
- **Not a CRM.**
- **Not analog-capable.** Bridge an analog line with an ATA; Tel-Agent only speaks SIP.

## Why it exists

Well-funded closed products already do "AI receptionist for business". What does not
exist is a good **open, self-hosted** one — where you own the recordings, choose the
models, and decide which callers ever reach the AI at all.

---

## Project status

**Alpha. Native installers and container images are available today.** Choose a platform on the [download page](https://tel-agent.com/download), or get the packages from the
[releases page](https://github.com/Dpro-at/Tel-Agent/releases/latest): a Windows
installer, macOS packages for Apple Silicon and Intel, DEB and RPM packages for Linux,
and a `docker-compose.release.yml` that pulls the published images. The installers are
unsigned while code signing is not yet configured, so the operating system will ask
once before it runs.

**What works now.** A conversation is answered end to end: the reply streams token by
token, can be interrupted mid-sentence, is stored, and raises a notification so a person
knows someone wrote in. The phone implementation includes streaming speech recognition and synthesis, interruption handling, caller-ID routing, and stored call transcripts through the SIP/LiveKit transport. Twilio integration handles SMS with customer-owned credentials. The core messaging channels are wired — web chat, WhatsApp, Telegram,
Messenger, Instagram, Discord, Slack, email and SMS — and the dashboard serves them
from a real API: sign-in and the account flows, home, the conversation archive, the
notification tray, contacts, assistants, knowledge, the catalogue, apps, numbers,
routing rul
```
