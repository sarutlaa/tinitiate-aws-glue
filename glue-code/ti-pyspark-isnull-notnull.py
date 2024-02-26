from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="category").toDF()

# Filter for null values in a specific column
df_null = df.filter(col("categoryname").isNull())

# Filter for not null values in a specific column
df_not_null = df.filter(col("categoryname").isNotNull())

# Show the resulting DataFrames
df_null.show()
df_not_null.show()
