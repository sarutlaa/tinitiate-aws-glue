# Aggregation and Sorting with PySpark in AWS Glue

 This document outlines the process of using PySpark in AWS Glue to perform aggregation on data sourced from AWS Glue Data Catalog, followed by sorting and saving the results in various formats to Amazon S3.

## Overview of Aggregation

Aggregation in PySpark involves summarizing data from multiple rows into a single result. Typical aggregation functions include count, sum, avg, etc. In this script, we use the count function to determine the number of occurrences of each combination of 'make' and 'model' from a dataset of electric vehicles.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [Crawler Prerequisites](/crawler-prerequisites.md)
* [Crawler Setup Instructions](/set-up-instructions.md)

##  PySpark Script - [pyspark-orderby](../glue-code/ti-pyspark-orderby.py)
- Input tables          : purchase
- Output files          : csv, json and parquet files in S3 buckets.
- Crawlers used         : purchase_crawler

## Main Operations
### 1. Initializing Spark and Glue Contexts:
* Objective: Set up necessary contexts for PySpark and AWS Glue operations, ensuring that informative logging is enabled.
* Implementation :
  ```python
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```
  
### 2. Data Loading:
* Objective: Load data from the AWS Glue Data Catalog into Spark DataFrames, preparing it for subsequent processing.
* Implementation:
  ```python
  grouped_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="electric_vehicle_population_data_csv").toDF()
  ```

### 3. Data Aggregation and Sorting:
* Objective: Group data by 'make' and 'model', count occurrences, and sort the results in both ascending and descending order based on count.
* Implementation:
  ```python
  result_df = grouped_df.groupBy("make", "model").agg(count("*").alias("count"))
  result_df_desc = result_df.orderBy("count", ascending=False)
  result_df_asc = result_df.orderBy("count", ascending=True)
  ```
  
### 4. Output Formatting and Storage:
* Objective: Save the sorted data in CSV, JSON, and Parquet formats to predefined S3 bucket paths for both ascending and descending orders.
* Implementation:
  ```python
  output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-orderby-outputs/"
  result_df_desc.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/desc/")
  result_df_desc.write.mode("overwrite").json(output_base_path + "json/desc/")
  result_df_desc.write.mode("overwrite").parquet(output_base_path + "parquet/desc/")
  result_df_asc.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/asc/")
  result_df_asc.write.mode("overwrite").json(output_base_path + "json/asc/")
  result_df_asc.write.mode("overwrite").parquet(output_base_path + "parquet/asc/")

  ```
  
### 5. Logging and Verification:
* Objective: Log the completion of data writes, confirming successful storage in both orders and formats.
* Implementation:
  ```python
  glueContext.get_logger().info("Data successfully written to S3 in both ascending and descending order in CSV, JSON, and Parquet formats.")
  ```
