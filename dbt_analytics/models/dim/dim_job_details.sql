with src_job_details as (select * from {{ ref('src_job_details') }})

select
    {{ dbt_utils.generate_surrogate_key(['employment_type', 'salary_type', 'duration', 'scope_of_work_min', 'scope_of_work_max'])}} as job_details_id,
    employment_type,
    salary_type,
    duration,
    scope_of_work_min,
    scope_of_work_max
from src_job_details
group by job_details_id
