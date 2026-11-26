# pubchem-finder

**Overview:** Molecular similarity search over PubChem with RDKit: CLI, MCP server for Claude, local fingerprint index

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/pubchem-finder](https://github.com/hamids-ai-automations/pubchem-finder) |
| Live website | https://pypi.org/project/pubchem-finder/ |
| Visibility | public |
| Status | fork |
| Creation date | 2026-11-11 |
| Last update | 2026-11-20 |
| Last push | 2026-11-20 |
| Default branch | master |
| License | MIT |
| Primary language | Python |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 13 |
| Size | 4341 KB |
| Topics | - |

## Objectives

# PubChem Finder

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude, .claude-plugin, .github, docs, examples, plugins, scripts, src, tests
- **Total files (tracked in default branch):** 134
- **CI workflows:** .github/workflows/ci.yml, .github/workflows/e2e-real.yml, .github/workflows/live.yml, .github/workflows/monthly-e2e.yml, .github/workflows/promote-plugin.yml, .github/workflows/python-next.yml, .github/workflows/release.yml, .github/workflows/released-wheel.yml, .github/workflows/scheduled-failure.yml
- **Test files detected:** 42

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Python | 737327 |
| Makefile | 1243 |

**Frameworks / libraries detected:** MCP, NumPy, pytest

**Dependencies:** none detected

## Important source files

- `plugins/pubchem-finder/pyproject.toml`
- `pyproject.toml`

## Installation and setup

No installation instructions found in the README.

## Deployment

Firebase/other hosting declared via homepage field: https://pypi.org/project/pubchem-finder/

## Documentation links

- https://modelcontextprotocol.io
- https://pypi.org/project/pubchem-finder
- https://pubchem.ncbi.nlm.nih.gov
- https://raw.githubusercontent.com/MysterionRise/pubchem-finder/master/docs/media/search-demo.gif
- https://raw.githubusercontent.com/MysterionRise/pubchem-finder/master/docs/media/search-demo.mp4
- https://docs.astral.sh/uv/getting-started/installation
- https://raw.githubusercontent.com/MysterionRise/pubchem-finder/master/docs/images/sulfonamides-smarts.png
- https://registry.modelcontextprotocol.io
- http://127.0.0.1:8000/mcp`
- https://raw.githubusercontent.com/MysterionRise/pubchem-finder/master/docs/images/analogues-diff.png
- https://raw.githubusercontent.com/MysterionRise/pubchem-finder/master/docs/images/similarity-map.png
- https://www.ncbi.nlm.nih.gov/home/about/policies
- https://pubchem.ncbi.nlm.nih.gov/docs/citation-guidelines
- https://doi.org/10.1093/nar/gkae1059
- https://www.accessdata.fda.gov/scripts/cder/daf
- https://www.rdkit.org
- https://duckdb.org
- https://arrow.apache.org
- https://docs.astral.sh/uv
- http://127.0.0.1:8000/mcp

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

Full README: https://github.com/hamids-ai-automations/pubchem-finder/blob/master/README.md

```markdown
# PubChem Finder

Search [PubChem](https://pubchem.ncbi.nlm.nih.gov/) by chemical structure from your
terminal or from Claude. PubChem Finder builds a local fingerprint index of PubChem (all
of it, or the slice you need) for exact similarity and substructure search with no rate
limits, wraps PubChem's live services for names, safety data and bioassays, and adds RDKit
chemistry: structure drawings, med-chem triage and descriptors. Local search works from the
first question, on a built-in set of 1,932 FDA-approved drugs, until you build a PubChem
index. It runs as a command-line tool, a Python library and an
[MCP](https://modelcontextprotocol.io/) server for Claude Desktop, Claude Code and other MCP
clients.

[![PyPI](https://img.shields.io/pypi/v/pubchem-finder.svg)](https://pypi.org/project/pubchem-finder/)
[![Python](https://img.shields.io/pypi/pyversions/pubchem-finder.svg)](https://pypi.org/project/pubchem-finder/)
[![CI](https://github.com/MysterionRise/pubchem-finder/actions/workflows/ci.yml/badge.svg)](https://github.com/MysterionRise/pubchem-finder/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/MysterionRise/pubchem-finder/blob/master/LICENSE)
<!-- mcp-name: io.github.MysterionRise/pubchem-finder -->

![A similarity search for aspirin and a SMARTS substructure search over 444,794 PubChem compounds, with the hits appearing and their key atoms highlighted](https://raw.githubusercontent.com/MysterionRise/pubchem-finder/master/docs/media/search-demo.gif)

*Real searches over the first 444,794 compounds of PubChem, rendered from the index the
project's real-data workflow builds: similarity hits for aspirin with the atoms that differ
from it highlighted, then hits for an aryl sulfonamide SMARTS with the match highlighted.
[MP4 version](https://raw.githubusercontent.com/MysterionRise/pubchem-finder/master/docs/media/search-demo.mp4).*

## Why this one

Other PubChem tools, MCP servers and hosted connectors included, forward questions to
PubChem's web API. That works for looking compounds up, but structure search through the
API is rate-limited, times out on generic queries and returns unscored samples. PubChem
Finder also keeps a local index:

- **Exact, scored similarity search** over every indexed compound (ECFP4 Tanimoto by
  default) in milliseconds, using [FPSim2](https://github.com/chembl/FPSim2), the engine
  behind ChEMBL's similarity search.
- **Local substructure search** with SMILES or SMARTS: a fingerprint screen, then an
  atom-by-atom match, so every hit is a real match.
- **Offline chemistry** with RDKit: descriptors, standardization, PAINS/Brenk/NIH alerts,
  QED, synthetic accessibility, and drawings that show what changed between analogues.
- **PubChem knowledge, cited:** synonyms and CAS numbers, cross-references, GHS
  classification, pharmacology, toxicity and bioassay summaries, each with its source.

No database server, no Docker: the index is a pair of files in your data directory.

## Use it from Claude

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/), which fetches
Python and everything else on first run.

**Claude Code:**

```bash
claude mcp add pubchem-finder -- uvx --python 3.14 pubchem-finder mcp
```

or as a plugin, which also works in Cowork:

```
/plugin install pubchem-finder --marketplace MysterionRise/pubchem-finder
```

**Claude Desktop** (Settings, Developer, Edit Config, then restart Claude):

```json
{
  "mcpServers": {
    "pubchem-finder": {
      "command": "uvx",
      "args": ["--python", "3.14", "pubchem-finder", "mcp"]
    }
  }
}
```

Then ask things like:

- "What is the molecular weight and XLogP of caffeine? Is it Lipinski-compliant?"
- "Is ibuprofen hazardous? What does its GHS label say? Cite the sources."
- "What are the main targets of celecoxib in PubChem bioassays?"
- "Show me the closest analogues of aspirin and highlight what changed."
- "Does this compound have any PAINS alerts? `O=C1C(=Cc2ccccc2)SC(=S)N1`"
- "Find the 20 compounds most similar to ibuprofen" or "Which indexed compounds contain an
  aryl sulfonamide? Draw a few with the group highlighted." (local search: the demo set of
  FDA-approved drugs until you build an index)

![Sulfonamide drugs with the aryl sulfonamide SMARTS match highlighted](https://raw.githubusercontent.com/MysterionRise/pubchem-finder/master/docs/images/sulfonamides-smarts.png)

*`draw_molecules` with `highlight="smarts"`: eight sulfonamide drugs with the match for
`[NX3][SX4](https://github.com/hamids-ai-automations/pubchem-finder/blob/master/=O)(=O)c` highlighted, as Claude shows it inline.*

Local similarity and substructure search work from the first question: until you build
an index, they search a built-in demo set of 1,932 FDA-approved drugs (built in about a
second on first use) and say so. Build a PubChem index from the command line (below) and
the server switches to it, no restart needed. To use a non-default data directory, add
`"env": {"PUBCHEM_FINDER_HOME": "/path"}` to the Claude Desktop entry, or
`--env PUBCHEM_FINDER_HOME=/path` to `claude mcp add`.

**Other MCP clients:** the server speaks standard MCP over stdio, so any client that runs
local MCP servers (Cursor, VS Code, Windsurf, Zed, JetBrains IDEs, Codex CLI, LM Studio...)
can start it with the same command and arguments. It is listed in the
[MCP registry](https://registry.modelcontextprotocol.io) as `io.github.MysterionRise/pubchem-finder`
for clients that install servers from there.
[docs/clients.md](https://github.com/MysterionRise/pubchem-finder/blob/master/docs/clients.md)
has the settings, a quick check, and setups people have tested; if you use one of those
clients, adding yours there is a good first contribution.

**Over HTTP:** `pubchem-finder mcp --transport http` serves the same tools at
`http://127.0.0.1:8000/mcp` (MCP streamable HTTP) for clients that connect to a URL
rather than start a process, and for one shared index on a team machine. For example,
`claude mcp add --transport http pubchem-finder http://127.0.0.1:8000/mcp`. The server has
no authentication or TLS of its own: read
[Over HTTP](https://github.com/MysterionRise/pubchem-finder/blob/master/docs/clients.md#over-http)
before binding it to anything but `127.0.0.1`.

### Tools

| Tool | What it does |
|---|---|
| `pubchem_lookup(query, by, limit)` | Resolve a name, CID, SMILES or InChIKey to PubChem records: identifiers, formula, MW, XLogP, H-bond counts, TPSA, link. |
| `compound_properties(smiles)` | RDKit descriptors and Lipinski check for any SMILES. Offline. |
| `standardize(smiles)` | Remove salts and counter-ions, neutralize, canonicalize; says what it removed. Offline. |
| `compare(smiles_a, smiles_b)` | Tanimoto similarity on ECFP4 and MACCS fingerprints. Offline. |
| `medchem_profile(smiles)` | QED, synthetic accessibility, Lipinski/Veber, PAINS/Brenk/NIH alerts with atoms, Murcko scaffold. Offline. |
| `draw_molecules(smiles, legends, highlight, smarts, reference_smiles)` | Structures as an inline image, highlighting a SMARTS match, what changed relative to a reference, or a similarity map. Offline. |
| `similarity_search(smiles, threshold, top_k, metric, group_by_scaffold)` | Most similar compounds in the local index (the demo set until one is built), optionally grouped by Murcko scaffold. |
| `substructure_search(query, query_type, max_hits)` | Indexed compounds containing a SMILES or SMARTS fragment, lowest CID first. |
| `index_status()` | Whether the local index is built, what it holds, what local searches cover now, and how to build what is missing. |
| `pubchem_similarity_search(smiles, threshold, max_records)` | Similar compounds across all of PubChem, live, re-scored with ECFP4. |
| `pubchem_substructure_search(smiles, max_records)` | Compounds across all of PubChem that contain a fragment, live. |
| `pubchem_exact_match(smiles, identity_type, max_records)` | The PubChem record(s) for exactly this structu
```
