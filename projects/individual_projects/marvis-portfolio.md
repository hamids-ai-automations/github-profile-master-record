# marvis-portfolio

**Overview:** Automated GitHub-driven portfolio for Muhammad Hamid — AI Automation Engineer. Static site generated from github-profile-master-record and deployed to Firebase Hosting.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/marvis-portfolio](https://github.com/hamids-ai-automations/marvis-portfolio) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-11-25 |
| Last update | 2026-11-26 |
| Last push | 2026-11-27 |
| Default branch | main |
| License | none declared |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 1 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 2 |
| Size | 873 KB |
| Topics | - |

## Objectives

# Marvis Portfolio — Muhammad Hamid

## Features

- **Every page is a landing page** — unique title, meta description, canonical URL, OG/Twitter cards, exactly one H1, WhatsApp CTA.
- **Structured data** — JSON-LD: Person, WebSite, ProfilePage, BreadcrumbList, FAQPage, Service, BlogPosting, SoftwareSourceCode, ContactPage.
- **Machine surface** — `sitemap.xml` and `robots.txt` generated from the same data as the pages, `llms.txt` for AI crawlers, manifest, custom 404.
- **Enforced, not promised** — a dependency-free validation gate (`scripts/validate.mjs`) checks the built `out/`: metadata uniqueness, canonicals, single H1, OG tags, WhatsApp presence, internal link resolution, sitemap↔page match. Exit 1 blocks deploy.
- **Fast by default** — fully static HTML, self-hosted fonts with `font-display: swap`, ~zero CLS.
- **Secure headers** — strict CSP, nosniff, frame protection, referrer policy; no forms, no external scripts.

## Technical architecture

- **Top-level directories:** .github, data, docs, public, scripts, src
- **Total files (tracked in default branch):** 112
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/firebase-deploy.yml, .github/workflows/live-check.yml, .github/workflows/sync-master-record.yml
- **Test files detected:** 0

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 374544 |
| JavaScript | 12549 |
| CSS | 6369 |

**Frameworks / libraries detected:** Firebase, MCP, Next.js, React, Tailwind CSS

**Dependencies:** @radix-ui/react-accordion, @radix-ui/react-dialog, @radix-ui/react-navigation-menu, @radix-ui/react-select, @tailwindcss/postcss, @types/react, @types/react-dom, bun-types, class-variance-authority, clsx, eslint, eslint-config-next, framer-motion, lucide-react, next, next-themes, react, react-dom, react-markdown, sharp, tailwind-merge, tailwindcss, tw-animate-css, typescript

## Important source files

- `.firebaserc`
- `firebase.json`
- `package.json`
- `tsconfig.json`

## Installation and setup

```bash
git clone https://github.com/hamids-ai-automations/marvis-portfolio.git
cd marvis-portfolio
bun install
bun run dev        # http://localhost:3000
bun run ci         # lint → typecheck → og → build:export → validate — run before every push
```

## Deployment

No deployment configuration detected.

## Documentation links

- https://marvis.web.app
- https://wa.me/923167417135
- http://localhost:3000

## Development status

Active — last push 2026-11-27

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

Full README: https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/README.md

```markdown
# Marvis Portfolio — Muhammad Hamid

> **AI Automation Engineer | Gemini Developer | AI Agent Builder | GoHighLevel Automation Developer**

[![Deploy to Firebase Hosting](https://github.com/hamids-ai-automations/marvis-portfolio/actions/workflows/firebase-deploy.yml/badge.svg)](https://github.com/hamids-ai-automations/marvis-portfolio/actions/workflows/firebase-deploy.yml)
[![CI](https://github.com/hamids-ai-automations/marvis-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/hamids-ai-automations/marvis-portfolio/actions/workflows/ci.yml)

**Live site: <https://marvis.web.app>** — the personal portfolio of **Muhammad Hamid** (Lahore, Pakistan).

This repository is the single source of truth for the site: every push to `main` that changes site files runs the full quality gate (lint → typecheck → OG generation → static export → SEO/link validation) and, if the checks pass, deploys itself to Firebase Hosting and verifies the live URLs.

> **Screenshots:** coming soon — binaries can't be committed from every environment; capture and add them to the README per [NEXT_STEPS.md](https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/docs/NEXT_STEPS.md) #5.

## What this is

A **Next.js 16 static export** — no server runtime, no database, no client-side data fetching. The site presents 46 indexable URLs:

- **10 service landing pages** — AI automation, AI agent development, Gemini development, LLM development, AI integration, MCP development, GoHighLevel automation, marketing technology, Python automation, AI security — each with benefits, use cases, process, evidence, FAQ, and structured data.
- **19 project case pages** — real open-source repositories (98 public repos on [GitHub](https://github.com/hamids-ai-automations)), with facts curated from the GitHub API (frozen 2026-11-25). No invented clients, testimonials, or metrics.
- **14 technical articles** — long-form, internally linked, funneling readers to the matching services.
- Home, about, contact, privacy, terms — every existing URL from the previous site preserved, with all legacy 301 redirects kept.

**Conversion is WhatsApp-only:** contextual CTAs throughout, plus a client-side project brief builder on the contact page that opens `wa.me` with a prefilled message. Nothing is stored, nothing is sent — enforced by CSP `form-action 'none'`.

## Technology stack

| Layer | Technology |
| --- | --- |
| Framework | Next.js 16 (App Router) + React 19, static export (`NEXT_OUTPUT=export`) |
| Language | TypeScript |
| Styling | Tailwind CSS 4 + shadcn/ui (Radix primitives) |
| Animation | framer-motion |
| Theming | next-themes (dark-first emerald-on-charcoal, light mode) |
| Content | react-markdown, typed content model in `src/data/` |
| Fonts | Space Grotesk / Inter / JetBrains Mono — self-hosted via `next/font` |
| Icons | lucide-react |
| Build/OG | sharp (rasterizes committed SVG → `og.png` 1200×630 + touch icon) |
| Tooling | Bun (`bun.lock`), ESLint, `tsc` |
| Hosting | Firebase Hosting — site `marvis`, project `my-1st-web-app-ef52d` (Spark plan) |

## Features

- **Every page is a landing page** — unique title, meta description, canonical URL, OG/Twitter cards, exactly one H1, WhatsApp CTA.
- **Structured data** — JSON-LD: Person, WebSite, ProfilePage, BreadcrumbList, FAQPage, Service, BlogPosting, SoftwareSourceCode, ContactPage.
- **Machine surface** — `sitemap.xml` and `robots.txt` generated from the same data as the pages, `llms.txt` for AI crawlers, manifest, custom 404.
- **Enforced, not promised** — a dependency-free validation gate (`scripts/validate.mjs`) checks the built `out/`: metadata uniqueness, canonicals, single H1, OG tags, WhatsApp presence, internal link resolution, sitemap↔page match. Exit 1 blocks deploy.
- **Fast by default** — fully static HTML, self-hosted fonts with `font-display: swap`, ~zero CLS.
- **Secure headers** — strict CSP, nosniff, frame protection, referrer policy; no forms, no external scripts.

## Page inventory (46 routes)

| Section | Routes |
| --- | --- |
| Home | `/` |
| About / Contact | `/about/`, `/contact/` (project brief → WhatsApp handoff, no storage) |
| Services index | `/services/` |
| Services | 10 landing pages — `/services/ai-automation/`, `/services/ai-agent-development/`, `/services/gemini-development/`, `/services/llm-development/`, `/services/ai-integration/`, `/services/mcp-development/`, `/services/gohighlevel-automation/`, `/services/marketing-technology/`, `/services/python-automation/`, `/services/ai-security/` |
| Projects index | `/projects/` |
| Projects | 19 case pages — `/projects/<repo-slug>/` (shopify-growth-mcp, servicenow-ultimate-mcp, google-services-mcp, gemini-agent-reliability-kit, gemini-agent-automation-toolkit, ai-agent-testing-lab, ghl-automation-engine, ghl-devops-toolkit, leadflow-sentinel, firebase-ai-starter-kit, conversionbridge, ppc-waste-detector, meta-lead-quality-analyzer, ai-search-visibility-auditor, geo-visibility-lab, envscope, searchpulse-ai, conversion-tracking-doctor, sarif-verify) |
| Articles index | `/articles/` |
| Articles | 14 long-form pieces — `/articles/<slug>/` (10 migrated with URLs preserved, 4 new) |
| Legal | `/privacy/`, `/terms/` |
| Machine surfaces | `/sitemap.xml`, `/robots.txt`, `/llms.txt`, `/manifest.webmanifest`, `/404.html` |

## Quick start

```bash
git clone https://github.com/hamids-ai-automations/marvis-portfolio.git
cd marvis-portfolio
bun install
bun run dev        # http://localhost:3000
bun run ci         # lint → typecheck → og → build:export → validate — run before every push
```

## Project structure

```
src/app/            App Router routes (page.tsx, layout.tsx, about/ contact/
                    services/[slug]/ projects/[slug]/ articles/[slug]/ privacy/ terms/,
                    not-found.tsx, sitemap.ts, robots.ts, manifest.ts, globals.css)
src/components/site/ header, footer, cards, faq, breadcrumbs, markdown, json-ld,
                    whatsapp-cta, brief-builder, section, reveal, theme-*,
                    service-icon, legal-page
src/components/ui/  shadcn components in use: accordion, badge, button, card,
                    navigation-menu, select, sheet, textarea
src/lib/            site.ts (config/facts), types.ts (content model),
                    seo.ts (metadata builder), utils.ts
src/data/           projects.ts (19), services/ (10 + index),
                    articles/ (14 + index), legal.ts
public/             favicon.svg, llms.txt (og.png + apple-touch-icon.png are
                    generated at build time — gitignored)
scripts/            generate-og.mjs, validate.mjs
docs/               full documentation set
```

## SEO implementation

- Unique metadata per page via the Next.js Metadata API (`src/lib/seo.ts`): title, description, canonical, Open Graph, Twitter cards.
- 9 JSON-LD types with verified facts only; visible breadcrumbs mirrored by `BreadcrumbList`.
- `sitemap.xml` / `robots.txt` generated from the same data modules that render the pages.
- All 36 legacy 301 redirects preserved; all migrated article URLs unchanged.
- One H1 per page, semantic HTML, crawlable navigation — all enforced by the validation gate.

Details: [docs/SEO_IMPLEMENTATION.md](https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/docs/SEO_IMPLEMENTATION.md) · Keyword targeting: [docs/SEO_KEYWORD_MAP.md](https://github.com/hamids-ai-automations/marvis-portfolio/blob/main/docs/SEO_KEYWORD_MAP.md)

## Automated deployment

```
push to main → GitHub Actions → bun install → lint → typecheck → generate OG
             → next build (static export) → validate out/ → deploy to Firebase
             Hosting "marvis" → verify live URLs → summary
```

- Deploy credentials live in GitHub Actions secrets only — Workload Identity Federation (`WIF_PROVIDER` + `WIF_SERVICE_ACCOUNT`, preferred) or a service-account JSON (`FIREBASE_SERVICE_ACCOUNT`). With neither set, the build is still validated and deploy is skipped with a noti
```
