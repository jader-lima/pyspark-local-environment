from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType


# Create spark session
spark = SparkSession.builder.appName("olist_customer_ingestion").getOrCreate()

df_customer  = spark.read.format('csv').load('/opt/spark/data/olist/olist_customers_dataset.csv')

df_customer.printSchema()
df_customer.write.format('parquet').mode('overwrite').save('/opt/spark/data/bronze/olist/customers')

# stopping spark session
spark.stop()
