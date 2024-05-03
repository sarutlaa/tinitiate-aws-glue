from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_utc_timestamp, current_timestamp, date_format, unix_timestamp, expr

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="dispatch").toDF()

# Convert string column to DateTime type and then to UTC timezone
df_utc = df.withColumn("datetime_utc_column", from_utc_timestamp(df["dispatch_date"], "UTC"))

# Convert UTC datetime to desired timezone
# Note: Replace 'desired_timezone' with the desired timezone string, such as 'America/New_York'
df_with_timezone = df_utc.withColumn("datetime_with_timezone_column", from_utc_timestamp(df_utc["datetime_utc_column"], "America/New_York"))

# Additional DateTime operations
# 1. Formatting DateTime
df_formatted = df_with_timezone.withColumn("formatted_date", date_format("datetime_with_timezone_column", "yyyy-MM-dd HH:mm:ss"))

# 2. Time Difference in seconds between current time and dispatch time
df_time_diff = df_formatted.withColumn("time_difference_seconds", unix_timestamp(current_timestamp()) - unix_timestamp("datetime_with_timezone_column"))

# Specify the output path for the S3 bucket
output_base_path = "s3://your-bucket-name/your-folder/"

# Save the resulting DataFrame to the S3 bucket in CSV format
df_time_diff.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")

# Save the resulting DataFrame to the S3 bucket in JSON format
df_time_diff.write.mode("overwrite").json(output_base_path + "json/")

# Save the resulting DataFrame to the S3 bucket in Parquet format
df_time_diff.write.mode("overwrite").parquet(output_base_path + "parquet/")

# Log information after saving to S3
glueContext.get_logger().info("Data successfully written to S3 in CSV, JSON, and Parquet formats.")
