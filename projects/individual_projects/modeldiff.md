# modeldiff

**Overview:** Regression testing for local AI

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/modeldiff](https://github.com/hamids-ai-automations/modeldiff) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-29 |
| Last update | 2026-10-29 |
| Last push | 2026-10-31 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 7 |
| Size | 153 KB |
| Topics | - |

## Objectives

# ModelDiff

## Features

- **Test cases as data.** Suites in YAML or JSON, validated against a schema, with error messages that name the case and field at fault. Every problem in the file is reported at once.
- **Six check types.**
  | Type | Passes when |
  | --- | --- |
  | `exact` | output equals `expected` (whitespace-stripped by default; optional case-insensitive) |
  | `json` | output parses as JSON and, if `schema` is given, validates against that JSON Schema |
  | `classification` | the predicted label equals `expected` and is one of `labels` (if given) |
  | `required_fields` | the JSON output contains every dotted path in `required` and matches `values` |
  | `tool_call` | the output is a tool call with the expected `name`, and its arguments equal `arguments` and/or validate against `arguments_schema` |
  | `custom` | a Python function you register returns a pass |
- **Baseline vs candidate comparison** that separates *regressions* (pass to fail) from *fixes* (fail to pass), cases still failing, *behavior changes* (passing in both runs but with different output), classification label changes, and cases missing from one side.
- **Reproducible result files** (`modeldiff.run/v1` JSON) recording the output or its hash, status, failure reason, latency, timestamp, runtime and model metadata, and errors. Keys that look like secrets are redacted.
- **Reports** in text, Markdown, or JSON, written to stdout or a file.
- **Latency comparison** with an opt-in threshold. Slowdowns are reported but do not fail the build unless you ask them to.
- **Optional process memory** measurement via `psutil`, clearly labelled as ModelDiff's own process.
- **Two providers.** `replay` serves recorded outputs and needs no model; `ollama` calls a local Ollama server using only the standard library.
- **CI-friendly CLI** with stable exit codes.

## Technical architecture

- **Top-level directories:** .github, docs, examples, src, tests
- **Total files (tracked in default branch):** 49
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 7

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 129057 |

**Frameworks / libraries detected:** pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

Requires Python 3.11 or newer.

```bash
git clone https://github.com/OpenWave-India/modeldiff.git
cd modeldiff
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

Optional extras:

```bash
pip install -e ".[memory]"   # per-case process memory via psutil
pip install -e ".[dev]"      # pytest and ruff for development
```

## Deployment

No deployment configuration detected.

## Documentation links

- https://ollama.com
- http://localhost:11434
- https://www.linkedin.com/company/openwave-india
- https://allcontributors.org
- https://avatars.githubusercontent.com/u/101915083?v=4?s=80
- https://avatars.githubusercontent.com/u/317772335?v=4?s=80
- https://avatars.githubusercontent.com/u/184008125?v=4?s=80
- https://avatars.githubusercontent.com/u/165297479?v=4?s=80
- https://avatars.githubusercontent.com/u/176455968?v=4?s=80
- https://avatars.githubusercontent.com/u/210186755?v=4?s=80

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

- No semantic or similarity scoring. A changed output that still meets its criterion is reported for review, not judged.
- One live provider (Ollama, `/api/generate`, single-turn prompts). Chat-style message lists and native tool-call responses are not sent or parsed from the provider. `tool_call` checks evaluate the output text.
- Cases run sequentially. There is no parallelism and no repeated sampling to estimate variance.
- Memory measurement covers the ModelDiff process only.
- Latency thresholds compare single measurements per case and are sensitive to noise.

## Future development opportunities

These are ideas, not commitments. See the issue tracker for what is being worked on.

- Repeated runs per case, with variance reported, to separate noise from change.
- A chat/messages input format and a provider for OpenAI-compatible local servers (llama.cpp, vLLM, LM Studio).
- JUnit XML output for CI systems.

## README source

Full README: https://github.com/hamids-ai-automations/modeldiff/blob/main/README.md

```markdown
# ModelDiff

[![CI](https://github.com/OpenWave-India/modeldiff/actions/workflows/ci.yml/badge.svg)](https://github.com/OpenWave-India/modeldiff/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](pyproject.toml)

**Regression testing for local AI.**

ModelDiff is a local-first testing framework for detecting behavioral regressions across AI model versions, inference configurations, prompt templates, and runtime changes. You describe test cases in a version-controlled YAML or JSON file, run them against a baseline and a candidate configuration, and get a report of what broke, what got fixed, and what merely changed.

No API keys are needed. The framework, its test suite, and the example workflow run fully offline. Running against a live model is optional and uses a local [Ollama](https://ollama.com) server.

## Why

Swapping a model version, quantization level, prompt template, inference runtime, or generation setting can silently break an application that depends on the model's output:

- JSON that used to parse now arrives wrapped in a Markdown code fence.
- A classifier starts returning a different label.
- A tool call passes `7730` where the schema expects `"7730"`.
- A required field disappears from a structured response.
- Responses get noticeably slower.

Ordinary unit tests do not cover these cases well, because the "code" that changed is a model. ModelDiff gives you repeatable test cases with explicit pass criteria, so a model or config change can be checked like any other change.

## Features

- **Test cases as data.** Suites in YAML or JSON, validated against a schema, with error messages that name the case and field at fault. Every problem in the file is reported at once.
- **Six check types.**
  | Type | Passes when |
  | --- | --- |
  | `exact` | output equals `expected` (whitespace-stripped by default; optional case-insensitive) |
  | `json` | output parses as JSON and, if `schema` is given, validates against that JSON Schema |
  | `classification` | the predicted label equals `expected` and is one of `labels` (if given) |
  | `required_fields` | the JSON output contains every dotted path in `required` and matches `values` |
  | `tool_call` | the output is a tool call with the expected `name`, and its arguments equal `arguments` and/or validate against `arguments_schema` |
  | `custom` | a Python function you register returns a pass |
- **Baseline vs candidate comparison** that separates *regressions* (pass to fail) from *fixes* (fail to pass), cases still failing, *behavior changes* (passing in both runs but with different output), classification label changes, and cases missing from one side.
- **Reproducible result files** (`modeldiff.run/v1` JSON) recording the output or its hash, status, failure reason, latency, timestamp, runtime and model metadata, and errors. Keys that look like secrets are redacted.
- **Reports** in text, Markdown, or JSON, written to stdout or a file.
- **Latency comparison** with an opt-in threshold. Slowdowns are reported but do not fail the build unless you ask them to.
- **Optional process memory** measurement via `psutil`, clearly labelled as ModelDiff's own process.
- **Two providers.** `replay` serves recorded outputs and needs no model; `ollama` calls a local Ollama server using only the standard library.
- **CI-friendly CLI** with stable exit codes.

What ModelDiff does **not** do: it does not judge semantic correctness, factuality, or hallucination. A case passes or fails only according to its explicit criterion. When an output changes but the criterion is still met, ModelDiff reports a behavior change for you to review, not a regression.

## Installation

Requires Python 3.11 or newer.

```bash
git clone https://github.com/OpenWave-India/modeldiff.git
cd modeldiff
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

Optional extras:

```bash
pip install -e ".[memory]"   # per-case process memory via psutil
pip install -e ".[dev]"      # pytest and ruff for development
```

The package is not yet published to PyPI. When it is, the distribution name will be `openwave-modeldiff`, because the name `modeldiff` is already taken on PyPI by an unrelated project. The import name and the command are both `modeldiff`.

## Quick start

The repository includes an example suite for a customer-support assistant, with two sets of recorded outputs. These outputs are hand-written fixtures that illustrate typical regressions. They are not real model outputs.

```bash
# 1. Check the suite file. The example uses a custom check defined in checks.py.
modeldiff validate examples/quickstart/suite.yaml --plugin examples/quickstart/checks.py

# 2. Produce a baseline and a candidate result file.
modeldiff run examples/quickstart/suite.yaml \
  --config examples/quickstart/configs/baseline.yaml \
  --plugin examples/quickstart/checks.py \
  --output out/baseline.json

modeldiff run examples/quickstart/suite.yaml \
  --config examples/quickstart/configs/candidate.yaml \
  --plugin examples/quickstart/checks.py \
  --output out/candidate.json

# 3. Compare them.
modeldiff compare out/baseline.json out/candidate.json --latency-threshold 25 --min-latency-delta 100
```

Output of step 3 (exit code 1 because regressions were found):

```text
ModelDiff comparison: support-assistant
Baseline: baseline-q8    Candidate: candidate-q4

REGRESSIONS FOUND (4)  -  9 cases: 4 regressed, 1 fixed, 0 still failing, 4 passing in both, 3 passing with changed output

Regressions (4):
  ticket-json [json] pass -> fail: output is not valid JSON (line 1, column 1: Expecting value)
  ticket-required-fields [required_fields] pass -> fail: missing field(s): shipping.city
  intent-billing [classification] pass -> fail: predicted 'technical', expected 'billing'
  tool-lookup [tool_call] pass -> fail: tool arguments differ: order_id=7730 (expected '7730')

Fixed (1):
  sentiment-positive [classification] fail -> pass

Passing with changed output (review, not a regression) (3):
  sentiment-negative [classification] pass -> pass
  tool-refund [tool_call] pass -> pass
  summary-length [custom] pass -> pass

Classification changes (2):
  sentiment-positive: 'neutral' -> 'positive'
  intent-billing: 'billing' -> 'technical'

Warnings:
  summary-length: latency 1720.0 ms exceeds max_latency_ms 1500 (new)

Latency (median over 9 cases): 420.0 ms -> 450.0 ms (+7.1%; baseline recorded, candidate recorded)
Slower than +25%:
  summary-length: 900.0 ms -> 1720.0 ms
```

For a Markdown report, for example to attach to a pull request:

```bash
modeldiff compare out/baseline.json out/candidate.json --format markdown --output report.md
```

```markdown
| Case | Type | Change | Output changed | Latency | Candidate reason |
| --- | --- | --- | --- | --- | --- |
| `ticket-json` | json | regression (pass -> fail) | yes | 820.0 ms -> 870.0 ms | output is not valid JSON (line 1, column 1: Expecting value) |
| `intent-billing` | classification | regression (pass -> fail) | yes (`billing` -> `technical`) | 148.0 ms -> 151.0 ms | predicted 'technical', expected 'billing' |
| `sentiment-positive` | classification | fixed (fail -> pass) | yes (`neutral` -> `positive`) | 155.0 ms -> 158.0 ms |  |
| `greeting-exact` | exact | unchanged pass (pass -> pass) | no | 310.0 ms -> 330.0 ms |  |
...
```

### Structured extraction example

The `examples/extraction` suite demonstrates invoice and address extraction with
JSON Schema and required-field checks. Its baseline and candidate outputs are
hand-written replay fixtures, so the workflow is deterministic and needs no
model or network access:

```bash
modeldiff validate examples/extraction/suite.yaml
modeldiff run examples/extraction/suite.yaml \
  --config examples/extraction/configs/baseline.yaml \
  --output out/extraction-baseline.json
modeldiff run examples/
```
