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

# Load the source table "purchase" from Athena into a DataFrame
purchase_df = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="purchase").toDF()

# Perform any required transformations and filtering
result_df = purchase_df.select("purchase_tnx_id", "product_supplier_id","purchase_tnxdate","quantity","invoice_price").filter(purchase_df["quantity"] > 100)

# Create a new table using CTAS
result_df.createOrReplaceTempView("temp_table")
# spark.sql("CREATE TABLE new_purchase_table AS SELECT * FROM temp_table")

# Optionally, you can also specify the table location and format
spark.sql("CREATE TABLE new_purchase_table USING PARQUET LOCATION 's3://ti-p-etl-glue/glue_logs/' AS SELECT * FROM temp_table")

# Show the resulting DataFrame
result_df.show()
