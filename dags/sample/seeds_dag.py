from datetime import datetime
from pathlib import Path

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

from cosmos import DbtTaskGroup, ProjectConfig, RenderConfig
from cosmos import ExecutionConfig
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
    tags=["filtering"],
)
def seeds_dag() -> None:

    pre_dbt = EmptyOperator(task_id="pre_dbt")

    seeds = DbtTaskGroup(
        group_id="jaffle_shop_seeds",
        project_config=ProjectConfig(jaffle_shop_path),
        profile_config=snowflake_trial,
        execution_config=venv_execution_config,
        # new render config
        render_config=RenderConfig(
            select=["path:seeds"],
        )
    )

    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> seeds >> post_dbt

seeds_dag()

