# bite

**Overview:** Checks whether the "fixed" in your AI coding agent's commits is true. It takes each fix back out and runs your tests. Free, with no key.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/bite](https://github.com/hamids-ai-automations/bite) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-04 |
| Last update | 2026-11-04 |
| Last push | 2026-11-04 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 6 |
| Size | 1208 KB |
| Topics | - |

## Objectives

<p>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/connabyss/bite/main/assets/bite-header-dark.png">
    <img alt="Bite" src="https://raw.githubusercontent.com/connabyss/bite/main/assets/bite-header-light.png" width="300">
  </picture>
</p>

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude-plugin, .github, assets, bot, evidence, plugin, tests
- **Total files (tracked in default branch):** 111
- **CI workflows:** .github/workflows/bite.yml, .github/workflows/bot.yml, .github/workflows/pr-checklist.yml, .github/workflows/publish.yml, .github/workflows/self-check.yml, .github/workflows/tests.yml
- **Test files detected:** 58

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 592061 |

**Frameworks / libraries detected:** MCP, pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

- uses: actions/setup-python@v7
      - run: python -m pip install pytest -r requirements.txt
      - uses: connabyss/bite@v1.0.3
```

Options go under `with:`: `args` (extra `bite` options, e.g. `--serious`), `max-commits` (default 20),
`fail-on-gap` (set to `false` to report without failing) and `comment` (set to `false` for no comment). It posts one comment on the pull request that says, per
commit, whether a test noticed the change being taken out, and updates that same comment on later pushes. The
rerun steps for each flagged commit are on the job's summary page.

## Deployment

No deployment configuration detected.

## Documentation links

- https://docs.astral.sh/uv
- https://raw.githubusercontent.com/connabyss/bite/main/assets/bite-header-dark.png
- https://raw.githubusercontent.com/connabyss/bite/main/assets/bite-header-light.png
- https://raw.githubusercontent.com/connabyss/bite/main/assets/bite-demo.svg
- https://pipx.pypa.io
- https://zdravkov.info
- https://dev.to/izdravkov/comment/3jdej
- https://code.claude.com/docs/en/agent-sdk/overview

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/marvis-streamlit-dashboard
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/adwaste-intelligence

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/bite/blob/main/README.md

```markdown
<p>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/connabyss/bite/main/assets/bite-header-dark.png">
    <img alt="Bite" src="https://raw.githubusercontent.com/connabyss/bite/main/assets/bite-header-light.png" width="300">
  </picture>
