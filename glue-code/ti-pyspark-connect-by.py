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

# Sample data
data = [(1, "Manager", None),
        (2, "Supervisor", 1),
        (3, "Employee", 2),
        (4, "Employee", 2)]

columns = ["emp_id", "emp_role", "manager_id"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Create a temporary view
df.createOrReplaceTempView("employees")

# Execute hierarchical query using SQL
hierarchical_query = """
WITH RECURSIVE hierarchy AS (
  SELECT emp_id, emp_role, manager_id, 1 as level
  FROM employees
  WHERE manager_id IS NULL

  UNION ALL

  SELECT e.emp_id, e.emp_role, e.manager_id, h.level + 1
  FROM employees e
  JOIN hierarchy h ON e.manager_id = h.emp_id
)
SELECT * FROM hierarchy
"""
result_df = spark.sql(hierarchical_query)

# Show the resulting DataFrame
result_df.show()
