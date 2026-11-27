# supabase-py

**Overview:** Python Client for Supabase. Query Postgres from Flask, Django, FastAPI. Python user authentication, security policies, edge functions, file storage, and realtime data streaming. Good first issue.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/supabase-py](https://github.com/hamids-ai-automations/supabase-py) |
| Live website | https://supabase.com/docs/reference/python |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-11-02 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 118 |
| Size | 4604 KB |
| Topics | - |

## Objectives

# `supabase-py`

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .devcontainer, .github, docs, src
- **Total files (tracked in default branch):** 302
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/conventional-commits.yml, .github/workflows/stale.yml, .github/workflows/sync-compliance.yml, .github/workflows/validate-capabilities.yml
- **Test files detected:** 89

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 1038051 |
| Makefile | 13363 |
| Dockerfile | 4116 |
| Nix | 2767 |
| Batchfile | 1529 |

**Frameworks / libraries detected:** Supabase, pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`
- `src/auth/infra/docker-compose.yml`
- `src/auth/pyproject.toml`
- `src/functions/pyproject.toml`
- `src/postgrest/docs/requirements.txt`
- `src/postgrest/pyproject.toml`
- `src/realtime/pyproject.toml`
- `src/storage/pyproject.toml`
- `src/supabase/pyproject.toml`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://supabase.com/docs/reference/python

## Documentation links

- https://supabase.com/docs/reference/python
- https://pypi.org/project/supabase
- https://supabase.com
- https://supabase.com/docs/reference/python/introduction
- https://supabase.com/blog/oauth2-login-python-flask-apps
- https://supabase.com/blog/loading-data-supabase-python
- https://docs.astral.sh/uv/concepts/projects/workspaces

## Development status

Fork of another project; see upstream for original authorship.

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

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/supabase-py/blob/main/README.md

```markdown
# `supabase-py`

[![CI](https://github.com/supabase/supabase-py/actions/workflows/ci.yml/badge.svg)](https://github.com/supabase/supabase-py/actions/workflows/ci.yml)
[![Version](https://img.shields.io/pypi/v/supabase?color=%2334D058)](https://pypi.org/project/supabase)
[![Coverage Status](https://coveralls.io/repos/github/supabase/supabase-py/badge.svg?branch=main)](https://coveralls.io/github/supabase/supabase-py?branch=main)

Python monorepo for all [Supabase](https://supabase.com) libraries.

- [supabase](https://github.com/hamids-ai-automations/supabase-py/blob/main/src/supabase/README.md)
- [realtime-py](https://github.com/hamids-ai-automations/supabase-py/blob/main/src/realtime/README.md)
- [supabase_functions](https://github.com/hamids-ai-automations/supabase-py/blob/main/src/functions/README.md)
- [storage3](https://github.com/hamids-ai-automations/supabase-py/blob/main/src/storage/README.md)
- [postgrest](https://github.com/hamids-ai-automations/supabase-py/blob/main/src/postgrest/README.md)
- [supabase_auth](https://github.com/hamids-ai-automations/supabase-py/blob/main/src/auth/README.md)

Relevant links:

- Documentation: [supabase.com/docs](https://supabase.com/docs/reference/python/introduction)
- Usage:
  - [GitHub OAuth in your Python Flask app](https://supabase.com/blog/oauth2-login-python-flask-apps)
  - [Python data loading with Supabase](https://supabase.com/blog/loading-data-supabase-python)

## Local Development

### Clone the Repository

```bash
git clone https://github.com/supabase/supabase-py.git
cd supabase-py
```

### Dependencies

This repository relies on the following dependencies for development: 
- `uv` for python project management.
- `make` for running project commands.
- `docker` for both `postgrest` and `auth` test containers.
- `supabase-cli` for both `storage` and `realtime` test containers.

All of these dependencies are included in the nix shell environment, through `flake.nix`. If you've got `nix` installed, you may prefer to use it through `nix develop`.

### Use a Virtual Environment

We recommend using a virtual environment, preferably through `uv`, given it is currently the only tool that understands the workspace setup (you can read more about it in [the uv docs](https://docs.astral.sh/uv/concepts/projects/workspaces/)).

```
uv venv supabase-py
source supabase-py/bin/activate
uv sync
```

If you're using nix, the generated `python` executable should have the correct dependencies installed for the whole workspace, given it is derived from the root's `pyproject.toml` using [uv2nix](https://github.com/pyproject-nix/uv2nix).

### Running tests and other commands

We use `make` to store and run the relevant commands. The structure is set up such that each sub package can individually set its command in its own `Makefile`, and the job of the main `Makefile` is just coordinate calling each of them.

For instance, in order to run all tests of all packages, you should use the following root command
```bash
make ci
```
Which internally dispatches `make -C src/{package} tests` calls to each package in the monorepo.

You should also consider using
```bash
make ci -jN # where N is the number of max concurrent jobs, or just -j for infinite jobs
```
To run each of the packages' tests in parallel. This should be generally faster than running in 1 job, but has the downside of messing up the CLI output, so parsing error messages might not be easy.

Other relevant commands include
```bash
make install-hooks # install all commit hooks into the local .git folder
make stop-infra    # stops all running containers from all packages
make clean         # delete all intermediary files created by testing
```
All the subpackages command are available from the main root by prefixing the command with `{package_name}.`. Examples:
```bash
make realtime.tests # run only realtime tests
make storage.clean  # delete temporary files only in the storage package
```

```
