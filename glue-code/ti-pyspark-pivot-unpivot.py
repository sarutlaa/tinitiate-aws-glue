from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, array, col

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load CSV data into a DataFrame
df = spark.read.option("header", "true").csv("s3://ti-author-data/hr-data/employee_dept/emp_dept.csv")

# Define columns to pivot
months = ['January', 'February', 'March']

# Pivot the data
pivot_df = df.select(
    "employee_id", "employee_name", "department",
    *[col(month + "_salary").alias(month) for month in months]
)

# Specify the output path for the S3 bucket
output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-pivot-unpivot-outputs/"

# Save the pivoted DataFrame to S3 bucket in different formats
pivot_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "pivot/csv/")
pivot_df.write.mode("overwrite").json(output_base_path + "pivot/json/")
pivot_df.write.mode("overwrite").parquet(output_base_path + "pivot/parquet/")

# Unpivot the pivoted DataFrame
unpivot_df = pivot_df.selectExpr(
    "employee_id", "employee_name", "department",
    "stack(3, 'January', January, 'February', February, 'March', March) as (month, salary)"
)

# Save the unpivoted DataFrame to S3 bucket in different formats
unpivot_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "unpivot/csv/")
unpivot_df.write.mode("overwrite").json(output_base_path + "unpivot/json/")
unpivot_df.write.mode("overwrite").parquet(output_base_path + "unpivot/parquet/")

# Log information after saving to S3
glueContext.get_logger().info("Pivoted and unpivoted DataFrames successfully written to S3 in CSV, JSON, and Parquet formats.")
