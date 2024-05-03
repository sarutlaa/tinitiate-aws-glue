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

# Apply filter similar to HAVING clause
result_df_filtered = result_df.filter(result_df["count"] > 1000)

# Specify the output path for the S3 bucket
output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-having-outputs/"

# Save the filtered DataFrame to S3 bucket in CSV format
result_df_filtered.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")

# Save the filtered DataFrame to S3 bucket in JSON format
result_df_filtered.write.mode("overwrite").json(output_base_path + "json/")

# Save the filtered DataFrame to S3 bucket in Parquet format
result_df_filtered.write.mode("overwrite").parquet(output_base_path + "parquet/")

# Log information after saving to S3
glueContext.get_logger().info("Data successfully written to S3 in CSV, JSON, and Parquet formats.")
