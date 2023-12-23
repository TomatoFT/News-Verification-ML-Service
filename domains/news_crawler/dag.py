from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define the default_args dictionary to specify the default parameters for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define a DAG with the specified default_args
dag = DAG(
    'your_airflow_dag',
    default_args=default_args,
    description='A simple Airflow DAG to run main.py',
    schedule_interval='30 19 * * *',  # Run every day at 19:30
)

# Define the PythonOperator to run main.py
run_main_script_task = PythonOperator(
    task_id='run_main_script',
    python_callable=lambda: exec(open("/app/main.py").read()),
    dag=dag,
)

# Set the task dependencies
run_main_script_task

if __name__ == "__main__":
    dag.cli()
