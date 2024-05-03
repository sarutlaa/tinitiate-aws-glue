from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Set log level to INFO to control the verbosity of log output

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="purchase").toDF()

# Define output base path for S3 bucket
output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-condition-outputs/"

# IN condition
df_in = df.filter(df["product_supplier_id"].isin([150,259,21])) 
df_in.write.mode("overwrite").option("header", "true").csv(output_base_path + "in_condition/csv/")
df_in.write.mode("overwrite").json(output_base_path + "in_condition/json/")
df_in.write.mode("overwrite").parquet(output_base_path + "in_condition/parquet/")

# NOT IN condition
df_not_in = df.filter(~df["quantity"].isin([295,743,67]))
df_not_in.write.mode("overwrite").option("header", "true").csv(output_base_path + "not_in_condition/csv/")
df_not_in.write.mode("overwrite").json(output_base_path + "not_in_condition/json/")
df_not_in.write.mode("overwrite").parquet(output_base_path + "not_in_condition/parquet/")

# Greater than condition
df_gt = df.filter(df["quantity"] > 200)
df_gt.write.mode("overwrite").option("header", "true").csv(output_base_path + "greater_than_condition/csv/")
df_gt.write.mode("overwrite").json(output_base_path + "greater_than_condition/json/")
df_gt.write.mode("overwrite").parquet(output_base_path + "greater_than_condition/parquet/")

# Less than condition
df_lt = df.filter(df["quantity"] < 200)
df_lt.write.mode("overwrite").option("header", "true").csv(output_base_path + "less_than_condition/csv/")
df_lt.write.mode("overwrite").json(output_base_path + "less_than_condition/json/")
df_lt.write.mode("overwrite").parquet(output_base_path + "less_than_condition/parquet/")

# Not equal to condition
df_ne = df.filter(df["quantity"] != 743)
df_ne.write.mode("overwrite").option("header", "true").csv(output_base_path + "not_equal_condition/csv/")
df_ne.write.mode("overwrite").json(output_base_path + "not_equal_condition/json/")
df_ne.write.mode("overwrite").parquet(output_base_path + "not_equal_condition/parquet/")

# Logging information after saving to S3
glueContext.get_logger().info("Data successfully written to S3 in all conditions and formats.")
