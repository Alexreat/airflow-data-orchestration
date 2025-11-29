#  Airflow Data Orchestration

![Airflow](https://img.shields.io/badge/Apache%20Airflow-2.8-blue?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-ETL-yellow?style=for-the-badge)

A production-ready **Apache Airflow** setup designed to orchestrate complex ETL workflows. This project demonstrates how to containerize Airflow using Docker and schedule daily data ingestion pipelines.

##  Architecture
* **Executor:** CeleryExecutor (Scalable worker architecture for parallel tasks).
* **Database:** PostgreSQL (Metadata store).
* **Broker:** Redis (Message broker for task queuing).
* **Containerization:** Fully defined in `docker-compose.yaml`.

##  Project Structure
```bash
├── dags/                # ⚡ Python workflows (DAGs)
│   └── my_article_pipeline.py # Data extraction logic
├── plugins/             # 🔌 Custom operators/hooks
├── config/              # ⚙️ Airflow configuration overrides
├── docker-compose.yaml  # Infrastructure definition
└── Dockerfile           # Custom image with dependencies
