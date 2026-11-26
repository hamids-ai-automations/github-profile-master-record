# imgproxykit

**Overview:** A type-safe Python toolkit for imgproxy with signed URLs, image transformations, and seamless Django & FastAPI integration

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/imgproxykit](https://github.com/hamids-ai-automations/imgproxykit) |
| Live website | https://imgproxykit.rtfd.io |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-29 |
| Last update | 2026-11-09 |
| Last push | 2026-10-30 |
| Default branch | master |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 7 |
| Size | 450 KB |
| Topics | - |

## Objectives

<h1 align="center">imgproxykit</h1>

## Features

- [x] Fully typed and checked with `mypy`, `pyright`, `ty` and `pyrefly` in strict modes
- [x] Signed URLs using your `imgproxy` server's `key` and `salt`
- [x] Immutable, reusable transforms combining typed options and scalar arguments
- [x] Variants: generate multiple image URLs from a reusable set of transforms
- [x] Support for named presets configured on your `imgproxy` server
- [x] Native `Django` integration with settings, shortcuts, and template tags
- [x] Native `Django REST Framework` integration with serializers
- [x] Native `FastAPI` integration with dependency injection

---------

## Technical architecture

- **Top-level directories:** .github, docs, imgproxykit, test_apps, tests
- **Total files (tracked in default branch):** 214
- **CI workflows:** .github/workflows/lychee.yml, .github/workflows/release.yml, .github/workflows/test-extras.yml, .github/workflows/test.yml
- **Test files detected:** 76

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 157442 |
| Makefile | 2280 |
| HTML | 1142 |

**Frameworks / libraries detected:** Django, FastAPI, pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`
- `test_apps/django/manage.py`
- `test_apps/fastapi/app.py`

## Installation and setup

Requires **Python 3.12+** and a running [imgproxy](https://github.com/imgproxy/imgproxy) server.

```bash
pip install imgproxykit
```

There are several included extras:

- `'imgproxykit[django]'` provides [Django integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/django.html)
  with settings, shortcuts, and template tags
- `'imgproxykit[drf]'` provides [Django REST Framework integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/drf.html)
  with serializer fields for image URLs and named variants
- `'imgproxykit[fastapi]'` provides [FastAPI integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/fastapi.html)
  with client registration and dependency injection

## Deployment

Firebase/other hosting declared via homepage field: https://imgproxykit.rtfd.io

## Documentation links

- https://imgproxykit.rtfd.io
- https://pypi.org/project/imgproxykit
- https://static.pepy.tech/personalized-badge/imgproxykit?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=BLUE&left_text=downloads
- https://pepy.tech/projects/imgproxykit
- https://imgproxykit.readthedocs.io/en/latest/pages/integrations/django.html
- https://imgproxykit.readthedocs.io/en/latest/pages/integrations/drf.html
- https://imgproxykit.readthedocs.io/en/latest/pages/integrations/fastapi.html
- https://imgproxy.example.com
- https://originals.example.com/products/backpack.jpg
- https://imgproxy.example.com/unsafe/resize:fill:300:300/quality:80/format:webp
- https://imgproxykit.readthedocs.io/en/latest
- https://imgproxykit.readthedocs.io/en/latest/pages/changelog.html

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/imgproxykit/blob/master/README.md

```markdown
<h1 align="center">imgproxykit</h1>

<p align="center">
  <em>A typed Python toolkit for building imgproxy URLs.</em>
</p>

<div align="center">

[![Tests Result](https://img.shields.io/github/actions/workflow/status/kondratevdev/imgproxykit/test.yml?branch=master&label=tests&labelColor=black&color=blue)](https://github.com/kondratevdev/imgproxykit/actions/workflows/test.yml)
[![PyPI Version](https://img.shields.io/pypi/v/imgproxykit.svg?labelColor=black&color=blue)](https://pypi.org/project/imgproxykit/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/imgproxykit?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/imgproxykit)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/imgproxykit.svg?labelColor=black&color=blue)](https://pypi.org/project/imgproxykit/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?labelColor=black)](LICENSE)

</div>

## Features

- [x] Fully typed and checked with `mypy`, `pyright`, `ty` and `pyrefly` in strict modes
- [x] Signed URLs using your `imgproxy` server's `key` and `salt`
- [x] Immutable, reusable transforms combining typed options and scalar arguments
- [x] Variants: generate multiple image URLs from a reusable set of transforms
- [x] Support for named presets configured on your `imgproxy` server
- [x] Native `Django` integration with settings, shortcuts, and template tags
- [x] Native `Django REST Framework` integration with serializers
- [x] Native `FastAPI` integration with dependency injection

---------

## Installation

Requires **Python 3.12+** and a running [imgproxy](https://github.com/imgproxy/imgproxy) server.

```bash
pip install imgproxykit
```

There are several included extras:

- `'imgproxykit[django]'` provides [Django integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/django.html)
  with settings, shortcuts, and template tags
- `'imgproxykit[drf]'` provides [Django REST Framework integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/drf.html)
  with serializer fields for image URLs and named variants
- `'imgproxykit[fastapi]'` provides [FastAPI integration](https://imgproxykit.readthedocs.io/en/latest/pages/integrations/fastapi.html)
  with client registration and dependency injection

## Examples

### Single URL

Build a URL for a cropped `webp` thumbnail:

```python
>>> from imgproxykit import Client, Transform
>>> from imgproxykit.options import Resize

>>> # Public URL of your imgproxy server.
>>> client = Client('https://imgproxy.example.com')

>>> thumbnail = Transform(
...     Resize(width=300, height=300, mode='fill'),  # Pass typed option objects.
...     quality=80,  # Or scalar keywords, equivalent to Quality(80).
...     format='webp',
... )

>>> source_url = 'https://originals.example.com/products/backpack.jpg'
>>> thumbnail_url = client.url(source=source_url, transform=thumbnail)

```

The generated URL has this structure, with the source URL encoded as URL-safe Base64:

```text
https://imgproxy.example.com/unsafe/resize:fill:300:300/quality:80/format:webp/<encoded-source>
```

`thumbnail_url` points to a 300×300 `webp` thumbnail cropped to fill the dimensions.
Imgproxy fetches and processes the original image when this URL is requested.

### Variants

Build variants by combining shared transforms with different settings:

```python
>>> from imgproxykit import Client, Transform

>>> client = Client('https://imgproxy.example.com')

>>> # Share quality and output format across all variants.
>>> base = Transform(quality=85, format='webp')
>>> products = {
...     'small': Transform(*base.options, width=320),
...     'medium': Transform(*base.options, width=640),
...     'large': Transform(*base.options, width=1280),
... }

>>> source_url = 'https://originals.example.com/products/backpack.jpg'
>>> # Build one URL per variant for the same source image.
>>> product_urls = client.variants(source=source_url, variants=products)
>>> small_url = product_urls['small']  # Access a URL by its variant name.

```

`product_urls` contains a URL for each size, all using the shared quality
and WebP format. Reuse `products` with other source images to keep the same
variants across your catalog.

## Next steps

- Read the [documentation](https://imgproxykit.readthedocs.io/en/latest/)
  for client configuration, transformations, variants, and processing options.
- Check the [changelog](https://imgproxykit.readthedocs.io/en/latest/pages/changelog.html)
  for new features, fixes, and breaking changes.
- Find published releases on [PyPI](https://pypi.org/project/imgproxykit/).

## Contributing

See the [contributing guide](https://github.com/hamids-ai-automations/imgproxykit/blob/master/CONTRIBUTING.md) for development setup and checks.
Bug reports and feature requests are welcome on the
[issue tracker](https://github.com/kondratevdev/imgproxykit/issues).

## License

[MIT](https://github.com/hamids-ai-automations/imgproxykit/blob/master/LICENSE)

## Credits

Generated with
[`wemake-python-package`](https://github.com/wemake-services/wemake-python-package)
([template version](https://github.com/wemake-services/wemake-python-package/tree/47d9dddd29da8d6d3d1a403f8a143b323a812083)).

```
