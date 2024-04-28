# Understanding Timezone Conversion with PySpark in AWS Glue
This document explains how to use PySpark within AWS Glue to convert datetime information to different timezones, focusing on data from a "dispatch" table stored in Athena. The script sets up the necessary Spark and Glue contexts, loads the data, converts datetime values into UTC, adjusts them to a specified timezone, and displays the results.

## Prerequisites

Ensure the proper setup of the AWS environment, including S3 buckets and IAM roles. Detailed steps can be found here:

* [Prerequisites](/prerequisites.md)
* Setting up [AWS Glue Crawler](/aws-glue-crawler.md)

##  PySpark Script 
The script can be accessed and reviewed here:
[pyspark-date-formats](../glue-code/ti-pyspark-datetime.py)

## Main Operations

### 1. Initializing Spark and Glue Contexts:
* Purpose: Establishes the necessary Spark and Glue contexts for data manipulation with logging set to INFO to control verbosity.
* Code Example:
  ```ruby
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```

### 2. Data Loading:
* Purpose: Loads the "dispatch" table from the Athena database into a DataFrame, preparing it for datetime conversion.
* Code Example:
  ```ruby
  df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="dispatch").toDF()
  ```
### 3. Converting to UTC::
* Purpose: Converts the 'dispatch_date' string column to a UTC datetime format to standardize the timestamp data..
* Code Example:
  ```ruby
  from pyspark.sql.functions import from_utc_timestamp
  df_utc = df.withColumn("datetime_utc_column", from_utc_timestamp(df["dispatch_date"], "UTC"))
  ```  
    
### 4. Converting to Desired Timezone:
* Purpose: Adjusts the UTC datetime to a specified timezone, enhancing the data's relevance for specific regional analyses.
* Note: Replace 'desired_timezone' with the appropriate timezone string, like 'America/New_York'.
* Code Example:
  ```ruby
  df_with_timezone = df_utc.withColumn("datetime_with_timezone_column", from_utc_timestamp(df_utc["datetime_utc_column"], "desired_timezone"))
  ```

### 5. Displaying Results:
* Purpose: Shows the DataFrame with the new datetime columns adjusted for the specified timezone, validating the timezone conversion.
* Code Example:
  ```ruby
  df_with_timezone.show()
  ```
