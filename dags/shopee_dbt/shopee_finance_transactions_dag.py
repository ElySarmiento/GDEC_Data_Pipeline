from pathlib import Path

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

from cosmos import ExecutionConfig
from cosmos import DbtTaskGroup, ProjectConfig
from cosmos import ProfileConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

GDEC_DBT_PATH = Path("/opt/airflow/dbt/gdec_dbt")
DBT_EXECUTABLE = Path("/opt/airflow/dbt_venv/bin/dbt")

venv_execution_config = ExecutionConfig(
    dbt_executable_path=str(DBT_EXECUTABLE),
)

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

@dag(
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["shopee"],
)
def dag_shopee_finance_transactions() -> None:
    """
    The simplest example of using Cosmos to render a dbt project as a TaskGroup.
    """
    pre_dbt = EmptyOperator(task_id="pre_dbt")

    shopee_finance_transactions = DbtTaskGroup(
        group_id="shopee_finance_transactions",
        project_config=ProjectConfig(GDEC_DBT_PATH),
        profile_config=dbt_snowflake,
        execution_config=venv_execution_config,
    )

    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> shopee_finance_transactions >> post_dbt


dag_shopee_finance_transactions()