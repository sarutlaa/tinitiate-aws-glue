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
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="purchase").toDF()

# IN condition
df_in = df.filter(df["product_supplier_id"].isin([150,259,21])) 

# NOT IN condition
df_not_in = df.filter(~df["quantity"].isin([295,743,67]))

# Greater than condition
df_gt = df.filter(df["quantity"] > 200)

# Less than condition
df_lt = df.filter(df["quantity"] < 200)

# Not equal to condition
df_ne = df.filter(df["quantity"] != 743)

# Show the resulting DataFrames
df_in.show()
df_not_in.show()
df_gt.show()
df_lt.show()
df_ne.show()
