# Understanding GroupBy with PySpark in AWS Glue:

This document outlines the use of PySpark in AWS Glue for grouping and counting data stored in Athena, focusing on electric vehicle datasets. The script sets up the necessary Spark and Glue contexts, performs data aggregation based on certain attributes, and utilizes logging to track the process. 

## Main Operations
1. Initializing Spark and Glue Contexts:
   
- What It Does: Sets up the necessary contexts for Spark and Glue operations, including logging configurations.
- Code Example:
  ```ruby
    from pyspark.context import SparkContext
    from awsglue.context import GlueContext
    sc = SparkContext()
    sc.setLogLevel("INFO")
    glueContext = GlueContext(sc)
  ```

2. Data Loading and Conversion:
- What It Does: Loads data from the AWS Glue Data Catalog, specifically targeting the Athena database and converting dynamic frames to dataframes.
- Code Example:
   ```ruby
    grouped_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="electric_vehicles").toDF()
  ```
3. Grouping and Counting:
- What It Does: Groups the electric vehicle data by 'make' and 'model', then counts the number of occurrences for each combination.
- Use Case: Useful for understanding the distribution of different makes and models within the dataset.
- Code Example:
    ```ruby
    result_df = grouped_df.groupBy("make","model").agg(count("*").alias("count"))
  ```

## Prerequisites for the PySpark Script Execution:

Refer Prerequisties for setting up the S3 bucket, required IAM roles and
[Prerequisites]((/prerequisites.md)) and for crawler [crawler](/aws-glue-crawler.md)

## PySpark Script

[pyspark-groupby](../glue-code/ti-pyspark-groupby.py)

## Execution
