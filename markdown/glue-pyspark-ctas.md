# Managing Data Transformations and Table Creation with PySpark in AWS Glue

This documentation guides you through the process of using PySpark within AWS Glue to perform a Create Table As Select (CTAS) operation. The workflow focuses on transforming data from the "purchase" table stored in Athena, creating a new table in the AWS Glue Data Catalog, and storing the transformed data directly in Amazon S3 using the CTAS approach.

## Overview of CTAS
The CTAS command is a powerful SQL operation commonly used in data warehousing. It creates a new table by executing a SELECT query. This operation is particularly useful in data transformation processes where the transformed data needs to be stored persistently for future use. In AWS Glue, utilizing CTAS allows for efficient management and querying of large datasets by leveraging the scalable storage of S3 and the metadata management capabilities of the Glue Data Catalog.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:

* [Prerequisites]((/prerequisites.md)) 
* [Crawler Setup](/aws-glue-crawler.md)

##  PySpark Script - [pyspark-ctas](../glue-code/ti-pyspark-ctas.py)
- Input tables          : purchase
- Output                : New table in the AWS Glue Data Catalog stored in S3.
- Crawlers used         : purchase_crawler


## Main Operations
### 1. Initializing Spark and Glue Contexts:
* Objective: Establishes the necessary Spark and Glue contexts for data manipulation with logging set to INFO to control verbosity.
* Implementation:
  ```ruby
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```
### 2. Data Loading and Transformation:
* Objective: Load the "purchase" data from Athena, apply transformations, and prepare for storage.
* Implementation:
  ```ruby
  purchase_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
  result_df = purchase_df.select("purchase_tnx_id", "product_supplier_id", "purchase_tnxdate", "quantity", "invoice_price").filter(purchase_df["quantity"] > 100)

  ```
### 3. Executing the CTAS Operation:
* Objective: Use the CTAS command to create a new table from the transformed data, specifying Parquet as the storage format and S3 as the location
* Implementation:
  ```ruby
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
  ```ruby
  glueContext.get_logger().info("CTAS operation completed and new table created in S3.")
  ```

