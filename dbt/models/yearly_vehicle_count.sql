{{ config(materialized='table') }}

SELECT
    EXTRACT(YEAR FROM date_first_registration) AS registration_year,
    COUNT(*) AS number_of_cars
FROM {{ source('vehicle_data', 'vehicle') }}
GROUP BY registration_year
ORDER BY registration_year;
