from datetime import datetime
from pathlib import Path

from airflow.decorators import dag
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

GDEC_DBT_PATH =  Path("/opt/airflow/dbt/gdec_dbt")
DBT_EXECUTABLE = Path("/opt/airflow/dbt_venv/bin/dbt")

@dag(
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["shopee"],
)
def dag_shopee_finance_transactions():

    dbt_snowflake = ProfileConfig(
        profile_name="dbt_snowflake",
        target_name="dev",
        profile_mapping=SnowflakeUserPasswordProfileMapping(
            conn_id="dbt_snowflake",
            profile_args={
                "database": "DEV_DB",
                "schema": "DEV_INTEG_SPE_SCH"
            },
        ),
    )
    
    execution_config = ExecutionConfig(
        dbt_executable_path=DBT_EXECUTABLE,
    )

    shopee_finance_transactions = DbtTaskGroup(
        group_id="shopee_finance_transactions",
        project_config=ProjectConfig(GDEC_DBT_PATH),
        profile_config=dbt_snowflake,
        execution_config=execution_config,
    )

    return shopee_finance_transactions


dag_shopee_finance_transactions()
