# Warehouseworks

A project about proving the useability of an analytical tool to find job ads.

Make sure to run a virtual enviroment from the requirements.txt preferably using uv.

### dlt_code

This folder keeps the code about getting the data from arbetsförmedlingen.
Make sure to create a .dlt folder in the base folder of the repo with a file secrets.toml containing information about the dlt role for snowflake
Use this format:
```
[destination.snowflake.credentials]
database = "<database name>" # please set me up!
username = "<dlt username>" # please set me up!
password = "<password for dlt user>" # please set me up!
host = "<account_identifier>" # please set me up!  
warehouse = "<warehouse name>" # please set me up!
role = "<dlt user role>" # please set me up!
```

### dbt_analytics

This folder is a dbt project about transforming the data gotten from dlt to a usable state for streamlit dashboard.
Information about the models and the tests can be found using 'dbt docs generate' and then 'dbt docs serve'
Make sure to have or create a .dbt folder in your home folder with a profiles.yml file in it containing information about the dbt role for snowflake
Use this format:
```
dbt_analytics:
  outputs:
    dev:
      account: <account_identifier>.west-europe.azure #Or where you created your account
      database: <database name> # please set me up!
      password: <password for dbt user> # please set me up!
      role: <dbt user role> # please set me up!
      schema: <warehouse name> # please set me up!
      threads: 1
      type: snowflake
      user: <dbt username> # please set me up!
      warehouse: <warehouse name> # please set me up!
  target: dev
```

### dashboard

This folder is where we create a dashboard to serve the data to, using a connector file and a dashboard file.
Make sure to create a .env file inside the dashboard folder containing information about the streamlit role for snowflake
Use this format:
```
SNOWFLAKE_USER="<streamlit user>" # please set me up!
SNOWFLAKE_PASSWORD="<streamlit password>" # please set me up!
SNOWFLAKE_ACCOUNT="<account_identifier>.west-europe.azure" #Or where you created your account
SNOWFLAKE_WAREHOUSE="<warehouse name>" # please set me up!
SNOWFLAKE_DATABASE="<database name>" # please set me up!
SNOWFLAKE_SCHEMA="<schema name>" # please set me up!
SNOWFLAKE_ROLE="<streamlit role>" # please set me up!
```

### snowflake

This folder contains some of the snowflake setup information where we grant our program users privileges on the schemas and such in our database.
These do not include user creation so you will need to do that yourself using the same information you fill into the above user part.
They also are our specific names for schemas/warehouses/database/users so if you do not use the same ones you need to change it in your repo.
The only important files is the 'setup_' files, the other ones are just small tests and exploration and does not matter for setting up the project.
