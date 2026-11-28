# gemini-agent-reliability-kit

**Overview:** Offline-first reliability harness for Gemini tool-calling agents: schema, tool choice, argument contracts, retry telemetry, latency and cost report cards.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/gemini-agent-reliability-kit](https://github.com/hamids-ai-automations/gemini-agent-reliability-kit) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-11-21 |
| Last update | 2026-11-21 |
| Last push | 2026-11-22 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 37 KB |
| Topics | ai-agents, gemini, google-gemini, llm-eval, python, reliability, tool-calling |

## Objectives

# Gemini Agent Reliability Kit (GAR Kit)

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, docs, gar, suites, tests
- **Total files (tracked in default branch):** 33
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 6

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 57497 |

**Frameworks / libraries detected:** pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

No installation instructions found in the README.

## Deployment

No deployment configuration detected.

## Documentation links

- https://me.developers.google.com/u/hamidautomations

## Development status

Active — last push 2026-11-22

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

Full README: https://github.com/hamids-ai-automations/gemini-agent-reliability-kit/blob/main/README.md

```markdown
# Gemini Agent Reliability Kit (GAR Kit)

[![ci](https://github.com/hamids-ai-automations/gemini-agent-reliability-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/hamids-ai-automations/gemini-agent-reliability-kit/actions/workflows/ci.yml)
[![python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](pyproject.toml)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Most Gemini agent failures are not "the model is dumb". They are concrete, boring, and repeatable:

- the model picks the right tool but drops a required argument,
- it returns JSON that is 95% correct and unusable,
- it retries four times with the same backoff and burns your quota,
- one case in the suite takes 9 seconds and nobody notices until it is in production.

GAR Kit turns a handful of labelled cases into a **report card** that names the failure, on the case, in CI,
before your users find it. Zero dependencies, no network or API key needed for the default path.

```
GAR Kit report card  suite=smoke  model=mock-1  cases=6
------------------------------------------------------------------------------
ID                  PASS  SCHEMA  TOOLS  ARGS  RETRY  LATENCY  COST($)
tool-basic          no    ok      ok     ok    FAIL   ok       0.000000
schema-json         no    ok      ok     ok    FAIL   ok       0.000000
------------------------------------------------------------------------------
pass rate 0.0%  (gate 90.0%)  -> FAIL
failures by check: retry=6

EVIDENCE
  tool-basic / retry: 5 attempts exceeded budget of 3
  schema-json / retry: 5 attempts exceeded budget of 3
```

## Quickstart

```bash
git clone https://github.com/hamids-ai-automations/gemini-agent-reliability-kit
cd gemini-agent-reliability-kit
python -m venv .venv && . .venv/Scripts/activate   # Windows; use .venv/bin/activate on macOS/Linux
pip install -e ".[dev]"

gar run --suite suites/smoke.json --provider mock --report reports/smoke.md
```

Add `--fail-on-gate` to turn the gate into an exit code: `1` when the gate is missed, `0` when it passes. Without
the flag a failing card still exits `0`, which is what you want for an exploratory run and not what you want in CI.
The mock provider is deterministic: same suite in, same card out, no credentials.

## Running against a real model

```bash
# PowerShell
$env:GEMINI_API_KEY = "...."
gar run --suite suites/smoke.json --provider gemini --model gemini-2.0-flash `
        --report reports/gemini-smoke.md --json reports/gemini-smoke.json --fail-on-gate
```

The Gemini provider uses the plain REST endpoint over `urllib` — no SDK, no transitive dependency tree.
It reports what actually happened: `attempts`, `backoff_ms`, `usageMetadata` token counts. Nothing is estimated
except the price table, and if the response carries no usage metadata the cost is reported as `0`, never invented.

## What gets checked

| check | question it answers | failure looks like |
| --- | --- | --- |
| `schema` | Does the structured output satisfy the declared subset of JSON Schema? | missing key, wrong type, unparsable JSON |
| `tool_call` | Did the model pick the expected tool (and not a dangerous one)? | `delete_everything` instead of `get_weather` |
| `args` | Did the call carry every required argument with the expected value? | `{}` sent to a tool that needs `city` |
| `retry` | Did the turn stay inside the attempt budget with growing backoff? | 5 attempts, flat 40 ms spacing |
| `latency` | Did the case stay inside `max_latency_ms`? | p95 regression nobody caught in review |

Every failure carries a one-line evidence string naming the case and the check, so a red CI job tells you what to
fix instead of just that something is wrong.

## Suite format

```json
{
  "name": "smoke",
  "gate": {"min_pass_rate": 0.9},
  "cases": [
    {
      "id": "tool-basic",
      "prompt": "What is the weather in Lahore right now?",
      "tools": [{"name": "get_weather", "parameters": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"]}}],
      "expected_tool": "get_weather",
      "expected_args": {"city": "Lahore"},
      "max_latency_ms": 4000,
      "max_attempts": 3
    }
  ]
}
```

Anything you cannot assert on is omitted; a case with no `expected_tool` simply skips the tool checks.

## Example artefacts

Committed under [`docs/`](https://github.com/hamids-ai-automations/gemini-agent-reliability-kit/blob/main/docs) so the output is visible without running anything:

- `example-report-pass.md` / `.json` — a clean run
- `example-report-fail-retry-storm.md` — retry budget blown, everything else fine
- `example-report-fail-wrong-tool.md` — correct arguments, wrong tool

## Architecture

```
suite.json --> runner --> provider (mock | gemini)
                              |
                              +--> Turn(text, tool_calls, usage, latency_ms, attempts, backoff_ms)
                              |
                 checks: schema | tool_call | args | retry | latency
                              |
                 CaseResult --> aggregates (pass rate, p50/p95, cost) --> report card
                              |
                              +--> markdown / json / text  -->  exit code (CI gate)
```

Design notes, extension points and the reasoning behind the check set live in
[`docs/architecture.md`](https://github.com/hamids-ai-automations/gemini-agent-reliability-kit/blob/main/docs/architecture.md). A longer write-up on why the output is a named failure rather than a
score: [`docs/article-01-let-your-agent-failures-name-themselves.md`](https://github.com/hamids-ai-automations/gemini-agent-reliability-kit/blob/main/docs/article-01-let-your-agent-failures-name-themselves.md).

## Not in scope (on purpose)

- No leaderboard of model scores. A model benchmark ages badly; a suite you own does not.
- No LLM-as-judge. Judging with a model makes the harness as flaky as the thing it measures.
- No dashboard. A markdown card diffed in a PR is a better review artefact than a chart nobody opens.

## Status

- [x] Eval suite format + runner
- [x] Four reliability checks with per-case evidence
- [x] Mock provider (offline, deterministic) + live Gemini REST provider
- [x] Report card: text / markdown / JSON, CI gate via exit code
- [x] 53 tests, no network or credentials required
- [x] CI on Python 3.10 / 3.11 / 3.12
- [ ] Vertex AI provider
- [ ] HTML report card

## License

MIT — see [LICENSE](https://github.com/hamids-ai-automations/gemini-agent-reliability-kit/blob/main/LICENSE).

Built by Muhammad Hamid — [Google Developer profile](https://me.developers.google.com/u/hamidautomations).

```
