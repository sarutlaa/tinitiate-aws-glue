# Data Partitioning and Storage with PySpark in AWS Glue
In PySpark and AWS Glue, the partitionBy method is a crucial feature for organizing and optimizing how data is stored, especially when working with large datasets that need to be processed in distributed environments like Apache Spark or stored efficiently in systems like AWS S3. Understanding how partitionBy works and how to apply it correctly can significantly improve performance and cost-effectiveness of data operations.

## Key Points:

1. Purpose: Organizes data into partitions or directories based on column values. It's particularly useful for data that is queried frequently based on certain columns, such as date or region.
2. Functionality: When you save a DataFrame using partitionBy, PySpark creates a folder structure for each unique value or combination of values in the specified column(s). Each folder then contains only the data corresponding to its partition value, which can significantly improve query performance on large datasets.
3. Usage: Commonly used with file formats that support partition discovery like Parquet and ORC, which allow Spark to optimize queries by reading only relevant partitions of data.


AWS Glue uses the same principle as PySpark but adds additional integration with AWS services. Glue can read and write data from various sources like Amazon S3, and using partitionBy helps manage data storage more efficiently and reduce costs by minimizing the data scanned during queries.

The partitionBy() method is used primarily when writing DataFrames to disk. It partitions data based on one or more specified column values before saving it

## Prerequisites
Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  
##  PySpark Script - [pyspark-repartitioning.py](../glue-code/ti-pyspark-repartitioning.py)
* Input Table: electric_vehicle_population_data_csv
* Output Formats: CSV, JSON, and Parquet files in S3 buckets.
* Crawlers Used : eletricc_vehicles

## Main Operations
### 1. Initializing Spark and Glue Contexts:
  * Objective: Configures the Spark and Glue contexts to ensure proper execution of operations with informative logging.
  * Implementation:
    ```python
    from pyspark.context import SparkContext
    from awsglue.context import GlueContext
    sc = SparkContext()
    sc.setLogLevel("INFO")
    glueContext = GlueContext(sc)
    ```
### 2. Data Loading:
  * Objective: Load the purchase table from Athena into a DataFrame, preparing it for transformation.
  * Implementation:
    ```python
    df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="electric_vehicle_population_data_csv").toDF()

    ```
### 3. Data Partitioning:
  * Objective: Partition data based on specific columns to optimize storage and query performance.
  * Explanation: Partitioning is a tool that allows you to control what data is stored and where as you write it. By encoding a column as a folder when writing to a partitioned directory, you can dramatically improve read performance. This approach allows you to skip large amounts of irrelevant data when you read in the dataset later, focusing only on the data pertinent to your queries.
  * Implementation:
    ```python
    partition_columns = ["Model Year", "Make"]
    ```

### 4. Write Partitioned Data to S3:
  * Objective: Write the partitioned data to S3 in various formats, enabling efficient data storage and access.
  * Implementation:
    ```python
    df.write.partitionBy(*partition_columns).format("parquet").mode("overwrite").save(s3_base_path + "parquet/")
    df.write.partitionBy(*partition_columns).format("json").mode("overwrite").save(s3_base_path + "json/")
    df.write.partitionBy(*partition_columns).format("csv").option("header", "true").mode("overwrite").save(s3_base_path + "csv/")

    ```
  * Sample output for Partition By Column : "Model Year"
    <img width="928" alt="partition_1" src="https://github.com/sarutlaa/tinitiate-aws-glue/assets/141533429/fe59fb7c-75a1-4b6a-a84a-a4e2e2337d7d">
  * Sample output for Next Partition By Columns : "Make"
    <img width="934" alt="repartition_1" src="https://github.com/sarutlaa/tinitiate-aws-glue/assets/141533429/0bed9b85-7a29-4657-9d0c-081ab9ca895e">
    
### 5. Verify Data Structure:
  * Objective: Track the success and details of the data processing and writing operations.
  * Implementation:
    ```python
    df.printSchema()
    ```
