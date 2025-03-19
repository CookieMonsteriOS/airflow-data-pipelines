from airflow.decorators import dag, task  
from datetime import datetime, timedelta

default_args = {
    'owner': 'sc',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id='our_first_dag_with_task_flow_api_v01.1',
    default_args=default_args,
    description='Python Dag using TaskFlow API',
    start_date=datetime(2025, 3, 13),
    schedule_interval='@daily'
)
def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name': 'F'
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World, I'm {first_name} {last_name} and am aged {age}")

    # Task execution order
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'],age=age)

greet_day = hello_world_etl()
