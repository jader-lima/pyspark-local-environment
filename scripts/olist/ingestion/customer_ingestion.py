import os
os.system("pip install /opt/spark/data/libs/lib_custom_python-0.1.0-py3-none-any.whl")
os.system("pip freeze")
from pyspark.sql import SparkSession
from lib_custom_python.storage_functions import read_text_file  


# Create spark session
spark = SparkSession.builder.appName("olist_customer_ingestion").getOrCreate()

path = '/opt/spark/data/olist/olist_customers_dataset.csv'

df_customer = read_text_file( spark, csv, True,True, ',', path,'"', "UTF-8")

#df_customer  = spark.read.format('csv').load('/opt/spark/data/olist/olist_customers_dataset.csv')

df_customer.printSchema()
#df_customer.write.format('parquet').mode('overwrite').save('/opt/spark/data/bronze/olist/customers')

# stopping spark session
spark.stop()
