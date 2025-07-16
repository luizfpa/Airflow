import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

import pandas as pd

default_args = {
    'owner': 'airflow'
}

def read_csv_file():
    df = pd.read_csv('/opt/airflow/datasets/insurance.csv')
    print(df)
    return df.to_json()

with DAG(
    dag_id = 'python_pipeline',
    description = 'Running a Python Pipeline',
    default_args = default_args,
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = '@once',
    tags = ['LinkedIn', 'LrnAirflow', 'Python_Pipeline']
)as dag:

    read_csv_file = PythonOperator(
        task_id = 'read_csv_file',
        python_callable = read_csv_file
    )

read_csv_file