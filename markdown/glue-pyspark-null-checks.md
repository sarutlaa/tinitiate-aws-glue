# Handling Null and Non-Null Values
The script performs essential data cleansing operations by segregating null and non-null values within a specified column of the dataset. This process is critical for preparing the data for further analytics, ensuring that downstream processes such as reporting and data visualization are based on clean and accurate data.

DateTime manipulations are crucial for preparing data for analyses that depend on accurate timing and scheduling insights. This includes timezone adjustments, formatting dates for readability, and calculating time differences to understand durations or delays.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  


##  PySpark Script - [pyspark-null-checks](../glue-code/ti-pyspark-isnull-notnull.py)
- Input tables          : categories_csv
- Output                : Stored in CSV, JSON, and Parquet formats in the specified S3 bucket.
- Crawlers used         : category_crawler


## Main Operations

### 1. Initializing Spark and Glue Contexts:
* Objective: Establishes the necessary Spark and Glue contexts for data manipulation with logging set to INFO to control verbosity.
* Code Example:
  ```python
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```

### 2. Data Loading and Transformation:
* Objective: Load data from the Athena "categories_csv" table into a DataFrame, apply filters to segregate null and non-null values based on the 'categoryname' column.
* Implementation:
  ```python
  df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="category").toDF()
  df_null = df.filter(col("categoryname").isNull())
  df_not_null = df.filter(col("categoryname").isNotNull())
  ```
### 3. Output Formatting and Storage:
* Objective: Store the results of filtered data frames into Amazon S3 in multiple formats for various uses, enhancing data accessibility.
* Implementation:
  ```python
  output_base_path = "s3://your-bucket-name/your-folder/"
  df_null.write.mode("overwrite").option("header", "true").csv(output_base_path + "null/csv/")
  df_not_null.write.mode("overwrite").json(output_base_path + "not_null/json/")
  df_not_null.write.mode("overwrite").parquet(output_base_path + "not_null/parquet/")
  ```  
    
### 4. Logging and Execution Verification:
* Objective: Confirm the successful execution of the script and log the completion of data storage operations.
* Implementation:
  ```python
  glueContext.get_logger().info("Data with null and not null values successfully written to S3 in CSV, JSON, and Parquet formats.")
  ```


