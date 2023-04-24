from datetime import datetime
from airflow.decorators import task, dag
from airflow.operators.python import PythonOperator

args = {
    'depends_on_past': False,
    'retries': 0
}

def _hello_world_task(input_value):
    print(f'input_value is: {input_value}')
    input_value = input_value + "!"
    return input_value

@dag(
    schedule=None,
    start_date=datetime(2022, 12, 29),
    catchup=False,
    default_args=args
)

def hello_world_dag():

    hello_world_task = PythonOperator(
        task_id="hello_world_task",
        python_callable=_hello_world_task,
        op_kwargs={'input_value':'Hello world'}
    )

    @task
    def check_if_world_has_ended(lhc_url):
        from bs4 import BeautifulSoup
        import requests
        url = lhc_url
        req = requests.get(url,verify=False)
        soup = BeautifulSoup(req.content, 'html.parser')
        print(soup.prettify())
        return soup.noscript.string
    
    hello_world_task >> check_if_world_has_ended("https://www.hasthelargehadroncolliderdestroyedtheworldyet.com/")



hello_world_dag()
