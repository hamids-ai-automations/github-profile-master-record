# h-ssh

**Overview:** Multi-vendor network automation framework with parallel execution, safety gates, and audit logging

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/h-ssh](https://github.com/hamids-ai-automations/h-ssh) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-29 |
| Last update | 2026-10-29 |
| Last push | 2026-10-29 |
| Default branch | develop |
| License | NOASSERTION |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 2055 KB |
| Topics | - |

## Objectives

<div align="center">

## Features

- **Four transports, one interface.** Juniper (PyEZ over NETCONF), any SSH host through paramiko or the system `ssh` binary, and raw-socket telnet with IOS-, Junos-, Arista- and NX-OS-flavoured prompt handling. Same flags whichever you point it at; the ones only a Junos transport can honour (`--dry-run` on an edit, `--show-diff`, `--commit-confirmed`, and over NETCONF `--comment`, `--format`, `--rollback`, `--commit-status`) are refused on the others device by device: such a device is a FAIL with the reason, nothing is sent to it, and the run exits 1; never faked.
- **Parallel by default.** Devices are worked concurrently behind an `asyncio` semaphore, `--workers 8` out of the box.
- **One command or many, one device or many.** `--batch` runs several commands per device on a single connection; `--job` takes a JSON file with different commands — and different modes — per device, readable from a file or stdin.
- **A dead box costs seconds, not a worker.** Every run starts with a probe (`--no-probe` skips it) — a TCP connect and the SSH banner, no login, 100 boxes at a time — and goes to the boxes that answered; `--probe` alone is a health check of the fleet, with each box's TCP handshake round trip as the kernel measured it and the time its sshd took to answer. See [The probe](#the-probe).
- **Writes are gated.** The probe's question before a partial deployment, `y/N` confirmation, `--dry-run` that shows the diff without committing and `--commit-confirmed N` for changes that undo themselves unless you confirm within N minutes (both Junos), and an opt-in per-device rate limit and cooldown (`--safety-file`).
- **Templates instead of memorised syntax.** `-sC bgp` resolves through a per-vendor JSON template library — *per target*, so the same shortcut sends a Junos router and an EOS switch each their own command. Drop your own in `~/.h-ssh/commands/{dialect}.json` (`junos`, `ios`, `nxos`, `eos`, `none`) to add or override; `junos`, `eos` and `none` ship one.
- **Built to be scripted.** `--json` on stdout, a structured summary line on stderr, meaningful exit codes, and credentials from `HSSH_USER` / `HSSH_PASSWORD` — or import `hssh` and skip the CLI entirely. A whole fleet run fits in one YAML file (`--run fleet.yaml`) that a pipeline step or a jump-host session runs as it is.
- **Built for a maintenance, not just a run.** A session pool keeps one NETCONF session per router open for a whole script; `rpc()` and `--format json|xml` return the router's own data instead of CLI text; `begin()` holds a diffed candidate open until a gate decides; `--rollback N`, commit comments, `--commit-status` and `guarded_commit()` cover the commit-confirmed lifecycle without a `| match` in sight.
- **Two runtime dependencies — or none.** `paramiko` and `junos-eznc` come with the package. Telnet is a raw socket (no stdlib `telnetlib`, so it still works on Python 3.13+), and the `openssh` transport drives the system `ssh` binary, so a checkout on a locked-down jump host with nothing installable still runs shows and edits over `ssh`.

## Technical architecture

- **Top-level directories:** .github, assets, h-app
- **Total files (tracked in default branch):** 108
- **CI workflows:** .github/workflows/tests.yml
- **Test files detected:** 55

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 1937429 |
| Shell | 6213 |

**Frameworks / libraries detected:** pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

One line, no package manager. It needs `python3` 3.10 or newer with its venv module (Debian/Ubuntu:
`sudo apt install python3-venv`) and `git`:

```bash
curl -fsSL https://raw.githubusercontent.com/h-network/h-ssh/develop/install.sh | sh
h-ssh --list-vendors
```

The installer puts h-ssh in a Python environment of its own, `~/.h-ssh/venv`, with every transport
(paramiko and PyEZ come with it), and links `h-ssh` and `h-ssh-store` into `~/.local/bin`, creating
that directory when it is missing; if it is not on your `PATH` yet the script says so and how to add
it. Your config, inventory, shortcuts and profiles live next to the environment under `~/.h-ssh` (the
result store is `./h-ssh.db` in the directory you run from, unless you name another), and pip's
download cache lands in its usual place (`~/.cache/pip` on Linux). Running the same line again
upgrades, whatever the version number says. It installs the `develop` branch; a knob on the `sh` side
of the pipe picks another branch or tag: `curl -fsSL … | H_SSH_REF=main sh` for the release branch.
`H_SSH_REPO`, `H_SSH_HOME`, `H_SSH_BIN` and `H_SSH_PYTHON` are the others, see the script's header.

## Deployment

No deployment configuration detected.

## Documentation links

- https://docs.astral.sh/uv
- https://pipx.pypa.io
- https://raw.githubusercontent.com/h-network/h-ssh/develop/install.sh

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

Full README: https://github.com/hamids-ai-automations/h-ssh/blob/develop/README.md

```markdown
<div align="center">

<img src="assets/banner.svg" alt="H-SSH // the fleet loop, not the session // h-network" width="600">
 
<br/>

[![License: PolyForm Noncommercial 1.0.0](https://github.com/hamids-ai-automations/h-ssh/blob/develop/assets/badges/license.svg)](LICENSE)
![Python 3.10+](https://raw.githubusercontent.com/hamids-ai-automations/h-ssh/develop/assets/badges/python.svg)
![Vendors: junos ssh openssh telnet](https://raw.githubusercontent.com/hamids-ai-automations/h-ssh/develop/assets/badges/vendors.svg)
![Runtime dependencies: paramiko and PyEZ](https://raw.githubusercontent.com/hamids-ai-automations/h-ssh/develop/assets/badges/deps.svg)

</div>

# h-ssh

`h-ssh` runs commands across a fleet of network devices: one device or three hundred, Juniper, any SSH host, or a console
still speaking telnet. Devices are worked in parallel, results are collected per device, and one dead box does not sink a run:
every run probes the boxes first (unless you say `--no-probe`), without logging in, so a dead one is a FAIL within seconds,
and an edit does not go on without a box the probe found dead unless you say so.

The per-device session is a solved problem; what is left is everything around it: the thread pool, per-device result collection, a rate
limiter (`--safety-file`) so a router that already failed is not hammered, and a record of what changed (`--audit-log`). That is
the part h-ssh provides.

On Junos, everything goes through PyEZ over NETCONF, reads and writes alike, which gives one session, real RPC errors, and the lock, diff
and rollback that config changes need. Every edit is probed for reachability (unless `--no-probe`) and prompts before it commits;
with `--audit-log` it lands in a JSONL audit trail.
`--commit-confirmed` puts the device back the way it was if you never confirm.

## Features

- **Four transports, one interface.** Juniper (PyEZ over NETCONF), any SSH host through paramiko or the system `ssh` binary, and raw-socket telnet with IOS-, Junos-, Arista- and NX-OS-flavoured prompt handling. Same flags whichever you point it at; the ones only a Junos transport can honour (`--dry-run` on an edit, `--show-diff`, `--commit-confirmed`, and over NETCONF `--comment`, `--format`, `--rollback`, `--commit-status`) are refused on the others device by device: such a device is a FAIL with the reason, nothing is sent to it, and the run exits 1; never faked.
- **Parallel by default.** Devices are worked concurrently behind an `asyncio` semaphore, `--workers 8` out of the box.
- **One command or many, one device or many.** `--batch` runs several commands per device on a single connection; `--job` takes a JSON file with different commands — and different modes — per device, readable from a file or stdin.
- **A dead box costs seconds, not a worker.** Every run starts with a probe (`--no-probe` skips it) — a TCP connect and the SSH banner, no login, 100 boxes at a time — and goes to the boxes that answered; `--probe` alone is a health check of the fleet, with each box's TCP handshake round trip as the kernel measured it and the time its sshd took to answer. See [The probe](#the-probe).
- **Writes are gated.** The probe's question before a partial deployment, `y/N` confirmation, `--dry-run` that shows the diff without committing and `--commit-confirmed N` for changes that undo themselves unless you confirm within N minutes (both Junos), and an opt-in per-device rate limit and cooldown (`--safety-file`).
- **Templates instead of memorised syntax.** `-sC bgp` resolves through a per-vendor JSON template library — *per target*, so the same shortcut sends a Junos router and an EOS switch each their own command. Drop your own in `~/.h-ssh/commands/{dialect}.json` (`junos`, `ios`, `nxos`, `eos`, `none`) to add or override; `junos`, `eos` and `none` ship one.
- **Built to be scripted.** `--json` on stdout, a structured summary line on stderr, meaningful exit codes, and credentials from `HSSH_USER` / `HSSH_PASSWORD` — or import `hssh` and skip the CLI entirely. A whole fleet run fits in one YAML file (`--run fleet.yaml`) that a pipeline step or a jump-host session runs as it is.
- **Built for a maintenance, not just a run.** A session pool keeps one NETCONF session per router open for a whole script; `rpc()` and `--format json|xml` return the router's own data instead of CLI text; `begin()` holds a diffed candidate open until a gate decides; `--rollback N`, commit comments, `--commit-status` and `guarded_commit()` cover the commit-confirmed lifecycle without a `| match` in sight.
- **Two runtime dependencies — or none.** `paramiko` and `junos-eznc` come with the package. Telnet is a raw socket (no stdlib `telnetlib`, so it still works on Python 3.13+), and the `openssh` transport drives the system `ssh` binary, so a checkout on a locked-down jump host with nothing installable still runs shows and edits over `ssh`.

## How it works

```
  hosts / devices.csv / --job                 per device, up to --workers at once
  ──────────────────────────────────           ─────────────────────────────────────
                    │
                    ▼
        ┌───────────────────────┐
        │ probe, no login       │──▶ a dead box: FAIL in seconds
        │ TCP + SSH banner      │    (an edit asks before it goes
        │ 100 boxes at once     │     on without one)
        └───────────────────────┘
                    │ the boxes that answered
                    │                          ┌─ junos    PyEZ over NETCONF (830)
                    ▼                          │           show/edit → PyEZ NETCONF
        ┌───────────────────────┐              │                  lock → load → diff
        │ safety gate (opt-in)  │              │                  → commit → unlock
        │ rate limit 10/device  │──▶ workers ──┼─ ssh      exec_command
        │ cooldown 120s on fail │              │
        │ --safety-file, flock'd│              ├─ openssh  the ssh binary, no deps
        └───────────────────────┘              └─ telnet   raw TCP + prompt match
                    │                                          │
                    └──────────── every edit ──────────────────┴──▶ --audit-log (JSONL)
```

On Junos, show commands run through PyEZ `Device.cli()` over one NETCONF session (a batch shares it); a reply whose text opens with the CLI's refusal (`error: could not resolve file: ...` as the `<output>`, where most refusals come back as an RPC error) is a failure, `'CMD' was refused by the device: ...`, as on the text transports, and is not tried again; a transaction's `tx.show()` raises it too. The NETCONF port defaults to 830 for every Junos call; set the target's port to use NETCONF on 22. Config changes lock the candidate, load, diff, run `commit_check`, commit, and unlock, rolling back if any step fails. Confirming a commit-confirmed (`-eC "commit"`) first reads the commit history: with no commit-confirmed waiting (the timer expired, or it was confirmed already) the device fails with *nothing to confirm* and nothing is sent, because a plain commit there would hide that the change is already gone. It locks too, so another user's uncommitted edits in the shared candidate refuse it — nothing sent, retried like any other lock refusal — instead of riding along with the confirmation. The "don't forget to confirm" reminder prints only when at least one device actually armed a timer. A commit whose reply never arrives is reported as *outcome unknown* and is never retried or rolled back automatically — check the device (and any commit-confirmed timer) first. The NETCONF session verifies the router's host key by default since #150 (a default change: before it, the password went to whoever answered on the port, a router whose key had changed included), on the store the `ssh` transport keeps: `HSSH_NETCONF_HOSTKEY=accept-new` (the default) pins an unknown router in `~/.h-ssh/known_hosts` on first contact, under `[HOST]:PORT`, and refuses one whose key is not the one p
```
