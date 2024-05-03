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
df1 = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="products_csv").toDF()
df2 = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="product_un_in").toDF()

# Union operation (remove duplicates)
union_df = df1.union(df2).distinct()

# Union all operation (include duplicates)
union_all_df = df1.union(df2)  # In newer versions of PySpark, use union() instead

# Intersect operation
intersect_df = df1.intersect(df2)

# Specify the output path for the S3 bucket
output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-set-operations-outputs/"

# Save the resulting DataFrames to S3 bucket in different formats
# Save Union DataFrame
union_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "union/csv/")
union_df.write.mode("overwrite").json(output_base_path + "union/json/")
union_df.write.mode("overwrite").parquet(output_base_path + "union/parquet/")

# Save Union All DataFrame
union_all_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "union_all/csv/")
union_all_df.write.mode("overwrite").json(output_base_path + "union_all/json/")
union_all_df.write.mode("overwrite").parquet(output_base_path + "union_all/parquet/")

# Save Intersect DataFrame
intersect_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "intersect/csv/")
intersect_df.write.mode("overwrite").json(output_base_path + "intersect/json/")
intersect_df.write.mode("overwrite").parquet(output_base_path + "intersect/parquet/")

# Log information after saving to S3
glueContext.get_logger().info("Data successfully written to S3 in CSV, JSON, and Parquet formats for union, union all, and intersect operations.")
