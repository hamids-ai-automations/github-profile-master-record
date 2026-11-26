# flimanalyzer

**Overview:** Python package for analysis of Fluorescence Lifetime Imaging Microscopy (FLIM) data.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/flimanalyzer](https://github.com/hamids-ai-automations/flimanalyzer) |
| Live website | not deployed / not declared |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-03 |
| Last update | 2026-11-03 |
| Last push | 2026-11-03 |
| Default branch | main |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 6 |
| Size | 59725 KB |
| Topics | - |

## Objectives

# <img src="flim/resources/flimanalyzer.png" alt="" width="80" align="top"> FLIMAnalyzer

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .github, docs, flim, scripts, tests
- **Total files (tracked in default branch):** 344
- **CI workflows:** .github/workflows/docker.yml, .github/workflows/release.yml, .github/workflows/testpypi.yml, .github/workflows/tests.yml
- **Test files detected:** 50

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 908532 |
| Dockerfile | 2338 |

**Frameworks / libraries detected:** Next.js, NumPy, pandas, pytest

**Dependencies:** none detected

## Important source files

- `flim/gui/app.py`
- `pyproject.toml`

## Installation and setup

No installation instructions found in the README.

## Deployment

No deployment configuration detected.

## Documentation links

- https://docs.astral.sh/uv
- https://readthedocs.org/projects/flimanalyzer/badge/?version=latest
- https://flimanalyzer.readthedocs.io/en/latest
- https://zenodo.org/badge/DOI/10.5281/zenodo.23426563.svg
- https://doi.org/10.5281/zenodo.23426563
- https://flimanalyzer.readthedocs.io
- https://pytorch.org
- https://www.prefect.io
- https://download.pytorch.org/whl/cu128`
- https://pytorch.org/get-started/locally
- https://download.pytorch.org/whl/cu126
- https://download.pytorch.org/whl/cpu
- http://prefect.example.org:4200/api`
- https://my-prefect-server/api
- http://127.0.0.1:4200/api`
- http://127.0.0.1:4200
- https://www.dask.org
- https://docs.prefect.io/v3/develop/task-run-limits
- https://doi.org/10.1002/jbio.202400426
- https://doi.org/10.1186/s10020-026-01605-2
- https://doi.org/10.5281/zenodo.23438157
- https://doi.org/10.5281/zenodo.23426564

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

Full README: https://github.com/hamids-ai-automations/flimanalyzer/blob/main/README.md

```markdown
# <img src="flim/resources/flimanalyzer.png" alt="" width="80" align="top"> FLIMAnalyzer

[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://github.com/uvaKCCI/flimanalyzer/blob/main/pyproject.toml) [![Tests](https://github.com/uvaKCCI/flimanalyzer/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/uvaKCCI/flimanalyzer/actions/workflows/tests.yml) [![codecov](https://codecov.io/gh/uvaKCCI/flimanalyzer/branch/main/graph/badge.svg)](https://codecov.io/gh/uvaKCCI/flimanalyzer) [![Documentation Status](https://readthedocs.org/projects/flimanalyzer/badge/?version=latest)](https://flimanalyzer.readthedocs.io/en/latest/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23426563.svg)](https://doi.org/10.5281/zenodo.23426563)

Python package for analysis of Fluorescence Lifetime Imaging Microscopy (FLIM) data.

Documentation: https://flimanalyzer.readthedocs.io

## Requirements

* Python 3.12 or later
* All Python dependencies, including [PyTorch](https://pytorch.org) and [Prefect](https://www.prefect.io), are declared in `pyproject.toml` and installed automatically.

## Installation

### From PyPI with uv (recommended)

[uv](https://docs.astral.sh/uv/) creates a virtual environment in `.venv` (installing a matching Python if needed). Then install FLIMAnalyzer with its graphical user interface (GUI) into it:

    uv venv --python 3.12
    source .venv/bin/activate    # Windows: .venv\Scripts\activate
    uv pip install "flimanalyzer[gui]"

The `gui` extra installs the GUI. Without it, `uv pip install flimanalyzer` installs only what [batch mode](#run-flimanalyzer-in-batch-mode) needs, for example on a computing cluster. Add `dask` for the optional Dask support (see [Concurrent and distributed execution](#concurrent-and-distributed-execution)), e.g. `"flimanalyzer[gui,dask]"`.

### From PyPI with pip

    python3.12 -m venv .venv
    source .venv/bin/activate    # Windows: .venv\Scripts\activate
    pip install "flimanalyzer[gui]"

### PyTorch and the GPU

Installed from PyPI, FLIMAnalyzer gets PyTorch from PyPI, which provides a different build on each platform:

* **Linux:** the PyPI build includes CUDA, so an NVIDIA GPU is used if its driver is recent enough.
* **Windows:** the PyPI build is CPU-only. For an NVIDIA GPU, install with `uv pip install "flimanalyzer[gui]" --torch-backend=cu128`, or with pip install the CUDA build first: `pip install torch --index-url https://download.pytorch.org/whl/cu128`. See [pytorch.org](https://pytorch.org/get-started/locally/) for other CUDA versions.
* **macOS:** only Apple Silicon is supported, because current PyTorch versions are not available for Intel Macs. The PyPI build uses the Apple GPU (MPS).

### Latest development version

To install the current state of the repository, clone it and let uv create the environment. `uv sync` installs FLIMAnalyzer with the GUI in editable mode, with the exact package versions from `uv.lock` (the versions the tests run with). On Windows and Linux (x86_64), it installs the CUDA 12.8 build of PyTorch:

    git clone https://github.com/uvaKCCI/flimanalyzer.git
    cd flimanalyzer
    uv sync

Without the GUI, with the test dependencies, or with Dask support:

    uv sync --no-group gui
    uv sync --extra test
    uv sync --extra dask

With pip, in a virtual environment in the cloned folder: `pip install -e ".[gui]"`.

### With Docker

The Docker images run only [batch mode](#run-flimanalyzer-in-batch-mode). They don't include the GUI. Each release is published to the GitHub Container Registry:

| Image | |
|---|---|
| `ghcr.io/uvakcci/flimanalyzer:<version>`, `:latest` | with the CUDA build of PyTorch (x86_64, several GB) |
| `ghcr.io/uvakcci/flimanalyzer:<version>-cpu`, `:latest-cpu` | CPU only (x86_64 and ARM), much smaller |

    docker pull ghcr.io/uvakcci/flimanalyzer:latest-cpu

To build an image from the repository instead: with the CUDA 12.8 build of PyTorch, with the build for another CUDA version (here 12.6), with the CPU-only build, or with Dask support:

    docker build -t flimanalyzer .
    docker build -t flimanalyzer:cu126 --build-arg TORCH_INDEX=https://download.pytorch.org/whl/cu126 .
    docker build -t flimanalyzer:cpu --build-arg TORCH_INDEX=https://download.pytorch.org/whl/cpu .
    docker build -t flimanalyzer:dask --build-arg EXTRAS=dask .

`TORCH_INDEX` replaces PyTorch with the build from that PyTorch package index, in the same PyTorch version (the one in `uv.lock`, currently 2.11.0). Choose the CUDA version that the NVIDIA driver of your computer supports. PyTorch 2.11.0 is available for CUDA 12.6 (`cu126`), 12.8 (`cu128`, the default), 12.9 (`cu129`) and 13.0 (`cu130`).

`EXTRAS=gui` stops the build with an error, because the images do not support a display.

## Start FLIMAnalyzer with the GUI

With uv, no activation is needed:

    uv run flimanalyzer

In an activated environment:

    flimanalyzer

To open data files (tab- or comma-separated) right away, each in its own window:

    uv run flimanalyzer -i results.txt more-results.csv

Run `flimanalyzer --help` for all command line options.

## Using a GPU

The autoencoder tools (Autoencoder: Train, Run and Augment Data, and the FLIM Data Augmentation Tuning and FLIM Feature Analysis workflows) have a **Device** setting, in the GUI and in batch mode:

* `auto` (default): an NVIDIA GPU (`cuda`) if available, otherwise the Apple GPU (`mps`), otherwise the CPU.
* `cpu`, `cuda` or `mps`: uses that device, or the CPU if it is not available.

Which GPU can be used depends on the PyTorch build that was installed (see [Installation](#installation)). Trained models are saved so that they don't need a GPU, so a model trained on a GPU can also be used on a computer without one.

## Run FLIMAnalyzer in batch mode

`flimbatch` imports data files and runs tools or workflows on them without opening the GUI, for example on a computing cluster. It takes its settings from a settings file saved in the GUI (File > Export Settings...): the import settings and the settings of each tool. A tool's dialog can add its settings to such a file with Save Settings..., which keeps the file's other sections. Load Settings... reads the tool's own section back.

    uv run flimbatch -i data/ -o results/ -c settings.json \
        --run Summarize --run "Basic FLIRR Analysis"

The imported table is saved as `results/Imported.txt`, and each tool's results in `results/<tool name>/`. A workflow column that is not in the data (for example `FAD a1%` for `FAD a1[%]`) is an error. `--allow-guesses` uses the closest column instead and lists it in the run summary. The exit code is 1 if a check or task failed. Run `flimbatch --help` for all options.

`flimanalyzer --batch …` does the same as `flimbatch …`. On Windows, use `flimbatch`: `flimanalyzer` starts without a console there, so its messages are not shown.

### In Docker

The image runs `flimbatch`. Make the folder with the data and the settings file available inside the container as `/work`:

    docker run --rm -v "$PWD:/work" ghcr.io/uvakcci/flimanalyzer:latest-cpu \
        -i data/ -o results/ -c settings.json --run Summarize --no-prefect-server

* On Linux, add `-u $(id -u)` so that the result files belong to you.
* With the CUDA image, add `--gpus all` to use the GPU.
* With `--no-prefect-server`, each run uses a temporary Prefect server. To report to a Prefect server instead, pass its address, for example `-e PREFECT_API_URL=http://prefect.example.org:4200/api`.

## Prefect server

FLIMAnalyzer runs analyses and workflows as [Prefect](https://www.prefect.io) flows. At startup it looks for a Prefect server in this order:

1. The server configured in the active Prefect profile or in the `PREFECT_API_URL` environment variable, e.g.

       prefect profile use <profile>
       # or
       export PREFECT_API_URL=https://my-prefect-server/api

2. A server already running locally at `http://127.0.0.1:4200/api`.
3. If none is found, FLIMAnalyzer start
```
