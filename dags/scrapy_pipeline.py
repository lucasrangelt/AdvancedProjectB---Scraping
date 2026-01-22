from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.amazon.aws.operators.ecs import EcsRunTaskOperator
from datetime import datetime

project_path = '/opt/airflow/project'

CLUSTER_NAME = "default"
TASK_DEFINITION = "default-ecommerce-scraper-aws-repo-02fe:1"
SUBNETS = ["subnet-0f4aafd135a236f88"]
SECURITY_GROUPS = ["sg-0cfb5511c9fcd96f9"]


with DAG(
    dag_id="scrapy_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:
    
    run_cloud_scrape = EcsRunTaskOperator(
        task_id="run_scrapy_on_fargate",
        cluster=CLUSTER_NAME,
        task_definition=TASK_DEFINITION,
        launch_type="FARGATE",
        overrides={
            "containerOverrides": [
                {
                    "name": "Main",
                    "command": ["scrapy", "crawl", "cute_mercado_livre_spider"],
                },
            ],
        },
        network_configuration={
            "awsvpcConfiguration": {
                "subnets": SUBNETS,
                "securityGroups": SECURITY_GROUPS,
                "assignPublicIp": "ENABLED",
            },
        },
        aws_conn_id="aws_default",
        region_name="sa-east-1"
    )

    # #1: Scrapy
    # scrape_data = BashOperator(
    #     task_id='run_scrapy',
    #     bash_command='cd {project_path}/ecommerce_scraper && python3 -m scrapy crawl cute_mercado_livre_spider',
    # )

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

    run_cloud_scrape >> dbt_staging >> gx_validate >> dbt_marts