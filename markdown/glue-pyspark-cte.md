# Temporary Views and SQL Queries 
This document outlines using PySpark within AWS Glue to create temporary views and execute SQL queries, focusing on data from the "purchase" table stored in Athena. 
The script sets up the necessary Spark and Glue contexts, loads data, creates a temporary view, and queries it.

## CTE (Common Table Expression)
In this context, creating a temporary view can be seen as analogous to using a CTE in SQL. The temporary view allows for the data to be manipulated and queried as if 
it were a standalone table, aiding in simplifying SQL queries and improving readability.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  
##  PySpark Script - [pyspark-set-operations](../glue-code/ti-pyspark-cte.py)
- Input tables          : purchase
- Output files          : csv, json and parquet files in S3 buckets.
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
### 2. Data Loading:
* Objective: Loads the "purchase" table from the Athena database into a DataFrame.
* Implementation:
  ```python
  df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()

  ```
### 3. Creating a Temporary View:
* Objective: Creates a temporary view named "temp_table" which can be used in SQL queries, similar to how a CTE would be used.
* Implementation:
  ```python
  df.createOrReplaceTempView("temp_table")
  ```

### 4. Executing SQL Queries:
* Objective: Uses the temporary view to perform SQL queries, simplifying access to and manipulation of the data.
* Implementation:
  ```python
  result_df = spark.sql("SELECT * FROM temp_table")
  ```

### 5. Output Formatting and Storage:
* Objective: Save the SQL query results in CSV, JSON, and Parquet formats to predefined S3 bucket paths, ensuring data is accessible for further analysis.
* Implementation:
  ```python
  output_base_path = "s3://your-bucket-name/your-folder/"
  result_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
  result_df.write.mode("overwrite").json(output_base_path + "json/")
  result_df.write.mode("overwrite").parquet(output_base_path + "parquet/")
  ```
### 6. Logging and Execution Verification:
* Objective: Log operational details and confirm the successful execution and storage of data in all specified formats.
* Implementation:
  ```python
  glueContext.get_logger().info("Data successfully written to S3 in CSV, JSON, and Parquet formats.")
  ```
