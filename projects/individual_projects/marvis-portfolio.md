# marvis-portfolio

**Overview:** Automated GitHub-driven portfolio for Muhammad Hamid — AI Automation Engineer. Static site generated from github-profile-master-record and deployed to Firebase Hosting.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/marvis-portfolio](https://github.com/hamids-ai-automations/marvis-portfolio) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-11-25 |
| Last update | 2026-11-25 |
| Last push | 2026-11-25 |
| Default branch | main |
| License | none declared |
| Primary language | JavaScript |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 465 KB |
| Topics | - |

## Objectives

# marvis-portfolio

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, data, docs, scripts, src, tests
- **Total files (tracked in default branch):** 51
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/deploy.yml, .github/workflows/live-check.yml, .github/workflows/sync-master-record.yml
- **Test files detected:** 6

## Languages and technologies

| Language | Bytes |
| --- | --- |
| JavaScript | 213102 |
| CSS | 32382 |

**Frameworks / libraries detected:** Firebase, MCP

**Dependencies:** none detected

## Important source files

- `.firebaserc`
- `firebase.json`
- `package.json`

## Installation and setup

```bash
npm run build      # render dist/
npm run validate   # gate the output
npm test           # 30 unit tests
npm run serve      # preview at http://localhost:5000 with Firebase-like routing
npm run ci         # build + validate + test — run before every push
```

No install step is required: the project has no dependencies.

## Deployment

No deployment configuration detected.

## Documentation links

- https://wa.me/923167417135
- https://marvis.web.app**
- http://localhost:5000

## Development status

Active — last push 2026-11-25

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/restock-radar
- hamids-ai-automations/pinvault-pinterest-downloader
- hamids-ai-automations/volparossa-code
- hamids-ai-automations/dayjs

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/README.md

```markdown
# marvis-portfolio

Production site for **Muhammad Hamid** — Digital Marketing Head moving into AI automation
engineering. Live at **https://marvis.web.app**.

A dependency-free static site generator: Node 20, ES modules, zero npm packages. The build reads a
committed snapshot of a GitHub "master record" and renders 38 routes, then a validator gates the
output on links, SEO, and contact policy before anything reaches Firebase Hosting.

## Why it exists

The portfolio is generated, not hand-written. Facts about projects come from
`hamids-ai-automations/github-profile-master-record` (`MASTER_DATABASE.json`), so the site cannot
drift from the repositories it describes. A daily workflow refreshes the snapshot, and any change to
the record hash triggers a rebuild and deploy.

## Page inventory

| Section | Routes |
| --- | --- |
| Home | `/` |
| Work index | `/projects/` |
| Projects | 19 curated case pages (`/projects/<slug>/`) |
| Writing index | `/articles/` |
| Articles | 4 long-form pieces (`/articles/<slug>/`) |
| Services index | `/services/` |
| Services | 6 offers (`/services/<slug>/`) |
| About / Contact | `/about/`, `/contact/` |
| Legal | `/privacy/`, `/terms/` |
| Machine surfaces | `/sitemap.xml` (35 URLs), `/robots.txt`, `/llms.txt`, `/data/projects.json`, `/site.webmanifest`, `/404.html` |

## Quick start

```bash
npm run build      # render dist/
npm run validate   # gate the output
npm test           # 30 unit tests
npm run serve      # preview at http://localhost:5000 with Firebase-like routing
npm run ci         # build + validate + test — run before every push
```

No install step is required: the project has no dependencies.

## Structure

```
data/          committed snapshot of the master record (source of truth)
scripts/       sync, build entry, validate gate, local server
src/lib/       data parsing, normalisation, model, layout, SEO, markdown
src/pages/     one renderer per page family
src/content/   site copy, services, articles, curated project overrides
src/templates/ cards and shared components
src/styles.css the entire stylesheet
tests/         node:test suites
dist/          generated output (never edit)
```

## Content rules

- Every project claim traces to the master record or to a curated override that restates a verified
  field from it.
- WhatsApp `+923167417135` is the only contact channel: no forms, no email links, no phone-call CTAs.
- Every page carries a unique title, a unique meta description, a canonical URL, exactly one `<h1>`,
  JSON-LD where applicable, and a WhatsApp CTA.
- Forks, the profile-README repository, and repositories without a description or README are never
  published. Homepages that point back at this site or at the repository itself are dropped.
- Content works without JavaScript.

## Deployment

Firebase Hosting, site `marvis`, project `my-1st-web-app-ef52d` (Spark plan, hosting only).

```bash
npm run deploy           # ci + deploy --only hosting:marvis
npm run deploy:preview   # 7-day preview channel
```

CI/CD lives in `.github/workflows/`: `ci.yml` (build/validate/test), `deploy.yml` (live deploy on
push to `main`), `sync-master-record.yml` (daily snapshot refresh), `live-check.yml` (weekly
production smoke test). The deploy workflow needs the `FIREBASE_SERVICE_ACCOUNT` secret — see
[docs/OPERATIONS.md](https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/docs/OPERATIONS.md).

## Documentation

| Document | Contents |
| --- | --- |
| [docs/ARCHITECTURE.md](https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/docs/ARCHITECTURE.md) | Layers, data flow, inclusion rules, routing, invariants |
| [docs/OPERATIONS.md](https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/docs/OPERATIONS.md) | Commands, deploy and rollback, CI secrets, troubleshooting |
| [docs/AUTONOMY.md](https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/docs/AUTONOMY.md) | Standing authorization for autonomous work in this repo |
| [AGENTS.md](https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/AGENTS.md) | Hard facts and rules for agents and contributors |

## Contact

WhatsApp: [+92 316 7417135](https://wa.me/923167417135) — the only contact channel.

## License

UNLICENSED — private project. All rights reserved.

```
