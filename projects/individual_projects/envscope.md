# envscope

**Overview:** CLI that audits .env files against .env.example and a JSON schema without ever printing secrets. DevSecOps, Python.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/envscope](https://github.com/hamids-ai-automations/envscope) |
| Live website | https://marvis.web.app/ |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-30 |
| Last update | 2026-11-20 |
| Last push | 2026-11-21 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 2 |
| Size | 53 KB |
| Topics | cli, devsecops, dotenv, python, secrets-scanning, security |

## Objectives

envscope: zero-dependency CLI that audits .env files against .env.example and a JSON schema, never printing secret values.

## Features
- Drift detection (missing, extra, empty, duplicate keys)
- Type validation: string, int, float, bool, port, url, email, pattern, choices
- Duplicate detection
- Secret-aware (values flagged secret are never printed)
- CI-friendly (--json, --sarif, stable exit codes)
- SARIF 2.1.0 export for GitHub code scanning
- Zero dependencies (Python 3.9+)
- Fast (parses thousands of keys in milliseconds)

## Requirements
- Python 3.11 or newer
- macOS, Lin

## Features

- Drift detection (missing, extra, empty, duplicate keys)
- Type validation: string, int, float, bool, port, url, email, pattern, choices
- Duplicate detection
- Secret-aware (values flagged secret are never printed)
- CI-friendly (--json, --sarif, stable exit codes)
- SARIF 2.1.0 export for GitHub code scanning
- Zero dependencies (Python 3.9+)
- Fast (parses thousands of keys in milliseconds)

## Technical architecture

- **Top-level directories:** .github, docs, examples, src, tests
- **Total files (tracked in default branch):** 30
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 5

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 48113 |
| Makefile | 359 |

**Frameworks / libraries detected:** none detected from dependency files

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

```bash
git clone https://github.com/hamids-ai-automations/envscope.git
cd envscope
python -m pip install -e .
```

## Deployment

Firebase/other hosting declared via homepage field: https://marvis.web.app/

## Documentation links

- https://marvis.web.app

## Development status

Active — last push 2026-11-21

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine
- hamids-ai-automations/gemini-agent-reliability-kit
- hamids-ai-automations/searchpulse-ai

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/envscope/blob/main/README.md

```markdown
envscope: zero-dependency CLI that audits .env files against .env.example and a JSON schema, never printing secret values.

## Features
- Drift detection (missing, extra, empty, duplicate keys)
- Type validation: string, int, float, bool, port, url, email, pattern, choices
- Duplicate detection
- Secret-aware (values flagged secret are never printed)
- CI-friendly (--json, --sarif, stable exit codes)
- SARIF 2.1.0 export for GitHub code scanning
- Zero dependencies (Python 3.9+)
- Fast (parses thousands of keys in milliseconds)

## Requirements
- Python 3.11 or newer
- macOS, Linux, or Windows

## Install
```bash
git clone https://github.com/hamids-ai-automations/envscope.git
cd envscope
python -m pip install -e .
```

## Usage
```bash
envscope check [--env .env --example .env.example --schema envscope.json --strict --json --sarif PATH --quiet --no-color]
envscope init --example .env.example --out envscope.json
envscope version
```

## Schema format
envscope.json: `{"variables": {"APP_ENV":{"type":"string","choices":["development","staging","production"]},...}}`
Flat `{"PORT":"port"}` also accepted.

## CI example
```yaml
- name: Validate environment contract
  run: |
    python -m pip install -e .
    envscope check --strict --json > envscope-report.json
  env:
    PYTHONPATH: src
```

## SARIF / code scanning
`envscope check --sarif envscope.sarif` writes a SARIF 2.1.0 log next to the normal
output. Findings map to one rule per issue code (`parse`, `duplicate`, `missing`,
`empty`, `invalid`, `extra`) with error/warning levels, so GitHub code scanning can
group and annotate them inline on the offending dotenv line.

The log only contains key names, line numbers and envscope's own messages. Secret
values are never written to it, which is what makes it safe to upload as a build
artifact.

```yaml
- name: Validate environment contract
  run: |
    python -m pip install -e .
    envscope check --strict --sarif envscope.sarif
  env:
    PYTHONPATH: src
  continue-on-error: true

- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: envscope.sarif
    category: envscope
```

## Tests
42 tests, no dependencies. CI runs on Python 3.11, 3.12, 3.13.

## License
MIT

```
