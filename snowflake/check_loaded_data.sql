USE ROLE hr_dbt_transformer;
USE DATABASE hr_analytics;

SHOW SCHEMAS;

SHOW TABLES IN SCHEMA staging;

DESC TABLE staging.raw_jobs;

USE WAREHOUSE hr_warehouse;
SELECT
    headline,
    employer__workplace
FROM staging.raw_jobs;


SELECT * FROM staging.raw_jobs;