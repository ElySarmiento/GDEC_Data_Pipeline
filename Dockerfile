FROM apache/airflow:2.8.4

ENV AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT=120
ENV AIRFLOW__CORE__DAG_FILE_PROCESSOR_TIMEOUT=200
ENV AIRFLOW__WEBSERVER__BASE_URL="http://ec2-18-140-245-209.ap-southeast-1.compute.amazonaws.com:8080"

COPY requirements.txt .

RUN pip install apache-airflow==2.8.4 -r requirements.txt

ENV PIP_USER=false

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && deactivate

ENV PIP_USER=true