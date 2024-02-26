from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
import logging

# Initialize Spark context with log level
sc = SparkContext()
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Set up logging - check if this returns a valid logger
logger = glueContext.get_logger()
# Optional: Inspect the logger object
print("Logger: ", logger)
logger.info("IM Using Logger")
# Define Athena catalog and database
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames
product_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="product").toDF()
category_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="category").toDF()



# Join the tables on categoryid column
inner_df = product_df.join(category_df, product_df["categoryid"] == category_df["categoryid"], "inner")

# Log the count of rows in the joined DataFrame
logger.info("Number of rows in the joined DataFrame: {}".format(inner_df.count()))

# Left Join the tables on categoryid column
left_df = product_df.join(category_df, product_df["categoryid"] == category_df["categoryid"], "left")
 

# right Join the tables on categoryid column
right_df = product_df.join(category_df, product_df["categoryid"] == category_df["categoryid"], "right")
 
# full Join the tables on categoryid column
full_df = product_df.join(category_df, product_df["categoryid"] == category_df["categoryid"], "full_outer")
 
print("full_df: ", logger)
# Show the resulting DataFrame
full_df.show(n=full_df.count())

print("right_df: ", logger)
# Show the resulting DataFrame
right_df.show()

print("left_df: ", logger)
# Show the resulting DataFrame
left_df.show()

print("inner_df: ", logger)
# Display the joined data frame
inner_df.show()

 
 
