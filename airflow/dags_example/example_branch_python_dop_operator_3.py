from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'jayone',
    'start_date': days_ago(2),
    'depends_on_past': True,
}

dag = DAG(
    dag_id='example_branch_dop_operator_v3',
    schedule_interval='*/1 * * * *',
    default_args=args,
    tags=['example']
)


def should_run(**kwargs):
    """
    Determine which dummy_task should be run based on 
    if the execution date minute is even or odd.

    :param dict kwargs: Context
    :return: Id of the task to run
    :rtype: str
    """
    print('---------- exec dttm = {} and minute = {}'.
          format(kwargs['execution_date'], kwargs['execution_date'].minute))
    if kwargs['execution_date'].minute % 2 == 0:
        return "dummy_task_1"
    else:
        return "dummy_task_2"


cond = BranchPythonOperator(
    task_id='condition',
    python_callable=should_run,
    dag=dag,
    provide_context=True,
)

dummy_task_1 = DummyOperator(task_id='dummy_task_1', dag=dag, provide_context=True)
dummy_task_2 = DummyOperator(task_id='dummy_task_2', dag=dag, provide_context=True)

cond >> [dummy_task_1, dummy_task_2]
