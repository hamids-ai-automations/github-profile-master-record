# returns

**Overview:** Make your functions return something meaningful, typed, and safe!

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/returns](https://github.com/hamids-ai-automations/returns) |
| Live website | https://returns.rtfd.io |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-29 |
| Last update | 2026-10-29 |
| Last push | 2026-10-29 |
| Default branch | master |
| License | BSD-2-Clause |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 74 |
| Size | 6953 KB |
| Topics | - |

## Objectives

[![Returns logo](https://raw.githubusercontent.com/dry-python/brand/master/logo/returns_white-outline.png)](https://github.com/dry-python/returns)

## Features

- Brings functional programming to Python land
- Provides a bunch of primitives to write declarative business logic
- Enforces better architecture
- Fully typed with annotations and checked with `mypy`, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Adds emulated [Higher Kinded Types](https://returns.readthedocs.io/en/latest/pages/hkt.html) support
- Provides type-safe interfaces to create your own data-types with enforced laws
- Has a bunch of helpers for better composition
- Pythonic and pleasant to write and to read 🐍
- Supports functions and coroutines, framework agnostic
- Easy to start: has lots of docs, tests, and tutorials

[Quickstart](https://returns.readthedocs.io/en/latest/pages/quickstart.html) right now!

## Technical architecture

- **Top-level directories:** .github, benchmarks, docs, returns, tests, typesafety
- **Total files (tracked in default branch):** 415
- **CI workflows:** .github/workflows/codspeed.yml, .github/workflows/test.yml
- **Test files detected:** 264

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 689959 |
| Makefile | 1372 |

**Frameworks / libraries detected:** pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

```bash
pip install returns
```

You can also install `returns` with the latest supported `mypy` version:

```bash
pip install returns[compatible-mypy]
```

You would also need to configure our [`mypy` plugin](https://returns.readthedocs.io/en/latest/pages/contrib/mypy_plugins.html):

```ini

## Deployment

Firebase/other hosting declared via homepage field: https://returns.rtfd.io

## Documentation links

- https://returns.rtfd.io
- https://raw.githubusercontent.com/dry-python/brand/master/logo/returns_white-outline.png
- https://app.codspeed.io/dry-python/returns?utm_source=badge
- https://readthedocs.org/projects/returns/badge/?version=latest
- https://returns.readthedocs.io/en/latest/?badge=latest
- https://pypi.org/project/returns
- https://anaconda.org/conda-forge/returns
- https://t.me/drypython
- https://www.python.org/dev/peps/pep-0561
- https://returns.readthedocs.io/en/latest/pages/hkt.html
- https://returns.readthedocs.io/en/latest/pages/quickstart.html
- https://returns.readthedocs.io/en/latest/pages/contrib/mypy_plugins.html
- https://returns.readthedocs.io/en/latest
- https://repl.it/@sobolevn/returns#ex.py
- https://returns.readthedocs.io/en/latest/pages/create-your-own-container.html
- https://returns.readthedocs.io/en/latest/pages/do-notation.html
- https://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare
- https://mypy.readthedocs.io/en/stable/kinds_of_types.html#optional-types-and-the-none-type
- https://returns.readthedocs.io/en/latest/pages/maybe.html
- https://returns.readthedocs.io/en/latest/pages/context.html
- https://returns.readthedocs.io/en/latest/pages/context.html#requirescontextresult-container
- https://returns.readthedocs.io/en/latest/pages/context.html#requirescontextioresult-container
- https://returns.readthedocs.io/en/latest/pages/context.html#requirescontextfutureresult-container
- https://fsharpforfunandprofit.com/rop
- https://returns.readthedocs.io/en/latest/pages/result.html#safe
- https://returns.readthedocs.io/en/latest/pages/result.html
- https://returns.readthedocs.io/en/latest/pages/pipeline.html#flow
- https://returns.readthedocs.io/en/latest/pages/pointfree.html#bind
- https://en.wikipedia.org/wiki/Pure_function

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

response = requests.get('/api/users/{0}'.format(user_id))
    response.raise_for_status()
    return response


@safe
def _parse_json(response: requests.Response) -> 'UserProfile':
    return response.json()
```

Now we have a clean and a safe and declarative way
to express our business needs:

- We start from making a request, that might fail at any moment,
- Then parsing the response if the request was successful,
- And then return the result.

Now, instead of returning regular values

## README source

Full README: https://github.com/hamids-ai-automations/returns/blob/master/README.md

```markdown
[![Returns logo](https://raw.githubusercontent.com/dry-python/brand/master/logo/returns_white-outline.png)](https://github.com/dry-python/returns)

-----

[![test](https://github.com/dry-python/returns/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/dry-python/returns/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/dry-python/returns/branch/master/graph/badge.svg)](https://codecov.io/gh/dry-python/returns)
[![CodSpeed](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json)](https://app.codspeed.io/dry-python/returns?utm_source=badge)
[![Documentation Status](https://readthedocs.org/projects/returns/badge/?version=latest)](https://returns.readthedocs.io/en/latest/?badge=latest)
[![Python Version](https://img.shields.io/pypi/pyversions/returns.svg)](https://pypi.org/project/returns/)
[![conda](https://img.shields.io/conda/v/conda-forge/returns?label=conda)](https://anaconda.org/conda-forge/returns)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Telegram chat](https://img.shields.io/badge/chat-join-blue?logo=telegram)](https://t.me/drypython)

-----

Make your functions return something meaningful, typed, and safe!


## Features

- Brings functional programming to Python land
- Provides a bunch of primitives to write declarative business logic
- Enforces better architecture
- Fully typed with annotations and checked with `mypy`, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Adds emulated [Higher Kinded Types](https://returns.readthedocs.io/en/latest/pages/hkt.html) support
- Provides type-safe interfaces to create your own data-types with enforced laws
- Has a bunch of helpers for better composition
- Pythonic and pleasant to write and to read 🐍
- Supports functions and coroutines, framework agnostic
- Easy to start: has lots of docs, tests, and tutorials

[Quickstart](https://returns.readthedocs.io/en/latest/pages/quickstart.html) right now!


## Installation

```bash
pip install returns
```

You can also install `returns` with the latest supported `mypy` version:

```bash
pip install returns[compatible-mypy]
```

You would also need to configure our [`mypy` plugin](https://returns.readthedocs.io/en/latest/pages/contrib/mypy_plugins.html):

```ini
# In setup.cfg or mypy.ini:
[mypy]
plugins =
  returns.contrib.mypy.returns_plugin
```

or:

```toml
[tool.mypy]
plugins = ["returns.contrib.mypy.returns_plugin"]
```

We also recommend to use the same `mypy` settings we use, which you'll find in the `[tool.mypy]` sections in our [pyproject.toml](https://github.com/wemake-services/wemake-python-styleguide/blob/master/pyproject.toml) file.

Make sure you know how to get started, [check out our docs](https://returns.readthedocs.io/en/latest/)!
[Try our demo](https://repl.it/@sobolevn/returns#ex.py).


## Contents

- [Maybe container](#maybe-container) that allows you to write `None`-free code
- [RequiresContext container](#requirescontext-container) that allows you to use typed functional dependency injection
- [Result container](#result-container) that lets you to get rid of exceptions
- [IO container](#io-container) and [IOResult](#troublesome-io) that marks all impure operations and structures them
- [Future container](#future-container) and [FutureResult](#async-code-without-exceptions) to work with `async` code
- [Write your own container!](https://returns.readthedocs.io/en/latest/pages/create-your-own-container.html) You would still have all the features for your own types (including full existing code reuse and type-safety)
- Use [`do-notation`](https://returns.readthedocs.io/en/latest/pages/do-notation.html) to make your code easier!


## Maybe container

`None` is called the [worst mistake in the history of Computer Science](https://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare/).

So, what can we do to check for `None` in our programs?
You can use builtin [Optional](https://mypy.readthedocs.io/en/stable/kinds_of_types.html#optional-types-and-the-none-type) type
and write a lot of `if some is not None:` conditions.
But, **having `null` checks here and there makes your code unreadable**.

```python
user: Optional[User]
discount_program: Optional['DiscountProgram'] = None

if user is not None:
    balance = user.get_balance()
    if balance is not None:
        credit = balance.credit_amount()
        if credit is not None and credit > 0:
            discount_program = choose_discount(credit)
```

Or you can use
[Maybe](https://returns.readthedocs.io/en/latest/pages/maybe.html) container!
It consists of `Some` and `Nothing` types,
representing existing state and empty (instead of `None`) state respectively.

```python
from typing import Optional
from returns.maybe import Maybe, maybe


@maybe  # decorator to convert existing Optional[int] to Maybe[int]
def bad_function() -> Optional[int]: ...


maybe_number: Maybe[float] = bad_function().bind_optional(
    lambda number: number / 2,
)
# => Maybe will return Some[float] only if there's a non-None value
#    Otherwise, will return Nothing
```

You can be sure that `.bind_optional()` method won't be called for `Nothing`.
Forget about `None`-related errors forever!

We can also bind a `Optional`-returning function over a container.
To achieve this, we are going to use `.bind_optional` method.

And here's how your initial refactored code will look:

```python
user: Optional[User]

# Type hint here is optional, it only helps the reader here:
discount_program: Maybe['DiscountProgram'] = (
    Maybe
    .from_optional(
        user,
    )
    .bind_optional(  # This won't be called if `user is None`
        lambda real_user: real_user.get_balance(),
    )
    .bind_optional(  # This won't be called if `real_user.get_balance()` is None
        lambda balance: balance.credit_amount(),
    )
    .bind_optional(  # And so on!
        lambda credit: choose_discount(credit) if credit > 0 else None,
    )
)
```

Much better, isn't it?


## RequiresContext container

Many developers do use some kind of dependency injection in Python.
And usually it is based on the idea
that there's some kind of a container and assembly process.

Functional approach is much simpler!

Imagine that you have a `django` based game, where you award users with points for each guessed letter in a word (unguessed letters are marked as `'.'`):

```python
from django.http import HttpRequest, HttpResponse
from words_app.logic import calculate_points


def view(request: HttpRequest) -> HttpResponse:
    user_word: str = request.POST['word']  # just an example
    points = calculate_points(user_word)
    ...  # later you show the result to user somehow


# Somewhere in your `words_app/logic.py`:


def calculate_points(word: str) -> int:
    guessed_letters_count = len([letter for letter in word if letter != '.'])
    return _award_points_for_letters(guessed_letters_count)


def _award_points_for_letters(guessed: int) -> int:
    return 0 if guessed < 5 else guessed  # minimum 6 points possible!
```

Awesome! It works, users are happy, your logic is pure and awesome.
But, later you decide to make the game more fun:
let's make the minimal accountable letters threshold
configurable for an extra challenge.

You can just do it directly:

```python
def _award_points_for_letters(guessed: int, threshold: int) -> int:
    return 0 if guessed < threshold else guessed
```

The problem is that `_award_points_for_letters` is deeply nested.
And then you have to pass `threshold` through the whole callstack,
including `calculate_points` and all other functions that might be on the way.
All of them will have to accept `threshold` as a parameter!
This is not useful at all!
Large code bases will struggle a lot from this change.

Ok, you can directly use `django.settings` (or similar)
in your `_award_points_for_letters` function.
And **ruin your pure log
```
