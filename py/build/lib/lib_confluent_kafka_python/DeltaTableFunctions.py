from typing import Union, List
from pyspark.sql import DataFrame
from delta import DeltaTable
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField 

def create_empty_deltatable(spark: SparkSession, columns: List[StructField], location_tb: str):
    return DeltaTable \
        .create(spark) \
        .addColumns(columns) \
        .location(location_tb) \
        .execute()


def execute_upsert(spark: SparkSession, input_df: DataFrame, merge_condition ,location_tb: str):
    deltaTable = DeltaTable.forPath(spark, location_tb)
    deltaTable.alias('tgt') \
        .merge(
            input_df.alias('src'),
            merge_condition
        ) \
        .whenMatchedUpdateAll() \
        .whenNotMatchedInsertAll() \
        .execute()