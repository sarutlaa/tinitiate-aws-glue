# Import necessary libraries for Spark and AWS Glue functionalities
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_utc_timestamp

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="dispatch").toDF()

# Convert string column to DateTime type and then to UTC timezone
df_utc = df.withColumn("datetime_utc_column", from_utc_timestamp(df["dispatch_date"], "UTC"))

# Convert UTC datetime to desired timezone
# Note: Replace 'desired_timezone' with the desired timezone string, such as 'America/New_York'
df_with_timezone = df_utc.withColumn("datetime_with_timezone_column", from_utc_timestamp(df_utc["datetime_utc_column"], "desired_timezone"))

# Show the resulting DataFrame with DateTime with TimeZone type column
df_with_timezone.show()
