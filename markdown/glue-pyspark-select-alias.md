# Selecting and Aggregation with PySpark in AWS Glue

This document outlines the procedures and code necessary to perform data joins, selections, and transformations using PySpark within AWS Glue. The process includes joining two datasets (products_csv and categories_csv), filtering based on specific criteria, and saving the results in various data formats to Amazon S3. The operation aims to refine product data for better accessibility and further analysis.

## Objectives

- Data Joining: Combine data from the products_csv and categories_csv tables using a common key to enrich product information with category details.
- Data Filtering: Filter the data to focus on products with a unit price greater than 5, identifying higher-value items.
- Data Storage: Save the transformed data in multiple formats (CSV, JSON, Parquet) to S3 for varied application use cases.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:

* [Prerequisites]((/prerequisites.md)) 
* [Crawler Setup](/aws-glue-crawler.md)

##  PySpark Script - [pyspark-select-alias](../glue-code/ti-pyspark-select.py)
- Input tables          : products_csv, categories_csv
- Output files          : csv, json and parquet files in S3 buckets.
- Crawlers used         : product_crawler, category_crawler

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
  category_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="categories_csv").toDF()
  ```
### 3. Data Joining and Aliasing
* Objective: Combine products and categories data based on the categoryid field, enriching product records with category names.
* Implementation:
    ```ruby
    joined_df = product_df.join(category_df, product_df.categoryid == category_df.categoryid, "inner").select(
    col("productid").alias("Product ID"),
    col("productname").alias("Product Name"),
    category_df["categoryname"].alias("Category Name"),
    col("unit_price").alias("Unit Price")
  )

  ```
  
### 3. Filtering and Output Formatting:
* Objective: Save the sorted data in CSV, JSON, and Parquet formats to predefined S3 bucket paths for both ascending and descending orders.
* Implementation:
  ```ruby
  filtered_product_df = product_selected_df.filter(col("Cost Per Unit") > 5)
  output_base_path = "s3://ti-author-scripts/ti-author-glue-scripts/ti-glue-pyspark-scripts-outputs/ti-pyspark-aliasing-outputs/"
  filtered_product_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
  filtered_product_df.write.mode("overwrite").json(output_base_path + "json/")
  filtered_product_df.write.mode("overwrite").parquet(output_base_path + "parquet/")
  ```
  
### 4. Logging and Verification:
* Objective: Log the completion of data writes, confirming successful storage in both orders and formats.
* Implementation:
  ```ruby
  glueContext.get_logger().info("Filtered data successfully written to S3 in CSV, JSON, and Parquet formats.")
  ```
