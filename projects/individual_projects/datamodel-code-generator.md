# datamodel-code-generator

**Overview:** Generate Pydantic v2 models, dataclasses, TypedDict, and msgspec.Struct from OpenAPI, JSON Schema, GraphQL, Avro, Protobuf, and raw JSON/YAML/CSV.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/datamodel-code-generator](https://github.com/hamids-ai-automations/datamodel-code-generator) |
| Live website | https://datamodel-code-generator.koxudaxi.dev/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-30 |
| Last update | 2026-10-30 |
| Last push | 2026-10-31 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 216 |
| Size | 77012 KB |
| Topics | - |

## Objectives

# datamodel-code-generator

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, docs, overrides, scripts, skills, src, tests
- **Total files (tracked in default branch):** 19501
- **CI workflows:** .github/workflows/action-smoke.yaml, .github/workflows/behaviour-diff.yaml, .github/workflows/behaviour-record.yaml, .github/workflows/changelog.yaml, .github/workflows/cli-docs.yaml, .github/workflows/codeql.yaml, .github/workflows/codespell.yaml, .github/workflows/codspeed.yaml, .github/workflows/config-types.yaml, .github/workflows/docker.yaml, .github/workflows/docs-deploy.yaml, .github/workflows/docs.yaml, .github/workflows/generated-docs-sync.yaml, .github/workflows/lint.yaml, .github/workflows/llms-txt.yaml, .github/workflows/payload-runtime-compatibility.yaml, .github/workflows/perf-memory.yaml, .github/workflows/playground-lint.yaml, .github/workflows/publish.yaml, .github/workflows/readme.yaml
- **Test files detected:** 18841

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 29111000 |
| Jinja | 256843 |
| HTML | 4981 |
| Shell | 3662 |
| JavaScript | 2168 |
| Dockerfile | 1669 |

**Frameworks / libraries detected:** Express, FastAPI, pytest

**Dependencies:** none detected

## Important source files

- `docs/assets/playground/app.py`
- `docs/assets/playground/pyproject.toml`
- `pyproject.toml`
- `src/datamodel_code_generator/_fastapi/_compiled_templates/main.py`
- `tests/data/config/external_ref_mapping_round_trip/pyproject.toml`
- `tests/data/docs/howto/app/main.py`
- `tests/data/expected/api_generation/fastapi_cli/check_outputs[json-package-in-models-services].2/server/main.py`
- `tests/data/expected/api_generation/fastapi_cli/check_outputs[json-package-in-models].2/server/main.py`
- `tests/data/expected/main/generate_returns_dict_for_multiple_modules/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/binary-allowed/pydantic_v2_BaseModel/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/docstrings/pydantic_v2_BaseModel/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/native-merged-null/pydantic_v2_BaseModel/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/pets/pydantic_v2_BaseModel/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/pets/pydantic_v2_BaseModel~generate_server_without_output/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/pets~fastapi_render[pets]/pydantic_v2_BaseModel/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/references/pydantic_v2_BaseModel/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/scheme-names/pydantic_v2_BaseModel/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/packages/templates/pydantic_v2_BaseModel/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/defaults/pydantic_v2_BaseModel/defaults_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/entrypoint/nested/app/server/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/entrypoint/secured/secured/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/locals/pydantic_v2_BaseModel/locals_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/nullable-results/pydantic_v2_BaseModel/nullable_results_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/nullable/pydantic_v2_BaseModel/nullable_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/parameters/pydantic_v2_BaseModel/parameters_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/pets-type-checking/pydantic_v2_BaseModel/pets_type_checking_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/pets/pydantic_v2_BaseModel/pets_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/pets/pydantic_v2_dataclass/pets_dataclass/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/spellings-exact/pydantic_v2_BaseModel/spellings_exact_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/spellings/pydantic_v2_BaseModel/spellings_basemodel/main.py`
- `tests/data/expected/main/generation_platform/fastapi/servers/packages/strict/pydantic_v2_BaseModel/strict_basemodel/main.py`
- `tests/data/expected/main/jsonschema/main_jsonschema/merged_external_false_member/main.py`
- `tests/data/expected/main/jsonschema/reuse_model_same_name_references/main.py`
- `tests/data/expected/main/openapi/discriminator/msgspec_tagged_base_redefined_field/app.py`
- `tests/data/expected/main/openapi/discriminator/msgspec_tagged_base_subclass_modules/app.py`
- `tests/data/generation_platform/client/line-length/pyproject.toml`
- `tests/data/generation_platform/client/publication/app.py`
- `tests/data/generation_platform/client/type-checking/pyproject.toml`
- `tests/data/generation_platform/fastapi/install/app.py`
- `tests/data/jsonschema/merged_external_refs/package.json`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://datamodel-code-generator.koxudaxi.dev/

## Documentation links

- http://localhost:8000
- https://datamodel-code-generator.koxudaxi.dev
- https://datamodel-code-generator.koxudaxi.dev/playground
- https://koxudaxi.dev/?utm_source=github_readme&utm_medium=top&utm_campaign=open_to_work
- https://pypi.python.org/pypi/datamodel-code-generator
- https://anaconda.org/conda-forge/datamodel-code-generator
- https://api.pepy.tech/badge/datamodel-code-generator/month
- https://pepy.tech/projects/datamodel-code-generator
- https://pydantic.dev
- https://packages.debian.org/search?keywords=datamodel-codegen&searchon=names&suite=all&section=all
- https://packages.ubuntu.com/search?keywords=datamodel-codegen&searchon=names&suite=all&section=all
- https://search.nixos.org/packages?query=datamodel-code-generator
- https://software.opensuse.org/package/python-datamodel-code-generator
- https://datamodel-code-generator.koxudaxi.dev/faq/#http-backend-selection
- https://datamodel-code-generator.koxudaxi.dev/cli-reference
- https://datamodel-code-generator.koxudaxi.dev/presets
- https://datamodel-code-generator.koxudaxi.dev/cli-reference/base-options/#preset
- https://datamodel-code-generator.koxudaxi.dev/cli-reference/base-options/#input-file-type
- https://datamodel-code-generator.koxudaxi.dev/cli-reference/model-customization/#output-model-type
- https://datamodel-code-generator.koxudaxi.dev/presets/#practical-py312-20261027
- https://datamodel-code-generator.koxudaxi.dev/recommend-options
- http://json-schema.org/draft-07/schema#
- https://datamodel-code-generator.koxudaxi.dev/formatter-behavior
- https://datamodel-code-generator.koxudaxi.dev/performance-benchmarks
- https://datamodel-code-generator.koxudaxi.dev/experimental
- https://datamodel-code-generator.koxudaxi.dev/fastapi-server/#quick-start
- https://datamodel-code-generator.koxudaxi.dev/fastapi-server
- https://datamodel-code-generator.koxudaxi.dev/python-client

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine
- hamids-ai-automations/gemini-agent-reliability-kit
- hamids-ai-automations/envscope
- hamids-ai-automations/searchpulse-ai

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/datamodel-code-generator/blob/main/README.md

```markdown
# datamodel-code-generator

🚀 Generate Python data models from schema definitions in seconds.

📚 [Documentation](https://datamodel-code-generator.koxudaxi.dev/) ·
🧪 [Playground](https://datamodel-code-generator.koxudaxi.dev/playground/) ·
💼 [Lead maintainer available for work](https://koxudaxi.dev/?utm_source=github_readme&utm_medium=top&utm_campaign=open_to_work)

> [!NOTE]
> Playground privacy: Generation runs locally in your browser with Pyodide. Your schema and options are not sent to a
> backend. Shared repro URLs encode them in the URL fragment (`#state=...`), which browsers do not send to the server;
> the full URL can still be stored in your browser history or wherever you share it.

[![PyPI version](https://img.shields.io/pypi/v/datamodel-code-generator.svg)](https://pypi.python.org/pypi/datamodel-code-generator)
[![Conda-forge](https://img.shields.io/conda/v/conda-forge/datamodel-code-generator)](https://anaconda.org/conda-forge/datamodel-code-generator)
[![Downloads](https://api.pepy.tech/badge/datamodel-code-generator/month)](https://pepy.tech/projects/datamodel-code-generator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datamodel-code-generator)](https://pypi.python.org/pypi/datamodel-code-generator)
[![codecov](https://codecov.io/gh/datamodel-code-generator/datamodel-code-generator/graph/badge.svg?token=plzSSFb9Li)](https://codecov.io/gh/datamodel-code-generator/datamodel-code-generator)
![license](https://img.shields.io/github/license/datamodel-code-generator/datamodel-code-generator.svg)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)

## ✨ What it does

<!-- Source of truth: docs/assets/diagrams/hero.mmd — regenerate with `tox run -e diagrams` -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/diagrams/hero-dark.svg">
    <img alt="Schema files, raw data, and existing Python models flow through datamodel-code-generator into Python model output types" src="docs/assets/diagrams/hero-light.svg" width="760">
  </picture>
</p>

Pick any one of the supported inputs and pick the Python model style you want as output.
`--input-model path/to/file.py:ClassName` can even retarget an existing Pydantic, dataclass, or TypedDict class defined
in another Python file to a different output type.

- 📄 Converts **OpenAPI 3**, **AsyncAPI**, **JSON Schema**, **Apache Avro**, **XML Schema**, **Protocol Buffers/gRPC**, **GraphQL**, **MCP tool schemas**, and raw data (JSON/YAML/CSV) into Python models
- 🐍 Generates from **existing Python types** (Pydantic, dataclass, TypedDict) via `--input-model`
- 🎯 Generates **Pydantic v2**, **Pydantic v2 dataclass**, **dataclasses**, **TypedDict**, or **msgspec** output
- 🔗 Handles complex schemas: `$ref`, `allOf`, `oneOf`, `anyOf`, enums, and nested types
- ✅ Produces type-safe, validated code ready for your IDE and type checker

---

## 📦 Installation

Recommended for standalone CLI use:

```bash
uv tool install datamodel-code-generator
```

Conda users can install from conda-forge:

```bash
conda install -c conda-forge datamodel-code-generator
```

For projects that should pin the generator version, add it as a development dependency instead:

```bash
uv add --dev datamodel-code-generator
```

> [!NOTE]
> Community-maintained distribution packages are also available from
> [Debian](https://packages.debian.org/search?keywords=datamodel-codegen&searchon=names&suite=all&section=all),
> [Ubuntu](https://packages.ubuntu.com/search?keywords=datamodel-codegen&searchon=names&suite=all&section=all),
> [nixpkgs](https://search.nixos.org/packages?query=datamodel-code-generator), and
> [openSUSE Tumbleweed](https://software.opensuse.org/package/python-datamodel-code-generator).
> Availability and versions vary by distribution.

<details>
<summary>Other installation methods</summary>

**pip:**
```bash
pip install datamodel-code-generator
```

**uv (run without adding to project):**
```bash
uv run --with datamodel-code-generator datamodel-codegen --help
```

**With stable HTTP support** (for resolving remote `$ref`):
```bash
pip install 'datamodel-code-generator[http]'
```

The `http` extra is supported and is not deprecated. To require the experimental
HTTPX2 backend instead, install `datamodel-code-generator[httpx2]` and pass
`--http-backend httpx2`. The experimental extra is not included in
`datamodel-code-generator[all]`. See
[HTTP backend selection](https://datamodel-code-generator.koxudaxi.dev/faq/#http-backend-selection)
for automatic and explicit selection behavior.

**With GraphQL support:**
```bash
pip install 'datamodel-code-generator[graphql]'
```

**With Protocol Buffers support:**
```bash
pip install 'datamodel-code-generator[protobuf]'
```

**Docker:**
```bash
docker pull koxudaxi/datamodel-code-generator
```

Published Docker images run as a non-root `appuser`. When writing generated files
to a bind-mounted directory, make sure the directory is writable by the container
user or pass an explicit Docker user, for example `--user "$(id -u):$(id -g)"`.

</details>

---

## 🏃 Quick Start

<!-- BEGIN AUTO-GENERATED PRESET QUICK START -->
**Command**

```bash
datamodel-codegen \
  --input schema.json \
  --input-file-type jsonschema \
  --output-model-type pydantic_v2.BaseModel \
  --preset standard-py312-20261027 \
  --output model.py
```

This quick start uses `standard-py312-20261027` as the modern Python 3.12 baseline.
Preset names include the target Python version: `py312` means Python 3.12.

See [CLI Reference](https://datamodel-code-generator.koxudaxi.dev/cli-reference/) for all options. See [Presets](https://datamodel-code-generator.koxudaxi.dev/presets/),
[`--preset`](https://datamodel-code-generator.koxudaxi.dev/cli-reference/base-options/#preset), [`--input-file-type`](https://datamodel-code-generator.koxudaxi.dev/cli-reference/base-options/#input-file-type), and
[`--output-model-type`](https://datamodel-code-generator.koxudaxi.dev/cli-reference/model-customization/#output-model-type) for this command.

For more schema-aware output that preserves schema-authored names, reuses models, and embeds generated
documentation, use [`practical-py312-20261027`](https://datamodel-code-generator.koxudaxi.dev/presets/#practical-py312-20261027).

**Not sure which options fit your schema?** Add `--recommend-options` to the command above (experimental). It
analyses the schema and prints the options to add on top of the latest preset with the reason for each, and a ready
command and `pyproject.toml` block. See
[Option recommendations](https://datamodel-code-generator.koxudaxi.dev/recommend-options/).

<details>
<summary>Input (<code>schema.json</code>)</summary>

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Pet",
  "type": "object",
  "required": ["name"],
  "properties": {
    "name": {
      "type": "string",
      "description": "The pet's name"
    },
    "species": {
      "type": "string",
      "enum": ["dog", "cat", "bird", "fish"],
      "default": "dog"
    },
    "age": {
      "type": "integer",
      "minimum": 0,
      "description": "Age in years"
    },
    "vaccinated": {
      "type": "boolean",
      "default": false
    }
  }
}
```

</details>

**Output (`model.py`)**

<!-- fmt: off -->

```python
# generated by datamodel-codegen:
#   filename:  schema.json

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class Species(StrEnum):
    dog = 'dog'
    cat = 'cat'
    bird = 'bird'
    fish = 'fish'


class Pet(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: Annotated[str, Field(description="The pet's name")]
    species: Species = Species.dog
    age: Annotated[int | None, Field(description='Age in years', ge=0)] = None
    vaccinated: bool = False
```

<!-- fmt: on --
```
