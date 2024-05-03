# Analytical Processing with PySpark in AWS Glue

This document explains how to use PySpark in AWS Glue for conducting advanced analytical queries using window functions. The script sets up the required Spark and Glue contexts, applies window functions to compute various statistics, and saves the results in different formats to S3. 

## Overview of Window Functions
Window functions in PySpark allow for advanced data analysis and manipulation within a defined "window" of data. These functions enable calculations across a range of data rows that are related to the current row, providing powerful tools for aggregation and comparison without collapsing rows, unlike group-by functions which aggregate data to a single row. Commonly used window functions include lag, lead, rank, and row_number, each of which serves a specific purpose in data analysis:

- *LAG*: Retrieves a value from a previous row in the window, often used to compare current values with those of previous entries.
- *LEAD*: Retrieves a value from a subsequent row in the window, useful for comparing current values to future values.
- *RANK*: Assigns a rank to each row within a partition of a result set, with ties receiving the same rank.
- *ROW_NUMBER*: Assigns a unique sequential integer to rows within a partition of a result set, starting at 1 for the first row in each partition.

Below is a breakdown of the script's components and operations:

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:

* [Prerequisites]((/prerequisites.md)) 
* [Crawler Setup](/aws-glue-crawler.md)

##  PySpark Script - [pyspark-analytical-functions](../glue-code/ti-pyspark-analytical.py)
- Input tables          : purchase
- Output files          : csv, json and parquet files in S3 buckets.
- Crawlers used         : purchase_crawler

## Main Operations

### 1. Initializing Spark and Glue Contexts:
* What It Does: Configures the Spark and Glue contexts necessary for data operations, with logging set to provide informative messages.
* Implementation:
  ```ruby
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```

### 2. Data Loading and Preparation:
* Objective: Load data from Athena into Spark DataFrames and prepare them for analytical processing.
* Implementation:
  ```ruby
  analyzed_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
  ```


### 3. Applying Window Functions:
* Objective: Execute window functions to compute prior and next invoice prices, rank and dense rank by invoice price, and save the results to specified S3 buckets in 3 different formats.
* Implementation:
  ```ruby
  analyzed_df = analyzed_df.withColumn("previous_invoice_price", lag("invoice_price").over(Window.partitionBy("product_supplier_id").orderBy("purchase_tnxdate")))
  analyzed_df = analyzed_df.withColumn("next_invoice_price", lead("invoice_price").over(Window.partitionBy("product_supplier_id").orderBy("purchase_tnxdate")))
  analyzed_df = analyzed_df.withColumn("invoice_price_rank", rank().over(Window.partitionBy("product_supplier_id").orderBy(col("invoice_price").desc())))
  analyzed_df = analyzed_df.withColumn("invoice_price_dense_rank", dense_rank().over(Window.partitionBy("product_supplier_id").orderBy(col("invoice_price").desc())))
  ```

### 4. Output Formatting and Storage:
* Objective: Format the DataFrame with specific column names and save in CSV, JSON, and Parquet formats to an S3 bucket.
* Implementation:
  ```ruby
  column_names = ["purchase_tnx_id", "product_supplier_id", "purchase_tnxdate", "quantity", "invoice_price", "previous_invoice_price", "next_invoice_price", "invoice_price_rank", "invoice_price_dense_rank"]
  analyzed_df = analyzed_df.toDF(*column_names)
  output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/glue-pyspark-analytical-outputs/"
  analyzed_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
  analyzed_df.write.mode("overwrite").json(output_base_path + "json/")
  analyzed_df.write.mode("overwrite").parquet(output_base_path + "parquet/")
  ```

### 5. Logging and Verification:
* Objective: Log operational details and confirm the success of data writes.
* Implementation:
  ```ruby
  logger.info("DataFrame saved in CSV, JSON, and Parquet formats to S3 successfully, including dense rank.")
  ```
