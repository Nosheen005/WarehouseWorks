USE ROLE SYSADMIN;
CREATE WAREHOUSE hr_warehouse
WITH 
WAREHOUSE_SIZE = 'X-Small' -- t-shirt sizes
AUTO_SUSPEND = 300 
AUTO_RESUME = TRUE
INITIALLY_SUSPENDED = TRUE
COMMENT = 'try to create warehouse';

use warehouse hr_warehouse;

CREATE DATABASE IF NOT EXISTS hr_analytics;

CREATE SCHEMA IF NOT EXISTS hr_analytics.staging;