from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="categories_csv").toDF()

# Filter for null values in a specific column
df_null = df.filter(col("categoryname").isNull())

# Filter for not null values in a specific column
df_not_null = df.filter(col("categoryname").isNotNull())

# Specify the output path for the S3 bucket
output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-null-checks-outputs/"

# Save the resulting DataFrame with null values to the S3 bucket in different formats
df_null.write.mode("overwrite").option("header", "true").csv(output_base_path + "null/csv/")
df_null.write.mode("overwrite").json(output_base_path + "null/json/")
df_null.write.mode("overwrite").parquet(output_base_path + "null/parquet/")

# Save the resulting DataFrame with not null values to the S3 bucket in different formats
df_not_null.write.mode("overwrite").option("header", "true").csv(output_base_path + "not_null/csv/")
df_not_null.write.mode("overwrite").json(output_base_path + "not_null/json/")
df_not_null.write.mode("overwrite").parquet(output_base_path + "not_null/parquet/")

# Log information after saving to S3
glueContext.get_logger().info("Data with null and not null values successfully written to S3 in CSV, JSON, and Parquet formats.")
