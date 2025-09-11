with stg_job_ads as (select * from {{ source('hr_analytics', 'stg_ads') }})

select
    COALESCE(employment_type__label, 'Ospecifierad') as employment_type,
    COALESCE(salary_type__label, 'Ospecifierad') as salary_type,
    COALESCE(duration__label, 'Ospecifierad') as duration,
    scope_of_work__min as scope_of_work_min,
    scope_of_work__max as scope_of_work_max
from stg_job_ads 