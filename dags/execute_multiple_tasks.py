import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner' : 'airflow '

}

with DAG(
    dag_id = 'executing_multiple_tasks',
    description = 'DAG with multiple tasks and dependencies',
    default_args = default_args,
    tags = ['Lrn Airflow', 'LinkedIn'],
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = '@once'
) as dag:
    
    taskA = BashOperator(
        task_id = 'taskA',
        bash_command = 'echo TASK A has executed.'
    )

    taskB = BashOperator(
        task_id = 'taskB',
        bash_command = 'echo Task B has executed.'
    )

taskA.set_downstream(taskB)