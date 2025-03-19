from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'sc',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
# Define the DAG
with DAG(
    dag_id='dag_postgres_operator_v02.1',
    default_args=default_args,
    start_date=datetime(2021, 12, 19),
    schedule_interval='0 0 * * *',
) as dag:
    
    # Define the tasks
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='postgres_localhost',  
        sql="""
            CREATE TABLE IF NOT EXISTS dag_runs (
                dt DATE,
                dag_id CHARACTER VARYING,
                PRIMARY KEY (dt, dag_id)
            )
        """
    )

    task2 = PostgresOperator(
        task_id='insert_into_table',
        postgres_conn_id='postgres_localhost', 
        sql="""
            INSERT INTO dag_runs (dt, dag_id) 
            VALUES ('{{ ds }}', '{{ dag.dag_id }}')
        """
    )

    task3 = PostgresOperator(
        task_id='delete_data_from_table',
        postgres_conn_id='postgres_localhost',  
        sql="""
            DELETE FROM dag_runs 
            WHERE dt = '{{ ds }}' AND dag_id = '{{ dag.dag_id }}'
        """
    )

    # Define the task dependencies
    task1 >> task3 >> task2