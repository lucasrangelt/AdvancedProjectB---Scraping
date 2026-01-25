SELECT
    MD5(TRIM(LOWER(full_title)) || memory || storage || color) as product_key,
    short_title,
    price,
    rating,
    scraped_at,
    site_name
FROM
    {{ref('stg_data')}}