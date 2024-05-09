# Managing Data Transformations and Table Creation with PySpark in AWS Glue

This documentation guides you through the process of using PySpark within AWS Glue to perform a Create Table As Select (CTAS) operation. The workflow focuses on transforming data from the "purchase" table stored in Athena, creating a new table in the AWS Glue Data Catalog, and storing the transformed data directly in Amazon S3 using the CTAS approach.

## Overview of CTAS
Temporary Views in PySpark:
- Scope: Temporary views are limited to the Spark session they are created in and disappear once the session ends.
- Purpose: They allow SQL queries on DataFrame data without saving it in a database, enabling more complex SQL operations.
- Usage: Once a temporary view is created, you can run SQL queries on it as though it's a table in a database, until the Spark session ends.
- Creation: Temporary views are created with the createOrReplaceTempView method on a DataFrame, registering it as a view in Spark’s SQL catalog.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  
##  PySpark Script - [pyspark-ctas](../glue-code/ti-pyspark-ctas.py)
- Input tables          : purchase
- Output                : Glue data catalog, new_purchase_table
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
### 3. Executing the CTAS Operation:
* Objective: Use the CTAS command to create a new table from the transformed data, specifying Parquet as the storage format and S3 as the location
* Implementation:
  ```python
  result_df.createOrReplaceTempView("temp_table")
  spark.sql("""
    CREATE TABLE glue_db.new_purchase_table
    USING PARQUET
    LOCATION 's3://your-bucket-name/your-folder/new_purchase_table/'
    AS SELECT * FROM temp_table
  """)

  ```

### 4. Verification and Logging:
* Objective: Log the successful creation of the table and verify that the operation has been executed as expected.
* Implementation:
  ```python
  glueContext.get_logger().info("CTAS operation completed and new table created in S3.")
  ```

