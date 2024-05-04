# Aggregation and Sorting with PySpark in AWS Glue

This document outlines the process of using PySpark in AWS Glue to perform data selection and aliasing operations on data 
sourced from the AWS Glue Data Catalog, followed by filtering based on specific criteria and saving the results in various formats to Amazon S3.

## Overview of Selecting and Aliasing

Selecting and aliasing in PySpark involves choosing specific columns from a dataset and potentially renaming them to enhance readability and manageability.
This is particularly useful in data transformation processes where clarity and precision in data representation are crucial.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:

* [Prerequisites]((/prerequisites.md)) 
* [Crawler Setup](/aws-glue-crawler.md)

##  PySpark Script - [pyspark-select-alias](../glue-code/ti-pyspark-select.py)
- Input tables          : products_csv
- Output files          : csv, json and parquet files in S3 buckets.
- Crawlers used         : product_crawler

## Main Operations
### 1. Initializing Spark and Glue Contexts:
* Objective: Set up necessary contexts for PySpark and AWS Glue operations, ensuring that informative logging is enabled.
* Implementation :
  ```ruby
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```
  
### 2. Data Loading:
* Objective: Load data from the AWS Glue Data Catalog into Spark DataFrames, preparing it for subsequent processing.
* Implementation:
  ```ruby
  product_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="products_csv").toDF()
  ```

### 3. Data Selection and Aliasing:
* Objective: Group data by 'make' and 'model', count occurrences, and sort the results in both ascending and descending order based on count.
* Implementation:
  ```ruby
  product_selected_df = product_df.select(
    col("productid").alias("Product ID"),
    col("productname").alias("Product Name"),
    col("categoryid").alias("Product Category ID"),
    col("unit_price").alias("Cost Per Unit")
  )

  ```
  
### 4. Filtering and Output Formatting:
* Objective: Save the sorted data in CSV, JSON, and Parquet formats to predefined S3 bucket paths for both ascending and descending orders.
* Implementation:
  ```ruby
  filtered_product_df = product_selected_df.filter(col("Cost Per Unit") > 5)
  output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-aliasing-outputs/"
  filtered_product_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
  filtered_product_df.write.mode("overwrite").json(output_base_path + "json/")
  filtered_product_df.write.mode("overwrite").parquet(output_base_path + "parquet/")
  ```
  
### 5. Logging and Verification:
* Objective: Log the completion of data writes, confirming successful storage in both orders and formats.
* Implementation:
  ```ruby
  glueContext.get_logger().info("Filtered data successfully written to S3 in CSV, JSON, and Parquet formats.")
  ```
