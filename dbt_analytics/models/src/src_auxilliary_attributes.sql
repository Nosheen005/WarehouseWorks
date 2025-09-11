with stg_job_ads as (select * from {{ source('hr_analytics', 'stg_ads') }})

select
    COALESCE(experience_required, FALSE) as experience_required,
    COALESCE(access_to_own_car, FALSE) as access_to_own_car,
    COALESCE(driving_license_required, FALSE) as driving_license_required
from stg_job_ads 