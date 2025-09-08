with raw as (
    select *
    from {{ source('staging', 'raw_jobs') }}
)

select
    id as job_id,
    occupation_field,
    occupation,
    occupation_group,
    employer,
    headline,
    description,
    employment_type,
    application_deadline,
    number_of_vacancies as vacancies,
    relevance
from raw