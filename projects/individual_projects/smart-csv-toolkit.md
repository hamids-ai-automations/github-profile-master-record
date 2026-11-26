# Smart_CSV_Toolkit

**Overview:** Streamlit app for LLM-assisted CSV cleaning, metadata inference, and multi-file merging, with guided decision-tree workflows.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/Smart_CSV_Toolkit](https://github.com/hamids-ai-automations/Smart_CSV_Toolkit) |
| Live website | https://smart-csv-toolkit.onrender.com |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-29 |
| Last update | 2026-10-29 |
| Last push | 2026-10-30 |
| Default branch | main |
| License | none declared |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 1 |
| Size | 607 KB |
| Topics | - |

## Objectives

# Smart CSV Toolkit — LLM‑Assisted CSV Cleaning & Metadata Inference

## Features

* **Guided CSV Cleaning**

  * Configurable steps defined in `table_steps.json` (sliders, selects, text inputs rendered dynamically)
  * LLM proposes **5 non‑redundant** cleaning suggestions (excludes already‑selected steps)
  * Any natural‑language instruction → **executable Python code** that mutates `df` in place
    *(code is displayed before execution for review)*

* **Metadata Inference & Usability**

  * Infers semantic types like: *Categorical, Text, Numerical, Datetime, GPS Coordinates, Email, Phone, Currency, Percentage, Color Code, Image/Video/Document/General URL, Identifier/ID, Null‑heavy, Constant/Low Variance*, etc.
  * Context‑aware visualizations:

    * Categorical → top‑k bar chart
    * Text → word cloud
    * Numerical → box plot + correlation heatmap
    * Datetime → time‑series line plot
    * GPS → map from `lat,lon`

## Technical architecture

- **Top-level directories:** .devcontainer, .github, .streamlit, DB, LLM, docs, tests, vector_store
- **Total files (tracked in default branch):** 35
- **CI workflows:** .github/workflows/ci-cd.yml
- **Test files detected:** 5

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 175840 |
| Dockerfile | 1460 |

**Frameworks / libraries detected:** BeautifulSoup, LangChain, NumPy, OpenAI API, Streamlit, pandas, requests

**Dependencies:** Pillow, beautifulsoup4, chromadb, dateparser, dtale, geopy, imbalanced-learn, joblib, langchain, matplotlib, nltk, numpy, openai, pandas, plotly, python-dotenv, pyvis, requests, scikit-learn, seaborn, streamlit, streamlit-agraph, tldextract, torch, transformers, wordcloud

## Important source files

- `app.py`
- `docker-compose.yml`
- `requirements.txt`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://smart-csv-toolkit.onrender.com

## Documentation links

- https://render.com
- https://smart-csv-toolkit.onrender.com
- https://smart-csv-toolkit.onrender.com/**
- https://openrouter.ai/keys
- http://localhost:9000/generate

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

* Real sandboxing for LLM‑generated code (`__builtins__ = {}` alone doesn't cut it — see #4)
* Non‑LLM heuristics for the type-inference fallback, so it degrades better without an API key
* Undo/history for Tab 2's in‑place cleaning steps (#13)
* Built‑in CSV join diagnostics and key suggestions
* Executable cleaning **playback** (export steps as a Python script)
* Multi‑page layout (Cleaner / Inspector / Recipes / Logs)

---

## README source

Full README: https://github.com/hamids-ai-automations/Smart_CSV_Toolkit/blob/main/README.md

```markdown
# Smart CSV Toolkit — LLM‑Assisted CSV Cleaning & Metadata Inference

**Live demo → https://smart-csv-toolkit.onrender.com/** (free-tier Render instance, so the first load after idle can take 30-60s to spin up)

A Streamlit app for cleaning messy CSVs, figuring out what's actually in each column, merging multiple files, and generating plots without writing pandas by hand every time. I built this mostly to stop rewriting the same `df.dropna()` / dtype-coercion boilerplate for every one-off dataset — an LLM proposes the cleaning code, you read it before it runs, and every action gets logged to SQLite so you can see what happened after the fact.

> **TL;DR**
> • **Tab 1 – CSV Cleaner:** choose built‑in steps from `table_steps.json`, get **LLM suggestions**, optionally apply **LLM‑generated Python code** (shown before execution), and download the cleaned CSV.
> • **Tab 2 – Metadata Inspector:** upload/merge up to 5 CSVs, **infer column types**, preview media/links, and **auto‑generate plots** (with or without LLM help).
> • **Advanced:** interactive **decision‑tree UI** for guided cleaning; optional **custom LLM API**; session/file/event **audit logging** with timestamped CSVs.

---

## Screenshots

A quick walkthrough of the CSV Cleaner tab (Tab 1), using a small sample CSV with a missing `age` value, a missing `city`, a missing `signup_date`, and a duplicated row:

**1. Upload a CSV** — drag-and-drop or browse, 25MB limit enforced client-side and server-side.

![Upload CSV](https://raw.githubusercontent.com/hamids-ai-automations/Smart_CSV_Toolkit/main/docs/screenshots/01_upload.png)

**2. Preview the raw data** — the app renders the first N rows immediately so you can sanity-check what was uploaded before picking any cleaning steps. Note the missing `age`, `city`, and `signup_date` cells.

![Preview of uploaded data](https://raw.githubusercontent.com/hamids-ai-automations/Smart_CSV_Toolkit/main/docs/screenshots/02_preview.png)

**3. Pick a cleaning step** — here, `Impute Missing Values` (strategy: mean) is checked from the config-driven step list defined in `table_steps.json`.

![Selecting the Impute Missing Values step](https://raw.githubusercontent.com/hamids-ai-automations/Smart_CSV_Toolkit/main/docs/screenshots/03_steps_selected.png)

**4. Run the pipeline and preview the cleaned result** — the missing `age` values (`None`) have been imputed to the column mean (`226.4`, pulled up by the `999` outlier in the sample — a good illustration of why `Remove Outliers` is a separate, composable step).

![Cleaned data preview after running the pipeline](https://raw.githubusercontent.com/hamids-ai-automations/Smart_CSV_Toolkit/main/docs/screenshots/04_cleaned_result.png)

---

## Features

* **Guided CSV Cleaning**

  * Configurable steps defined in `table_steps.json` (sliders, selects, text inputs rendered dynamically)
  * LLM proposes **5 non‑redundant** cleaning suggestions (excludes already‑selected steps)
  * Any natural‑language instruction → **executable Python code** that mutates `df` in place
    *(code is displayed before execution for review)*

* **Metadata Inference & Usability**

  * Infers semantic types like: *Categorical, Text, Numerical, Datetime, GPS Coordinates, Email, Phone, Currency, Percentage, Color Code, Image/Video/Document/General URL, Identifier/ID, Null‑heavy, Constant/Low Variance*, etc.
  * Context‑aware visualizations:

    * Categorical → top‑k bar chart
    * Text → word cloud
    * Numerical → box plot + correlation heatmap
    * Datetime → time‑series line plot
    * GPS → map from `lat,lon`
    * Color codes → swatches
    * Email/Phone → frequency bars
    * URLs → previews (images, videos) + **webpage summarization** via LLM for general links

* **Multi‑CSV Merge UI**

  * Upload up to **5** CSVs, configure pairwise joins (keys + type), then merge CSVs with one click

* **Interactive Cleaning Graph**

  * AGraph‑based decision tree per column; **click leaf nodes** to apply LLM‑generated cleaning for the chosen path; executed code is surfaced and actions are tracked

* **Exploration via D‑Tale**

  * One‑click link to open D‑Tale and explore the current DataFrame

* **Audit Logging**

  * Sessions, files, and events logged to SQLite via `DB/log_to_db.py`
  * Uploaded/merged CSVs saved into an **audit folder** with timestamp + session id

* **Optional Custom LLM API**

  * `LLM/config.py` can point the type-inference fallback at your own model endpoint instead of OpenRouter, if you're running something locally (e.g. DeepSeek Coder behind a small FastAPI wrapper)

---

## Repository Layout

```
my_data_cleaning_app/
├─ app.py                      # Streamlit UI (tabs, LLM helpers, decision tree, logging)
├─ pipeline_logic.py           # Executes selected cleaning steps on df
├─ metadata_inference.py       # Column type inference + LLM‑assisted helpers
├─ cleaningDecisionTree.py     # AGraph/PyVis decision tree + click‑to‑clean
├─ table_steps.json            # Declarative config driving the Cleaner UI
├─ DB/
│  ├─ log_to_db.py            # log_session, log_file, log_event (SQLite)
│  └─ auditCSVFiles/          # audit folder for saved CSVs (created at runtime)
├─ LLM/
│  └─ config.py               # custom LLM endpoint (fallback type-inference path only)
├─ .streamlit/                # Streamlit settings
├─ .devcontainer/             # VS Code Dev Container setup
├─ requirements.txt           # Python dependencies
└─ README.md                  # (this file)
```

---

## How It Works (High Level)

1. **Config‑Driven UI** — `table_steps.json` defines sections, step names, descriptions, and typed options. `app.py` renders controls automatically and builds a `steps` list.
2. **Pipeline Execution** — `pipeline_logic.run_pipeline(df, steps)` executes selected steps in order. If an LLM instruction was accepted, its generated code is appended as a step and executed safely within the pipeline wrapper.
3. **LLM Helpers**

   * `call_llm()` uses the OpenRouter API (OpenAI-compatible) with model `z-ai/glm-4.6` to:

     * generate *cleaning suggestions* (`fetch_llm_suggestions`)
     * translate a *natural instruction* → **raw Python code** (`get_cleaning_code_from_llm`)
   * `fallback_infer_type_with_llm()` posts to the endpoint in `LLM.config.API_URL` as a secondary type-inference path when the heuristics are unsure.
4. **Metadata Inference & Visuals** — `metadata_inference.analyze_dataframe(df)` infers types and suggests basic visualizations; URL columns can be summarized via an LLM.
5. **Decision Tree** — `cleaningDecisionTree.render_agraph_tree()` builds a compact action tree (max branching/leaf count). Clicking a **leaf** triggers `custom_cleaning_via_llm()` with contextual instruction; code and results are shown.
6. **Auditability** — All key actions are logged via `log_session`, `log_file`, and `log_event`. CSVs are saved to an audit directory with timestamp and session id.

---

## Quick Start

### 1) Clone & Create Environment

```bash
git clone https://github.com/iamvisheshsrivastava/Smart_CSV_Toolkit.git
cd Smart_CSV_Toolkit

# (recommended) Python 3.10+ virtual env
python -m venv .venv
# Windows
. .venv/Scripts/activate
# macOS/Linux
# source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

### 2) Configure LLMs (Optional but recommended)

**OpenRouter API (used by `call_llm`)**

* Create an account at [OpenRouter](https://openrouter.ai/keys) and get an API key.
* Copy [`.env.example`](https://github.com/hamids-ai-automations/Smart_CSV_Toolkit/blob/main/.env.example) to `.env` and fill in the local values for development.
* Add the API key to your `.streamlit/secrets.toml` file:

```toml
OPENROUTER_API_KEY = "your-openrouter-api-key-here"
```

Alternatively, set the environment variable before running Streamlit:

```bash
# Windows PowerShell
$env:OPENROUTER_API_KEY = "YOUR_KEY"

# macOS/Linux
export OPENROUTER_API_KEY="YOUR_KEY"
```

The model defaults to `z-ai/glm-4.6` and can be overridd
```
