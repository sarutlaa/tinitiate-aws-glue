# SQL-like Filtering with PySpark in AWS Glue
This document provides an overview of using PySpark within AWS Glue to apply SQL-like filtering conditions, specifically on a "purchase" dataset stored in Athena. The script initializes the necessary Spark and Glue contexts, loads data, and applies various conditions such as IN, NOT IN, Greater Than, Less Than, and Not Equal To to filter the data accordingly.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [Crawler Prerequisites](/crawler-prerequisites.md)
* [Crawler Setup Instructions](/set-up-instructions.md)
  
##  PySpark Script - [pyspark-filtering](../glue-code/ti-pyspark-condition.py)
- Input tables          : purchase
- Output files          : csv, json and parquet files in S3 buckets.
- Crawlers used         : purchase_crawler

## Main Operations

### 1. Initializing Spark and Glue Contexts:
* Objective: Establish the foundational Spark and Glue contexts necessary for data manipulation, with logging configured to INFO level to manage verbosity.
* Implementation:
  ```python
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```

### 2. Data Loading:
* Objective: Loads the "purchase" table from the Athena database into a DataFrame for subsequent filtering operations.
* Implementation:
  ```python
  df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
  ```
### 3. Applying Filters:
* Objective: Apply various SQL-like filters to demonstrate data segmentation based on specified criteria.
* Filters Applied:
  -  IN Condition: Filters rows where product_supplier_id matches any of the specified values.
    ```python
    df_in = df.filter(df["product_supplier_id"].isin([150, 259, 21]))
    ```
  - NOT IN Condition: Excludes rows where quantity matches any of the specified values.
    ```python
    df_not_in = df.filter(~df["quantity"].isin([295, 743, 67]))
    ```
  - Greater Than Condition: Selects rows where quantity is greater than 200.
    ```python
    df_gt = df.filter(df["quantity"] > 200)
    ```
  - Less Than Condition: Selects rows where quantity is less than 200.
    ```python
    df_lt = df.filter(df["quantity"] < 200)
    ```
  - Not Equal To Condition: Filters out rows where quantity is not equal to 743.
    ```python
    df_ne = df.filter(df["quantity"] != 743)
    ```    
    
### 4. Output Formatting and Storage:
* Objective: Format and save the filtered results in CSV, JSON, and Parquet formats to designated S3 paths for both ascending and descending orders.
* Implementation:
  ```python
  output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-filtering-outputs/"
  df_in.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/in_condition/")
  df_in.write.mode("overwrite").json(output_base_path + "json/in_condition/")
  df_in.write.mode("overwrite").parquet(output_base_path + "parquet/in_condition/")
  ```

### 5. Logging and Verification:
* Objective: Confirm the successful execution and storage of filtered data in all specified formats and conditions.
* Implementation:
  ```ruby
    glueContext.get_logger().info("Data successfully written to S3 in all specified filters and formats.")
  ```  
