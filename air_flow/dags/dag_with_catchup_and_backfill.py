from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'sc',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='catch_up_backfill_v1',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime(2021, 11, 1),  
    schedule_interval='@daily',
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "This is a simple task command"'  
    )
