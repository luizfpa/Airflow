FROM apache/airflow:2.8.1

USER root

# Instalar Java 17 (disponível no Debian 12)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk wget && \
    apt-get clean

# Configurar JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Criar diretório para JARs e baixar PostgreSQL JDBC
RUN mkdir -p /opt/airflow/jars && \
    wget -O /opt/airflow/jars/postgresql-42.7.7.jar \
    https://jdbc.postgresql.org/download/postgresql-42.7.7.jar

USER airflow