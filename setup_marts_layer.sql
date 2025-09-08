USE ROLE SYSADMIN;

USE DATABASE hr_analytics;   

CREATE SCHEMA IF NOT EXISTS marts;

SHOW SCHEMAS IN DATABASE hr_analytics;

USE ROLE securityadmin;

GRANT USAGE,
CREATE TABLE,
CREATE VIEW ON SCHEMA hr_analytics.marts TO ROLE hr_dbt_transformer;

-- grant CRUD and select tables and views
GRANT SELECT,
INSERT,
UPDATE,
DELETE ON ALL TABLES IN SCHEMA hr_analytics.marts TO ROLE hr_dbt_transformer;
GRANT SELECT ON ALL VIEWS IN SCHEMA hr_analytics.marts TO ROLE hr_dbt_transformer;

-- grant CRUD and select on future tables and views
GRANT SELECT,
INSERT,
UPDATE,
DELETE ON FUTURE TABLES IN SCHEMA hr_analytics.marts TO ROLE hr_dbt_transformer;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA hr_analytics.marts TO ROLE hr_dbt_transformer;
USE ROLE hr_dbt_transformer;

SHOW GRANTS ON SCHEMA hr_analytics.marts;

-- manual test
USE SCHEMA hr_analytics.marts;
CREATE TABLE test (id INTEGER);
SHOW TABLES;
DROP TABLE TEST;