# Understanding Having with PySpark in AWS Glue:

This document provides a guide on using PySpark within AWS Glue to perform group by and count operations, and additionally, to apply filtering similar to the HAVING clause in SQL, specifically on an "electric_vehicles" dataset stored in Athena. The script sets up the necessary Spark and Glue contexts, loads data, groups it by vehicle make and model, counts occurrences, applies a filter on these counts, and displays the results in descending order.

## HAVING Clause:
The HAVING clause is used in SQL to filter the results of a query based on aggregate functions, such as COUNT, SUM, AVG, etc. It filters groups of rows after they have been aggregated, unlike the WHERE clause which filters rows before aggregation. This functionality is crucial for working with grouped data when conditions need to be applied to the results of aggregate functions.

## Prerequisites
Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:

* [Prerequisites]((/prerequisites.md)) 
* [Crawler Setup](/aws-glue-crawler.md)

##  PySpark Script - [pyspark-having](../glue-code/ti-pyspark-having.py)
- Input tables          : electric_vehicle_population_data_csv
- Output files          : csv, json and parquet files in S3 buckets.
- Crawlers used         : purchase_crawler


## Main Operations
### 1. Initializing Spark and Glue Contexts:
  * Objective: Configures the Spark and Glue contexts to ensure proper execution of operations with informative logging.
  * Implementation:
    ```ruby
    from pyspark.context import SparkContext
    from awsglue.context import GlueContext
    sc = SparkContext()
    sc.setLogLevel("INFO")
    glueContext = GlueContext(sc)
    ```
### 2. Data Loading:
  * Objective: Loads the "electric_vehicles" table from Athena into a DataFrame, preparing it for analysis.
  * Implementation:
    ```ruby
    grouped_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="electric_vehicles").toDF()
    ```
### 3. Data Aggregation and Filtering:
  * Objective: Group data by 'make' and 'model', count occurrences, and filter results based on a predefined threshold.
  * Implementation:
    ```ruby
    result_df = grouped_df.groupBy("make", "model").agg(count("*").alias("count"))
    result_df_filtered = result_df.filter(result_df["count"] > 1000)

    ```

### 4. Output Formatting and Storage:
  * Objective: Save the aggregated and filtered data in CSV, JSON, and Parquet formats to an S3 bucket, facilitating data utilization across different platforms and applications.
  * Implementation:
    ```ruby
    output_base_path = "s3://your-bucket-name/your-folder/"
    result_df_filtered.write.mode("overwrite").option("header", "true").csv(output_base_path + "csv/")
    result_df_filtered.write.mode("overwrite").json(output_base_path + "json/")
    result_df_filtered.write.mode("overwrite").parquet(output_base_path + "parquet/")

    ```

### 5. Logging and Verification:
  * Objective: Log the successful execution and storage of data to confirm the operation completed as intended.
  * Implementation:
    ```ruby
    glueContext.get_logger().info("Data successfully written to S3 in CSV, JSON, and Parquet formats.")

    ```
