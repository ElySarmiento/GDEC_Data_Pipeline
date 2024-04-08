# Airflow DAGs

This repository contains the tasks (scripts and DAGs) executed by Airflow. Kindly push your DAGs here following these conventions:

- Group the DAGs according to their purpose (e.g. shopee dbt models, ingestion, pipelines)
- For dbt DAGs, name the DAG as: `<name of final dbt model>_dag.py`
- For DAGs that call external scripts, place the DAG and the scripts together inside a folder. Folder name should be the same with the DAG

```
airflow-dags
├── lazada_dbt
├── shopee_dbt
│   ├── shopee_finance_transactions_dag.py
│   └── shopee_escrow_details_dag.py
├── pipelines
│   └── random_pipeline
│       ├── random_pipeline_dag.py
│       ├── python_script1.py
│       └── python_script2.py
├── .airflowignore
└── README.md
```