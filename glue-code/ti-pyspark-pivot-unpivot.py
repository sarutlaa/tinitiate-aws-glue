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
df = spark.read.option("header", "true").csv("s3://ti-p-data/hr-data/employee_dept/")

# Define columns to pivot
months = ['January', 'February', 'March']

# Pivot the data
pivot_df = df.select(
    "employee_id", "employee_name", "department",
    *[col(month + "_salary").alias(month) for month in months]
)

# Show the pivoted DataFrame
pivot_df.show()


# Unpivot the pivoted DataFrame
unpivot_df = pivot_df.selectExpr(
    "employee_id", "employee_name", "department",
    "stack(3, 'January', January, 'February', February, 'March', March) as (month, salary)"
)

# Show the unpivoted DataFrame
unpivot_df.show()
