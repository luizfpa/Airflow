import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args ={
    'owner' : 'airflow '
}

def print_function():
        print("The simplest possible PythonOperator!")

with DAG(
    dag_id = 'execute_python_operators',
    description = 'Python operators in DAGs',
    default_args = default_args,
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = '@daily',
    tags = ['Lrn Airflow', 'LinkedIn','simple/python']
) as dag:

    task = PythonOperator(
        task_id = 'python_task',
        python_callable = print_function
    )

task