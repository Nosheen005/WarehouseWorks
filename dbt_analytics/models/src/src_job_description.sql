with stg_job_ads as (select * from {{ source('hr_analytics', 'stg_ads') }})

select
    id,
    headline,
    COALESCE(description__text, 'Beskrivning saknas') as description_text,
    COALESCE(description__text_formatted, 'Beskrivning saknas') as description_html
from stg_job_ads
