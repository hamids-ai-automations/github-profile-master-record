# pygrpc-native

**Overview:** Drop-in grpcio server with HTTP/2 and gRPC in Rust, outside the GIL. Your servicers stay in Python.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/pygrpc-native](https://github.com/hamids-ai-automations/pygrpc-native) |
| Live website | https://pypi.org/project/pygrpc-native/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-03 |
| Last update | 2026-11-03 |
| Last push | 2026-11-14 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 5 |
| Size | 703 KB |
| Topics | - |

## Objectives

<p align="center">
  <img src="https://raw.githubusercontent.com/pygrpc/pygrpc-native/main/assets/logo.png" alt="pygrpc-native" width="96">
</p>

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, assets, benchmarks, docs, examples, interop, python, src, tests, vendor
- **Total files (tracked in default branch):** 113
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/dco.yml, .github/workflows/perf-comment.yml, .github/workflows/perf.yml, .github/workflows/release.yml, .github/workflows/stale.yml
- **Test files detected:** 26

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 305012 |
| Rust | 113438 |
| Tape | 663 |

**Frameworks / libraries detected:** pytest

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

```bash
pip install pygrpc-native
```

Wheels are available for Linux (x86_64, aarch64) and macOS (arm64, x86_64),
for CPython 3.10 and later.

Change the line that creates the server:

```diff
 from concurrent import futures
-import grpc
+import pygrpc_native

-server = grpc.server(futures.ThreadPoolExecutor(16))
+server = pygrpc_native.server(futures.ThreadPoolExecutor(16))
 greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

## Deployment

Firebase/other hosting declared via homepage field: https://pypi.org/project/pygrpc-native/

## Documentation links

- https://pypi.org/project/pygrpc-native
- https://raw.githubusercontent.com/pygrpc/pygrpc-native/main/assets/logo.png
- https://raw.githubusercontent.com/pygrpc/pygrpc-native/main/assets/how-it-works-light.svg
- https://raw.githubusercontent.com/pygrpc/pygrpc-native/main/assets/benchmark.gif

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/agentshield-ai
- hamids-ai-automations/seo-intelligence-ai
- hamids-ai-automations/github-profile-master-record
- hamids-ai-automations/adwaste-intelligence
- hamids-ai-automations/leadflow-sentinel

## Known issues and limitations

- `NativeGrpcFront` only serves unary and server-streaming methods. Other
  kinds can go through the fallback server, and `server()` and `aio.server()`
  send them there for you.
- There's no TLS yet. `NativeGrpcFront` checks bearer tokens itself, while
  `server()` and `aio.server()` run grpcio interceptors.
- As with grpc-core, binding a Unix socket path replaces any socket file
  already there.
- `SO_REUSEPORT` is set only when `grpc.so_reuseport` is 1. grpcio sets it by
  default, so binding a port that another server already uses works with
  grpcio but fails here.
- Each connection allows up to 1024 concurrent streams unless
  `grpc.max_concurrent_streams` says otherwise. A connection that hasn't
  finished the HTTP/2 preface within 120 s is dropped.
- `maximum_concurrent_rpcs` counts a call to a method on the fallback server
  only while its handler runs, while grpcio also counts calls waiting for a
  worker. With `server()`, such a call over the limit is refused when a worker
  picks it up rather than as it arrives.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/pygrpc-native/blob/main/README.md

```markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/pygrpc/pygrpc-native/main/assets/logo.png" alt="pygrpc-native" width="96">
</p>

<h1 align="center">pygrpc-native</h1>

<p align="center">
  A gRPC server for Python that does the HTTP/2 and gRPC work in Rust, outside the GIL.<br>
  Your handlers stay in Python.
</p>

<p align="center">
  <a href="https://pypi.org/project/pygrpc-native/"><img src="https://img.shields.io/pypi/v/pygrpc-native?logo=pypi&logoColor=white&label=PyPI" alt="PyPI"></a>
  <a href="https://pypi.org/project/pygrpc-native/"><img src="https://img.shields.io/pypi/pyversions/pygrpc-native?logo=python&logoColor=white" alt="Python versions"></a>
  <a href="https://github.com/pygrpc/pygrpc-native/actions/workflows/ci.yml"><img src="https://github.com/pygrpc/pygrpc-native/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <a href="https://github.com/pygrpc/pygrpc-native/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/pygrpc/pygrpc-native/main/assets/how-it-works-light.svg" alt="With grpc.server(), C-core does HTTP/2 and Python handles each call's events one at a time under the GIL. With pygrpc_native.server(), Rust threads do HTTP/2 and the per-call work outside the GIL and hand calls to Python in batches." width="100%">
</p>

When a Python gRPC server runs short of CPU, the usual answers are more server
processes or a rewrite in another language. pygrpc-native moves the gRPC work
itself (HTTP/2, flow control, deadlines, cancellation) into Rust, outside the
GIL, and leaves your servicers, interceptors and generated code as they are.

- **Switching is one line.** `pygrpc_native.server()` and
  `pygrpc_native.aio.server()` take the same arguments as grpcio's servers.
  Clients don't change.
- **It behaves like grpcio.** Status codes, metadata, deadlines,
  cancellation, interceptors and `ServicerContext` work the same way. The few
  differences are listed below, and anything else is a bug.
- **Nothing stops working.** Methods it can't serve itself, such as
  bidirectional streaming or server reflection, are passed to a grpcio server
  running behind it.
- **It's faster under load.** With an empty handler it answers about 1.5x as
  many calls per second as grpcio from one client thread, and about 5x from
  32. See [Benchmarks](#benchmarks).

## Quick start

```bash
pip install pygrpc-native
```

Wheels are available for Linux (x86_64, aarch64) and macOS (arm64, x86_64),
for CPython 3.10 and later.

Change the line that creates the server:

```diff
 from concurrent import futures
-import grpc
+import pygrpc_native

-server = grpc.server(futures.ThreadPoolExecutor(16))
+server = pygrpc_native.server(futures.ThreadPoolExecutor(16))
 greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
 server.add_insecure_port("[::]:50051")
 server.start()
 server.wait_for_termination()
```

For `grpc.aio`:

```diff
+import pygrpc_native.aio
+
-server = grpc.aio.server()
+server = pygrpc_native.aio.server()
 greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
 server.add_insecure_port("[::]:50051")
 await server.start()
 await server.wait_for_termination()
```

For runnable sync and asyncio servers with a grpcio client, see
[examples/README.md](https://github.com/pygrpc/pygrpc-native/blob/main/examples/README.md).

To build from source:

```bash
pip install maturin
maturin develop --release
```

## How it works

Every call reaches Python as an event: an id, the method, the request bytes
and who sent it.

```
grpc client ──HTTP/2──▶ tokio threads (no GIL)
                          │ path → method id
                          ▼
                    event queue ──▶ recv_batch() in Python
                          ◀── respond(call_id, bytes) from any thread
```

Python picks up calls in batches, so a burst costs one trip across the GIL
instead of one per call. `server()` and `aio.server()` are built on top of
this and run your handlers the way grpcio does.

## What runs natively

| | Native | grpcio fallback |
|:--|:-:|:-:|
| Unary and server-streaming methods | ✓ | |
| Client-streaming and bidirectional methods | | ✓ |
| Code generated by any grpcio-tools, and handlers added with `add_generic_rpc_handlers` | ✓ | |
| Server reflection | | ✓ |
| Interceptors | ✓ | ✓ |

The fallback is a grpcio server listening on a Unix socket behind this one.
Calls that go there work but aren't any faster, and `peer()` in them returns
the socket. The native server listens on a single insecure port.

<details>
<summary><b>Server options</b></summary>

<br>

| | Options |
|:--|:--|
| Same as grpcio | `grpc.max_receive_message_length`, `grpc.max_send_message_length`, `grpc.keepalive_time_ms`, `grpc.keepalive_timeout_ms`, `grpc.keepalive_permit_without_calls`, `grpc.max_concurrent_streams`, `grpc.max_metadata_size`, `grpc.absolute_max_metadata_size`, `grpc.so_reuseport`, `maximum_concurrent_rpcs` |
| Raise an error | `grpc.max_connection_age_ms`, `grpc.max_connection_age_grace_ms`, `grpc.max_connection_idle_ms`, `grpc.max_allowed_incoming_connections`, response compression, TLS, `xds=True` |
| Ignored | Everything else. grpcio also ignores the many options that only clients read. This includes the limits on client pings, which are accepted but not enforced, and `grpc.http2.max_frame_size`, which grpc-core's flow control overrides anyway. |

As in grpcio, a value that isn't an integer is ignored.

</details>

<details>
<summary><b>Known differences from grpcio</b></summary>

<br>

- If a unary handler calls `send_initial_metadata()` and then fails, the
  metadata is sent along with the status, so the client sees it as trailing
  metadata.
- If a client doesn't answer a keepalive ping, the connection is closed after
  `grpc.keepalive_timeout_ms`, as gRPC's keepalive docs describe. grpcio waits
  for `grpc.http2.ping_timeout_ms` instead, which is a minute by default.

</details>

<details>
<summary><b>Notes on <code>aio.server()</code></b></summary>

<br>

- Handlers run on the event loop that called `start()`, including uvloop.
- `abort()` raises `grpc.aio.AbortError`. If the client cancels or the
  deadline passes, the handler gets `asyncio.CancelledError`, as in grpc.aio.
- Streaming handlers can yield from an async generator or call
  `context.write()`.
- Handlers that aren't coroutines run in `migration_thread_pool` with
  grpcio's sync context, where `abort()` returns instead of raising.
- The fallback, the options and the differences above are the same as for
  the sync server.

</details>

## Low-level API

`NativeGrpcFront` is the layer under `server()`. You receive each call as an
event and answer it by id:

```python
import threading
from pygrpc_native import EVENT_CALL, NativeGrpcFront

front = NativeGrpcFront("0.0.0.0:50051", [("/echo.Echo/Say", False)])
front.start()

def serve():
    while (events := front.recv_batch(64)) is not None:
        for kind, call_id, method_id, payload, client_key in events:
            if kind == EVENT_CALL:
                front.respond(call_id, payload)

threading.Thread(target=serve).start()
```

Streaming, call details, response metadata, bearer tokens and metrics are
covered in [docs/low-level-api.md](https://github.com/pygrpc/pygrpc-native/blob/main/docs/low-level-api.md).

## Benchmarks

<p align="center">
  <img src="https://raw.githubusercontent.com/pygrpc/pygrpc-native/main/assets/benchmark.gif" alt="benchmarks/echo.py against grpc.server(), then against pygrpc_native.server()" width="100%">
</p>

An empty unary handler on an Apple M4 Pro, called by grpcio clients on the
same machine. Calls per second, median of three runs:

| Server | 1 client thread | 32 client threads (8 processes x 4) |
|:--|--:|--:|
| `grpc.server()` | 7,739 | 10,955 |
| `grpc.aio.server()` | 4,804 | 10,322 |
| `pygrpc_native.server()` | 11,428 | 57,419 |
| `pygrpc_native.aio.ser
```
