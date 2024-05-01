from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

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

# Select specific columns from the loaded tables to avoid duplicate column names and rename for clarity.
product_selected_df = product_df.select("productid", "productname", "categoryid", "unit_price").withColumnRenamed("categoryid", "product_categoryid")
category_selected_df = category_df.select("categoryid", "categoryname")

# Define S3 bucket paths for different file formats to store outputs.
s3_bucket_path_csv = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-joins-output/csv/"
s3_bucket_path_json = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-joins-output/json/"
s3_bucket_path_parquet = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-joins-output/parquet/"

# Define join types and prepare a dictionary to store DataFrames after joins.
join_types = ["inner", "left", "right", "outer"]
joined_dataframes = {}

# Loop through each join type to perform joins and save the results in different formats.
for join_type in join_types:
    # Perform each type of join using a common key between product and category DataFrames.
    joined_df = product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], join_type)
    # Drop redundant column after join to avoid ambiguity in DataFrame schema.
    joined_df = joined_df.drop("product_categoryid")
    
    # Save the joined DataFrame to S3 in CSV, JSON, and Parquet formats.
    joined_df.write.csv(s3_bucket_path_csv + join_type, mode="overwrite", header=True)
    joined_df.write.json(s3_bucket_path_json + join_type, mode="overwrite")
    joined_df.write.parquet(s3_bucket_path_parquet + join_type, mode="overwrite")
    
    # Store the joined DataFrame in a dictionary for possible further use.
    joined_dataframes[join_type] = joined_df

# Log a completion message to indicate successful writing of data to S3.
glueContext.get_logger().info("Data successfully written to S3 in all formats.")
