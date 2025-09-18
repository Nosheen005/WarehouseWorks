## dbt – Tests and Documentation

In this project we have used dbt to ensure both data quality and traceability in our data warehouse. Below is a summary of the key tests and how documentation is managed.

### Tests (highlights)

**Fact table – fct_job_ads**
- Primary and foreign keys (`occupation_id`, `auxilliary_id`, `employer_id`, `job_details_id`, `job_description_id`) are tested with `not_null` and `relationships`.
- `job_description_id` is also tested with `unique`.
- `relevance` is tested with range control (0–1) and type control (float).
- `vacancies` is tested with quantile and max tests (max 20, warning if exceeded) and type control (number).
- `application_deadline` is tested with `not_null`.

**Dimension tables**
- `dim_employer`: all fields tested with `not_null`; `employer_id` also `unique`.
- `dim_occupation`: `occupation_id` and `occupation` tested with both `unique` and `not_null`; other fields with `not_null`.
- `dim_auxilliary_attributes`: `auxilliary_id` tested with `unique` and `not_null`; all boolean fields with `not_null`.
- `dim_job_description`: `job_description_id` tested with `unique` and `not_null`; text fields with `not_null`.
- `dim_job_details`: `job_details_id` tested with `unique` and `not_null`; other attributes with `not_null`. Columns `scope_of_work_min` and `scope_of_work_max` tested with range controls (0–100) where exceeding values are logged as warnings.

### Documentation
- All models and columns are described in `schema.yml`.
- Documentation is generated automatically using `dbt docs generate` and can be viewed with `dbt docs serve`.
- The lineage graph in dbt docs shows how the fact table is connected to the respective dimension tables.

