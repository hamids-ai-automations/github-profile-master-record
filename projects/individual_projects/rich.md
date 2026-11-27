# rich

**Overview:** Rich is a Python library for rich text and beautiful formatting in the terminal.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/rich](https://github.com/hamids-ai-automations/rich) |
| Live website | https://rich.readthedocs.io/en/latest/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-28 |
| Last update | 2026-10-28 |
| Last push | 2026-10-28 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 268 |
| Size | 50492 KB |
| Topics | - |

## Objectives

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich)](https://pypi.org/project/rich/) [![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .faq, .github, assets, benchmarks, docs, examples, imgs, questions, rich, tests, tools
- **Total files (tracked in default branch):** 553
- **CI workflows:** .github/workflows/codeql.yml, .github/workflows/codespell.yml, .github/workflows/comment.yml, .github/workflows/newissue.yml, .github/workflows/pythonpackage.yml, .github/workflows/readmechanged.yml
- **Test files detected:** 71

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 1701402 |
| Batchfile | 799 |
| Makefile | 307 |

**Frameworks / libraries detected:** pytest

**Dependencies:** none detected

## Important source files

- `docs/requirements.txt`
- `pyproject.toml`

## Installation and setup

Install with `pip` or your favorite PyPI package manager.

```sh
python -m pip install rich
```

Run the following to test Rich output on your terminal:

```sh
python -m rich
```

## Deployment

Firebase/other hosting declared via homepage field: https://rich.readthedocs.io/en/latest/

## Documentation links

- https://rich.readthedocs.io/en/latest
- https://pypi.org/project/rich
- https://badge.fury.io/py/rich.svg
- https://badge.fury.io/py/rich
- https://pepy.tech/badge/rich/month
- https://pepy.tech/project/rich
- https://www.willmcgugan.com/tag/rich
- https://twitter.com/willmcgugan
- https://calmcode.io/rich/introduction.html
- https://twitter.com/fishnets88
- https://www.willmcgugan.com/blog/pages/post/rich-tweets
- https://jupyter.org
- https://rich.readthedocs.io/en/latest/introduction.html#quick-start
- https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console
- https://en.wikipedia.org/wiki/BBCode
- https://rich.readthedocs.io/en/latest/console.html
- https://rich.readthedocs.io/en/latest/reference/init.html?highlight=inspect#rich.inspect
- https://rich.readthedocs.io/en/latest/reference/init.html#rich.inspect
- https://rich.readthedocs.io/en/latest/logging.html
- https://rich.readthedocs.io/en/latest/tables.html
- https://rich.readthedocs.io/en/latest/progress.html
- https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console.status
- https://www.npmjs.com/package/cli-spinners
- https://rich.readthedocs.io/en/latest/tree.html
- https://rich.readthedocs.io/en/latest/columns.html
- https://rich.readthedocs.io/en/latest/markdown.html
- https://pygments.org
- https://rich.readthedocs.io/en/latest/syntax.html
- https://rich.readthedocs.io/en/latest/traceback.html

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/rich/blob/main/README.md

```markdown
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich)](https://pypi.org/project/rich/) [![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)

[![Downloads](https://pepy.tech/badge/rich/month)](https://pepy.tech/project/rich)
[![codecov](https://img.shields.io/codecov/c/github/Textualize/rich?label=codecov&logo=codecov)](https://codecov.io/gh/Textualize/rich)
[![Rich blog](https://img.shields.io/badge/blog-rich%20news-yellowgreen)](https://www.willmcgugan.com/tag/rich/)
[![Twitter Follow](https://img.shields.io/twitter/follow/willmcgugan.svg?style=social)](https://twitter.com/willmcgugan)

![Logo](https://github.com/textualize/rich/raw/main/imgs/logo.svg)

[English readme](https://github.com/textualize/rich/blob/main/README.md)
 • [简体中文 readme](https://github.com/textualize/rich/blob/main/README.cn.md)
 • [正體中文 readme](https://github.com/textualize/rich/blob/main/README.zh-tw.md)
 • [Lengua española readme](https://github.com/textualize/rich/blob/main/README.es.md)
 • [Deutsche readme](https://github.com/textualize/rich/blob/main/README.de.md)
 • [Läs på svenska](https://github.com/textualize/rich/blob/main/README.sv.md)
 • [日本語 readme](https://github.com/textualize/rich/blob/main/README.ja.md)
 • [한국어 readme](https://github.com/textualize/rich/blob/main/README.kr.md)
 • [Français readme](https://github.com/textualize/rich/blob/main/README.fr.md)
 • [Schwizerdütsch readme](https://github.com/textualize/rich/blob/main/README.de-ch.md)
 • [हिन्दी readme](https://github.com/textualize/rich/blob/main/README.hi.md)
 • [Português brasileiro readme](https://github.com/textualize/rich/blob/main/README.pt-br.md)
 • [Italian readme](https://github.com/textualize/rich/blob/main/README.it.md)
 • [Русский readme](https://github.com/textualize/rich/blob/main/README.ru.md)
 • [Indonesian readme](https://github.com/textualize/rich/blob/main/README.id.md)
 • [فارسی readme](https://github.com/textualize/rich/blob/main/README.fa.md)
 • [Türkçe readme](https://github.com/textualize/rich/blob/main/README.tr.md)
 • [Polskie readme](https://github.com/textualize/rich/blob/main/README.pl.md)


Rich is a Python library for _rich_ text and beautiful formatting in the terminal.

The [Rich API](https://rich.readthedocs.io/en/latest/) makes it easy to add color and style to terminal output. Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, tracebacks, and more — out of the box.

![Features](https://github.com/textualize/rich/raw/main/imgs/features.png)

For a video introduction to Rich see [calmcode.io](https://calmcode.io/rich/introduction.html) by [@fishnets88](https://twitter.com/fishnets88).

See what [people are saying about Rich](https://www.willmcgugan.com/blog/pages/post/rich-tweets/).

## Compatibility

Rich works with Linux, macOS and Windows. True color / emoji works with new Windows Terminal, classic terminal is limited to 16 colors. Rich requires Python 3.8 or later.

Rich works with [Jupyter notebooks](https://jupyter.org/) with no additional configuration required.

## Installing

Install with `pip` or your favorite PyPI package manager.

```sh
python -m pip install rich
```

Run the following to test Rich output on your terminal:

```sh
python -m rich
```

## Rich Print

To effortlessly add rich output to your application, you can import the [rich print](https://rich.readthedocs.io/en/latest/introduction.html#quick-start) method, which has the same signature as the builtin Python function. Try this:

```python
from rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
```

![Hello World](https://github.com/textualize/rich/raw/main/imgs/print.png)

## Rich REPL

Rich can be installed in the Python REPL, so that any data structures will be pretty printed and highlighted.

```python
>>> from rich import pretty
>>> pretty.install()
```

![REPL](https://github.com/textualize/rich/raw/main/imgs/repl.png)

## Using the Console

For more control over rich terminal content, import and construct a [Console](https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console) object.

```python
from rich.console import Console

console = Console()
```

The Console object has a `print` method which has an intentionally similar interface to the builtin `print` function. Here's an example of use:

```python
console.print("Hello", "World!")
```

As you might expect, this will print `"Hello World!"` to the terminal. Note that unlike the builtin `print` function, Rich will word-wrap your text to fit within the terminal width.

There are a few ways of adding color and style to your output. You can set a style for the entire output by adding a `style` keyword argument. Here's an example:

```python
console.print("Hello", "World!", style="bold red")
```

The output will be something like the following:

![Hello World](https://github.com/textualize/rich/raw/main/imgs/hello_world.png)

That's fine for styling a line of text at a time. For more finely grained styling, Rich renders a special markup which is similar in syntax to [bbcode](https://en.wikipedia.org/wiki/BBCode). Here's an example:

```python
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
```

![Console Markup](https://github.com/textualize/rich/raw/main/imgs/where_there_is_a_will.png)

You can use a Console object to generate sophisticated output with minimal effort. See the [Console API](https://rich.readthedocs.io/en/latest/console.html) docs for details.

## Rich Inspect

Rich has an [inspect](https://rich.readthedocs.io/en/latest/reference/init.html?highlight=inspect#rich.inspect) function which can produce a report on any Python object, such as class, instance, or builtin.

```python
>>> my_list = ["foo", "bar"]
>>> from rich import inspect
>>> inspect(my_list, methods=True)
```

![Log](https://github.com/textualize/rich/raw/main/imgs/inspect.png)

See the [inspect docs](https://rich.readthedocs.io/en/latest/reference/init.html#rich.inspect) for details.

# Rich Library

Rich contains a number of builtin _renderables_ you can use to create elegant output in your CLI and help you debug your code.

Click the following headings for details:

<details>
<summary>Log</summary>

The Console object has a `log()` method which has a similar interface to `print()`, but also renders a column for the current time and the file and line which made the call. By default Rich will do syntax highlighting for Python structures and for repr strings. If you log a collection (i.e. a dict or a list) Rich will pretty print it so that it fits in the available space. Here's an example of some of these features.

```python
from rich.console import Console
console = Console()

test_data = [
    {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
    {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
    {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
]

def test_log():
    enabled = False
    context = {
        "foo": "bar",
    }
    movies = ["Deadpool", "Rise of the Skywalker"]
    console.log("Hello from", console, "!")
    console.log(test_data, log_locals=True)


test_log()
```

The above produces the following output:

![Log](https://github.com/textualize/rich/raw/main/imgs/log.png)

Note the `log_locals` argument, which outputs a table containing the local variables where the log method was called.

The log method could be used for logging to the terminal for long running applications such as servers, but is also a very nice debugging aid.

</details>
<details>
<summary>Logging Handler</summary>

You can also use the builtin [Handler class](https://rich.readthedocs.io/en/latest/logging.html) to format and colorize output from Python's logging module. Here's an example of the output:

![Logging](https://github.com/textualize/rich/raw/main/imgs/logging.png)

</details>

<details>
```
