# nexgen-financial-experts

**Overview:** NexGen Financial Experts — Next.js 16 marketing website (rebuilt from recovered WordPress content)

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/nexgen-financial-experts](https://github.com/hamids-ai-automations/nexgen-financial-experts) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-31 |
| Last update | 2026-11-21 |
| Last push | 2026-11-21 |
| Default branch | main |
| License | MIT |
| Primary language | TypeScript |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 3984 KB |
| Topics | marketing-website, nextjs, prisma, shadcn-ui, tailwindcss, typescript |

## Objectives

# NexGen Financial Experts — Website

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .zscripts, deploy, download, evidence, examples, mini-services, prisma, public, scripts, src, tests
- **Total files (tracked in default branch):** 172
- **CI workflows:** none detected
- **Test files detected:** 5

## Languages and technologies

| Language | Bytes |
| --- | --- |
| TypeScript | 338980 |
| HTML | 318364 |
| Shell | 34942 |
| PHP | 6962 |
| Python | 5190 |
| CSS | 5155 |
| JavaScript | 1713 |

**Frameworks / libraries detected:** Next.js, React, Tailwind CSS

**Dependencies:** @dnd-kit/core, @dnd-kit/sortable, @dnd-kit/utilities, @hookform/resolvers, @mdxeditor/editor, @prisma/client, @radix-ui/react-accordion, @radix-ui/react-alert-dialog, @radix-ui/react-aspect-ratio, @radix-ui/react-avatar, @radix-ui/react-checkbox, @radix-ui/react-collapsible, @radix-ui/react-context-menu, @radix-ui/react-dialog, @radix-ui/react-dropdown-menu, @radix-ui/react-hover-card, @radix-ui/react-label, @radix-ui/react-menubar, @radix-ui/react-navigation-menu, @radix-ui/react-popover, @radix-ui/react-progress, @radix-ui/react-radio-group, @radix-ui/react-scroll-area, @radix-ui/react-select, @radix-ui/react-separator, @radix-ui/react-slider, @radix-ui/react-slot, @radix-ui/react-switch, @radix-ui/react-tabs, @radix-ui/react-toast, @radix-ui/react-toggle, @radix-ui/react-toggle-group, @radix-ui/react-tooltip, @reactuses/core, @tailwindcss/postcss, @tanstack/react-query, @tanstack/react-table, @types/nodemailer, @types/react, @types/react-dom, bun-types, class-variance-authority, clsx, cmdk, date-fns, embla-carousel-react, eslint, eslint-config-next, framer-motion, input-otp, lucide-react, next, next-auth, next-intl, next-themes, nodemailer, prisma, react, react-day-picker, react-dom

## Important source files

- `package.json`
- `tsconfig.json`

## Installation and setup

```bash
bun install          # or npm install
cp .env.example .env # adjust if needed (SMTP optional)
bun run db:push      # create SQLite schema
bun run dev          # http://localhost:3000
```

Production:

```bash
bun run build && bun run start
```

## Deployment

No deployment configuration detected.

## Documentation links

- http://localhost:3000
- https://nexgenfinancialexperts.com

## Development status

Active — last push 2026-11-21

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/marvis-portfolio
- hamids-ai-automations/firebase-ai-starter-kit
- hamids-ai-automations/ghl-servicepro-theme
- hamids-ai-automations/servicenow-ultimate-mcp
- hamids-ai-automations/shopify-growth-mcp

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/nexgen-financial-experts/blob/main/README.md

```markdown
# NexGen Financial Experts — Website

Production rebuild of https://nexgenfinancialexperts.com after an SEO-spam compromise of the original WordPress site. Next.js 16 (App Router) + TypeScript + Tailwind CSS 4 + shadcn/ui + Prisma (SQLite).

**Business:** NexGen Financial Experts — accounting, tax, audit & business advisory, Fort Lauderdale, FL.
**Contact:** +1 (954) 306-3823 · WhatsApp +1 (954) 770-1568 · paudalus@nexgenfinancialexperts.com · 1975 East Sunrise Blvd, Suite 705, Fort Lauderdale, FL 33304

---

## Pages

| Route | Purpose |
|---|---|
| `/` | Home: hero, 6 service pillars, industries, why-us, featured services, about teaser, testimonials, FAQs, CTA |
| `/about` | Firm story, mission, values |
| `/services` | Services hub (12 cards) |
| `/services/[slug]` | 12 service landing pages (all original WP slugs preserved) |
| `/insights` + `/insights/[slug]` | Blog hub + 3 educational articles |
| `/contact` | Working form + NAP + map |
| `/privacy-policy`, `/terms-of-use` | Legal drafts (flagged for review) |
| 404 | Custom recovery page |
| `/sitemap.xml`, `/robots.txt` | Auto-generated; 301s from legacy URLs (`/aboutus`, `/blog`, `/home`) |
| `POST /api/contact` | Validated contact endpoint (rate limit + honeypot + time trap; stores to DB; optional SMTP email) |

## Quick Start

```bash
bun install          # or npm install
cp .env.example .env # adjust if needed (SMTP optional)
bun run db:push      # create SQLite schema
bun run dev          # http://localhost:3000
```

Production:

```bash
bun run build && bun run start
```

## Environment

See `.env.example`. Only `DATABASE_URL` is required; SMTP variables enable contact-form email delivery. Never commit real secrets.

## Key Files

```
src/lib/site.ts        — NAP config, nav, redirects (single source of truth)
src/lib/services.ts    — all 12 service definitions + SEO metadata
src/lib/articles.ts    — educational articles
src/components/site/   — header, footer, forms, shared blocks
src/app/api/contact/   — secure contact endpoint
prisma/schema.prisma   — ContactSubmission model
public/images/         — official logo, favicon set, hero image
```

## Design System

- Brand colors sampled from the official logo: magenta `#C01040`, blue `#4090D0`, navy `#0B1F3A`, white.
- Fonts: Inter (body), Source Serif 4 (display headings) via `next/font`.
- Logo: `public/images/nexgen-logo.png` (recovered from the official domain). Favicon derived from the logo mark at `src/app/icon.png`.

## Security Notes

- Original WordPress site was compromised (hidden casino-link widgets + spam posts — see `download/docs/security-audit.md`). This rebuild contains no WordPress code path.
- Contact form: server-side validation, per-IP rate limiting (5/10 min), honeypot + time-trap, no PII in URLs, data stored only in the DB (email optional via SMTP).
- Security headers configured in `next.config.ts` (CSP, frame-options, nosniff, referrer/permissions policy).

## Documentation

Full project deliverables (audit, security, competitor research, keyword map, content & marketing strategy, QA, deployment, recovery checklist, analytics, 90-day roadmap) live in **`download/docs/`**.

```
