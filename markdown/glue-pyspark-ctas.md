# Managing Data Transformations and Table Creation with PySpark in AWS Glue

This documentation guides you through the process of using PySpark within AWS Glue to perform a Create Table As Select (CTAS) operation. The workflow focuses on transforming data from the "purchase" table stored in Athena, creating a new table in the AWS Glue Data Catalog, and storing the transformed data directly in Amazon S3 using the CTAS approach.

## Overview of CTAS


## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  
##  PySpark Script - [pyspark-ctas](../glue-code/ti-pyspark-ctas.py)
- Input tables          : purchase
- Output                : New table in csv format stored in S3 bucket.
- Crawlers used         : purchase_crawler


## Main Operations
### 1. Initializing Spark and Glue Contexts:
* Objective: Establishes the necessary Spark and Glue contexts for data manipulation with logging set to INFO to control verbosity.
* Implementation:
  ```python
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```
### 2. Data Loading and Transformation:
* Objective: Load the "purchase" data from Athena, apply transformations, and prepare for storage.
* Implementation:
  ```python
  purchase_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
  result_df = purchase_df.select("purchase_tnx_id", "product_supplier_id", "purchase_tnxdate", "quantity", "invoice_price").filter(purchase_df["quantity"] > 100)

  ```
### 3. Data Transformation:
* Objective: Filtering the 'purchase' table data and chossing the specific columns. 
* Implementation:
  ```python
  # Filter purchases where the quantity is greater than a threshold, e.g., 100
  filtered_df = purchase_df.filter(purchase_df["quantity"] > 100)
  
  # Optionally, further transformations or selections can be applied here
  selected_df = filtered_df.select("purchase_tnx_id", "product_supplier_id", "purchase_tnxdate", "quantity", "invoice_price")
  ```
### 4. Creating the new table:
* Objective: Creating a temporary view ctas_purchase_view in glue datacatalog for storing the CTAS results the query results. 
* Implementation:
  ```python
   # Create or replace a temporary view to use in an SQL query
    selected_df.createOrReplaceTempView("ctas_purchase_view")
    
    # Define an SQL query to manipulate data further if needed
    query_results = spark.sql("""
    SELECT product_supplier_id, SUM(quantity) as total_quantity, AVG(invoice_price) as average_price
    FROM ctas_purchase_view
    GROUP BY product_supplier_id
    ORDER BY total_quantity DESC
  """)
  ```
### 5. Executing CTAS and Displaying the result
* Objective: Executes the CTAS query and displays the result in cloudwatch logs.
* Implementation:
  ```python
  # Execute the CTAS operation
  result_df = spark.sql(ctas_query)
  print("Sample CTAS Table")
  result_df.show()
  ```

### 5. Logging and Verification:
* Objective: Logging and verifying that the operation has been executed as expected and stopping the spark context.
* Implementation:
  ```python
  # Log the completion of the CTAS operation
  glueContext.get_logger().info("CTAS operation completed and new table 'ctas_purchase_table' created in the Glue Data Catalog.")
  
  # Stop the Spark context to free up resources and close the session
sc.stop()
  ```

