FROM apache/airflow:2.8.4

COPY requirements.txt .

RUN pip install apache-airflow==2.8.4 -r requirements.txt

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && deactivate