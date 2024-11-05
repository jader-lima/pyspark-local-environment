from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import col, avg, sum
import argparse

def process_streaming_data(transient_path, checkpoint_path):
    # creating spark session and setting log level to error , it coudl be warn,info and error
    spark = SparkSession.builder.appName("StructuredStreamingExample").getOrCreate()
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

    # creating a aggregation using product field as group by field 
    aggregated_stream = input_stream.groupBy("product") \
        .agg(
            sum("total_price").alias("total_sales"),
            avg("discount").alias("average_discount")
        )

    # write data to the destination, in this case the data will be displayed only in the console
    query = aggregated_stream.writeStream \
        .format("console") \
        .outputMode("complete") \
        .trigger(processingTime="10 seconds") \
        .option("checkpointLocation", checkpoint_path) \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processamento de dados de produtos em streaming.")
    parser.add_argument("--transient_path", type=str, required=True, help="Diretório de entrada para os arquivos de dados")
    parser.add_argument("--checkpoint_path", type=str, required=True, help="Diretório para armazenar os checkpoints")

    args = parser.parse_args()
    process_streaming_data(args.transient_path, args.checkpoint_path)
