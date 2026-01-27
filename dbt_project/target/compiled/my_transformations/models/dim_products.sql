WITH products_to_dim as (
    SELECT DISTINCT
        MD5(TRIM(LOWER(full_title)) || memory || storage || color) as product_key,
        full_title,
        storage,
        memory,
        color
    FROM
        "scrapy_data"."my_dbt_schema"."stg_data"
)

SELECT
    product_key,
    full_title,
    storage,
    memory,
    color
FROM
    products_to_dim