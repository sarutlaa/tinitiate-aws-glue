# Hierarchical Data Processing and Storage with PySpark in AWS Glue
This documentation describes a PySpark script used within AWS Glue to handle hierarchical data from a catalog table, perform a recursive query, and save the outputs in multiple formats (Parquet, JSON, and CSV). The script is designed to process hierarchical structures, making it suitable for scenarios like organizational charts, category trees, or any nested relationship data.

Managing Data Partitions with PySpark in AWS Glue
## Key Concepts:
1. Hierarchical Query: Processes data recursively to build a hierarchical structure.
2. Data Formats: Outputs data in multiple formats to suit various downstream processing needs.
3. Parallel Writing: Writing data in parallel to reduce execution time and improve throughput.

## Prerequisites
Ensure proper configuration of IAM roles and S3 buckets and run necessary crawleras outlined here:
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  
##  PySpark Script - [pyspark-repartitioning.py](../glue-code/ti-pyspark-repartitioning.py)
* Input Table: Sample inputs through list.
* Output Formats: CSV, JSON, and Parquet files in S3 buckets.

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
### 2. Data Generation and Loading:
 
