with src_auxilliary_attributes as (select * from {{ ref('src_auxilliary_attributes')}})


select
    {{ dbt_utils.generate_surrogate_key(['experience_required', 'access_to_own_car', 'driving_license_required'])}} as auxilliary_id,
    experience_required,
    access_to_own_car,
    driving_license_required
from src_auxilliary_attributes
group by auxilliary_id