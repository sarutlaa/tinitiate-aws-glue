from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id, row_number
from pyspark.sql.window import Window

# Initialize Spark context with log level
sc = SparkContext.getOrCreate()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = SparkSession.builder.appName("Data Processing with Pseudo Columns").getOrCreate()

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="purchase").toDF()

# Add a monotonically increasing id column
df_with_id = df.withColumn("row_id", monotonically_increasing_id())

# Define a window specification and add a row number column
window_spec = Window.partitionBy("product_supplier_id").orderBy("quantity")
df_with_row_number = df.withColumn("row_number", row_number().over(window_spec))

# Specify the output path for the S3 bucket
output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-psuedo-columns-outputs/"

# Save the DataFrame with row_id to the S3 bucket in CSV, JSON, and Parquet formats
df_with_id.write.mode("overwrite").option("header", "true").csv(output_base_path + "with_id/csv/")
df_with_id.write.mode("overwrite").json(output_base_path + "with_id/json/")
df_with_id.write.mode("overwrite").parquet(output_base_path + "with_id/parquet/")

# Save the DataFrame with row_number to the S3 bucket in CSV, JSON, and Parquet formats
df_with_row_number.write.mode("overwrite").option("header", "true").csv(output_base_path + "with_row_number/csv/")
df_with_row_number.write.mode("overwrite").json(output_base_path + "with_row_number/json/")
df_with_row_number.write.mode("overwrite").parquet(output_base_path + "with_row_number/parquet/")

# Log a completion message to indicate successful writing of data to S3
glueContext.get_logger().info("Data with pseudo columns successfully written to S3 in CSV, JSON, and Parquet formats.")
