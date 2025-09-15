USE ROLE useradmin;
CREATE ROLE reporter_role;

USE ROLE securityadmin;

GRANT USAGE ON WAREHOUSE hr_warehouse TO ROLE reporter_role;
GRANT USAGE ON DATABASE hr_analytics TO ROLE  reporter_role;
GRANT USAGE ON SCHEMA hr_analytics.marts TO ROLE reporter_role;
GRANT SELECT ON ALL TABLES IN SCHEMA hr_analytics.marts TO ROLE reporter_role;
GRANT SELECT ON ALL VIEWS IN SCHEMA hr_analytics.marts TO ROLE reporter_role;
GRANT SELECT ON FUTURE TABLES IN SCHEMA hr_analytics.marts TO ROLE reporter_role;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA hr_analytics.marts TO ROLE reporter_role;


GRANT ROLE reporter_role TO USER reporter;
GRANT ROLE reporter_role TO USER Milou;

USE ROLE reporter_role;

SHOW GRANTS TO ROLE reporter_role;

USE WAREHOUSE hr_warehouse;
SELECT * FROM hr_analytics.marts.mart_IT;