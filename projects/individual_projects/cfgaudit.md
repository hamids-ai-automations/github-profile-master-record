# cfgaudit

**Overview:** Static security auditor for AI-agent configuration: Claude Code, MCP servers, Cursor, Codex, Copilot, Gemini CLI and more. 116 rules, SARIF output, OWASP LLM Top 10 mapping.

| Attribute | Value |
| --- | --- |
| Repository | [hamids-ai-automations/cfgaudit](https://github.com/hamids-ai-automations/cfgaudit) |
| Live website | https://cfgaudit.github.io |
| Visibility | public |
| Status | fork |
| Creation date | 2026-10-30 |
| Last update | 2026-10-30 |
| Last push | 2026-11-01 |
| Default branch | main |
| License | Apache-2.0 |
| Primary language | Go |
| Stars / Forks / Watchers | 0 / 0 / 0 |
| Issues (open / closed) | 0 / 0 |
| Pull requests (open / merged) | 0 / 0 |
| Releases | 0 |
| Contributors | 10 |
| Size | 13642 KB |
| Topics | - |

## Objectives

<p align="center">
  <img src="assets/cfgaudit.png" alt="cfgaudit" width="460">
</p>

## Features

No explicit feature list found in the README.

## Technical architecture

- **Top-level directories:** .claude-plugin, .github, .vex, LICENSES, assets, bin, cmd, docs, hooks, internal, rules, skills, templates, testdata
- **Total files (tracked in default branch):** 647
- **CI workflows:** .github/workflows/attestation-backfill.yml, .github/workflows/bench-history.yml, .github/workflows/bench.yml, .github/workflows/build-image.yml, .github/workflows/build-release.yml, .github/workflows/check-ave-ids.yml, .github/workflows/check-framework-versions.yml, .github/workflows/check-typosquat-allowlist.yml, .github/workflows/ci.yml, .github/workflows/codeql.yml, .github/workflows/docker.yml, .github/workflows/fuzz.yml, .github/workflows/linkcheck.yml, .github/workflows/pypi.yml, .github/workflows/release-smoke.yml, .github/workflows/release.yml, .github/workflows/sbom-backfill.yml, .github/workflows/schema-validation.yml, .github/workflows/scorecard.yml, .github/workflows/sensitive-paths.yml
- **Test files detected:** 268

## Languages and technologies

| Language | Bytes |
| --- | --- |
| Go | 2502742 |
| Dockerfile | 3716 |
| Shell | 3547 |

**Frameworks / libraries detected:** none detected from dependency files

**Dependencies:** none detected

## Important source files

- `.github/tools/ajv/package.json`
- `.github/tools/benchstat/go.mod`
- `.github/tools/gobco/go.mod`
- `.github/tools/zizmor/requirements.txt`
- `go.mod`

## Installation and setup

Homebrew (macOS / Linux):

```sh
brew install cfgaudit/tap/cfgaudit
```

With Python tooling (the wheel carries the prebuilt binary, no Python code):

```sh
pipx install cfgaudit      # or: uv tool install cfgaudit
uvx cfgaudit .             # run once without installing
```

Pin it next to your other linters with `cfgaudit==X.Y.Z` in a requirements file.

With the Go toolchain:

## Deployment

Firebase/other hosting declared via homepage field: https://cfgaudit.github.io

## Documentation links

- https://`
- https://token.actions.githubusercontent.com
- https://docs.anthropic.com/en/docs/claude-code
- https://cfgaudit.github.io
- https://scorecard.dev/viewer/?uri=github.com/cfgaudit/cfgaudit
- https://api.scorecard.dev/projects/github.com/cfgaudit/cfgaudit/badge
- https://www.bestpractices.dev/projects/15618
- https://www.bestpractices.dev/projects/15618/badge
- https://slsa.dev/images/gh-badge-level3.svg
- https://gitlab.com/explore/catalog/cfgaudit/cfgaudit
- https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026
- https://www.shellcheck.net
- https://slsa.dev
- https://slsa.dev/spec/v1.0/levels
- https://docs.github.com/actions/security-guides/using-artifact-attestations-and-reusable-workflows-to-achieve-slsa-v1-build-level-3
- https://github\.com/cfgaudit/cfgaudit/\.github/workflows/(build-
- https://docs.gitlab.com/ci/components
- https://pre-commit.com
- http://$(env
- http://`/`ws://`
- https://owasp.org/www-project-mcp-top-10
- https://x?d=
- https://…`
- https://…
- http://`
- https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026
- https://json.schemastore.org/claude-code-settings.json
- https://reuse.software

## Development status

Fork of another project; see upstream for original authorship.

## Associated contributions

- Open issues: 0
- Merged pull requests: 0
- Releases: 0

## Related projects

- hamids-ai-automations/k8s-ai-bench

## Known issues and limitations

No limitations documented in the README.

## Future development opportunities

No roadmap documented in the README.

## README source

Full README: https://github.com/hamids-ai-automations/cfgaudit/blob/main/README.md

```markdown
<p align="center">
  <img src="assets/cfgaudit.png" alt="cfgaudit" width="460">
</p>

<p align="center">
  <a href="https://app.codecov.io/gh/cfgaudit/cfgaudit"><img src="https://codecov.io/gh/cfgaudit/cfgaudit/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/cfgaudit/cfgaudit"><img src="https://api.scorecard.dev/projects/github.com/cfgaudit/cfgaudit/badge" alt="OpenSSF Scorecard"></a>
  <a href="https://www.bestpractices.dev/projects/15618"><img src="https://www.bestpractices.dev/projects/15618/badge" alt="OpenSSF Best Practices"></a>
  <a href="#verifying-a-release"><img src="https://slsa.dev/images/gh-badge-level3.svg" alt="SLSA Build Level 3"></a>
  <a href="https://github.com/marketplace/actions/cfgaudit"><img src="https://img.shields.io/badge/GitHub_Marketplace-cfgaudit-2088FF?logo=githubactions&logoColor=white" alt="GitHub Marketplace"></a>
  <a href="https://gitlab.com/explore/catalog/cfgaudit/cfgaudit"><img src="https://img.shields.io/badge/GitLab_CI%2FCD_Catalog-cfgaudit-FC6D26?logo=gitlab&logoColor=white" alt="GitLab CI/CD Catalog"></a>
  <a href="#badge"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/cfgaudit/cfgaudit/main/assets/badge/v1.json" alt="agent security: cfgaudit"></a>
</p>

# cfgaudit

Security auditor for AI-agent configuration files.

cfgaudit scans the configuration of AI coding assistants — starting with [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — and flags settings that violate the principle of least privilege or leave sensitive files exposed to the agent's context.

Every finding maps to an [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) risk (the primary mapping). Two secondary lenses are also provided: the [OWASP MCP Top 10](#owasp-mcp-top-10-mapping-secondary) for the MCP-server rules, and the [OWASP AISVS 1.01 mapping](https://github.com/hamids-ai-automations/cfgaudit/blob/main/docs/aisvs-mapping.md) for teams who verify against the AI Security Verification Standard. A behavioral [crosswalk to AVE](https://github.com/hamids-ai-automations/cfgaudit/blob/main/docs/cfgaudit-to-ave.md) (Agentic Vulnerability Enumeration) maps the rules to AVE's behavioral classes. The primary OWASP LLM id **and** the mapped AVE id ride in the JSON and SARIF output (`OWASP`/`AVEID` in JSON; `properties.owasp_llm`/`properties.ave_id` in SARIF, alongside the CFG `ruleId`). The rule→AVE mapping lives in a single file (`cmd/cfgaudit/avemap.go`) with the crosswalk doc as its human-readable companion.

---

## Install

Homebrew (macOS / Linux):

```sh
brew install cfgaudit/tap/cfgaudit
```

With Python tooling (the wheel carries the prebuilt binary, no Python code):

```sh
pipx install cfgaudit      # or: uv tool install cfgaudit
uvx cfgaudit .             # run once without installing
```

Pin it next to your other linters with `cfgaudit==X.Y.Z` in a requirements file.

With the Go toolchain:

```sh
go install github.com/cfgaudit/cfgaudit/cmd/cfgaudit@latest
```

Or download a pre-built binary (Linux / macOS / Windows, amd64 / arm64) from the [releases page](https://github.com/cfgaudit/cfgaudit/releases).

Container image:

```sh
docker run --rm -v "$PWD:/work" -w /work ghcr.io/cfgaudit/cfgaudit:latest .
```

The image includes [ShellCheck](https://www.shellcheck.net/), so `--shellcheck` ([CFG045](https://github.com/hamids-ai-automations/cfgaudit/blob/main/docs/rules/CFG045.md)) works there and in the GitHub Action and GitLab components, which run the same image.

The image runs unprivileged as uid `65532`, so the files you mount must be readable by that uid (normal `644`/`755` permissions are fine). cfgaudit only reads them — write the report with a shell redirection on the host (`> report.sarif`) rather than into the mount.

---

## Verifying a release

Every release is built by a GitHub Actions workflow that publishes [build provenance](https://slsa.dev/), and the container image is additionally signed with [cosign](https://github.com/sigstore/cosign). Both are keyless — the signing identity *is* the workflow, so a verified artifact provably came from this repository's release pipeline.

From **v1.17.0** on, the release archives and the container image meet [SLSA](https://slsa.dev/spec/v1.0/levels) **Build Level 3**: they are built in reusable workflows (`build-release.yml`, `build-image.yml`) that the tag-triggered workflows only call, so the build workflow signs the provenance. That is the isolation GitHub documents as [SLSA v1 Build Level 3 for artifact attestations](https://docs.github.com/actions/security-guides/using-artifact-attestations-and-reusable-workflows-to-achieve-slsa-v1-build-level-3). Releases v1.8.0 to v1.16.0 meet Build Level 2: their provenance is signed by `release.yml` and `docker.yml` themselves. `--signer-workflow` below requires the build workflow; drop it for releases before v1.17.0.

**Release archive** — provenance for the archive you downloaded:

```sh
gh attestation verify cfgaudit_1.17.0_linux_amd64.tar.gz -R cfgaudit/cfgaudit \
  --signer-workflow cfgaudit/cfgaudit/.github/workflows/build-release.yml
```

**`checksums.txt`** — verify this too if you check downloads against it (the plugin wrapper in `bin/cfgaudit` does):

```sh
gh attestation verify checksums.txt -R cfgaudit/cfgaudit \
  --signer-workflow cfgaudit/cfgaudit/.github/workflows/build-release.yml
```

**Container image** — provenance and signature, both bound to the image digest rather than a tag, since a tag can be repointed later:

```sh
DIGEST=$(docker buildx imagetools inspect ghcr.io/cfgaudit/cfgaudit:latest --format '{{.Manifest.Digest}}')

gh attestation verify "oci://ghcr.io/cfgaudit/cfgaudit@$DIGEST" -R cfgaudit/cfgaudit \
  --signer-workflow cfgaudit/cfgaudit/.github/workflows/build-image.yml

cosign verify "ghcr.io/cfgaudit/cfgaudit@$DIGEST" \
  --certificate-identity-regexp '^https://github.com/cfgaudit/cfgaudit/' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

Attestations and the image signature are published from **v1.8.0** onward, the first release built by the signing pipeline; `checksums.txt` is covered from the same release.

**Without the GitHub API**: from v1.8.0 onward, the same attestation is also attached to each release as two assets: `cfgaudit_<version>.sigstore.json`, the Sigstore bundle with the signature, signing certificate and transparency log entry, and `cfgaudit_<version>.intoto.jsonl`, the signed SLSA provenance on its own. One bundle covers all six archives and `checksums.txt`. Verify a download against it with cosign:

```sh
VERSION=<version>   # e.g. the release you downloaded, without the leading v
cosign verify-blob-attestation \
  --bundle "cfgaudit_${VERSION}.sigstore.json" \
  --type slsaprovenance1 \
  --certificate-identity-regexp '^https://github\.com/cfgaudit/cfgaudit/\.github/workflows/(build-)?release\.yml@refs/tags/v' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  "cfgaudit_${VERSION}_linux_amd64.tar.gz"
```

The identity pins the signer to this repository's release workflow running on a tag, so a bundle signed by any other workflow or repository fails, as does a file whose digest is not in the provenance. The regex accepts `release.yml`, which signed releases before v1.17.0, and `build-release.yml`, which signs them from v1.17.0 on; use only the latter to require Build Level 3.

**Rebuilding a release**: the binaries are reproducible. Building the tag with the Go version recorded in the release binary and the release flags gives a byte-identical binary, so you can check a download without trusting the pipeline at all. For example, for the Linux amd64 binary of v1.17.1:

```sh
go version -m cfgaudit | head -1        # the Go version the release used, e.g. go1.24.13
git clone --branch v1.17.1 https://github.com/cfgaudit/cfgaudit.git cfgaudit-src && cd cfgaudit-src
GOTOOLCHAIN=go1.24.13 CGO_ENABLED=0
```
