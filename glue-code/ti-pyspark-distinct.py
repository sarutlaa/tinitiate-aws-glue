# Import necessary libraries for Spark and AWS Glue functionalities
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="purchase").toDF()

# Obtain distinct records from the DataFrame to remove duplicates
# This is particularly useful in scenarios where you need to ensure that each row in your DataFrame is unique
distinct_df = df.distinct()

# Specify the output path for the S3 bucket
output_base_path = "s3://your-bucket-name/your-folder/"

# Save the distinct records to the S3 bucket in your preferred format
# Here we demonstrate saving in CSV, JSON, and Parquet formats
distinct_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
distinct_df.write.mode("overwrite").json(output_base_path + "json/")
distinct_df.write.mode("overwrite").parquet(output_base_path + "parquet/")

# Log information after saving to S3
glueContext.get_logger().info("Distinct records successfully written to S3 in CSV, JSON, and Parquet formats.")
