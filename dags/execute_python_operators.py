import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args ={
    'owner' : 'airflow '
}

def task_a():
        print("Task A executed!")

def task_b():
        print("Task B executed!")
        
def task_c():
        print("Task C executed!")

def task_d():
        print("Task D executed!")

with DAG(
    dag_id = 'execute_python_operators',
    description = 'Python operators in DAGs',
    default_args = default_args,
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = '@daily',
    tags = ['Lrn Airflow', 'LinkedIn','dependecies']
) as dag:
    taskA = PythonOperator(
        task_id = 'taskA',
        python_callable = task_a
    )

    taskB = PythonOperator(
        task_id = 'taskB',
        python_callable = task_b
    )

    taskC = PythonOperator(
        task_id = 'taskC',
        python_callable = task_c
    )

    taskD = PythonOperator(
        task_id = 'taskD',
        python_callable = task_d
    )

taskA >> [taskB, taskC]
[taskB, taskC] >> taskD