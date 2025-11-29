FROM apache/airflow:3.1.1
USER root
# install Docker CLI + the Compose plugin inside the Airflow image
RUN apt-get update && \
    apt-get install -y --no-install-recommends docker.io docker-compose-plugin && \
    rm -rf /var/lib/apt/lists/*
# let the 'airflow' user run docker
RUN groupadd -f docker && usermod -aG docker airflow || true
USER airflow
