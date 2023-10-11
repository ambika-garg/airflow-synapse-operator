from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="airflow-ci-cd-tutorial",
    start_date=datetime(2023, 8, 15),
    schedule="0 0 * * *",
    tags=["tutorial", "CI/CD"]
) as dag:
    python_version = BashOperator(task_id="pythonversion", bash_command="python --version")
    python_version
