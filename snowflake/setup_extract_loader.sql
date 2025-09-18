
-- grant role to user
USE ROLE SECURITYADMIN;

GRANT ROLE hr_dlt_loader TO USER extract_loader;

-- grant privileges to role
GRANT USAGE ON WAREHOUSE hr_warehouse TO ROLE hr_dlt_loader;
GRANT USAGE ON DATABASE hr_analytics TO ROLE hr_dlt_loader;
GRANT USAGE ON SCHEMA hr_analytics.staging TO ROLE hr_dlt_loader;
GRANT CREATE TABLE ON SCHEMA hr_analytics.staging TO ROLE hr_dlt_loader;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA hr_analytics.staging TO ROLE hr_dlt_loader;
GRANT SELECT, INSERT, UPDATE, DELETE ON FUTURE TABLES IN SCHEMA hr_analytics.staging TO ROLE hr_dlt_loader;

-- check grants
SHOW GRANTS ON SCHEMA hr_analytics.staging;
SHOW FUTURE GRANTS IN SCHEMA hr_analytics.staging;
SHOW GRANTS TO ROLE hr_dlt_loader;
SHOW GRANTS TO USER extract_loader;
