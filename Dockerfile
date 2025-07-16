FROM apache/airflow:2.10.2
USER airflow

RUN pip install --no-cache-dir pandas==2.2.2 pyspark==3.5.0 psycopg2-binary==2.9.9

# Configurar JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Criar diretório para JARs e baixar PostgreSQL JDBC
RUN mkdir -p /opt/airflow/jars && \
    wget -O /opt/airflow/jars/postgresql-42.7.7.jar \
    https://jdbc.postgresql.org/download/postgresql-42.7.7.jar


USER ${AIRFLOW_UID:-50000}