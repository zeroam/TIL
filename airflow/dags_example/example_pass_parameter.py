from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago, datetime

from time import sleep
from datetime import datetime

args = {
    'owner': 'jayone',
    'start_date': days_ago(2)
}


def my_func(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    return args[0]


with DAG('python_dag', description='Python DAG', default_args=args) as dag:
    dummy_task = DummyOperator(task_id='dummy_task', retries=3)
    python_task = PythonOperator(task_id='python_task', python_callable=my_func,
                                 op_args=['one', 'two', 'three'],
                                 op_kwargs={'today': '{{ ds }}'})

    dummy_task >> python_task