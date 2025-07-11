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
    tags = ['Lrn Airflow', 'LinkedIn','down/up'],
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = timedelta(days=1)
) as dag:
    
    taskA = BashOperator(
        task_id = 'taskA',
        bash_command = '''
        echo TASK A has started!

        for i in {1..10}
        do
            echo TASK A printing $i
        done

        echo TASK A has ended!
        '''
    )

    taskB = BashOperator(
        task_id = 'taskB',
        bash_command = '''
        echo TASK B has started!
        sleep 4
        echo TASK B has ended!
        '''
    )

    taskC = BashOperator(
        task_id = 'taskC',
        bash_command = '''
        echo TASK C has started!
        sleep 15
        echo TASK C has ended!
        '''
    )

    taskD = BashOperator(
        task_id = 'taskD',
        bash_command = 'echo TASK D completed!'
    )

taskA >> taskB
taskA >> taskC

taskD << taskB
taskD << taskC