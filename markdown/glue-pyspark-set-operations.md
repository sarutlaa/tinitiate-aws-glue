# Understanding Set Operations (Union, Union All, Intersect) with PySpark in AWS Glue
This document provides a comprehensive guide on using PySpark within AWS Glue to perform set operations such as union, union all, and intersect, focusing on data from "product" and "product_un_in" tables stored in Athena. The script sets up the necessary Spark and Glue contexts, loads the data, applies set operations to combine and compare datasets, and displays the results.

## Prerequisites

Ensure the proper setup of the AWS environment, including S3 buckets and IAM roles. Detailed steps can be found here:

* [Prerequisites](/prerequisites.md)
* Setting up [AWS Glue Crawler](/aws-glue-crawler.md)

##  PySpark Script 
The script can be accessed and reviewed here:
[pyspark-set-operations](../glue-code/ti-pyspark-union-unionall-intersect.py)

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
* Loads the "product" and "product_un_in" tables from the Athena database into DataFrames to prepare them for set operations.
* Code Example:
  ```ruby
  df1 = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="product").toDF()
  df2 = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="product_un_in").toDF()

  ```
### 3. Applying Set Operations:
* Union Operation: Combines rows from two datasets while removing duplicates.
  ```ruby
   union_df = df1.union(df2)
  ```
* Union All Operation: Combines all rows from two datasets, including duplicates (Note: In newer versions of PySpark, use union() to include duplicates).
  ```ruby
   union_all_df = df1.unionAll(df2)  # In newer versions of PySpark, use union() instead
  ```
* Intersect Operation: Retrieves only the common rows between two datasets.
  ```ruby
   intersect_df = df1.intersect(df2)
  ```

### 5. Displaying Results:
* Purpose: Shows the results of each set operation to verify the data manipulation processes.
* Code Example:
  ```ruby
  union_df.show()
  union_all_df.show()
  intersect_df.show()

  ```

