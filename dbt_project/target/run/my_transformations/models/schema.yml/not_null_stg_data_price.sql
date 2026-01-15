
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select price
from "scrapy_data"."my_dbt_schema"."stg_data"
where price is null



  
  
      
    ) dbt_internal_test