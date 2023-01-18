from sqlalchemy.engine import create_engine
from dotenv import dotenv_values
from pathlib import Path
import os
from pyspark.sql import SparkSession
config = dotenv_values(os.path.join(Path(__file__).parent,"environment.env"))
def create_the_pg_engine():
    

    host=config["pg_host"]
    port=config["pg_port"]
    database=config["pg_database"]


    url = f"jdbc:postgresql://{host}:{port}/{database}"
    return url

def load_green_table():
    url = create_the_pg_engine()
    spark = SparkSession.builder.master("local").config("spark.jars.packages","org.postgresql:postgresql:42.5.1").appName("none").getOrCreate()
    spark.read.csv("/Users/danie/datazoom/green_tripdata_2019-01.csv",inferSchema='true',header='true')\
        .write.mode("append").format("jdbc").option("url",url)\
        .option("user", config["pg_user"]).option("password", config["pg_password"])\
        .option("dbtable","green")\
        .option("driver", "org.postgresql.Driver").save()

def load_zone_table():
    url = create_the_pg_engine()
    spark = SparkSession.builder.master("local").config("spark.jars.packages","org.postgresql:postgresql:42.5.1").appName("none").getOrCreate()
    spark.read.csv("/Users/danie/datazoom/taxi+_zone_lookup.csv",inferSchema='true',header='true')\
        .write.mode("append").format("jdbc").option("url",url)\
        .option("user", config["pg_user"]).option("password", config["pg_password"])\
        .option("dbtable","zone")\
        .option("driver", "org.postgresql.Driver").save()

load_zone_table()