# tsoa

**Overview:** Build OpenAPI-compliant REST APIs using TypeScript and Node

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/tsoa](https://github.com/hamids-ai-automations/tsoa) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-11-09 |
| Default branch | master |
| License | MIT |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 193 |
| Size | 7560 KB |
| Topics | - |

## Objectives

<div align="center">
  <a href="https://tsoa-community.github.io/docs/" target="blank">
    <h1>tsoa</h1>
  </a>
Pronounced so·uh

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, .vscode, docs, packages, tests
- **Total files (tracked in default branch):** 354
- **CI workflows:** .github/workflows/closeStaleIssuesAndPRs.yml, .github/workflows/runTestsOnPush.yml, .github/workflows/welcome-first-time-contributors.yml
- **Test files detected:** 247

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 1791437 |
| Handlebars | 31654 |
| JavaScript | 2601 |

**Frameworks / libraries detected:** Express

**Dependencies:** @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-config-prettier, husky, lerna, lint-staged, prettier, ts-node, typedoc

## Important source files

- `package.json`
- `packages/cli/package.json`
- `packages/cli/tsconfig.json`
- `packages/runtime/package.json`
- `packages/runtime/tsconfig.json`
- `packages/tsoa/package.json`
- `packages/tsoa/tsconfig.json`
- `tests/esm/package.json`
- `tests/esm/tsconfig.json`
- `tests/fixtures/tsconfig-bundler/tsconfig.json`
- `tests/package.json`
- `tests/tsconfig.json`

## Installation and setup

- [Documentation](https://tsoa-community.github.io/docs/)
- [API Reference](https://tsoa-community.github.io/reference/)
- [Getting started guide](https://tsoa-community.github.io/docs/getting-started)

## Deployment

No deployment configuration detected.

## Documentation links

- https://tsoa-community.github.io/docs
- https://www.npmjs.com/package/tsoa
- https://tsoa-community.github.io/reference
- https://tsoa-community.github.io/docs/getting-started

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/ghl-servicepro-theme
- hamids-ai-automations/servicenow-ultimate-mcp
- hamids-ai-automations/shopify-growth-mcp
- hamids-ai-automations/ghl-devops-toolkit
- hamids-ai-automations/nexgen-financial-experts

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/tsoa/blob/master/README.MD

```markdown
<div align="center">
  <a href="https://tsoa-community.github.io/docs/" target="blank">
    <h1>tsoa</h1>
  </a>
Pronounced so·uh

OpenAPI-compliant REST APIs using TypeScript and Node

![build status](https://github.com/lukeautry/tsoa/actions/workflows/runTestsOnPush.yml/badge.svg)
[![npm version](https://img.shields.io/npm/v/tsoa/latest)](https://www.npmjs.com/package/tsoa)

</div>

## Goal

- TypeScript controllers and models as the single source of truth for your API
- A valid OpenAPI (formerly Swagger) spec (2.0 or 3.0 if you choose 😍) is generated from your controllers and models, including:
  - Paths (e.g. GET /users)
  - Definitions based on TypeScript interfaces (models)
  - Parameters/model properties marked as required or optional based on TypeScript (e.g. myProperty?: string is optional in the OpenAPI spec)
  - jsDoc supported for object descriptions (most other metadata can be inferred from TypeScript types)
- Routes are generated for middleware of choice
  - Express, Hapi, and Koa currently supported, other middleware can be supported using a simple handlebars template
  - Validate request payloads

## Philosophy

- Rely on TypeScript type annotations to generate API metadata if possible
- If regular type annotations aren't an appropriate way to express metadata, use decorators
- Use jsdoc for pure text metadata (e.g. endpoint descriptions)
- Minimize boilerplate
- Models are best represented by interfaces (pure data structures), but can also be represented by classes
- Runtime validation of tsoa should behave as closely as possible to the specifications that the generated OpenAPI 2/3 schema describes. Any differences in validation logic are clarified by logging warnings during the generation of the OpenAPI Specification (OAS) and/or the routes.
  - Please note that by enabling OpenAPI 3 you minimize the chances of divergent validation logic since OpenAPI 3 has a more expressive schema syntax.

## Framework packages

`@tsoa/runtime` does not install a web framework. Its framework packages are optional peer dependencies, so install the ones for the framework you use:

| Framework | Packages                             |
| --------- | ------------------------------------ |
| Express   | `express`, `@types/express` (4 or 5) |
| Koa       | `koa`, `@types/koa` (2 or 3)         |
| Hapi      | `@hapi/hapi`, `@hapi/boom`           |

The generated Hapi routes import `boomify` and `isBoom` from `@hapi/boom`. `@hapi/hapi` depends on it, but list it in your own `package.json` as well: with pnpm or another strict layout, the routes cannot resolve it otherwise.

Each framework's template service has its own entry point. The `@tsoa/runtime` and `tsoa` roots do not export them, so custom route templates (`routes.middlewareTemplate`) and classes that extend a template service import them from the subpath:

```ts
import { ExpressTemplateService } from '@tsoa/runtime/express';
import { HapiTemplateService } from '@tsoa/runtime/hapi';
import { KoaTemplateService } from '@tsoa/runtime/koa';
```

## Getting Started

- [Documentation](https://tsoa-community.github.io/docs/)
- [API Reference](https://tsoa-community.github.io/reference/)
- [Getting started guide](https://tsoa-community.github.io/docs/getting-started)

## Examples

Check out the [guides](https://tsoa-community.github.io/docs/getting-started)

See example controllers in [the tests](https://github.com/hamids-ai-automations/tsoa/blob/master/tests/fixtures/controllers)

See example models in [the tests](https://github.com/hamids-ai-automations/tsoa/blob/master/tests/fixtures/testModel.ts)

## Help wanted

### Contributing code

To contribute (via a PR), please first see the [Contributing Guide](https://github.com/lukeautry/tsoa/tree/master/docs/CONTRIBUTING.md)

### Becoming a maintainer

tsoa wants additional maintainers! The library has increased in popularity and has quite a lot of pull requests and issues. [Please post in this issue](https://github.com/lukeautry/tsoa/issues/236) if you're willing to take on the role of a maintainer.

```
