# Pseudo Columns with PySpark in AWS Glue

This document provides a comprehensive guide on using PySpark within AWS Glue to enrich data with pseudo columns and save the results to Amazon S3 in various formats. Specifically, the script involves adding unique identifiers and row numbers to a dataset stored in Athena, illustrating the application of functions like monotonically_increasing_id and row_number.

## Pseudo Columns in PySpark:
Pseudo columns are columns generated through functions rather than retrieved directly from the data source. They are used to perform unique row identification or to create sortable attributes within the data that do not naturally exist in the source. In PySpark, in built functions like monotonically_increasing_id() and window functions such as row_number() are commonly used to generate these columns
- monotonically_increasing_id() : Generates a unique identifier for each row, which increases across the entire DataFrame.
- row_number() : Assigns a sequential number to each row within its partition, starting at 1.

## Prerequisites
Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:

* [Prerequisites]((/prerequisites.md)) 
* [Crawler Setup](/aws-glue-crawler.md)

##  PySpark Script - [pyspark-having](../glue-code/ti-pyspark-psuedo.py)
- Input tables          : purchase
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
  * Objective: Load the purchase table from Athena into a DataFrame, preparing it for transformation.
  * Implementation:
    ```ruby
    df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
    ```
### 3. Adding Pseudo Columns:
  * Objective: Enrich the DataFrame by adding a monotonically increasing ID and row numbers within specified partitions.
  * Implementation:
    ```ruby
    df_with_id = df.withColumn("row_id", monotonically_increasing_id())

    window_spec = Window.partitionBy("product_supplier_id").orderBy("quantity")
    df_with_row_number = df.withColumn("row_number", row_number().over(window_spec))


    ```

### 4. Output Formatting and Storage:
  * Objective: Save the data enhanced with pseudo columns to an S3 bucket in multiple formats, facilitating data utilization across different platforms and applications.
  * Implementation:
    ```ruby
    output_base_path = "s3://your-bucket-name/data-outputs/"
    df_with_id.write.mode("overwrite").option("header", "true").csv(output_base_path + "with_id/csv/")
    df_with_id.write.mode("overwrite").json(output_base_path + "with_id/json/")
    df_with_id.write.mode("overwrite").parquet(output_base_path + "with_id/parquet/")
    
    df_with_row_number.write.mode("overwrite").option("header", "true").csv(output_base_path + "with_row_number/csv/")
    df_with_row_number.write.mode("overwrite").json(output_base_path + "with_row_number/json/")
    df_with_row_number.write.mode("overwrite").parquet(output_base_path + "with_row_number/parquet/")

    ```

### 5. Logging and Verification:
  * Objective: Log the successful execution and storage of data to confirm the operation completed as intended.
  * Implementation:
    ```ruby
    glueContext.get_logger().info("Data successfully written to S3 in CSV, JSON, and Parquet formats.")

    ```
