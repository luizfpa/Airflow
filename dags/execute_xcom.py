import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args ={
    'owner' : 'airflow '
}

def increment_by_1(counter):
        print("Count, {counter}!".format(counter=counter))
        return counter + 1

def multiply_by_100(counter):
        print("Count, {counter}!".format(counter=counter))
        return counter * 100

with DAG(
    dag_id = 'cross_task_communication',
    description = 'Cross-tasks communication with XCom',
    default_args = default_args,
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = '@daily',
    tags = ['Lrn Airflow', 'LinkedIn','XCom']
) as dag:
    taskA = PythonOperator(
        task_id = 'increment_by_1',
        python_callable = increment_by_1,
        op_kwargs ={'counter': 55}
    )

    taskB = PythonOperator(
        task_id = 'multiply_by_100',
        python_callable = multiply_by_100,
        op_kwargs = {'counter':98}
    )

taskA >> taskB