import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner' : 'airflow '
}

with DAG(
    dag_id='hello_world',
    description='Our first "Hello World" DAG!',
    default_args = default_args,
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = '@daily',
    tags = ['Lrn Airflow', 'LinkedIn']
) as dag:

    task = BashOperator(
        task_id = 'hello_world_task',
        bash_command = 'echo Hello - created DAG using with'
    )

task