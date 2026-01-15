from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

project_path = '/opt/airflow/project'

with DAG(
    dag_id="scrapy_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:
    
    #1: Scrapy
    scrape_data = BashOperator(
        task_id='run_scrapy',
        cwd='/opt/airflow/project/ecommerce_scraper',
        # We explicitly export the path in the command itself
        bash_command='export PYTHONPATH=$PYTHONPATH:/opt/airflow/project/ecommerce_scraper && python3 -m scrapy crawl cute_mercado_livre_spider',
    )

    #2: DBT Staging
    dbt_staging = BashOperator(
        task_id='run_dbt_part1',
        bash_command=f'cd {project_path}/dbt_project && dbt run --select stg_data --profiles-dir .'
    )

    #3: Great Expectations
    gx_validate = BashOperator(
        task_id='run_gx',
        bash_command=f'python3 {project_path}/run_validation.py'
    )

    #4: DBT Marts
    dbt_marts = BashOperator(
        task_id='run_dbt_part2',
        bash_command=f'cd {project_path}/dbt_project && dbt run --select dim_products fact_listings --profiles-dir .'
    )

    scrape_data >> dbt_staging >> gx_validate >> dbt_marts