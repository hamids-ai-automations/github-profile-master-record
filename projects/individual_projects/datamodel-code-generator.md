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

Objectives are not documented in a README. Repository description: Generate Pydantic v2 models, dataclasses, TypedDict, and msgspec.Struct from OpenAPI, JSON Schema, GraphQL, Avro, Protobuf, and raw JSON/YAML/CSV..

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

- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine
- hamids-ai-automations/gemini-agent-reliability-kit
- hamids-ai-automations/envscope

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/datamodel-code-generator/blob/main/README.md
