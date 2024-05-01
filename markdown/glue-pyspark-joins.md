
# Understanding Joins with PySpark in AWS Glue:

This document outlines the use of PySpark in AWS Glue for performing different types of joins between data stored in Glue Data Catalog. The script prepares the Spark and Glue contexts, performs data transformations, executes various joins, and displays the results.

## Types of Joins

![Joins_Diagram](https://github.com/sarutlaa/tinitiate-aws-glue/assets/141533429/4e134bfc-8804-4f57-80e6-af11137383af)


### 1. Inner Join: An inner join returns records that have matching values in both tables
   
### 2. Left Join: A left join returns all records from the left table, and the matched records from the right table. If there is no match, the result is NULL on the side of the right table.
  
### 3. Right Join: It is similar to the left join but returns all records from the right table, and the matched records from the left table. If there is no match, the result is NULL on the side of the left table.

### 4. Full Outer Join: A full outer join returns all records when there is a match in either the left or right table. This means it shows all records from both tables, with matching records from both sides where available. If there is no match, the result is NULL on the side of the table without a match.

Below is a detailed breakdown of the script's components and operations.

## Prerequisites for the pyspark script execution

Ensure proper configuration of IAM roles and S3 buckets as outlined here:

* [Prerequisites]((/prerequisites.md)) 
* [Crawler Setup](/aws-glue-crawler.md)


## PySpark Script - [pyspark-joins](../glue-code/ti-pyspark-joins.py)
- Input           : products_csv, categories_csv.
- Output          : csv, json and parquet files in S3 buckets.


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
  - Objective: Load tables from Athena into Spark DataFrames and prepare them for joining.
  - Implementation:
    ```ruby
    product_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="products_csv").toDF()
    category_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="categories_csv").toDF()
    product_selected_df = product_df.select("productid", "productname", "categoryid",       "unit_price").withColumnRenamed("categoryid", "product_categoryid")
    category_selected_df = category_df.select("categoryid", "categoryname")
    ```

### 3. Executing Joins and Saving Results:
  - Objective: Perform different types of joins and save the results to specified S3 buckets in various formats.
  - Implementation:
    ```ruby
     join_types = ["inner", "left", "right", "outer"]
    s3_bucket_paths = {
        "csv": "s3://bucket/csv/",
        "json": "s3://bucket/json/",
        "parquet": "s3://bucket/parquet/"
    }
    for join_type in join_types:
        joined_df = product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], join_type)
        for format, path in s3_bucket_paths.items():
            joined_df.write.format(format).save(path + join_type, mode="overwrite")
      ```
     
### 4. Logging and Output Verification:
   - Objective: Log operational details and confirm the success of data writes
   - Implementation:
     ```ruby
        glueContext.get_logger().info("Data successfully written to S3 in all formats.")
      ```