</p>

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Bite%20free%20check-blue?logo=github)](https://github.com/marketplace/actions/bite-free-check)

**Would your tests catch it if the bug came back?**

Bite checks whether an AI coding agent's "fixed" is actually true.

<img alt="bite --demo: one fix is noticed by a test, the other has no test at all" src="https://raw.githubusercontent.com/connabyss/bite/main/assets/bite-demo.svg" width="760">

**Try it now.** It's free, needs no key, and never changes your files. If you have Python, paste these two
lines into any terminal window (PowerShell, cmd, Terminal):

```
python -m pip install bite-check
python -m bite_check --free
```

Outside a project, Bite first shows a demo on a tiny made-up one. To check your own project, type the second line
and a space, drag your project's folder into the window (that types its path), and press Enter.

Have [pipx](https://pipx.pypa.io) or [uv](https://docs.astral.sh/uv/)? One line does it, no install:
`pipx run bite-check --free` or `uvx bite-check --free`. (On Linux or a Mac, if pip says "externally managed",
use one of those.) If your commits never say "fix", add `--any` to check every recent change. To keep Bite
installed as a `bite` command, see [Try it in a minute](#try-it-in-a-minute).

**Here for Hack Week or your first open-source PR?** These [good first issues](https://github.com/connabyss/bite/labels/good%20first%20issue)
are small, and each one says where to look and when it's done. Comment on one to claim it.

## Why you need this

When an AI fixes a bug for you, it often says "Fixed, and I added a test." If you don't read code, you can't tell
if that's true.

A test is a tiny robot that checks one thing, like "2 + 2 should be 4", and shouts when it isn't. A good test
shouts if the bug ever comes back. A weak one stays quiet no matter what.

Bite checks your robots. It puts the old bug back on purpose and watches whether any test shouts. It's like
testing a smoke alarm with real smoke instead of trusting the little green light.

If a test shouts, that fix is guarded. If they all stay quiet, the next change, by you or your AI, could bring the
bug back and nobody would notice. Bite names that fix, so you can tell your AI: "add a test that fails without
this fix."

## How it works

It takes each recent fix back out of your code and runs your tests. If they still pass, nothing guards that fix,
and Bite tells you which one. That free check needs no key and works with pytest, npm test, cargo test, go test,
dotnet test, Maven and Gradle (Java and Kotlin):

```
pipx install bite-check
bite --free
```

With your own API key it goes one step further: it writes one small test of the commit's exact claim and runs it.
That is how it found a memory leak in [prosemirror-py](#the-catch-that-shows-what-its-for) that a commit said it
had fixed.

> "Reverting the claimed fix and making the change prove itself under a real test is exactly the kind of check that
> should exist for every "fixed" commit."
>
> — [Ivan Zdravkov](https://zdravkov.info), [on DEV](https://dev.to/izdravkov/comment/3jdej)

## Try it in a minute

Install once with [pipx](https://pipx.pypa.io), which gives Bite its own space so there's no venv to set up or
activate:

```
python -m pip install --user pipx
python -m pipx ensurepath
```

Close the terminal window and open a new one, then:

```
pipx install bite-check
bite --demo
```

`bite --demo` builds a tiny made-up shop project in a temporary folder and runs the free check on it. Two of
its commits say they fixed something: one added a test for its fix, the other didn't. Bite takes each fix back
out and runs the tests, and you see the difference:

```
  9661edcf ✅ noticed by test_discount_never_below_zero Fix discounts over 100% making the price negative
  e5c329ec ⚠️ NO TEST NOTICED           Fix totals showing long decimals like 0.30000000000000004
```

It needs nothing besides git, takes a few seconds, and doesn't touch your files. Then try it on your own project:

```
bite --free /path/to/your-repo
```

(Or type `bite --free ` and drag the project's folder into the window. From inside the project's folder, plain
`bite --free` works too.)

`bite` now works in any terminal window. `bite --free` needs no key and costs nothing. It takes each recent
change back out, runs your tests, and lists the changes no test guards, plus any new test that still passes
without its commit's code (it tests nothing). If something it needs is missing, like git or pytest, it says
so and gives you the line that installs it. Each run ends with a one-page report, `bite_proof/report.html`, to open in your browser. To update Bite later, see [Updating Bite](#updating-bite).

To test the claims themselves (the paid step), add one extra package and set `ANTHROPIC_API_KEY`, then run `bite`:

```
pipx inject bite-check claude-agent-sdk
```

This step uses your own API key, and `--budget` caps what a run spends ($1 by default). It runs on Anthropic's
Agent SDK, so it needs an API key and never uses a Claude login or plan (Anthropic's Agent SDK rule:
https://code.claude.com/docs/en/agent-sdk/overview). The commits Bite checks can come from any coding AI or person.

Works with pytest, npm test, cargo test, go test, dotnet test, Maven and Gradle. Settings and limits: [AGENTS.md](https://github.com/connabyss/bite/blob/main/AGENTS.md),
written so your coding AI (Claude Code, Codex, Cursor, Copilot) can set Bite up for you. To work on Bite itself: clone it, `pip install -e .[test]`, then `python -m pytest`.

## When a check is slow

Bite runs your tests several times for each change, so a slow test suite makes a slow check. Four ways to speed it up:

- `bite --free --jobs 4` checks 4 changes at a time. If two checks get in each other's way (a shared file, a port),
  Bite runs the failed one again on its own before it counts, so a clash never shows up as a result.
- Bite remembers the changes it checked with ✅ in `bite_proof/checked.json`, and skips them next time when the
  tests, settings and dependency files (requirements.txt, package-lock.json, go.sum, ...) are the same. Add,
  change or delete a test, or update a library, and those changes are checked again. `--again`
  checks everything anyway. The Action keeps that memory between runs for you.
- `bite --free --shard 2/5` runs part 2 of 5. Run parts 1/5 to 5/5 on 5 machines at once and together they check
  every change, in about a fifth of the time. On GitHub Actions that's a matrix:

  ```yaml
  strategy:
    matrix:
      part: [1, 2, 3, 4, 5]
  steps:
    # ... check out and install, as usual
    - run: bite --free --shard ${{ matrix.part }}/5
  ```

- pytest: install pytest-xdist and put `test_command = python -m pytest -n auto` in `.bite.ini` to run the tests
  themselves 4 at a time. Or point `free_test_command` at a faster part of your tests.

When each change takes over 3 minutes, Bite prints these tips at the end of the run.

## Updating Bite

`bite --version` prints your version, and when a newer one is out it says so and gives you the line to paste.
That line always gets the newest version:

```
pipx install --force bite-check --pip-args="--no-cache-dir"
```

Installed with pip instead of pipx? `python -m pip install --upgrade --no-cache-dir bite-check`

Why not just `pipx upgrade bite-check`? Right after a release, pip can keep using the list of versions it saved
earlier and say you're already on the latest. `--no-cache-dir` makes it ask PyPI fresh, and `--force` also replaces
an older `bite` or `bite.exe` that's in the way.

What changed in each version: [CHANGELOG.md](https://github.com/connabyss/bite/blob/main/CHAN
```
