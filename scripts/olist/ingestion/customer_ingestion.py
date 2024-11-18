import os
os.system("pip install /opt/spark/data/libs/lib_custom_python-0.1.0-py3-none-any.whl")
os.system("pip freeze")

from pyspark.sql import SparkSession
from lib_custom_python.storage_functions.storage_functions import read_text_file, write_parquet

# Create spark session
spark = SparkSession.builder.appName("olist_customer_ingestion").getOrCreate()

path = '/opt/spark/data/olist/olist_customers_dataset.csv'

# load csv data to a spark dataframe
df_customer = read_text_file( spark, 'csv', True,True, ',', path,'"', "UTF-8")

df_customer.printSchema()

path_bronze = '/opt/spark/data/bronze/olist/customers'
mode = 'overwrite'
# saving dataframe

write_parquet(df_customer, path_bronze, mode)

# stopping spark session
spark.stop()
