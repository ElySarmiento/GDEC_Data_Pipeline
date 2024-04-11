import os
from datetime import datetime
from pathlib import Path

from airflow.decorators import dag
from airflow.models import Variable

from cosmos import DbtTaskGroup, ExecutionConfig, ProjectConfig, ProfileConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


gdec_dbt_path = Path("/opt/airflow/dbt/gdec_dbt")
dbt_executable = Path("/opt/airflow/dbt_venv/bin/dbt")
target = Variable.get("target")
profile_yml_path = "/opt/airflow/dbt/gdec_dbt/profiles.yml"

venv_execution_config = ExecutionConfig(
    dbt_executable_path=str(dbt_executable),
)

dbt_snowflake = ProfileConfig(
    profile_name="dbt_snowflake",
    target_name=target,
    profiles_yml_filepath=profile_yml_path,
)

@dag(
    schedule_interval="*/10 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["shopee"],
)
def dag_shopee_finance_transactions() -> None:
    shopee_finance_transactions = DbtTaskGroup(
        group_id="shopee_finance_transactions",
        project_config=ProjectConfig(gdec_dbt_path),
        profile_config=dbt_snowflake,
        execution_config=venv_execution_config
    )

    shopee_finance_transactions


dag_shopee_finance_transactions()