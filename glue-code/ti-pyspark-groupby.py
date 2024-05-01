from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

# Initialize Spark context and set the log level to INFO to capture informational messages during execution
sc = SparkContext.getOrCreate()
sc.setLogLevel("INFO")

# Create a GlueContext and retrieve the associated Spark session
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Setup logging
logger = glueContext.get_logger()
logger.info("Using Logger: Starting script execution")

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load data from Athena into a DataFrame using Glue's DynamicFrame
electric_vehicles_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="electric_vehicle_population_data_csv").toDF()

# Group by 'make' and 'model' columns, and count the occurrences
result_df = electric_vehicles_df.groupBy("make", "model").agg(count("*").alias("count"))

# Define the paths to store the output in different formats in S3
s3_bucket_path_csv = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-joins-output/csv/"
s3_bucket_path_json = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-joins-output/json/"
s3_bucket_path_parquet = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-joins-output/parquet/"

# Save the results to S3 in CSV format
result_df.write.csv(s3_bucket_path_csv, mode="overwrite", header=True)
logger.info(f"Results written to CSV at {s3_bucket_path_csv}")

# Save the results to S3 in JSON format
result_df.write.json(s3_bucket_path_json, mode="overwrite")
logger.info(f"Results written to JSON at {s3_bucket_path_json}")

# Save the results to S3 in Parquet format
result_df.write.parquet(s3_bucket_path_parquet, mode="overwrite")
logger.info(f"Results written to Parquet at {s3_bucket_path_parquet}")

# Final log to indicate successful completion of the script
logger.info("Script execution completed successfully.")
