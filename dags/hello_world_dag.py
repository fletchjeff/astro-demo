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
    def hello_world_task(input_value):
        input_value = input_value + "!"
        return input_value

    @task
    def check_if_world_has_ended():
        from bs4 import BeautifulSoup
        import requests
        url = "https://www.hasthelargehadroncolliderdestroyedtheworldyet.com/"
        req = requests.get(url,verify=False)
        soup = BeautifulSoup(req.content, 'html.parser')
        print(soup.prettify())
        return soup.noscript.string
    
    hello_world_task('Hello world from first Airflow DAG') >> check_if_world_has_ended()

hello_world_dag()