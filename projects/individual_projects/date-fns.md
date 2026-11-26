# date-fns

**Overview:** ⏳ Modern JavaScript date utility library ⌛️

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/date-fns](https://github.com/hamids-ai-automations/date-fns) |
| Live website | https://date-fns.org |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-11-01 |
| Default branch | main |
| License | none declared |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 394 |
| Size | 27089 KB |
| Topics | - |

## Objectives

🔥️ **NEW**: [date-fns v4.0 with first-class time zone support is out!](https://blog.date-fns.org/v40-with-time-zone-support/)

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .agents, .devcontainer, .github, .opencode, .vscode, codemods, pkgs, tmp
- **Total files (tracked in default branch):** 2070
- **CI workflows:** .github/workflows/browser_tests.yaml, .github/workflows/code_quality.yaml, .github/workflows/coverage.yaml, .github/workflows/node_tests.yaml, .github/workflows/smoke_tests.yaml, .github/workflows/tz_tests.yaml
- **Test files detected:** 398

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 3154031 |
| JavaScript | 60434 |
| Shell | 15834 |
| Makefile | 2377 |
| CSS | 1767 |
| HTML | 366 |
| Dockerfile | 157 |

**Frameworks / libraries detected:** none detected from dependency files

**Dependencies:** oxfmt, oxlint, oxlint-tsgolint, typescript, vitest

## Important source files

- `package.json`
- `pkgs/core/examples/cdn/package.json`
- `pkgs/core/examples/cjs/package.json`
- `pkgs/core/examples/cts/package.json`
- `pkgs/core/examples/cts/tsconfig.json`
- `pkgs/core/examples/esm/package.json`
- `pkgs/core/examples/lodash-fp/package.json`
- `pkgs/core/examples/node-esm/package.json`
- `pkgs/core/examples/package.json`
- `pkgs/core/examples/rollup/package.json`
- `pkgs/core/examples/ts/package.json`
- `pkgs/core/examples/ts/tsconfig.json`
- `pkgs/core/examples/vite/package.json`
- `pkgs/core/examples/vite/tsconfig.json`
- `pkgs/core/examples/webpack/package.json`
- `pkgs/core/package.json`
- `pkgs/core/tsconfig.json`
- `pkgs/dev/config/tsconfig.json`
- `pkgs/dev/package.json`
- `pkgs/dev/tsconfig.json`
- `pkgs/docs/package.json`
- `pkgs/docs/tsconfig.json`
- `pkgs/tz/examples/cjs/package.json`
- `pkgs/tz/examples/cts/package.json`
- `pkgs/tz/examples/cts/tsconfig.json`
- `pkgs/tz/examples/esm/package.json`
- `pkgs/tz/examples/ts/package.json`
- `pkgs/tz/examples/ts/tsconfig.json`
- `pkgs/tz/package.json`
- `pkgs/tz/playground/package.json`
- `pkgs/tz/playground/tsconfig.json`
- `pkgs/tz/src/date/index.js`
- `pkgs/tz/test/engines/package.json`
- `pkgs/tz/test/engines/tsconfig.json`
- `pkgs/tz/tsconfig.json`
- `pkgs/utc/examples/cjs/package.json`
- `pkgs/utc/examples/cts/package.json`
- `pkgs/utc/examples/cts/tsconfig.json`
- `pkgs/utc/examples/esm/package.json`
- `pkgs/utc/examples/ts/package.json`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://date-fns.org

## Documentation links

- https://date-fns.org
- https://blog.date-fns.org/v40-with-time-zone-support
- https://raw.githubusercontent.com/date-fns/date-fns/refs/heads/main/pkgs/core/docs/logotype.svg
- https://blog.date-fns.org
- https://lodash.com
- https://date-fns.org/docs/Getting-Started
- https://coderabbit.link/datefns
- https://www.coderabbit.ai/content/assets/white-typemark.svg
- https://www.coderabbit.ai/content/assets/orange-typemark.svg
- https://www.npmjs.com/package/date-fns
- https://kossnocorp.mit-license.org

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/marvis-portfolio
- hamids-ai-automations/ghl-servicepro-theme
- hamids-ai-automations/servicenow-ultimate-mcp
- hamids-ai-automations/shopify-growth-mcp
- hamids-ai-automations/ghl-devops-toolkit

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/date-fns/blob/main/README.md

```markdown
🔥️ **NEW**: [date-fns v4.0 with first-class time zone support is out!](https://blog.date-fns.org/v40-with-time-zone-support/)

<img alt="date-fns" title="date-fns" src="https://raw.githubusercontent.com/date-fns/date-fns/refs/heads/main/pkgs/core/docs/logotype.svg" width="150" />

date-fns provides the most comprehensive, yet simple and consistent toolset for manipulating JavaScript dates in a browser & Node.js

👉 [Documentation](https://date-fns.org/)

👉 [Blog](https://blog.date-fns.org/)

<hr>

It's like [Lodash](https://lodash.com) for dates

- It has [**200+ functions** for all occasions](https://date-fns.org/docs/Getting-Started/).
- **Modular**: Pick what you need. Works with webpack, Browserify, or Rollup and also supports tree-shaking.
- **Native dates**: Uses existing native type. It doesn't extend core objects for safety's sake.
- **Immutable & Pure**: Built using pure functions and always returns a new date instance.
- **TypeScript**: The library is 100% TypeScript with brand-new handcrafted types.
- **I18n**: Dozens of locales. Include only what you need.
- [and many more benefits](https://date-fns.org/)

---

Sponsored by:

<a href="https://coderabbit.link/datefns">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://www.coderabbit.ai/content/assets/white-typemark.svg">
    <img alt="CodeRabbit" src="https://www.coderabbit.ai/content/assets/orange-typemark.svg" width="170">
  </picture>
</a>

---

```js
import { compareAsc, format } from "date-fns";

format(new Date(2014, 1, 11), "yyyy-MM-dd");
//=> '2014-02-11'

const dates = [
  new Date(1995, 6, 2),
  new Date(1987, 1, 11),
  new Date(1989, 6, 10),
];
dates.sort(compareAsc);
//=> [
//   Wed Feb 11 1987 00:00:00,
//   Mon Jul 10 1989 00:00:00,
//   Sun Jul 02 1995 00:00:00
// ]
```

The library is available as an [npm package](https://www.npmjs.com/package/date-fns).
To install the package run:

```bash
npm install date-fns --save
```

## Docs

[See date-fns.org](https://date-fns.org/) for more details, API,
and other docs.

## License

[MIT © Sasha Koss](https://kossnocorp.mit-license.org/)

```
