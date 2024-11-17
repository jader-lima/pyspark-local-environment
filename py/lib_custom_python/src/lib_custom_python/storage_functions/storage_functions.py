from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.utils import AnalysisException
from pyspark.sql.types import StructType
from delta.tables import *
import io
import json

OVERWRITE = 'overwrite'


def IsDelta(spark: SparkSession, path: str):
    try:
        data = read_delta_file(spark, path)
        return True
    except AnalysisException as ex:
        print(ex)
        return False

def read_json_file( spark: SparkSession, path: str):
    #if not is_empty(path):
    data = spark.read.format('json').load(path)
    return data


def read_json_multiline(spark, path):
    try:
        return spark.read.option("multiline", "true").json(path)
    except:
        return spark.createDataFrame([], StructType([]))


def read_json_with_schema(spark, schema, path):
    try:
        return spark.read.schema(schema.schema).json(path)
    except:
        return spark.createDataFrame([], StructType([]))


def read_text_file( spark: SparkSession, file_format: str, has_header: bool,
                   infer_schema: bool, delimiter: str, path: str,text_delimiter:str, charset: str = "UTF-8"):
    #if not is_empty(, path):
    data = spark.read.format(file_format) \
        .option('header', has_header) \
        .option('inferSchema', infer_schema) \
        .option('sep', delimiter) \
        .option("quote", text_delimiter) \
        .option("charset", charset) \
        .load(path)

    return data


def read_text_file_from_schema( spark: SparkSession, file_format: str, schema: StructType,
                   delimiter: str, path: str):
    #if not is_empty(dbutils, path):
    data = spark.read.format(file_format) \
        .option('header', False) \
        .option('schema', schema) \
        .option('sep', delimiter) \
        .load(path)

    return data


def read_delta_file(spark: SparkSession, path: str):
    #if not is_empty(dbutils, path):
    return spark.read \
        .format('delta') \
        .option('inferSchema', 'true') \
        .load(path)


def read_delta_table(spark: SparkSession, path: str):
    table = DeltaTable.forPath(spark, path)
    return table


def write_delta_file(data: DataFrame, path: str, mode: str):
    #if not data.rdd.isEmpty():
    data.write \
        .format('delta') \
        .option("overwriteSchema", "true") \
        .save(path, mode=mode)


def read_parquet(spark: SparkSession, path: str):
    #if not is_empty(dbutils, path):
    data = spark.read.format('parquet').load(path)
    return data

def write_parquet(data: DataFrame, path: str, mode: str):
    data.write \
            .format('parquet') \
            .option("overwriteSchema", "true") \
            .save(path, mode=mode)

def create_table(spark, df_empty,df_input, db_name, table_name,folder_path, overwrite):
    if not (spark._jsparkSession.catalog().tableExists(f"{db_name}.{table_name}")):
        df_empty.write.mode('overwrite').format('delta')\
        .option('path',folder_path)\
        .option('delta.enableChangeDataFeed', 'true')\
        .saveAsTable(f"{db_name}.{table_name}")
    else:
        if(overwrite == True):
            df_input.write.mode('overwrite').format('delta').insertInto(f"{db_name}.{table_name}")
