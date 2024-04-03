from datetime import datetime
from pathlib import Path

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

from cosmos import ExecutionConfig
from cosmos import DbtTaskGroup, ProjectConfig
from cosmos import ProfileConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

jaffle_shop_path = Path("/opt/airflow/dbt/jaffle_shop")
dbt_executable = Path("/opt/airflow/dbt_venv/bin/dbt")

venv_execution_config = ExecutionConfig(
    dbt_executable_path=str(dbt_executable),
)

snowflake_trial = ProfileConfig(
    profile_name="snowflake_trial",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_trial",
        profile_args={
            "database": "dbt_hol_dev",
            "schema": "public"
      },
    ),
)

@dag(
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example"],
)
def simple_dag() -> None:
    jaffle_shop = DbtTaskGroup(
        group_id="my_jaffle_shop_project",
        project_config=ProjectConfig(jaffle_shop_path),
        profile_config=snowflake_trial,
        execution_config=venv_execution_config,
    )
    jaffle_shop


simple_dag()
