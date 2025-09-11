-- this is an extract of the model

with stg_job_ads as (select * from {{ source('hr_analytics', 'stg_ads') }})

select
    headline,
    employer__name as employer_name,
    occupation__label as occupation,
    COALESCE(number_of_vacancies, 1) as vacancies,
    relevance,
    application_deadline
from stg_job_ads