from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize the SparkContext and GlueContext to use AWS Glue features within Spark.
sc = SparkContext.getOrCreate()
sc.setLogLevel("INFO")  # Set log level to INFO to view informational messages during script execution.
spark = SparkSession(sc)  # Create a SparkSession which is required to perform SQL operations and read data.
glueContext = GlueContext(sc)  # Initialize GlueContext which provides additional methods to work with Glue.

# Define the AWS Glue catalog and database where the tables are stored.
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load data from AWS Glue catalog into DynamicFrames and convert them to Spark DataFrames.
product_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="products_csv").toDF()

# Select specific columns from product table and apply aliases
product_selected_df = product_df.select(
    col("productid").alias("Product ID"),
    col("productname").alias("Product Name"),
    col("categoryid").alias("Product Category ID"),
    col("unit_price").alias("Cost Per Unit")
)

# Filter products where unit price is greater than 5
filtered_product_df = product_selected_df.filter(col("Cost Per Unit") > 5)

# Specify the output path for the S3 bucket
output_base_path_csv = "s3://your-bucket-name/your-data-folder/csv/"
output_base_path_json = "s3://your-bucket-name/your-data-folder/json/"
output_base_path_parquet = "s3://your-bucket-name/your-data-folder/parquet/"

# Save the filtered DataFrame to the S3 bucket in CSV format
filtered_product_df.write.mode("overwrite").option("header", "true").csv(output_base_path_csv)

# Save the filtered DataFrame to the S3 bucket in JSON format
filtered_product_df.write.mode("overwrite").json(output_base_path_json)

# Save the filtered DataFrame to the S3 bucket in Parquet format
filtered_product_df.write.mode("overwrite").parquet(output_base_path_parquet)

# Log a completion message to indicate successful writing of data to S3.
glueContext.get_logger().info("Filtered data successfully written to S3 in CSV, JSON, and Parquet formats.")
