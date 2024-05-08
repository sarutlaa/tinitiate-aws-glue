from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize the SparkContext and GlueContext to use AWS Glue features within Spark.
sc = SparkContext.getOrCreate()
sc.setLogLevel("INFO")  # Set log level to INFO to view informational messages during script execution.
spark = SparkSession(sc)  # Create a SparkSession which is required to perform SQL operations and read data.
glueContext = GlueContext(sc)  # Initialize GlueContext which provides additional methods to work with Glue.

# Define the AWS Glue catalog and database where the tables are stored.
catalog = "awsglue_data_catalog"
database = "glue_db"

# Load data from AWS Glue catalog into DynamicFrames and convert them to Spark DataFrames.
product_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="products_csv").toDF()
category_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="categories_csv").toDF()

# Join the products and categories DataFrames on the categoryid
joined_df = product_df.join(category_df, product_df.categoryid == category_df.categoryid, "inner").select(
    col("productid").alias("Product ID"),
    col("productname").alias("Product Name"),
    category_df.categoryname.alias("Category Name"),
    col("unit_price").alias("Unit Price")
)

# Filter the joined DataFrame where the unit price is greater than 5
filtered_df = joined_df.filter(col("Unit Price") > 5)

# Display the final filtered DataFrame in the console
print("Filtered DataFrame:")
filtered_df.show(truncate=False)

# Log a completion message using print instead of using the Glue logger
print("Filtered data displayed in console successfully.")
