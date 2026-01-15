
  
    

  create  table "scrapy_data"."my_dbt_schema"."stg_data__dbt_tmp"
  
  
    as
  
  (
    WITH data_to_stg AS (
    SELECT * FROM "scrapy_data"."public"."raw_data"
)

SELECT
    CAST(id AS INTEGER) AS id,
    full_title,
    memory,
    storage,
    LOWER(color) AS color,
    CAST(REPLACE(REPLACE(price, '.', ''), ',', '.') AS NUMERIC(10, 2)) AS price,
    scraped_at,
    CAST(rating AS NUMERIC(10, 2)) AS rating,
    site_name
FROM
    data_to_stg
  );
  