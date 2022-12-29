from datetime import datetime
from airflow import DAG
from airflow.decorators import task, dag

args = {
    'depends_on_past': False,
    'retries': 0
}

@dag(
    schedule=None,
    start_date=datetime(2022, 12, 29),
    catchup=False,
    default_args=args
)

def hello_world_dag():
    @task
    def hello_world_task():
        return 'Hello world from first Airflow DAG!'

    hello_world = hello_world_task()

hello_world_dag()