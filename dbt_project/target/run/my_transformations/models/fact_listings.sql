
  
    

  create  table "scrapy_data"."my_dbt_schema"."fact_listings__dbt_tmp"
  
  
    as
  
  (
    SELECT
    MD5(TRIM(LOWER(full_title)) || memory || storage || color) as product_key,
    short_title,
    price,
    rating,
    scraped_at,
    site_name
FROM
    "scrapy_data"."my_dbt_schema"."stg_data"
  );
  