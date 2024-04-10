# Importing necessary libraries from PySpark and AWS Glue
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lag, lead, rank
from pyspark.sql.window import Window


import logging

# Initialize Spark context with log level
sc = SparkContext()

# Setting log level to INFO to see informative messages during execution
sc.setLogLevel("INFO")    

# Initialize Glue context and Spark session for AWS Glue operations
glueContext = GlueContext(sc) # Creating a Glue context based on the Spark context
spark = glueContext.spark_session # Getting the Spark session from the Glue context

# Set up logging - check if this returns a valid logger.
logger = glueContext.get_logger()

# Optional: Inspect the logger object.
print("Logger: ", logger)
logger.info("IM Using Logger")

# Define Athena catalog and database.
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load tables from Athena into data frames.
analyzed_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="purchase").toDF()

'''Apply analytical functions on the sales data using window functions'''

# Calculate the previous invoice price for each product supplier - using 'LAG()' Function.
analyzed_df = analyzed_df.withColumn("previous_invoice_price", lag("invoice_price").over(Window.partitionBy("product_supplier_id").orderBy("purchase_tnxdate")))

# Calculate the next invoice price for each product supplier - using 'LEAD()' Function.
analyzed_df = analyzed_df.withColumn("next_invoice_price", lead("invoice_price").over(Window.partitionBy("product_supplier_id").orderBy("purchase_tnxdate")))

# Calculate the next invoice price for each product supplier - using 'RANK()' Function in descending order.
analyzed_df = analyzed_df.withColumn("invoice_price_rank", rank().over(Window.partitionBy("product_supplier_id").orderBy(col("invoice_price").desc())))


# Define the column names for the DataFrame
column_names = ["purchase_tnx_id", "product_supplier_id", "purchase_tnxdate", "quantity","invoice_price","previous_invoice_price","next_invoice_price","invoice_price_rank"] 

# Rename DataFrame columns names for the DataFrame
analyzed_df = analyzed_df.toDF(*column_names)

# Show the resulting DataFrame
analyzed_df.show()

 

