# Set Operations (Union, Union All, Intersect) with PySpark in AWS Glue
This document provides a comprehensive guide on using PySpark within AWS Glue to perform set operations such as union, union all, and intersect, focusing on data from "product" and "product_un_in" tables stored in Athena. The script sets up the necessary Spark and Glue contexts, loads the data, applies set operations to combine and compare datasets, and displays the results.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  
##  PySpark Script - [pyspark-set-operations](../glue-code/ti-pyspark-union-unionall-intersect.py)
- Input tables          : products_csv, products_csv
- Output files          : csv, json and parquet files in S3 buckets.
- Crawlers used         : products_crawler

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

### 2. Data Loading:
* Objective: Loads the "product" and "product_un_in" tables from the Athena database into DataFrames to prepare them for set operations.
* Implementation:
  ```python
  df1 = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="product").toDF()
  df2 = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="product_un_in").toDF()

  ```
### 3. Applying Set Operations:
* Union Operation: Combines rows from two datasets while removing duplicates.
  ```python
   union_df = df1.union(df2)
  ```
* Union All Operation: Combines all rows from two datasets, including duplicates (Note: In newer versions of PySpark, use union() to include duplicates).
  ```python
   union_all_df = df1.unionAll(df2)  # In newer versions of PySpark, use union() instead
  ```
* Intersect Operation: Retrieves only the common rows between two datasets.
  ```python
   intersect_df = df1.intersect(df2)
  ```

### 4. Output Formatting and Storage:
* Objective: Store the results of each set operation in CSV, JSON, and Parquet formats in predefined paths on an S3 bucket.
* Implementation:
  ```python
  output_base_path = "s3://your-bucket-name/your-folder/"
  union_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "union/csv/")
  union_df.write.mode("overwrite").json(output_base_path + "union/json/")
  union_df.write.mode("overwrite").parquet(output_base_path + "union/parquet/")
  union_all_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "union_all/csv/")
  union_all_df.write.mode("overwrite").json(output_base_path + "union_all/json/")
  union_all_df.write.mode("overwrite").parquet(output_base_path + "union_all/parquet/")
  intersect_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "intersect/csv/")
  intersect_df.write.mode("overwrite").json(output_base_path + "intersect/json/")
  intersect_df.write.mode("overwrite").parquet(output_base_path + "intersect/parquet/")
  ```

### 5. Logging and Execution Verification:
* Objective: Log the completion of operations and confirm the successful storage of data in all specified formats and operations.
* Implementation:
  ```python
   glueContext.get_logger().info("Set operations data successfully written to S3 in CSV, JSON, and Parquet formats.")
  ```
