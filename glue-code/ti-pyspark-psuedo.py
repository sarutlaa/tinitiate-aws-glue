from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id, row_number
from pyspark.sql.window import Window

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

# Add a monotonically increasing id column
df_with_id = df.withColumn("row_id", monotonically_increasing_id())

# Add a row number column within a window partitioned by some column
window_spec = Window.partitionBy("product_supplier_id").orderBy("quantity")
df_with_row_number = df.withColumn("row_number", row_number().over(window_spec))

# Show the resulting DataFrame with pseudo-columns
df_with_id.show()
df_with_row_number.show()
