import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args ={
    'owner' : 'airflow '
}

def greet_hello(name):
        print("Hello, {name}!".format(name=name))
              
def greet_hello_with_city(name, city):
        print("Hello, {name} from {city}.".format(name=name, city=city))

with DAG(
    dag_id = 'execute_python_operators',
    description = 'Python operators in DAGs with parameters',
    default_args = default_args,
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = '@daily',
    tags = ['Lrn Airflow', 'LinkedIn','parameters']
) as dag:
    taskA = PythonOperator(
        task_id = 'greet_hello',
        python_callable = greet_hello,
        op_kwargs ={'name': 'Ozzy'}
    )

    taskB = PythonOperator(
        task_id = 'greet_hello_with_city',
        python_callable = greet_hello_with_city,
        op_kwargs = {'name':'Louise', 'city':'Seattle'}
    )

taskA >> taskB