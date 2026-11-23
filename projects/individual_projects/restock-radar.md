# restock-radar

**Overview:** Shopify app for back-in-stock alerts and preorder recovery

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/restock-radar](https://github.com/hamids-ai-automations/restock-radar) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-26 |
| Last update | 2026-11-20 |
| Last push | 2026-11-21 |
| Default branch | main |
| License | MIT |
| Primary language | JavaScript |
| Stars / Forks / Watchers | 1 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 42 KB |
| Topics | back-in-stock, ecommerce, nodejs, notifications, shopify, javascript |

## Objectives

# Restock Radar

## Features

- 🔔 **Back-in-Stock Alerts** — Notify customers when out-of-stock products return to inventory
- 🔄 **Preorders** — Allow customers to pre-order unavailable products
- 📊 **Analytics** — Track subscribers, notifications, click-through rates, and attributed orders
- ✉️ **Custom Email Templates** — Brand your restock notification emails

## Technical architecture

- **Top-level directories:** app, docs, models, prisma
- **Total files (tracked in default branch):** 28
- **CI workflows:** none detected
- **Test files detected:** 1

## Languages and technologies

| Language | Bytes |
| --- | --- |
| JavaScript | 36749 |
| TypeScript | 327 |

**Frameworks / libraries detected:** React

**Dependencies:** @prisma/client, @remix-run/dev, @remix-run/node, @remix-run/react, @remix-run/serve, @shopify/app, @shopify/cli, @shopify/polaris, @shopify/shopify-api, @types/react, @types/react-dom, isbot, prisma, react, react-dom, typescript, vite, vitest

## Important source files

- `package.json`

## Installation and setup

```bash

## Deployment

No deployment configuration detected.

## Documentation links

- https://your-app-url.com
- https://fly.io
- https://railway.app
- https://vercel.com
- https://restock-radar.example.com

## Development status

Active — last push 2026-11-21

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/pinvault-pinterest-downloader
- hamids-ai-automations/volparossa-code
- hamids-ai-automations/dayjs

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/restock-radar/blob/main/README.md

```markdown
# Restock Radar

A Shopify app that helps merchants recover lost sales from stockouts via back-in-stock alerts and preorders.

## Features

- 🔔 **Back-in-Stock Alerts** — Notify customers when out-of-stock products return to inventory
- 🔄 **Preorders** — Allow customers to pre-order unavailable products
- 📊 **Analytics** — Track subscribers, notifications, click-through rates, and attributed orders
- ✉️ **Custom Email Templates** — Brand your restock notification emails

## Architecture

```
restock-radar/
├── app/
│   ├── components/
│   │   ├── NotifyButton.jsx       # Storefront notify button
│   │   └── PolarisProvider.jsx    # Polaris theme provider
│   ├── models/
│   │   ├── dashboard.server.jsx   # Dashboard stats
│   │   ├── subscriber.server.jsx  # Subscriber CRUD
│   │   ├── shop.server.jsx        # Shop settings
│   │   └── restock-event.server.jsx # Restock tracking
│   ├── routes/
│   │   ├── app._index.jsx         # Main dashboard
│   │   ├── app.subscribers.jsx    # Subscriber list + export
│   │   ├── app.settings.jsx       # Settings + email template
│   │   └── api.webhooks.jsx       # Webhook handlers
│   ├── shopify.server.jsx         # OAuth + API config
│   └── root.jsx                    # Remix root
├── prisma/
│   └── schema.prisma               # Database schema
├── extensions/
│   └── restock-notify/            # Shopify app extension
│       └── blocks/
│           └── notify-button/
├── package.json
├── shopify.app.toml
└── remix.config.js
```

## Quick Start

### Prerequisites

- Node.js 18+
- Shopify Partner account
- Development store

### Setup

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env

# Set your Shopify credentials
SHOPIFY_API_KEY=your_api_key
SHOPIFY_API_SECRET=your_api_secret
SHOPIFY_APP_URL=https://your-app-url.com
DATABASE_URL=file:./dev.db

# Start the dev server
npm run dev
```

### Environment Variables

```env
SHOPIFY_API_KEY=your_api_key
SHOPIFY_API_SECRET=your_api_secret
SHOPIFY_APP_URL=https://your-app-url.com
SHOPIFY_APP_SHOPIFY_EMAIL=admin@example.com
SHOPIFY_APP_BOT_USERNAME=your-bot-username
DATABASE_URL="file:./dev.db"

SENDGRID_API_KEY=your_sendgrid_key
TWILIO_API_KEY=your_twilio_key
```

## Deployment

### Shopify App Deployment

1. `npm run prepare:app`
2. Deploy via Shopify CLI:
   ```bash
   npm run deploy
   ```

### Custom Hosting

The app can be deployed to any Node.js host that supports Remix:

- [Fly.io](https://fly.io)
- [Railway](https://railway.app)
- [Vercel](https://vercel.com)

### Environment Variables

| Variable | Description |
|----------|-------------|
| SHOPIFY_API_KEY | Your Shopify app API key |
| SHOPIFY_API_SECRET | Your Shopify app API secret |
| SHOPIFY_APP_URL | Your app URL (e.g., https://restock-radar.example.com) |
| DATABASE_URL | Database connection string |
| SENDGRID_API_KEY | Email sending API key |
| TWILIO_API_KEY | SMS sending API key |

## Development

### Running Dev Server

```bash
npm run dev
```

### Testing

```bash
npm run test
```

## App Store Requirements

- Secure authentication and least-privilege access ✓
- Proper tenant isolation ✓
- Input validation and error handling ✓
- Rate-limit handling and webhook verification ✓
- Reliable data storage where required ✓
- Privacy and data deletion workflows ✓
- Automated tests and development-store testing ✓
- Clear installation and troubleshooting documentation ✓
- No exposed API keys or credentials ✓

## License

MIT
```
