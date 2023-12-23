from datetime import datetime, timedelta

import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from config import directory_path, output_file
from get_article import GetArticle
from get_links import (CombineCSV, DKNNewsLink, LinkCrawler, LuatKhoaLink,
                       NgoisaoLink, ThanhNienNewsLinks, VnExpressNewsLink,
                       VTVNewsLinks)


def get_article_and_update_row(row):
    url = row['link']
    get_article_instance = GetArticle(url)
    get_article_instance()
    row['title'] = get_article_instance.get_title()
    row['content'] = get_article_instance.get_content()
    return row

def combine_csv_files():
    link_crawler = LinkCrawler(sources=[
        VTVNewsLinks, ThanhNienNewsLinks, VnExpressNewsLink,
        NgoisaoLink, DKNNewsLink, LuatKhoaLink
    ])()
    CombineCSV(directory_path=directory_path, output_file=output_file)()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_airflow_dag',
    default_args=default_args,
    description='An Airflow DAG for your task',
    schedule_interval=timedelta(days=1),  # Adjust as needed
)

combine_csv_task = PythonOperator(
    task_id='combine_csv_task',
    python_callable=combine_csv_files,
    dag=dag,
)

apply_get_article_task = PythonOperator(
    task_id='apply_get_article_task',
    python_callable=get_article_and_update_row,
    provide_context=True,
    op_args=[],
    dag=dag,
)

combine_csv_task >> apply_get_article_task
