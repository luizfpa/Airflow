import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
from Postgres_ETL import *

# Configuração para ambiente Linux/Docker
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'
os.environ['SPARK_HOME'] = '/opt/spark'
os.environ['HADOOP_HOME'] = '/opt/spark'
os.environ['PYSPARK_SUBMIT_ARGS'] = '--driver-class-path /opt/airflow/jars/postgresql-42.7.7.jar pyspark-shell'
os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'

def etl_pipeline():
    movies_df = extract_movies_to_df()
    users_df = extract_users_to_df()
    transformed_df = transform_avg_ratings(movies_df, users_df)
    load_df_to_db(transformed_df)

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),
    'depends_on_past': False,
    'email': ['info@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    dag_id='etl_pipeline',
    default_args=default_args,
    schedule_interval='0 0 * * *',
    catchup=False
)

etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=etl_pipeline,
    dag=dag
)