
    
    

select
    id as unique_field,
    count(*) as n_records

from "scrapy_data"."my_dbt_schema"."stg_data"
where id is not null
group by id
having count(*) > 1


