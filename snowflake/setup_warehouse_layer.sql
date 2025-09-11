USE ROLE SYSADMIN;

USE DATABASE hr_analytics;

CREATE SCHEMA IF NOT EXISTS warehouse;

SHOW SCHEMAS IN DATABASE hr_analytics;

-- grant privileges to work on warehouse schema
USE ROLE securityadmin;

GRANT ROLE hr_dlt_loader TO ROLE hr_dbt_transformer;

SHOW GRANTS TO ROLE hr_dbt_transformer; --privileges and roles granted to this role, for existing objects
SHOW GRANTS OF ROLE hr_dbt_transformer; --users granted this role

GRANT USAGE,
CREATE TABLE,
CREATE VIEW ON SCHEMA hr_analytics.warehouse TO ROLE hr_dbt_transformer; --note that hr_analytics_dlt_role already has the usage privilege on database hr_analytics

-- grant CRUD and select tables and views
GRANT SELECT,
INSERT,
UPDATE,
DELETE ON ALL TABLES IN SCHEMA hr_analytics.warehouse TO ROLE hr_dbt_transformer;
GRANT SELECT ON ALL VIEWS IN SCHEMA hr_analytics.warehouse TO ROLE hr_dbt_transformer;

-- grant CRUD and select on future tables and views
GRANT SELECT,
INSERT,
UPDATE,
DELETE ON FUTURE TABLES IN SCHEMA hr_analytics.warehouse TO ROLE hr_dbt_transformer;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA hr_analytics.warehouse TO ROLE hr_dbt_transformer;

-- test on the new role
USE ROLE hr_dbt_transformer;

SHOW GRANTS ON SCHEMA hr_analytics.warehouse;

USE SCHEMA hr_analytics.warehouse;
CREATE TABLE test (id INTEGER);
SHOW TABLES;
SHOW GRANTS TO ROLE hr_dbt_transformer; --privileges and roles granted to this role, for existing objects
DROP TABLE TEST;