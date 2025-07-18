FROM apache/airflow:2.10.2
USER airflow

#RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir pandas==2.2.2 psycopg2-binary==2.9.9
#RUN mkdir -p /opt/airflow/jars && \
#    wget -O /opt/airflow/jars/postgresql-42.7.7.jar \
#    https://jdbc.postgresql.org/download/postgresql-42.7.7.jar

USER ${AIRFLOW_UID:-50000}