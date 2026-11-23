# dynamic-schema-generator

**Overview:** Dynamic Schema Generator for WordPress: Automated, accurate JSON-LD Schema.org structured data engine with Elementor integration.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/dynamic-schema-generator](https://github.com/hamids-ai-automations/dynamic-schema-generator) |
| Live website | https://hamid-resume.web.app/ |
| Visibility | public |
| Status | active |
| Creation date | 2026-10-18 |
| Last update | 2026-10-18 |
| Last push | 2026-11-21 |
| Default branch | main |
| License | MIT |
| Primary language | PHP |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 1 |
| Contributors | 2 |
| Size | 60 KB |
| Topics | elementor, faq-schema, geo, json-ld, local-seo, martech, php, schema, seo, structured-data, wordpress, wordpress-plugin |

## Objectives

<h1 align="center">Dynamic Schema Generator for WordPress</h1>
<h3 align="center">Automated, Production-Grade JSON-LD Schema.org Structured Data Engine with Elementor Integration</h3>

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, admin, includes, languages, tests
- **Total files (tracked in default branch):** 45
- **CI workflows:** .github/workflows/ci.yml
- **Test files detected:** 9

## Languages and technologies

| Language | Bytes |
| --- | --- |
| PHP | 158198 |
| CSS | 4035 |
| JavaScript | 3721 |

**Frameworks / libraries detected:** none detected from dependency files

**Dependencies:** none detected

## Important source files

- `docker-compose.yml`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://hamid-resume.web.app/

## Documentation links

- https://hamid-resume.web.app
- https://wordpress.org
- https://www.php.net
- https://schema.org
- https://wa.me/923167417135?text=Hello%20Hamid%2C%20I%20saw%20your%20Dynamic%20Schema%20Generator%20plugin%20on%20GitHub%20and%20would%20like%20to%20discuss%20a%20project%20or%20job%20opportunity
- http://localhost:8080
- https://wa.me/923167417135?text=Hello%20Hamid%2C%20I%20reviewed%20Dynamic%20Schema%20Generator%20and%20would%20like%20to%20discuss%20an%20enterprise%20SEO%20and%20Schema%20consulting%20project

## Development status

Active — last push 2026-11-21

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 1

## Related projects

- hamids-ai-automations/gohighlevel-php-sdk
- hamids-ai-automations/OpnForm

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/dynamic-schema-generator/blob/main/README.md

```markdown
<h1 align="center">Dynamic Schema Generator for WordPress</h1>
<h3 align="center">Automated, Production-Grade JSON-LD Schema.org Structured Data Engine with Elementor Integration</h3>

<p align="center">
  <a href="https://github.com/hamid-digitalmarketer/dynamic-schema-generator/actions"><img src="https://img.shields.io/badge/CI-Passing-2ea44f?style=for-the-badge&logo=githubactions&logoColor=white" alt="CI Status"></a>
  <a href="https://wordpress.org/"><img src="https://img.shields.io/badge/WordPress-5.8%20to%206.7+-21759b?style=for-the-badge&logo=wordpress&logoColor=white" alt="WordPress Compatibility"></a>
  <a href="https://www.php.net/"><img src="https://img.shields.io/badge/PHP-7.4%20|%208.0%20|%208.1%20|%208.2%20|%208.3-777bb4?style=for-the-badge&logo=php&logoColor=white" alt="PHP Versions"></a>
  <a href="https://schema.org/"><img src="https://img.shields.io/badge/Data%20Format-JSON--LD%20@graph-f59e0b?style=for-the-badge" alt="JSON-LD Format"></a>
  <a href="https://wa.me/923167417135?text=Hello%20Hamid%2C%20I%20saw%20your%20Dynamic%20Schema%20Generator%20plugin%20on%20GitHub%20and%20would%20like%20to%20discuss%20a%20project%20or%20job%20opportunity."><img src="https://img.shields.io/badge/WhatsApp-Contact%20Author-25d366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp Consultation"></a>
</p>

---

## 📌 Executive Overview

**Dynamic Schema Generator** (`dynamic-schema-generator`) is an enterprise-grade, object-oriented WordPress plugin engineered by **Muhammad Hamid** (Digital Marketing Head & MarTech Engineer). It automatically generates accurate, interconnected **Schema.org JSON-LD** structured data directly from WordPress content, landing pages, and **Elementor** layouts.

### The Problem It Solves
1. **AI-Generated Content Saturation:** Search engines (Google, Bing) and AI answer models (Gemini, ChatGPT, Perplexity) struggle to separate authentic business entities from synthetic spam. Structured, linked Knowledge Graphs enable crawlers to unambiguously verify who you are, what services you provide, and what questions you answer.
2. **Zero-Click Searches:** Rich snippets and AI Overviews summarize answers directly in SERPs. Structured data provides verified entity anchors without hallucinations.
3. **Bloatware in Legacy SEO Plugins:** Unlike bulky SEO suites that inject render-blocking scripts, heavy CSS, or vendor ads, Dynamic Schema Generator focuses exclusively on high-precision structured data with zero frontend runtime overhead.

> **Important SEO Reality Check:** Valid structured data improves machine readability and eligibility for search engine features. Search engines decide independently how and when to display rich snippets or cite pages in AI Overviews. Dynamic Schema Generator never promises guaranteed rankings or rich snippet placements.

---

## ⚡ Core Features

```
+-----------------------------------------------------------------------------------+
|                        Dynamic Schema Generator Engine                            |
+-----------------------------------------------------------------------------------+
            |                                           |
            v                                           v
[ Standard WordPress Content ]                 [ Elementor Layouts ]
  • Posts & Pages                              • Post Document Tree Traversal
  • Hierarchical Categories                    • Accordion Widgets -> FAQPage
  • Post Authors -> Person                     • Toggle Widgets    -> FAQPage
  • Featured Images -> ImageObject             • Heading Widgets   -> Section Outline
            |                                           |
            +---------------------+---------------------+
                                  |
                                  v
                    +---------------------------+
                    |  Schema.org Graph Builder |
                    +---------------------------+
                      • Organization / LocalBusiness (#organization)
                      • WebSite (#website) + SearchAction
                      • WebPage (#webpage) + BreadcrumbList (#breadcrumb)
                      • Article / BlogPosting (#article)
                      • Service (#service) + Offers & Pricing
                      • FAQPage (#faq)
                                  |
                                  v
                    +---------------------------+
                    |   In-House Validator      |
                    |   Syntax, @ids, Types     |
                    +---------------------------+
                                  |
                                  v
                    +---------------------------+
                    |   Clean JSON-LD Output    |
                    |   Injected into <head>    |
                    +---------------------------+
```

### 1. Interconnected Schema `@graph` Architecture
Generates a consolidated `@graph` array linking entities via persistent `#` URIs:
- **`Organization` / `LocalBusiness`:** Brand identity, legal name, telephone, email, physical address (`PostalAddress`), geographic coordinates (`GeoCoordinates`), opening hours (`OpeningHoursSpecification`), and authoritative social profiles (`sameAs`).
- **`WebSite`:** Site entity with `SearchAction` potentialAction for Google sitelinks search box.
- **`WebPage`:** Page entity linked to site hierarchy, authors, and canonical URLs.
- **`BreadcrumbList`:** Hierarchical navigation trail with numerical `ListItem` positions.
- **`Article` / `BlogPosting`:** Headline, datePublished, dateModified, author (`Person`), and featured image (`ImageObject`).
- **`Service`:** Mapped landing page service offerings, category, provider link, and explicit pricing (`Offer`).
- **`FAQPage`:** Question and answer pairs extracted from manual post configuration or Elementor widgets.

### 2. Dedicated Elementor Integration Layer
- **Non-Invasive Tree Traversal:** Directly reads `_elementor_data` document structures without DOM rendering penalties.
- **Automatic FAQ Extraction:** Converts `accordion` and `toggle` widgets into Schema.org `FAQPage` markup.
- **Heading Outline Inspection:** Extracts `heading` widgets for section context.
- **Zero-Dependency Fallback:** If Elementor is inactive or missing, the plugin operates smoothly on standard WordPress content without throwing errors.

### 3. Business Information & Local SEO Manager
Full management interface under **Dynamic Schema > Business Info**:
- 12 supported business types: `Organization`, `LocalBusiness`, `ProfessionalService`, `LegalService`, `MedicalBusiness`, `FinancialService`, `Store`, etc.
- Precision geographic latitude and longitude for Google Maps and Local 3-Pack proximity.
- Sanitized `sameAs` array for knowledge graph establishment across LinkedIn, X, GitHub, and corporate directories.

### 4. Service Schema Builder & Page Mapping
- Map specific services to dedicated landing pages.
- Optional, honest pricing: prices are only emitted when explicitly supplied by the administrator. Never fabricates estimates or pricing ranges.

### 5. In-House Schema Preview & Validator
- Select any published post or the global homepage to inspect the live generated JSON-LD.
- Real-time linting detects missing required properties, invalid `@context`, duplicate `@id`s, or malformed JSON syntax.
- One-click copy and direct links to the **Google Rich Results Test** and **Schema.org Validator**.

### 6. Conflict Safeguards & Diagnostics
- Detects existing active installations of **Yoast SEO**, **Rank Math**, **All in One SEO (AIOSEO)**, and **SEOPress**.
- Provides duplicate-output suppression and post-level exclusion checkboxes.

---

## 🗂️ Technical Directory Structure

```
dynamic-schema-generator/
├── dynamic-schema-generator.php     # Main bootstrap & autoloader
├── uninstall.php                    # Safe uninstaller with clean option
├── readme.txt                       # WordPress.org plugin directory specificati
```
