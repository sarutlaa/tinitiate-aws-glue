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
df1 = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="product").toDF()
df2 = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="product_un_in").toDF()

# Union operation (remove duplicates)
union_df = df1.union(df2)

# Union all operation (include duplicates)
union_all_df = df1.unionAll(df2)  # In newer versions of PySpark, use union() instead

# Intersect operation
intersect_df = df1.intersect(df2)

# Show the resulting DataFrames
union_df.show()
union_all_df.show()
intersect_df.show()
