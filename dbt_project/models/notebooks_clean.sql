with raw_data as (
    select * from {{source('raw_data', 'notebooks')}} 
)

select
    id,
    trim(full_title) as clean_title

from
    raw_data
where
    price is not null