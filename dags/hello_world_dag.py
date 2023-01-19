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

def hello_world_dag_demo_test():
    @task
    def hello_world_task(input_value):
        input_value = input_value + "!"
        return input_value

    hello_world_task('Hello world from first Airflow DAG')

hello_world_dag_demo_test()