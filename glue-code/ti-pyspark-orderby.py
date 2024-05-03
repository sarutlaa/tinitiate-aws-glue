from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
grouped_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="electric_vehicle_population_data_csv").toDF()

# Group by electric vehicle column and count the occurrences
result_df = grouped_df.groupBy("make", "model").agg(count("*").alias("count"))

# Specify the output path for the S3 bucket
output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-orderby-outputs/"

# Order by 'count' descending and save the results
result_df_desc = result_df.orderBy("count", ascending=False)
result_df_desc.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/desc/")
result_df_desc.write.mode("overwrite").json(output_base_path + "json/desc/")
result_df_desc.write.mode("overwrite").parquet(output_base_path + "parquet/desc/")

# Order by 'count' ascending and save the results
result_df_asc = result_df.orderBy("count", ascending=True)
result_df_asc.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/asc/")
result_df_asc.write.mode("overwrite").json(output_base_path + "json/asc/")
result_df_asc.write.mode("overwrite").parquet(output_base_path + "parquet/asc/")

# Log information after saving to S3
glueContext.get_logger().info("Data successfully written to S3 in both ascending and descending order in CSV, JSON, and Parquet formats.")
