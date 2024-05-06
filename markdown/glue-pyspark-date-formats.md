# Understanding Timezone Conversion with PySpark in AWS Glue
This document explains how to use PySpark within AWS Glue to convert datetime information to different timezones, focusing on data from a "dispatch" table stored in Athena. The script sets up the necessary Spark and Glue contexts, loads the data, converts datetime values into UTC, adjusts them to a specified timezone, and displays the results.

DateTime manipulations are crucial for preparing data for analyses that depend on accurate timing and scheduling insights. This includes timezone adjustments, formatting dates for readability, and calculating time differences to understand durations or delays.

## Prerequisites

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  

##  PySpark Script - [pyspark-date-formats](../glue-code/ti-pyspark-datetime.py)
- Input tables          : dispatch
- Output                : Stored in CSV, JSON, and Parquet formats in the specified S3 bucket.
- Crawlers used         : dispatch_crawler


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

### 2. Data Loading:
* Objective: Loads the "dispatch" table from the Athena database into a DataFrame, preparing it for datetime conversion.
* Implementation:
  ```python
  df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="dispatch").toDF()
  ```
### 3. Converting to UTC::
* Objective: Converts the 'dispatch_date' string column to a UTC datetime format to standardize the timestamp data..
* Implementation:
  ```python
  from pyspark.sql.functions import from_utc_timestamp
  df_utc = df.withColumn("datetime_utc_column", from_utc_timestamp(df["dispatch_date"], "UTC"))
  ```  
    
### 4.  Additional DateTime Operations:
* Objective: Enhance the dataset with formatted date strings and calculated time differences for detailed temporal analysis.
* Note: Replace 'desired_timezone' with the appropriate timezone string, like 'America/New_York'.
* Implementation:
  ```python
  df_formatted = df_with_timezone.withColumn("formatted_date", date_format("datetime_with_timezone_column", "yyyy-MM-dd HH:mm:ss"))
  df_time_diff = df_formatted.withColumn("time_difference_seconds", expr("unix_timestamp(current_timestamp()) - unix_timestamp(datetime_with_timezone_column)"))

  ```

### 5. Output Formatting and Storage:
* Objective: Save the enriched data to Amazon S3 in multiple formats for accessibility and further use.
* Implementation:
  ```python
  output_base_path = "s3://your-bucket-name/your-folder/"
  df_time_diff.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
  df_time_diff.write.mode("overwrite").json(output_base_path + "json/")
  df_time_diff.write.mode("overwrite").parquet(output_base_path + "parquet/")

  ```
### 6. Logging and Execution Verification:
* Objective: Confirm successful execution and storage of the data, ensuring traceability and reliability of the process.
* Implementation:
  ```python
   glueContext.get_logger().info("Data successfully written to S3 in CSV, JSON, and Parquet formats.")

  ```
