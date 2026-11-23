# gohighlevel-php-sdk

**Overview:** php sdk for gohighlevel api.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/gohighlevel-php-sdk](https://github.com/hamids-ai-automations/gohighlevel-php-sdk) |
| Live website | https://musheabdulhakim.github.io/gohighlevel-php-sdk/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-22 |
| Last update | 2026-11-22 |
| Last push | 2026-11-22 |
| Default branch | master |
| License | MIT |
| Primary language | PHP |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 2 |
| Size | 566 KB |
| Topics | - |

## Objectives

<div align="center">
<img src="art/sdk-art.jpg" height="100" alt="GoHighLevel PHP">
    <p align="center">
        <a href="https://github.com/MusheAbdulHakim/gohighlevel-php-sdk/actions"><img alt="GitHub Workflow Status (master)" src="https://github.com/MusheAbdulHakim/gohighlevel-php-sdk/actions/workflows/tests.yml/badge.svg"></a>
        <a href="https://packagist.org/packages/musheabdulhakim/gohighlevel-php"><img alt="Total Downloads" src="https://img.shields.io/packagist/dt/musheabdulhakim/gohighlevel-php"></a>
        <a href="https://packagist.org/packages/musheabdulhakim/gohighlevel-ph

## Features

* **100% PSR-compatible**: The SDK adheres to PSR standards, including PSR-18 for HTTP clients, making it compatible with any modern PHP framework.
  * **Type-Safe & Predictable**: Written in PHP 8.1 with `strict_types`, the code is reliable and predictable.
  * **Powerful Factory**: The `Factory` class gives you full control over the client's configuration, allowing you to set custom headers, API versions, and HTTP clients.
  * **Comprehensive Resource Coverage**: Access all major GoHighLevel API resources through dedicated, logical methods (e.g., `->contacts()`, `->businesses()`, `->workflows()`).

## Technical architecture

- **Top-level directories:** .github, art, docs, src, tests
- **Total files (tracked in default branch):** 235
- **CI workflows:** .github/workflows/formats.yml, .github/workflows/tests.yml
- **Test files detected:** 62

## Languages and technologies

| Language | Bytes |
| --- | --- |
| PHP | 403879 |

**Frameworks / libraries detected:** none detected from dependency files

**Dependencies:** none detected

## Important source files

- none of the well-known entry/config files detected

## Installation and setup

You can install the SDK via Composer.

```bash
composer require musheabdulhakim/gohighlevel-php-sdk
```

## Deployment

Firebase/other hosting declared via homepage field: https://musheabdulhakim.github.io/gohighlevel-php-sdk/

## Documentation links

- https://musheabdulhakim.github.io/gohighlevel-php-sdk
- https://packagist.org/packages/musheabdulhakim/gohighlevel-php
- https://highlevel.stoplight.io/docs/integrations/0443d7d1a4bd0-overview
- https://custom-api-endpoint.com
- https://services.leadconnectorhq.com/oauth/token
- https://pestphp.com

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/dynamic-schema-generator
- hamids-ai-automations/OpnForm

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/gohighlevel-php-sdk/blob/master/README.md

```markdown
<div align="center">
<img src="art/sdk-art.jpg" height="100" alt="GoHighLevel PHP">
    <p align="center">
        <a href="https://github.com/MusheAbdulHakim/gohighlevel-php-sdk/actions"><img alt="GitHub Workflow Status (master)" src="https://github.com/MusheAbdulHakim/gohighlevel-php-sdk/actions/workflows/tests.yml/badge.svg"></a>
        <a href="https://packagist.org/packages/musheabdulhakim/gohighlevel-php"><img alt="Total Downloads" src="https://img.shields.io/packagist/dt/musheabdulhakim/gohighlevel-php"></a>
        <a href="https://packagist.org/packages/musheabdulhakim/gohighlevel-php"><img alt="Latest Version" src="https://img.shields.io/packagist/v/musheabdulhakim/gohighlevel-php"></a>
        <a href="https://packagist.org/packages/musheabdulhakim/gohighlevel-php"><img alt="License" src="https://img.shields.io/packagist/l/musheabdulhakim/gohighlevel-php"></a>
    </p>
</div>

------

# GoHighLevel PHP SDK

This package provides a wonderful **PHP API** client that allows you to interact
with [GoHighLevel Api](https://highlevel.stoplight.io/docs/integrations/0443d7d1a4bd0-overview/). It's  built to simplify your interactions with the platform. This SDK provides a robust, type-safe, and easy-to-use interface for all major API endpoints, from managing businesses and contacts to handling payments and workflows.

## Features ✨

  * **100% PSR-compatible**: The SDK adheres to PSR standards, including PSR-18 for HTTP clients, making it compatible with any modern PHP framework.
  * **Type-Safe & Predictable**: Written in PHP 8.1 with `strict_types`, the code is reliable and predictable.
  * **Powerful Factory**: The `Factory` class gives you full control over the client's configuration, allowing you to set custom headers, API versions, and HTTP clients.
  * **Comprehensive Resource Coverage**: Access all major GoHighLevel API resources through dedicated, logical methods (e.g., `->contacts()`, `->businesses()`, `->workflows()`).

## Installation

You can install the SDK via Composer.

```bash
composer require musheabdulhakim/gohighlevel-php-sdk
```

## Quick Start

The easiest way to get started is to use the `GoHighLevel::client()` method. It handles the client configuration for you.

```php
use MusheAbdulHakim\GoHighLevel\GoHighLevel;

// Initialize the client with your API key
$client = GoHighLevel::client('ACCESS_TOKEN');

// Example: Get a business by its ID
$businessId = 'your_business_id_here';
$businessData = $client->businesses()->get($businessId);

print_r($businessData);
```

## Advanced Usage with the Factory

For more control over the client's configuration, use the `GoHighLevel::factory()` method. This is useful for setting a specific API version, a custom base URI, or integrating with a specific HTTP client like Guzzle.

```php
use MusheAbdulHakim\GoHighLevel\GoHighLevel;
use GuzzleHttp\Client as GuzzleClient;

$client = GoHighLevel::factory()
    ->withApiKey('YOUR_API_KEY')
    // Set a custom base URI (optional)
    ->withBaseUri('https://custom-api-endpoint.com')
    // Set the API Version (optional)
    ->withVersion('2024-05-15')
    // Use a custom PSR-18 HTTP client (optional)
    ->withHttpClient(new GuzzleClient())
    ->make();

// Now you can use the fully configured client
$contacts = $client->contacts()->all();
```

-----

## API Resources

The SDK provides a simple, object-oriented interface for accessing different GoHighLevel resources. Each resource is accessed via a dedicated method on the `Client` object.

| Method                    | Resource Class                                                              | Description                               |
| ------------------------- | --------------------------------------------------------------------------- | ----------------------------------------- |
| `->businesses()`          | `MusheAbdulHakim\GoHighLevel\Resources\Business`                            | Manage businesses.                        |
| `->calendars()`           | `MusheAbdulHakim\GoHighLevel\Resources\Calendars\Calendar`                  | Manage calendars and events.              |
| `->campaigns()`           | `MusheAbdulHakim\GoHighLevel\Resources\Campaigns\Campaign`                  | Manage campaigns and marketing automation. |
| `->companies()`           | `MusheAbdulHakim\GoHighLevel\Resources\Company`                             | Manage companies.                         |
| `->contacts()`            | `MusheAbdulHakim\GoHighLevel\Resources\Contacts\Contact`                    | Manage and retrieve contact information.  |
| `->conversations()`       | `MusheAbdulHakim\GoHighLevel\Resources\Conversations\Conversation`          | Access and manage conversations.          |
| `->courses()`             | `MusheAbdulHakim\GoHighLevel\Resources\Courses\Course`                      | Manage courses.                           |
| `->forms()`               | `MusheAbdulHakim\GoHighLevel\Resources\Forms\Form`                          | Work with forms.                          |
| `->invoices()`            | `MusheAbdulHakim\GoHighLevel\Resources\Invoices\Invoice`                    | Manage and create invoices.               |
| `->triggerLinks()`        | `MusheAbdulHakim\GoHighLevel\Resources\TriggerLinks\TriggerLink`            | Work with trigger links.                  |
| `->location()`            | `MusheAbdulHakim\GoHighLevel\Resources\Locations\Location`                  | Manage locations.                         |
| `->mediaLibrary()`        | `MusheAbdulHakim\GoHighLevel\Resources\MediaLibrary\MediaLibrary`           | Manage media assets.                      |
| `->funnel()`              | `MusheAbdulHakim\GoHighLevel\Resources\Funnels\Funnel`                      | Manage sales funnels.                     |
| `->opportunity()`         | `MusheAbdulHakim\GoHighLevel\Resources\Opportunities\Opportunity`           | Manage sales opportunities.               |
| `->payments()`            | `MusheAbdulHakim\GoHighLevel\Resources\Payments\Payment`                    | Manage payments.                          |
| `->products()`            | `MusheAbdulHakim\GoHighLevel\Resources\Products\Product`                    | Manage products.                          |
| `->saas()`                | `MusheAbdulHakim\GoHighLevel\Resources\SaaS\Saas`                           | Manage SaaS-related functionality.        |
| `->snapshot()`            | `MusheAbdulHakim\GoHighLevel\Resources\Snapshots\Snapshot`                  | Work with account snapshots.              |
| `->survey()`              | `MusheAbdulHakim\GoHighLevel\Resources\Surveys\Survey`                      | Manage surveys.                           |
| `->user()`                | `MusheAbdulHakim\GoHighLevel\Resources\Users\User`                          | Manage users.                             |
| `->workflow()`            | `MusheAbdulHakim\GoHighLevel\Resources\Workflows\Workflow`                  | Work with workflows.                      |
| `->oAuth()`               | `MusheAbdulHakim\GoHighLevel\Resources\Auth\OAuth`                          | Handle OAuth 2.0 authentication.          |

-----

## OAuth 2.0 Integration

The SDK includes a helper method to simplify the OAuth 2.0 authentication flow, which is necessary for certain API scopes.

### Getting an Access Token

You can use the static `getAccessToken` method to exchange an authorization code for an access token.

```php
use MusheAbdulHakim\GoHighLevel\GoHighLevel;

$params = [
    'grant_type' => 'authorization_code',
    'client_id' => 'YOUR_CLIENT_ID',
    'client_secret' => 'YOUR_CLIENT_SECRET',
    'redirect_uri' => 'YOUR_REDIRECT_URI',
    'code' => 'THE_AUTH_CODE_FROM_GOHIGHLEVEL',
];

$accessTokenResponse = GoHighLevel::getAccessToken(
    'https://services.leadconnectorhq.com/oauth/token',
    'application/x-www-form-urlencoded',
    $params
);

print_r($accessTokenResponse);
```

----
### [Visit The Documentation](https://musheabdulhakim.github.io/
```
