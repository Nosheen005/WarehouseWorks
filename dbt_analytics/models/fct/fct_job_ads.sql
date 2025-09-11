-- this is an extract of the model

with job_ads as (select * from {{ ref('src_job_ads') }})

select
    {{ dbt_utils.generate_surrogate_key(['id'])}} as job_description_id,
    {{ dbt_utils.generate_surrogate_key(['employment_type', 'salary_type', 'duration', 'scope_of_work_min', 'scope_of_work_max'])}} as job_details_id,
    {{ dbt_utils.generate_surrogate_key(['experience_required', 'access_to_own_car', 'driving_license_required'])}} as auxilliary_id,
    {{ dbt_utils.generate_surrogate_key(['occupation']) }} as occupation_id,
    {{ dbt_utils.generate_surrogate_key(['employer'])}} as employer_id,
    vacancies,
    relevance,
    application_deadline
from job_ads