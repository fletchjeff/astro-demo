from datetime import datetime
from platform import architecture
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.task_group import TaskGroup
import requests
import json

args = {
    'depends_on_past': False,
    'retries': 0
}

def print_hello():
    return 'Hello world from first Airflow DAG!'

def api_dag(dag_list_number):
    print("testing the dag")
    return dag_list_number

dag = DAG('hello_world_demo', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), 
          catchup=False,
          default_args=args
        )

with dag:        
    hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator
