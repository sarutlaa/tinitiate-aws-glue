# Managing Duplicate Records with PySpark in AWS Glue
This document provides a detailed guide on using PySpark within AWS Glue to remove duplicate records from a dataset, specifically focusing on a "purchase" table stored in Athena. The script sets up the necessary Spark and Glue contexts, loads the data, performs a distinct operation to ensure uniqueness, and displays the results.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:

* [Crawler Prerequisites](/crawler-prerequisites.md)
* [Crawler Setup Instructions](/set-up-instructions.md)
  
##  PySpark Script - [pyspark-distinct](../glue-code/ti-pyspark-distinct.py)
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
* Objective: Loads the "purchase" table from the Athena database into a DataFrame for subsequent filtering operations.
* Implementation :
  ```python
  df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
  ```
### 3. Obtaining Distinct Records:
* Objective: Removes duplicate entries from the DataFrame to ensure that each row is unique, which is crucial for accurate data analysis and reporting.
* Implementation :
  ```python
  distinct_df = df.distinct()
  ```
 
### 4. Output Formatting and Storage:
* Objective: Save the filtered data in CSV, JSON, and Parquet formats to predefined paths in an S3 bucket, facilitating easy access and utilization across different platforms.
* Implementation :
  ```python
  output_base_path = "s3://your-bucket-name/your-folder/"
  distinct_df.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
  distinct_df.write.mode("overwrite").json(output_base_path + "json/")
  distinct_df.write.mode("overwrite").parquet(output_base_path + "parquet/")
  ```
### 5. Logging and Execution Verification:
* Objective: Log the completion of the distinct operation and confirm the successful storage of data in all specified formats.
* Implementation :
  ```python
  glueContext.get_logger().info("Distinct records successfully written to S3 in CSV, JSON, and Parquet formats.")
  ```
