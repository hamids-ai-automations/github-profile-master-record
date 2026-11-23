# Sync Status

- **Last successful sync:** 2026-11-23T06:23:24+00:00
- **Sync mode:** full
- **Triggered by:** initial data collection
- **API requests this run:** 1062
- **Failed API requests:** 0
- **Runtime:** 75.4s

## Data quality

| Check | Value |
| --- | --- |
| total repositories discovered | 95 |
| total repositories documented | 94 |
| documentation coverage percent | 98.95 |
| repositories without description | 6 |
| total projects | 95 |
| total contributions | 169 |
| total external links | 787 |
| total gists | 0 |
| total releases | 6 |
| total packages | 0 |
| missing optional fields | ['hamids-ai-automations/langchain-google-cloud-sql-pg-python: description', 'hamids-ai-automations/sbsim: description', 'hamids-ai-automations/rai-toolkit: description', 'hamids-ai-automations/trustflow-backend: description', 'hamids-ai-automations/simple_invoicing: description', 'hamids-ai-automations/TermXtract: description'] |
| unavailable sources | ['packages unavailable: HTTP 422 for https://api.github.com/users/hamids-ai-automations/packages?package_type=pypi: {"message":"The package_type parameter is invalid.","documentation_url":"https://docs.github.com/rest/packages/packages#list-packages-for-a-user","status":"422"}'] |
| validation errors | 0 |
| validation warnings | 1 |
| last validated | 2026-11-23T06:23:24+00:00 |

## Automation schedule

| Workflow | Schedule (UTC) | Purpose |
| --- | --- | --- |
| `automatic-profile-sync.yml` | hourly at :17 | Detect new/updated repositories, profile changes, releases |
| `scheduled-full-sync.yml` | daily 02:41 | Full profile and repository audit |
| `scheduled-full-sync.yml` | weekly Sun 03:23 | Deep integrity and completeness audit |
| `validate-master-data.yml` | on push / PR / manual | Validate JSON, CSV, duplicates and internal links |
| `initial-data-collection.yml` | manual dispatch | Bootstrap or re-bootstrap the database |

## Failed or unavailable resources

- packages unavailable: HTTP 422 for https://api.github.com/users/hamids-ai-automations/packages?package_type=pypi: {"message":"The package_type parameter is invalid.","documentation_url":"https://docs.github.com/rest/packages/packages#list-packages-for-a-user","status":"422"}
