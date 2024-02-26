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

# Load the table "electric_vehicles" from the Glue Data Catalog into a DataFrame
df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="electric_vechiles").toDF()

# Define the partitioning columns
partition_columns = ["model year", "make"]

# Write the DataFrame partitioned by the specified columns
df.write.partitionBy(*partition_columns).format("parquet").mode("overwrite").save("s3://ti-p-etl-glue/glue_logs/")

# Optionally, you can also use other file formats like "orc", "json", etc.

# Show the DataFrame partitions
df.printSchema()
