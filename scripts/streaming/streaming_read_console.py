from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import col, avg, sum
import argparse

def process_streaming_data(transient_path, checkpoint_path):
    """Processa dados de produtos em streaming com PySpark."""
    spark = SparkSession.builder.appName("StructuredStreamingExample").getOrCreate()

    schema = StructType([
        StructField("id", StringType(), True),
        StructField("product", StringType(), True),
        StructField("price", FloatType(), True),
        StructField("amount", IntegerType(), True),
        StructField("total_price", FloatType(), True),
        StructField("discount", FloatType(), True)
    ])

    # Lê o fluxo de dados CSV
    input_stream = spark.readStream.format("csv") \
        .option("header", "true") \
        .schema(schema) \
        .load(transient_path)

    # Agregação de dados de exemplo
    aggregated_stream = input_stream.groupBy("product") \
        .agg(
            sum("total_price").alias("total_sales"),
            avg("discount").alias("average_discount")
        )

    # Escreve o fluxo de dados no console
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
