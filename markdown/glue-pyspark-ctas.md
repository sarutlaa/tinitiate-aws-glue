# Managing Data Transformations and Table Creation with PySpark in AWS Glue

This document demonstrates how to use PySpark within AWS Glue for data transformation and efficient table creation using the CTAS method, focusing on data from the "purchase" table stored in Athena. The script sets up necessary Spark and Glue contexts, performs data transformation, and creates a new table in a specified format and location.

## CTAS (Create Table As Select)
The CTAS command is crucial for creating a new table from selected data in one step, often used to store transformed data efficiently. This method is integral in workflows that require the generation of new, structured tables from existing datasets.

## Prerequisites

Ensure the proper setup of the AWS environment, including S3 buckets and IAM roles. Detailed steps can be found here:

* [Prerequisites](/prerequisites.md)
* Setting up [AWS Glue Crawler](/aws-glue-crawler.md)

##  PySpark Script 
The script can be accessed and reviewed here:
[pyspark-set-operations](../glue-code/ti-pyspark-ctas.py)

## Main Operations

### 1. Initializing Spark and Glue Contexts:
* Purpose: Establishes the necessary Spark and Glue contexts for data manipulation with logging set to INFO to control verbosity.
* Code Example:
  ```ruby
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```
### 2. Data Loading:
* Purpose: Purpose: Loads the "purchase" data from Athena into a DataFrame, applies necessary filters and transformations.
* Code Example:
  ```ruby
  purchase_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
  result_df = purchase_df.select("purchase_tnx_id", "product_supplier_id","purchase_tnxdate","quantity","invoice_price").filter(purchase_df["quantity"] > 100)
  ```
### 3. Creating a New Table Using CTAS:
* Purpose: Utilizes the CTAS command to create a new table from the transformed data, specifying the format (Parquet) and the location (S3).
* Code Example:
  ```ruby
  result_df.createOrReplaceTempView("temp_table")
  spark.sql("CREATE TABLE new_purchase_table USING PARQUET LOCATION 's3://ti-p-etl-glue/glue_logs/' AS SELECT * FROM temp_table")
  ```

### 4. Displaying Results:
* Purpose: Shows the transformed data to verify correctness before and after the table creation.
* Code Example:
  ```ruby
  result_df.show()
  ```

