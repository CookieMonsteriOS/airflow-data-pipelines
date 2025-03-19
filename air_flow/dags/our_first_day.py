from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'sc',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='our_first_dag_v2',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime.today(),  
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "hello world, this is the first task"'
    )
    
    task2 = BashOperator(
        task_id='second_task',  
        bash_command='echo "hello world, this is the second task"'
    )

    task1.set_downstream(task2)  
