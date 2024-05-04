from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark and Glue contexts
sc = SparkContext()
sc.setLogLevel("INFO")
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Load data from the AWS Glue catalog
products_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="products_csv").toDF()
categories_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="categories_csv").toDF()
dispatch_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="dispatch").toDF()

# Perform joins
# Join products with categories
product_category_df = products_df.join(categories_df, products_df.categoryid == categories_df.categoryid, "inner")

# Join the result with dispatch
final_df = product_category_df.join(dispatch_df, product_category_df.productid == dispatch_df.product_id, "inner")\
    .select(
        dispatch_df.dispatch_tnx_id,
        product_category_df.productname,
        categories_df.categoryname,
        dispatch_df.dispatch_date,
        dispatch_df.quantity,
        product_category_df.unit_price
    )

# Specify the output path for the S3 bucket
output_base_path = "s3://your-bucket-name/your-folder/"

# Save the resulting DataFrame to the S3 bucket in different formats
final_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
final_df.write.mode("overwrite").json(output_base_path + "json/")
final_df.write.mode("overwrite").parquet(output_base_path + "parquet/")

# Log the completion of data write operation
glueContext.get_logger().info("Data successfully written to S3 in CSV, JSON, and Parquet formats.")

