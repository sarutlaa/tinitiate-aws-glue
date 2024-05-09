# Import necessary libraries for Spark and AWS Glue functionalities
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

# Create a temporary view of the DataFrame
df.createOrReplaceTempView("temp_table")

# Use the temporary view in a SQL query
result_df = spark.sql("SELECT * FROM temp_table")

# Display the resulting DataFrame
print("Query Result:")
result_df.show(truncate=False)

# Log information after displaying the results
glueContext.get_logger().info("Data successfully displayed in the console.")
