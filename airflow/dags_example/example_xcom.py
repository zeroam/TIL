import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


args = {
    'owner': 'jayone',
    'start_date': days_ago(2),
}

dag = DAG('example_xcom', schedule_interval='@daily', default_args=args, tags=['example'])

value_1 = [1, 2, 3]
value_2 = {'a': 'b'}


def push(**kwargs):
    """Pushes an XCom without a specific target"""
    print(kwargs)
    print('push an Xcom:', datetime.datetime.now())
    kwargs['ti'].xcom_push(key='value from pusher 1', value=value_1)


def push_by_returning(**kwargs):
    print(kwargs)
    """Pushes an XCom without a specific target, just by returning it"""
    print('push by returning:', datetime.datetime.now())
    print('macro day: {{ ds }}')
    return value_2


def puller(**kwargs):
    """Pull all previously pushed XComs and check it the pushed values match the pulled values."""
    ti = kwargs['ti']

    # get value_1
    pulled_value_1 = ti.xcom_pull(key=None, task_ids='push')
    if pulled_value_1 != value_1:
        raise ValueError(f'The two values differ {pulled_value_1} and {value_1}')

    # get value_2
    pulled_value_2 = ti.xcom_pull(task_ids='push_by_returning')
    if pulled_value_2 != value_2:
        raise ValueError(f'The two values differ {pulled_value_2} and {value_2}')

    # get both value_1 and value_2
    pulled_value_1, pulled_value_2 = ti.xcom_pull(key=None, task_ids=['push', 'push_by_returning'])
    if pulled_value_1 != value_1:
        raise ValueError(f'The two values differ {pulled_value_1} and {value_1}')
    if pulled_value_2 != value_2:
        raise ValueError(f'The two values differ {pulled_value_2} and {value_2}')

    print(f'pulled_value_1: {pulled_value_1}')
    print(f'pulled_value_2: {pulled_value_2}')


push1 = PythonOperator(
    task_id='push',
    dag=dag,
    python_callable=push,
    provide_context=True,
)

push2 = PythonOperator(
    task_id='push_by_returning',
    dag=dag,
    python_callable=push_by_returning,
)

pull = PythonOperator(
    task_id='puller',
    dag=dag,
    python_callable=puller,
    provide_context=True,
)

pull << [push1, push2]
