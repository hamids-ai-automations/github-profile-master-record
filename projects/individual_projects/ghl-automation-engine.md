# ghl-automation-engine

**Overview:** Contract-first HighLevel (GoHighLevel) engine: honest pagination, single-flight OAuth refresh, PII-safe logging, signed webhook intake with replay protection, and an offline mock with fault injection. 83 tests, zero runtime dependencies.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/ghl-automation-engine](https://github.com/hamids-ai-automations/ghl-automation-engine) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-11-21 |
| Last update | 2026-11-22 |
| Last push | 2026-11-22 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 1 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 214 KB |
| Topics | api-client, automation, crm, gohighlevel, highlevel, idempotency, mcp, pagination, python, webhooks |

## Objectives

---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_64158b3be5e411f184bd52540072b1e8
    ReservedCode1: ADkDg75IRrLxsmT7VnbMUurc8BBlgxLfJaAPJHOg7LWEW+ueKuioY8QFZATuWTNEoJRqsGNUWG3hepfwmbLmL0XuCNH64gdvihEnI1zsBxixRDIeuyfWuZ+sGc9Or4GFJdx0SR/5NygP6xaEPWOnfr1LmPFUBGE20oVc7hSW4hLlshTWaPLYF31SDDQ=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_64158b3be5e411f184bd52540072b1e8
    ReservedCode2: ADkDg75IRrLxsmT7VnbMUurc8BBlgxLfJaAPJHOg7LWEW+ueKuioY8QFZATuWTNEoJRqsGNUWG3hepfwmbLm

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, docs, examples, src, tests
- **Total files (tracked in default branch):** 90
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 24

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 440509 |

**Frameworks / libraries detected:** MCP, pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`
- `src/ghl_mock/app.py`

## Installation and setup

```bash
git clone <this repo>
cd ghl-automation-engine
python -m pytest
```

No dependencies. The runtime uses only the standard library, so `pytest` is the
only thing you need, and CI needs no Docker and no network.

## Deployment

No deployment configuration detected.

## Documentation links

- Repository README: https://github.com/hamids-ai-automations/ghl-automation-engine/blob/main/README.md

## Development status

Active — last push 2026-11-22

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/ghl-automation-engine/blob/main/README.md

```markdown
---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_64158b3be5e411f184bd52540072b1e8
    ReservedCode1: ADkDg75IRrLxsmT7VnbMUurc8BBlgxLfJaAPJHOg7LWEW+ueKuioY8QFZATuWTNEoJRqsGNUWG3hepfwmbLmL0XuCNH64gdvihEnI1zsBxixRDIeuyfWuZ+sGc9Or4GFJdx0SR/5NygP6xaEPWOnfr1LmPFUBGE20oVc7hSW4hLlshTWaPLYF31SDDQ=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_64158b3be5e411f184bd52540072b1e8
    ReservedCode2: ADkDg75IRrLxsmT7VnbMUurc8BBlgxLfJaAPJHOg7LWEW+ueKuioY8QFZATuWTNEoJRqsGNUWG3hepfwmbLmL0XuCNH64gdvihEnI1zsBxixRDIeuyfWuZ+sGc9Or4GFJdx0SR/5NygP6xaEPWOnfr1LmPFUBGE20oVc7hSW4hLlshTWaPLYF31SDDQ=
---

# ghl-automation-engine

HighLevel (GoHighLevel) integration engine for teams that put automations in
production and cannot afford them to be quietly wrong.

The GoHighLevel ecosystem already has a 900-tool MCP server. Tool *count* is not
the bottleneck. Reliability is. This project is deliberately narrow: it makes the
failure modes visible instead of silent.

## The four failures this exists to prevent

| Failure | What it looks like in production | What this library does |
| --- | --- | --- |
| Silent pagination truncation | Page 2 of 5 fails, the caller returns page 1, a downstream workflow treats 100 contacts as "all contacts" and archives the rest | Cursor walking is exhaustive by contract: you get a `Collection` with an honest `complete` flag, or a `GhlPartialResultError` carrying what was collected |
| Refresh-token stampede | 12 concurrent workers see an expired token, all refresh, the provider rotates the refresh token, 11 calls return `invalid_grant`, the integration hard-fails | Single-flight refresh under a lock with a double-checked expiry, and the rotated token is persisted before the lock is released |
| PII in logs | A debug line logs the contact upsert body and every email address lands in the log aggregator | Recursive redaction of credentials, emails, and phone numbers before any log record is emitted |
| Untestable integrations | Every test needs a live sub-account and a private token, so there are no tests | An offline mock server with fault injection; the whole suite runs on a clean machine in seconds |
| Webhook replays processed twice | A captured delivery is resent, or a platform retry arrives after a partial write, and the contact is created or the invoice is paid twice | Signature + timestamp window + an atomic seen-set; a duplicate returns `200` with `process=false`, so the sender stops retrying and your code does not run again |

## Install

```bash
git clone <this repo>
cd ghl-automation-engine
python -m pytest
```

No dependencies. The runtime uses only the standard library, so `pytest` is the
only thing you need, and CI needs no Docker and no network.

## Quickstart

```python
from ghl_client import ContactsResource, GhlClient, PrivateIntegrationToken

client = GhlClient(
    PrivateIntegrationToken(token="pit-..."),
    location_id="loc_...",
)

contacts = ContactsResource(client)
result = contacts.search(query="@example.com")

if not result.complete:
    raise SystemExit(f"refusing to act on {len(result)} of an unknown total")

for contact in result.items:
    ...
```

Idempotent writes:

```python
# Replaying this call does not create a duplicate contact.
contacts.upsert({"email": "jane@example.com"}, idempotency_key="sync-run-2026-11-21")
```

## Webhooks

```python
from ghl_webhooks import Receiver

receiver = Receiver(["whsec_..."])

def handle_delivery(headers, raw_body):
    intake = receiver.handle(headers, raw_body)
    if intake.should_process:
        dispatch(intake.event)      # a real, first-time, verified event
    return intake.http_status, {"status": intake.status.value}
```

Three things this does that a naive handler does not:

* **Order matters.** Nothing is parsed until the signature verifies, and no event id is
  claimed until every other check has passed — so an attacker cannot burn event ids to
  block genuine deliveries.
* **Duplicates are visible.** A repeat delivery answers `200` with `process=false`. The
  sender stops retrying; your application does not re-run. "Received" and "acted on" are
  different questions and both get an answer.
* **Unknown event types are kept.** An unrecognised type is delivered with
  `event.is_known == False` and its raw body intact. Silently discarding it is how an
  integration appears healthy while ingesting nothing.

Signature framing (header names, hex vs base64, what exactly is signed) is configuration
rather than a guess, because getting it wrong silently rejects real traffic. See
`docs/adr/ADR-002-webhook-signature-framing.md` for the default assumption and how to
confirm it against one captured delivery.

Run the intake demo — no network, no credentials:

```bash
python examples/demo_webhooks.py
```

## Governed MCP server

```bash
export GHL_PIT_TOKEN=pit-...      export GHL_LOCATION_ID=loc_...
export GHL_MCP_MODE=read-write    # default is read-only
export GHL_MCP_APPROVAL_SECRET=... # required before any write will run
ghl-mcp                            # JSON-RPC over stdio
```

Five tools: `get_contact`, `search_contacts`, `upsert_contact`, `rate_limit_status`,
`server_governance`. Scope is narrow on purpose — a tool that returns a plausible empty
result is worse than a tool that is absent, so the unimplemented ones are listed with
reasons instead of being faked.

The part that matters is the interceptor every call passes through, in this order:

1. **Mode.** Read-only unless the operator turned writes on. A refusal is `read_only_mode`,
   never a `200` with an empty body.
2. **Schema.** Unknown properties are rejected, so there is no `locationId` to argue about —
   cross-account access is not a policy, it is a shape that does not exist.
3. **Location.** The server is bound to one sub-account; an unbound client gets
   `cross_location` rather than a default location.
4. **Approval.** A write needs a single-use, short-lived token issued for *that tool and
   those exact arguments*. A token for one contact cannot be spent on another.
5. **Budget.** Session ceilings stop a loop before the platform rate limiter or the invoice
   does.

```bash
# the human approves one specific change
ghl-mcp approve --tool upsert_contact \
  --args '{"email":"ada@example.com","first_name":"Ada"}'
```

`upsert_contact` also takes `dry_run: true`, which returns the payload it *would* send and
touches nothing. `server_governance` reports the active policy, the PII allowlist, and the
blocked-tool list. Without `GHL_PIT_TOKEN` the server exits `2` and says why, instead of
starting up to answer 401s that an agent would narrate as "no contacts found".

Full detail: [`docs/MCP.md`](https://github.com/hamids-ai-automations/ghl-automation-engine/blob/main/docs/MCP.md).

## Offline development

```bash
python -m ghl_mock --port 8080
python examples/demo_offline.py     # full round trip against the mock
```

The mock can be told to fail on purpose, which is the point:

```bash
curl -X POST localhost:8080/__admin/inject \
  -H 'content-type: application/json' \
  -d '{"path": "/contacts/search", "status": 429, "times": 1, "retry_after": "2"}'
```

## Architecture

```
src/ghl_client/
  errors.py       typed hierarchy; retryable is a property of the error, not the caller
  ratelimit.py    sliding-window budget, 90 req / 10 s (platform allows 100)
  retry.py        Retry-After (seconds and HTTP-date), capped at 120 s, full jitter
  transport.py    the only module that touches a socket; injectable
  auth.py         private tokens + OAuth with single-flight refresh and persistence
  pagination.py   exhaustive cursor walking with loop detection
  client.py       versioning, budgeting, redaction, request ids
  resources/      contacts (search, idempotent upsert)
src/ghl_mock/
  store.py        in-memory contacts with email/phone dedupe and cursor paging
  app.py          stdlib HTTP serve
```
