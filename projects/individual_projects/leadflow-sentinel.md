# leadflow-sentinel

**Overview:** Read-only GoHighLevel CRM observability engine: deterministic findings, explainable health score, optional AI narrative layer.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/leadflow-sentinel](https://github.com/hamids-ai-automations/leadflow-sentinel) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-11-22 |
| Last update | 2026-11-22 |
| Last push | 2026-11-22 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 1 |
| Contributors | 1 |
| Size | 235 KB |
| Topics | - |

## Objectives

---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_0701437fe6b411f184bd52540072b1e8
    ReservedCode1: EBgapKOuBjbmcqWTzR+4lZJbszzBQmtMRmP0eeGlEwXREZsm1UoxCzjud//xifQ3s9U43SDglGci71hmPpTrcjOTC6zvSuI350Q1XhwyA+vSXFyYz4j5etBtBy5n7LHi3A/bTPe9HHvFgAAVaaY35YcxVxMqP7mavIVjnDZJ1wWX5FA8kjE8xf2ZjYk=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_0701437fe6b411f184bd52540072b1e8
    ReservedCode2: EBgapKOuBjbmcqWTzR+4lZJbszzBQmtMRmP0eeGlEwXREZsm1UoxCzjud//xifQ3s9U43SDglGci71hmPpTr

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, docs, src, tests
- **Total files (tracked in default branch):** 63
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 12

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 212234 |

**Frameworks / libraries detected:** FastAPI, pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

```bash
git clone https://github.com/hamids-ai-automations/leadflow-sentinel
cd leadflow-sentinel

## Deployment

No deployment configuration detected.

## Documentation links

- https://marvis.web.app/projects/leadflow-sentinel

## Development status

Active — last push 2026-11-22

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 1

## Related projects

- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/ghl-automation-engine

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/leadflow-sentinel/blob/main/README.md

```markdown
---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_0701437fe6b411f184bd52540072b1e8
    ReservedCode1: EBgapKOuBjbmcqWTzR+4lZJbszzBQmtMRmP0eeGlEwXREZsm1UoxCzjud//xifQ3s9U43SDglGci71hmPpTrcjOTC6zvSuI350Q1XhwyA+vSXFyYz4j5etBtBy5n7LHi3A/bTPe9HHvFgAAVaaY35YcxVxMqP7mavIVjnDZJ1wWX5FA8kjE8xf2ZjYk=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_0701437fe6b411f184bd52540072b1e8
    ReservedCode2: EBgapKOuBjbmcqWTzR+4lZJbszzBQmtMRmP0eeGlEwXREZsm1UoxCzjud//xifQ3s9U43SDglGci71hmPpTrcjOTC6zvSuI350Q1XhwyA+vSXFyYz4j5etBtBy5n7LHi3A/bTPe9HHvFgAAVaaY35YcxVxMqP7mavIVjnDZJ1wWX5FA8kjE8xf2ZjYk=
---

# LeadFlow Sentinel

[![CI](https://github.com/hamids-ai-automations/leadflow-sentinel/actions/workflows/ci.yml/badge.svg)](https://github.com/hamids-ai-automations/leadflow-sentinel/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/hamids-ai-automations/leadflow-sentinel?display_name=tag)](https://github.com/hamids-ai-automations/leadflow-sentinel/releases)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://github.com/hamids-ai-automations/leadflow-sentinel/blob/main/pyproject.toml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-101%20passing-brightgreen)](https://github.com/hamids-ai-automations/leadflow-sentinel/tree/main/tests)

**Read-only CRM health, lead-to-booking monitoring and revenue-leakage detection for GoHighLevel (HighLevel) agencies.**

LeadFlow Sentinel audits a GoHighLevel sub-account snapshot, scores its health, and reports the exact leads, opportunities and bookings where money is leaking — with the evidence attached, not a vague "your CRM could be better".

- Zero-dependency Python core. No account, no API key, no dashboard needed to get a first report.
- Read-only by design: nothing in the CRM is created, updated or deleted.
- Deterministic: the same snapshot always produces the same score, so numbers in a client proposal cannot drift overnight.
- AI is optional and fenced: narratives are only accepted when every claim traces back to a finding.

```bash
python -m leadflow_sentinel demo --out demo-audit.json
```

That writes a full audit of a synthetic agency account (52 contacts, 24 opportunities, 15 webhook events, 12 planted defect classes) in under a second.

---

## Why this exists

GoHighLevel agencies do not lose money because a dashboard is missing. They lose it because:

1. **Leads arrive and nobody follows up.** A form fill creates a contact; no opportunity, no call, no appointment. The lead goes cold inside 72 hours.
2. **The same person exists three times.** One record from a Facebook lead form, one from a website form, one imported from a spreadsheet. Reporting counts them as three leads; the follow-up automation fires on the wrong one.
3. **Bookings are never confirmed.** An appointment sits in `pending` forever; the show-up rate collapses and nobody notices until the month ends.
4. **Webhooks fail silently.** HighLevel retries, times out or pauses a subscription; the workflow that was supposed to run simply did not run.

Each of those is measurable from data the account already holds. LeadFlow Sentinel measures them, prices them in severity, and tells the operator which specific records to fix first.

## Quick start

```bash
git clone https://github.com/hamids-ai-automations/leadflow-sentinel
cd leadflow-sentinel

# 1. Prove the detectors fire on known planted defects
python -m leadflow_sentinel selftest

# 2. Audit the synthetic demo account, write a JSON report
python -m leadflow_sentinel demo --out demo-audit.json

# 3. Audit the demo account and write a client-ready Markdown report
python -m leadflow_sentinel demo --out demo-audit.md

# 4. Audit your own snapshot (see docs/GHL-INTEGRATION.md for the shape)
python -m leadflow_sentinel audit --dataset snapshot.json --out reports --format both

# 5. Serve the HTTP API (needs the api extra)
pip install -e ".[api]"
python -m leadflow_sentinel serve --port 8080
```

Python 3.10+. The core installs with **zero** third-party dependencies.

## What you get

A JSON and/or Markdown report containing:

| Section | Content |
|---|---|
| Health score | 0–100 with a letter grade, split across four weighted components |
| Findings | One entry per rule hit, each with severity, affected record IDs, evidence and a concrete remediation |
| Duplicate clusters | Identity clusters with the match basis (email / phone / name) and confidence |
| Journey stats | Leads, opportunities, bookings, follow-ups and the measured booking rate against target |
| Integration stats | Duplicate webhook deliveries and failed events |
| Data completeness | Events received vs used vs rejected, with reasons — a partial picture is never read as a complete one |
| Root-cause notes | Optional, evidence-linked (see `--ai`) |

## Scoring model

The overall score is a weighted average of four components. Weights are configuration, not constants.

| Component | Default weight | Measures |
|---|---:|---|
| Data quality | 0.45 | Missing/invalid emails and phones, missing names and sources, duplicate clusters |
| Pipeline | 0.22 | Orphaned opportunities, missing stages, stalled deals, won deals without an appointment |
| Journey | 0.23 | Lead → opportunity → booking → follow-up conversion inside configured windows |
| Integration | 0.10 | Duplicate deliveries and failed webhook events |

Weights renormalise automatically when a component has no data (an account with no webhook subscriptions should not be punished for a missing integration score). Every excluded component is named in `score.excluded` with the reason and the weight it gave up, and `score_explanation` prints the arithmetic so the total can be recomputed by hand. See [docs/TRUST-MODEL.md](https://github.com/hamids-ai-automations/leadflow-sentinel/blob/main/docs/TRUST-MODEL.md).

Grade bands: `A ≥ 90`, `B ≥ 80`, `C ≥ 70`, `D ≥ 55`, `F < 55`.

Per-subject penalty: the worst finding dominates and every additional finding adds a quarter of its own penalty, capped at 100 — one seriously broken record is not diluted by fifty healthy ones, but a record with five problems still scores worse than one with a single problem.

## Rule catalogue

20 rules across four categories, all 20 live. `INT-003` is the one that exists to catch the tool's own blind spot: an integration that stops sending webhooks looks identical to a healthy funnel unless the silence is measured (see `docs/TRUST-MODEL.md`).

| Rule | Severity | Category | Checks |
|---|---|---|---|
| DQ-001 | medium | data quality | Missing email |
| DQ-002 | high | data quality | Invalid email format |
| DQ-003 | medium | data quality | Missing phone |
| DQ-004 | high | data quality | Invalid phone number |
| DQ-005 | low | data quality | Missing contact name |
| DQ-006 | low | data quality | Missing lead source |
| DQ-007 | low | data quality | Non-canonical phone format |
| DQ-008 | high | data quality | Duplicate contact cluster |
| OPP-001 | high | pipeline | Orphaned opportunity (contact no longer exists) |
| OPP-002 | medium | pipeline | Opportunity missing stage |
| OPP-003 | medium | pipeline | Stalled opportunity (no update in N days) |
| OPP-004 | medium | pipeline | Won deal without an appointment |
| JRN-001 | high | journey | Contact created without an opportunity |
| JRN-002 | high | journey | Appointment not confirmed |
| JRN-003 | medium | journey | Booked appointment without an opportunity |
| JRN-004 | medium | journey | Lead without recorded follow-up |
| JRN-005 | high | journey | Lead past booking window with no appointment |
| INT-001 | medium | integration | Duplicate webhook deliveries |
| INT-002 | high | integration | Event processing failure |
| INT-003 | high | integration | Missing expected event — expected types absent, recent contacts with
```
