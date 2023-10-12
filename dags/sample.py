import datetime
from airflow import DAG
from operators.googleOperator import MyFirstOperator
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="sample",
    schedule=None,
    start_date=datetime.datetime(2021, 1, 1),
    catchup=False,
    tags=["pipeline"],
) as dag:
    trigger_google_operator = MyFirstOperator(
        task_id="Google_operator"
    )

    airflow_info = BashOperator(task_id="airflow_info", bash_command="airflow info")

    trigger_google_operator >> airflow_info