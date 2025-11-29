from __future__ import annotations
import pendulum

# Airflow SDK imports
from airflow.sdk import dag
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator

# Define the project directory where the docker-compose.yaml is located
PROJECT_DIR = "/opt/my_job_pipeline"

@dag(
    dag_id="my_article_pipeline",
    schedule="0 8 * * *",                        # every day at 08:00
    start_date=pendulum.today("UTC").subtract(days=1),
    catchup=False,
    tags=["project", "docker", "etl"],
)
def run_my_etl_pipeline():
    start = EmptyOperator(task_id="start")

    # Task to run the Docker Compose ETL pipeline
    run_docker_compose_etl = BashOperator(
        task_id="run_docker_compose_etl",
        bash_command="docker compose up -d --build && docker compose ps",
        cwd=PROJECT_DIR,
        retries=2,
        retry_delay=pendulum.duration(minutes=1),
    )

    end = EmptyOperator(task_id="end")

    start >> run_docker_compose_etl >> end

run_my_etl_pipeline()
