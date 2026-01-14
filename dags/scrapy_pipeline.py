from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime

with DAG(
    dag_id="scrapy_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    #1: Scrapy
    scrape_data = BashOperator(
        task_id = 'run_scrapy',
        bash_command = 'cd /opt/airflow/project && scrapy crawl cute_mercado_livre_spider'
    )