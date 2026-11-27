# k8s-ai-bench

**Overview:** A benchmark to evaluate LLMs on Kubernetes tasks

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/k8s-ai-bench](https://github.com/hamids-ai-automations/k8s-ai-bench) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-21 |
| Last update | 2026-11-21 |
| Last push | 2026-11-21 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | Go |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 15 |
| Size | 2682 KB |
| Topics | - |

## Objectives

# k8s-ai-bench

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, dev, docs, pkg, scripts, site, tasks, tools
- **Total files (tracked in default branch):** 466
- **CI workflows:** .github/workflows/ci-periodic.yaml, .github/workflows/ci-presubmit.yaml, .github/workflows/k8s-bench-evals.yaml, .github/workflows/release.yaml, .github/workflows/static.yaml
- **Test files detected:** 0

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Go | 114016 |
| Shell | 99054 |
| HTML | 26725 |
| JavaScript | 11119 |
| Makefile | 5403 |
| Python | 478 |

**Frameworks / libraries detected:** none detected from dependency files

**Dependencies:** none detected

## Important source files

- `go.mod`

## Installation and setup

No installation instructions found in the README.

## Deployment

No deployment configuration detected.

## Documentation links

- http://localhost:8000
- https://gke-labs.github.io/k8s-ai-bench
- https://www.vcluster.com/docs/vcluster

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/cfgaudit

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/k8s-ai-bench/blob/main/README.md

```markdown
# k8s-ai-bench

`k8s-ai-bench` is a benchmark for assessing the performance of LLM models for Kubernetes related tasks. It evaluates AI agents (like `kubectl-ai`) on their ability to perform real-world Kubernetes operations such as creating deployments, debugging crash loops, and scaling applications.

## 📊 Live Dashboard

See [k8s-ai-bench live leaderboard](https://gke-labs.github.io/k8s-ai-bench/) for the latest benchmark results.

The leaderboard shows run results for widely used proprietary and open models over a few run types:

* **Pass@1**: Can the agent solve the task on the first try? This measures raw capability and immediate correctness.
* **Pass@5**: Can the agent solve the task at least once in 5 attempts? This shows if the agent can eventually find a solution.
* **Pass^5**: Does the agent solve the task every single time? This measures reliability and consistency, which is crucial for autonomous usage.



## 🚀 Quick Start

### 1. Build the Binary
```sh
go build
```

### 2. Run an Evaluation
Run the benchmark against your agent binary. Results will be saved to the `.build` directory.
```sh
# Basic usage
./k8s-ai-bench run --agent-bin <path/to/kubectl-ai> --output-dir .build/k8s-ai-bench

# Run a specific task type (e.g., scaling tasks)
./k8s-ai-bench run --agent-bin <path/to/kubectl-ai> --task-pattern "scale" --output-dir .build/k8s-ai-bench
```

## 🛠 Usage Guide

### `run` Subcommand
The `run` subcommand executes the benchmark evaluations. It creates ephemeral clusters to ensure test isolation. We support two platforms for the test environment: **Kind** (default) and **vCluster**.

**vCluster Prerequisites:**
For a detailed step-by-step guide on setting up and using vCluster, see [vCluster Guide](https://github.com/hamids-ai-automations/k8s-ai-bench/blob/main/docs/vcluster.md).

To use `vcluster`, you must have:
* The `vcluster` [CLI](https://www.vcluster.com/docs/vcluster/) installed.
* A running host Kubernetes cluster.
* A kubecontext to connect to the host cluster (passed via `--host-cluster-context`).


```sh
# Run with specific LLM provider and model
./k8s-ai-bench run \
  --agent-bin <path/to/kubectl-ai> \
  --llm-provider gemini \
  --models gemini-2.5-pro-preview-03-25 \
  --task-pattern fix \
  --output-dir .build/k8s-ai-bench
```

**Common Flags:**
| Flag | Description | Default |
|------|-------------|---------|
| `--agent-bin` | Path to kubectl-ai binary (Required) | - |
| `--output-dir` | Directory to write results (Required) | - |
| `--task-pattern` | RegEx pattern to filter tasks (e.g. 'pod', 'fix') | - |
| `--llm-provider` | LLM provider ID (e.g. 'gemini', 'openai') | gemini |
| `--models` | Comma-separated list of models | gemini-2.5-pro... |
| `--concurrency` | Number of parallel tasks (0 = auto) | 0 |
| `--cluster-provider` | Cluster provider to use (`kind` or `vcluster`) | kind |
| `--host-cluster-context` | Host cluster context for vcluster (Required if provider is vcluster) | - |

### `analyze` Subcommand
Process and summarize results from previous runs.

```sh
# Generate a Markdown report
./k8s-ai-bench analyze --input-dir .build/k8s-ai-bench --results-filepath report.md

# Generate JSONL for visualization
./k8s-ai-bench analyze --input-dir .build/k8s-ai-bench --output-format jsonl --results-filepath site/combined_results.jsonl
```

## 💻 Development Scripts
For a streamlined development loop, use the scripts in `dev/ci/periodics/`:

- **Run Evaluation Loop**: Runs evaluations multiple times to test consistency.
  ```sh
  ./dev/ci/periodics/run-eval-loop.sh --iterations 5 --task-pattern "create"
  ```
- **Run Single Evaluation**:
  ```sh
  TEST_ARGS="--task-pattern=fix-probes" ./dev/ci/periodics/run-evals.sh
  ```
- **Analyze Results**:
  ```sh
  ./dev/ci/periodics/analyze-evals.sh --show-failures
  ```

## 📈 Visualizing Results Locally

The `site` directory contains a static website (Vue.js based) for visualizing benchmark results.

1.  **Generate Data**:
    ```sh
    ./k8s-ai-bench analyze --input-dir .build/k8s-ai-bench --output-format jsonl --results-filepath site/combined_results.jsonl
    ```
2.  **Serve Locally**:
    ```sh
    cd site
    python3 -m http.server
    ```
3.  **View**: Open [http://localhost:8000](http://localhost:8000)

## 🤝 Contributions
We welcome contributions! Please check out the [contributions guide](https://github.com/hamids-ai-automations/k8s-ai-bench/blob/main/contributing.md).

```
