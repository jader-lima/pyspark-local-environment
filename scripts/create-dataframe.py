from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType


# Create spark session
spark = SparkSession.builder.appName("create_dataframe").getOrCreate()

# create python list for data
data2 = [("James","","Smith","36636","M",3000),
    ("Michael","Rose","","40288","M",4000),
    ("Robert","","Williams","42114","M",4000),
    ("Maria","Anne","Jones","39192","F",4000),
    ("Jen","Mary","Brown","","F",-1)
  ]

# create dataframe schema
schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ])
 
# create spark dataframe using python data list and schema , showing dataframe schema and data
df = spark.createDataFrame(data=data2,schema=schema)
df.printSchema()
df.show(truncate=False)

# stopping spark session
spark.stop()
