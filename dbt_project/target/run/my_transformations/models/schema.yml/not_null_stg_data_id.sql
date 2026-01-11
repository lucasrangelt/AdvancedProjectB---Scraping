
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select id
from "scrapy_data"."my_dbt_schema"."stg_data"
where id is null



  
  
      
    ) dbt_internal_test