# pysad

**Overview:** Streaming anomaly detection in Python: 16 online detectors (xStream, LODA, RS-Hash, Half-Space Trees, RRCF…) plus calibration and prequential evaluation for real-time data.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/pysad](https://github.com/hamids-ai-automations/pysad) |
| Live website | https://pysad.readthedocs.io/en/stable/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-29 |
| Last update | 2026-10-29 |
| Last push | 2026-10-30 |
| Default branch | master |
| License | BSD-3-Clause |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 39 |
| Size | 2085 KB |
| Topics | - |

## Objectives

<p align="center"><b>English</b> · <a href="https://github.com/selimfirat/pysad/blob/master/README_zh.md">简体中文</a></p>

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .circleci, .github, .qlty, benchmarks, docs, examples, pysad, tests
- **Total files (tracked in default branch):** 300
- **CI workflows:** .github/workflows/all-checks.yml, .github/workflows/benchmark.yml, .github/workflows/codeql.yml, .github/workflows/coverage.yml, .github/workflows/dependency-review.yml, .github/workflows/docs.yml, .github/workflows/examples.yml, .github/workflows/greetings.yml, .github/workflows/jupyterlite.yml, .github/workflows/lint-workflows.yml, .github/workflows/pr-labels.yml, .github/workflows/publish.yml, .github/workflows/scorecard.yml, .github/workflows/stale.yml
- **Test files detected:** 71

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 809148 |
| Jupyter Notebook | 14101 |
| Shell | 168 |

**Frameworks / libraries detected:** NumPy, pandas, pytest, requests

**Dependencies:** none detected

## Important source files

- `pyproject.toml`

## Installation and setup

```bash
pip install pysad
```

Or with Conda / Mamba / Pixi:

```bash
conda install -c conda-forge pysad
```

PySAD supports Python 3.10 to 3.14 on Linux, macOS and Windows. Every detector works after installation, with no optional extras.

To install the latest development version from `master`:

```bash
pip install git+https://github.com/selimfirat/pysad.git
```

## Deployment

Firebase/other hosting declared via homepage field: https://pysad.readthedocs.io/en/stable/

## Documentation links

- https://pysad.readthedocs.io/en/stable
- https://raw.githubusercontent.com/selimfirat/pysad/master/docs/images/logo.svg
- https://pypi.org/project/pysad
- https://anaconda.org/conda-forge/pysad
- https://doi.org/10.5281/zenodo.22983312
- https://dev.azure.com/selimfirat/pysad/_build/latest?definitionId=2&branchName=master
- https://results.pre-commit.ci/latest/github/selimfirat/pysad/master
- https://results.pre-commit.ci/badge/github/selimfirat/pysad/master.svg
- https://pysad.readthedocs.io/en/stable/getting_started.html
- https://pysad.readthedocs.io/en/stable/guides/index.html
- https://pysad.readthedocs.io/en/stable/benchmark.html
- https://pysad.readthedocs.io/en/stable/detectors.html
- https://pysad.readthedocs.io/en/stable/api.html
- https://selimfirat.github.io/pysad/lab/index.html?path=nyc_taxi_alerts.ipynb
- https://colab.research.google.com/github/selimfirat/pysad/blob/master/examples/quickstart.ipynb
- https://raw.githubusercontent.com/selimfirat/pysad/master/docs/images/stream.svg
- https://scholar.google.com/scholar?cites=3884618599898298487
- https://pysad.readthedocs.io/en/latest/contributing.html
- https://jupyterlite.rtfd.io/en/latest/_static/badge.svg
- https://colab.research.google.com/assets/colab-badge.svg
- https://pysad.readthedocs.io/en/stable/guides/choose_detector.html
- http://odds.cs.stonybrook.edu
- https://pysad.readthedocs.io/en/stable/benchmarks/methodology.html
- https://pysad.readthedocs.io/en/stable/benchmarks/datasets.html
- https://pysad.readthedocs.io/en/stable/benchmarks/run.html
- https://pysad.readthedocs.io/en/stable/contributing.html
- https://semver.org
- https://trunkbaseddevelopment.com

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/leadflow-sentinel
- hamids-ai-automations/ghl-automation-engine
- hamids-ai-automations/gemini-agent-reliability-kit
- hamids-ai-automations/envscope
- hamids-ai-automations/searchpulse-ai

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/pysad/blob/master/README.md

```markdown
<p align="center"><b>English</b> · <a href="https://github.com/selimfirat/pysad/blob/master/README_zh.md">简体中文</a></p>

<p align="center">
  <img src="https://raw.githubusercontent.com/selimfirat/pysad/master/docs/images/logo.svg" alt="PySAD" width="360">
</p>

<h3 align="center">One pass. Every outlier.</h3>

<p align="center">
  Streaming anomaly detection in Python. PySAD scores each data point when it arrives,<br>
  with 16 streaming detectors, calibrated alerts and streaming evaluation.
</p>

<p align="center">
  <a href="https://pypi.org/project/pysad/"><img src="https://img.shields.io/pypi/v/pysad?style=flat-square&logo=pypi&logoColor=white&label=PyPI" alt="PyPI version"></a>
  <a href="https://anaconda.org/conda-forge/pysad"><img src="https://img.shields.io/conda/vn/conda-forge/pysad?style=flat-square&logo=condaforge&logoColor=white&label=conda-forge" alt="conda-forge version"></a>
  <a href="https://pypi.org/project/pysad/"><img src="https://img.shields.io/pypi/pyversions/pysad?style=flat-square&logo=python&logoColor=white&label=Python" alt="Python versions"></a>
  <a href="https://github.com/selimfirat/pysad/blob/master/LICENSE"><img src="https://img.shields.io/github/license/selimfirat/pysad?style=flat-square&label=license" alt="License"></a>
  <a href="https://doi.org/10.5281/zenodo.22983312"><img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22983312-0741AD?style=flat-square" alt="DOI"></a>
  <br>
  <a href="https://github.com/selimfirat/pysad/actions/workflows/coverage.yml"><img src="https://img.shields.io/github/actions/workflow/status/selimfirat/pysad/coverage.yml?branch=master&style=flat-square&logo=githubactions&logoColor=white&label=tests" alt="Tests"></a>
  <a href="https://dev.azure.com/selimfirat/pysad/_build/latest?definitionId=2&branchName=master"><img src="https://img.shields.io/azure-devops/build/selimfirat/pysad/2/master?style=flat-square&logo=azurepipelines&label=Azure%20Pipelines" alt="Azure Pipelines"></a>
  <a href="https://circleci.com/gh/selimfirat/pysad"><img src="https://img.shields.io/circleci/build/github/selimfirat/pysad/master?style=flat-square&logo=circleci&label=CircleCI" alt="CircleCI"></a>
  <a href="https://results.pre-commit.ci/latest/github/selimfirat/pysad/master"><img src="https://results.pre-commit.ci/badge/github/selimfirat/pysad/master.svg" alt="pre-commit.ci status"></a>
  <a href="https://coveralls.io/github/selimfirat/pysad?branch=master"><img src="https://img.shields.io/coverallsCoverage/github/selimfirat/pysad?branch=master&style=flat-square&logo=coveralls&label=coverage" alt="Coverage"></a>
  <a href="https://pysad.readthedocs.io/en/stable/"><img src="https://img.shields.io/readthedocs/pysad?style=flat-square&logo=readthedocs&logoColor=white&label=docs" alt="Documentation"></a>
  <a href="https://github.com/selimfirat/pysad/commits/master"><img src="https://img.shields.io/github/last-commit/selimfirat/pysad?style=flat-square&label=last%20commit" alt="Last commit"></a>
</p>

<p align="center">
  <a href="https://pysad.readthedocs.io/en/stable/"><b>Documentation</b></a> ·
  <a href="https://pysad.readthedocs.io/en/stable/getting_started.html">Getting started</a> ·
  <a href="https://pysad.readthedocs.io/en/stable/guides/index.html">How-to guides</a> ·
  <a href="https://pysad.readthedocs.io/en/stable/benchmark.html">Benchmarks</a> ·
  <a href="https://pysad.readthedocs.io/en/stable/detectors.html">Detectors</a> ·
  <a href="https://pysad.readthedocs.io/en/stable/api.html">API</a> ·
  <a href="https://selimfirat.github.io/pysad/lab/index.html?path=nyc_taxi_alerts.ipynb">Live demo</a> ·
  <a href="https://colab.research.google.com/github/selimfirat/pysad/blob/master/examples/quickstart.ipynb">Try it in Colab</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/selimfirat/pysad/master/docs/images/stream.svg" alt="Three sensor readings stream in from left to right. A Robust Random Cut Forest scores each point when the point arrives. Conformal calibration raises alerts at a spike, a short plateau and a dip." width="100%">
</p>

<p align="center"><sub>A Robust Random Cut Forest scores three synthetic sensors one point at a time. Conformal calibration converts each score into the fraction of recent scores that it exceeds, and raises an alert at 0.995.</sub></p>

## Why PySAD

A batch detector needs the whole dataset before it can score a point. A stream does not give you the whole dataset. Points arrive one at a time, the data drifts (its distribution changes over time), and you must decide about each point before the next point arrives. PySAD is built for this setting. More than 60 publications on [Google Scholar](https://scholar.google.com/scholar?cites=3884618599898298487) cite it, and [30+ public repositories](https://github.com/selimfirat/pysad/network/dependents) on GitHub use it.

<table>
<tr>
<td width="50%" valign="top">

#### Built for streams

Every detector learns from and scores one point at a time with `fit_partial`, `score_partial` and `fit_score_partial`. Most detectors keep a window, a sketch or a set of trees of fixed size instead of the whole stream.

</td>
<td width="50%" valign="top">

#### 17 detectors from published papers

From robust statistics (MAD, Seasonal Hybrid ESD) to forests, sketches and projections (Half-Space Trees, Robust Random Cut Forest, RS-Hash, xStream, LODA). Each detector cites its paper, and the [detector catalog](https://pysad.readthedocs.io/en/stable/detectors.html) lists its input and memory.

</td>
</tr>
<tr>
<td valign="top">

#### From scores to alerts

The conformal calibrator converts a raw score into the fraction of recent scores that it exceeds. A threshold such as `0.99` then has the same meaning for every detector.

</td>
<td valign="top">

#### Evaluate on the stream

Streamers replay data one point at a time, and 17 labeled benchmark datasets download on first use. Metrics such as AUROC, AUPR, precision and recall update after every point.

</td>
</tr>
<tr>
<td valign="top">

#### Your batch models on a stream

Wrap any [PyOD](https://github.com/yzhao062/pyod) detector to train it again on a sliding window of recent points.

</td>
<td valign="top">

#### A complete pipeline

Preprocessors, random projections, score postprocessors, ensemblers and running statistics work with every detector.

</td>
</tr>
</table>

Batch outlier detectors such as [PyOD](https://github.com/yzhao062/pyod) train on a fixed dataset and must train again to use new data. PySAD detectors learn from every point, and PySAD can still run PyOD models on a stream with `ReferenceWindowModel`. General online learning frameworks such as [River](https://github.com/online-ml/river) treat anomaly detection as one module among many. PySAD is only about streaming anomaly detection: 17 detectors, with calibration, postprocessing, ensembling and evaluation around them.

## Installation

```bash
pip install pysad
```

Or with Conda / Mamba / Pixi:

```bash
conda install -c conda-forge pysad
```

PySAD supports Python 3.10 to 3.14 on Linux, macOS and Windows. Every detector works after installation, with no optional extras.

To install the latest development version from `master`:

```bash
pip install git+https://github.com/selimfirat/pysad.git
```

For an editable installation with development dependencies, follow the [contributing guide](https://pysad.readthedocs.io/en/latest/contributing.html).

## Quick start

[![Open in JupyterLite](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://selimfirat.github.io/pysad/lab/index.html?path=nyc_taxi_alerts.ipynb)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/selimfirat/pysad/blob/master/examples/quickstart.ipynb)

Score a stream point by point, and measure the detector while it runs:

```python
import numpy as np
from pysad.evaluation import AUROCMetric
from pysad.models import LODA
from pysad.utils import ArrayStreamer

# A str
```
