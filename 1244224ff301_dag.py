from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from datetime import datetime, timedelta

# Define params for the Databricks Submit Run Operator
notebook_task = {
    'notebook_path': '/path/to/your/notebook',  # Replace with the relative notebook path in Databricks
}

default_args = {
    'owner': '1244224ff301',  
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='1244224ff301_dag',  
    default_args=default_args,
    description='A simple DAG to trigger a Databricks Notebook',
    schedule_interval='@daily',  # This sets the schedule to daily
    start_date=datetime(2023, 1, 1),  # Start date for the DAG
    catchup=False,
) as dag:

    submit_run = DatabricksSubmitRunOperator(
        task_id='submit_run',
        databricks_conn_id='databricks_default',
        existing_cluster_id='1108-162752-8okw8dgg',  # Replace with your Databricks Cluster ID
        notebook_task=notebook_task
    )

    submit_run
    