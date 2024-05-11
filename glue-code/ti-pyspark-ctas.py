from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

# Initialize Spark and Glue contexts
sc = SparkContext()
sc.setLogLevel("INFO")
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Load the 'purchase' table from the AWS Glue Data Catalog
purchase_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()

# Assuming 'purchase' table has columns: purchase_tnx_id, product_supplier_id, purchase_tnxdate, quantity, invoice_price
# Filter purchases where the quantity is greater than a threshold, e.g., 100
filtered_df = purchase_df.filter(purchase_df["quantity"] > 100)

# Optionally, further transformations or selections can be applied here
selected_df = filtered_df.select("purchase_tnx_id", "product_supplier_id", "purchase_tnxdate", "quantity", "invoice_price")

# Create or replace a temporary view to use in an SQL query
selected_df.createOrReplaceTempView("ctas_purchase_view")

# Define an SQL query to manipulate data further if needed
query_results = spark.sql("""
SELECT product_supplier_id, SUM(quantity) as total_quantity, AVG(invoice_price) as average_price
FROM ctas_purchase_view
GROUP BY product_supplier_id
ORDER BY total_quantity DESC
""")

# Display the SQL query results
print("SQL Query Results:")
query_results.show(truncate=False)

# Log the completion of data processing
glueContext.get_logger().info("Displayed SQL query results successfully in the console.")

# Stop the Spark context to free up resources and close the session
sc.stop()
