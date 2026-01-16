WITH data_to_stg AS (
    SELECT * FROM "scrapy_data"."public"."raw_data"
)

SELECT
    CAST(id AS INTEGER) AS id,
    CASE
        WHEN full_title ILIKE '%notebook%' THEN 'notebook'
        ELSE 'other'
    END AS short_title,
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