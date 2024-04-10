# Import the necessary libraries for Spark and AWS Glue functionality
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

# Initialize Spark context with a specific log level to manage log output
sc = SparkContext()
sc.setLogLevel("INFO")  # Configure logging level to "INFO" for relevant log details

# Create an AWS Glue context from the Spark context for Glue-specific operations
glueContext = GlueContext(sc)

# Access the Spark session from the AWS Glue context for SQL and DataFrame operations
spark = glueContext.spark_session

# (These variables are defined but not used in this script) ----- Check this Sravya!!!
# Define identifiers for the Athena catalog and database to potentially access Athena tables
catalog = "awsglue_data_catalog"
database = "glue_db"

# Define sample employee data with columns for employee ID, role, and manager ID
data = [
    (1, "Manager", None),  # Top-level manager (no manager above)
    (2, "Supervisor", 1),  # Supervisor reports to the manager
    (3, "Employee", 2),    # Employee reports to the supervisor
    (4, "Employee", 2)     # Another employee reporting to the same supervisor
]
columns = ["emp_id", "emp_role", "manager_id"]

# Create a DataFrame from the sample data
df = spark.createDataFrame(data, columns)

# Create or replace a temporary view called 'employees' for SQL operations
df.createOrReplaceTempView("employees")

# Define a hierarchical SQL query to analyze the organizational structure
# This query uses a recursive common table expression (CTE) to build a hierarchy
hierarchical_query = """
WITH RECURSIVE hierarchy AS (
  SELECT emp_id, emp_role, manager_id, 1 as level
  FROM employees
  WHERE manager_id IS NULL  -- Start with the top-level manager (no manager)

  UNION ALL

  -- Recursively join to identify subordinates and calculate their level in the hierarchy
  SELECT e.emp_id, e.emp_role, e.manager_id, h.level + 1
  FROM employees e
  JOIN hierarchy h ON e.manager_id = h.emp_id
)
SELECT * FROM hierarchy
"""

# Execute the hierarchical query and store the results in a DataFrame
result_df = spark.sql(hierarchical_query)

# Display the hierarchical structure of the organization from the query result
result_df.show()
