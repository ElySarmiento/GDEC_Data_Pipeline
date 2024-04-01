FROM apache/airflow:2.8.4

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && python -m venv dbt_venv \
    && . dbt_venv/bin/activate \
    && pip install --no-cache-dir dbt-snowflake \
    && deactivate