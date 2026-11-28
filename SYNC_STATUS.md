# Sync Status

- **Last successful sync:** 2026-11-28T16:53:18+00:00
- **Sync mode:** incremental
- **Triggered by:** automatic profile sync
- **API requests this run:** 359
- **Failed API requests:** 0
- **Runtime:** 36.1s

## Data quality

| Check | Value |
| --- | --- |
| total repositories discovered | 103 |
| total repositories documented | 101 |
| documentation coverage percent | 98.06 |
| repositories without description | 7 |
| total projects | 103 |
| total contributions | 169 |
| total external links | 801 |
| total gists | 0 |
| total releases | 7 |
| total packages | 0 |
| missing optional fields | ['hamids-ai-automations/ghl-servicepro-theme: description', 'hamids-ai-automations/langchain-google-cloud-sql-pg-python: description', 'hamids-ai-automations/sbsim: description', 'hamids-ai-automations/rai-toolkit: description', 'hamids-ai-automations/trustflow-backend: description', 'hamids-ai-automations/simple_invoicing: description', 'hamids-ai-automations/TermXtract: description'] |
| unavailable sources | ['packages unavailable: HTTP 422 for https://api.github.com/users/hamids-ai-automations/packages?package_type=pypi: {"message":"The package_type parameter is invalid.","documentation_url":"https://docs.github.com/rest/packages/packages#list-packages-for-a-user","status":"422"}'] |
| validation errors | 0 |
| validation warnings | 2 |
| last validated | 2026-11-28T16:53:18+00:00 |

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
