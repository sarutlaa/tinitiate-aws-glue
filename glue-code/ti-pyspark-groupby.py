from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

import logging

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Set up logging - check if this returns a valid logger
logger = glueContext.get_logger()
# Optional: Inspect the logger object
print("Logger: ", logger)
logger.info("IM Using Logger")
# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames

grouped_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="electric_vechiles").toDF()

# Group by electric vehicle column and count the occurrences
#grouped_df = df.groupBy("electric_vehicle_column").count()
result_df = grouped_df.groupBy("make","model").agg(count("*").alias("count"))

print("grouped_df: ", logger)
# Show the resulting DataFrame
result_df .show(n=result_df.count())

 

