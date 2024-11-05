from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import col, avg, sum
import argparse

def process_streaming_data(transient_path):
    # creating spark session and setting log level to error
    spark = SparkSession.builder.appName("Streaming_Append_console").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")


    schema = StructType([
        StructField("id", StringType(), True),
        StructField("product", StringType(), True),
        StructField("price", FloatType(), True),
        StructField("amount", IntegerType(), True),
        StructField("total_price", FloatType(), True),
        StructField("discount", FloatType(), True)
    ])

    # reading streaming data
    input_stream = spark.readStream.format("csv") \
        .option("header", "true") \
        .schema(schema) \
        .load(transient_path)

    # here transformations can be done, in this case no transformations were done
    input_stream = input_stream.select('id','product','price','amount','total_price','discount')

    # write data to the destination, in this case the data will be displayed only in the console
    query = input_stream.writeStream \
        .format("console") \
        .outputMode("append") \
        .trigger(processingTime="10 seconds")\
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processamento de dados de produtos em streaming.")
    parser.add_argument("--transient_path", type=str, required=True, help="Diretório de entrada para os arquivos de dados")

    args = parser.parse_args()
    process_streaming_data(args.transient_path)
