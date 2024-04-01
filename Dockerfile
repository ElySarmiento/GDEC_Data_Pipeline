FROM apache/airflow:2.8.4

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install apache-airflow==2.8.4 \
    && python -m venv dbt_venv \
    && /bin/bash -c "source dbt_venv/bin/activate && pip install --no-cache-dir -r requirements.txt && deactivate || exit 0"
