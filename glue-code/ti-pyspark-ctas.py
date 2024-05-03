from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

sc = SparkContext()
sc.setLogLevel("INFO")
glueContext = GlueContext(sc)
spark = glueContext.spark_session

purchase_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
result_df = purchase_df.select(
    "purchase_tnx_id", "product_supplier_id", "purchase_tnxdate", "quantity", "invoice_price"
).filter(purchase_df["quantity"] > 100)

# Create or replace temporary view
result_df.createOrReplaceTempView("temp_table")

# Instead of showing the DataFrame, use Spark SQL to create a new table in the Glue catalog that stores data in S3
spark.sql(f"""
    CREATE TABLE glue_db.new_purchase_table
    USING PARQUET
    LOCATION 's3://your-bucket-name/your-folder/new_purchase_table/'
    AS SELECT * FROM temp_table
""")

glueContext.get_logger().info("CTAS operation completed and new table created in S3.")
