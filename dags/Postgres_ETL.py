# Importing Libraries
try:
    import pyspark.sql
    from pyspark.sql import SparkSession
    PYSPARK_AVAILABLE = True
    print("PySpark is available")
except ImportError:
    PYSPARK_AVAILABLE = False
    print("PySpark is not available")

# Initialize Spark Session only if PySpark is available
if PYSPARK_AVAILABLE:
    import os
    # Forçar modo local sem spark-submit
    os.environ['PYSPARK_SUBMIT_ARGS'] = '--driver-class-path /opt/airflow/jars/postgresql-42.7.7.jar pyspark-shell'
    os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'
    
    # Creating Spark Session with local mode
    spark = SparkSession.builder \
        .appName("Postgres Connection") \
        .master("local[1]") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .config("spark.ui.enabled", "false") \
        .config("spark.sql.adaptive.enabled", "false") \
        .config("spark.jars", "/opt/airflow/jars/postgresql-42.7.7.jar") \
        .getOrCreate()

    # Reading Data from Postgres
    def extract_movies_to_df():
        movies_df = spark.read.format("jdbc")\
            .option("url", "jdbc:postgresql://host.docker.internal:5432/etl_pipeline")\
            .option("dbtable", "movies")\
            .option("user", "postgres")\
            .option("password", "admin")\
            .option("driver", "org.postgresql.Driver")\
            .load()
        return movies_df

    def extract_users_to_df():
        users_df = spark.read.format("jdbc")\
            .option("url", "jdbc:postgresql://host.docker.internal:5432/etl_pipeline")\
            .option("dbtable", "users")\
            .option("user", "postgres")\
            .option("password", "admin")\
            .option("driver", "org.postgresql.Driver")\
            .load()
        return users_df

    def transform_avg_ratings(movies_df, users_df):
        avg_rating = users_df.groupBy("movie_id").mean("rating")
        df_join = movies_df.join(avg_rating, movies_df.id == avg_rating.movie_id)
        df_join = df_join.drop("movie_id")
        return df_join

    # Load transformed dataframe to the database
    def load_df_to_db(df):
        mode = "overwrite"
        url = "jdbc:postgresql://host.docker.internal:5432/etl_pipeline"
        properties = {"user": "postgres",
                      "password": "admin",
                      "driver": "org.postgresql.Driver"
                      }
        df.write.jdbc(url=url,
                      table="avg_ratings",
                      mode=mode,
                      properties=properties)

else:
    # Fallback functions when PySpark is not available
    def extract_movies_to_df():
        print("PySpark não disponível - usando pandas como alternativa")
        # Aqui você pode implementar com pandas se quiser
        return None

    def extract_users_to_df():
        print("PySpark não disponível - usando pandas como alternativa")
        return None

    def transform_avg_ratings(movies_df, users_df):
        print("PySpark não disponível - transformação não realizada")
        return None

    def load_df_to_db(df):
        print("PySpark não disponível - dados não carregados")
        return None

if __name__ == "__main__":
    if PYSPARK_AVAILABLE:
        movies_df = extract_movies_to_df()
        users_df = extract_users_to_df()
        ratings_df = transform_avg_ratings(movies_df, users_df)
        load_df_to_db(ratings_df)
    else:
        print("Não é possível executar sem PySpark")