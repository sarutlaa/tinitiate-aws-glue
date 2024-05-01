# Understanding GroupBy with PySpark in AWS Glue:

This document outlines the use of PySpark in AWS Glue for grouping and counting data stored in Athena, focusing on electric vehicle datasets. The script sets up the necessary Spark and Glue contexts, performs data aggregation based on certain attributes, and utilizes logging to track the process. 

## GroupBy Aggregation

GroupBy counts the number of occurrences for each group specified by one or more columns.

Below is a detailed breakdown of the script's components and operations.

## Prerequisites for the pyspark script execution

Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:

* [Prerequisites]((/prerequisites.md)) 
* [Crawler Setup](/aws-glue-crawler.md)

## PySpark Script - [pyspark-groupby](../glue-code/ti-pyspark-groupby.py)
- Input tables         : electric_vehicle_population_data_csv in Data Catalog
- Output files         : csv, json and parquet files in S3 buckets.
- Crawlers used        : electric_vechiles


## Main Operations
### 1. Context Initialization:
  - Objective: Establish necessary contexts for Spark and Glue operations and set appropriate log levels.
  - Implementation:
    ```ruby
    from pyspark.context import SparkContext
    from awsglue.context import GlueContext
    sc = SparkContext.getOrCreate()
    sc.setLogLevel("INFO")
    glueContext = GlueContext(sc)
    ```
### 2. Data Loading and Preparation:
  - Objective: Load tables from Athena into Spark DataFrames, transforming them for aggregation
  - Implementation:
    ```ruby
    electric_vehicles_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="electric_vehicle_population_data_csv").toDF()
    ```

### 3. Performing Group By and Saving Results:
   - Objective: Execute group by operations to aggregate data by specified keys and save the results to designated S3 buckets in multiple formats.
   - Implementation:
      ```ruby
       result_df = electric_vehicles_df.groupBy("make", "model").agg(count("*").alias("count"))
      s3_bucket_paths = {
          "csv": "s3://bucket/csv/",
          "json": "s3://bucket/json/",
          "parquet": "s3://bucket/parquet/"
      }
      for format, path in s3_bucket_paths.items():
          result_df.write.format(format).save(path, mode="overwrite")
     ```
      
### 4. Logging and Output Verification:
   - Objective: Log operational details and confirm the success of data writes.
   - Implementatione:
       ```ruby
      logger = glueContext.get_logger()
      logger.info("Results successfully written to S3 in all formats.")

     ```
