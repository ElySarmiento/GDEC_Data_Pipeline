from datetime import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


from cosmos import DbtTaskGroup, ProjectConfig, RenderConfig

from include.profiles import snowflake_con
from include.constants import shopee_wallet_transactions_path, venv_execution_config


@dag(
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["simple"],
)
def shopee_wallet_transactions() -> None:
    """
    dbt task to create fct_shopee_finance_transactions model
    """
    pre_dbt = EmptyOperator(task_id="pre_dbt")

    shopee_wallet_transactions = DbtTaskGroup(
        group_id="shopee_wallet_transactions",
        project_config=ProjectConfig(shopee_wallet_transactions_path),
        profile_config=snowflake_con,
        render_config=RenderConfig(
            select=["tag:shopee_wallet_transactions"],
        ),
        execution_config=venv_execution_config,
    )
    
    pre_dbt >> shopee_wallet_transactions


shopee_wallet_transactions()
