FROM apache/airflow:2.8.4

ADD requirements.txt .

RUN pip install apache-airflow==2.8.4 -r requirements.txt