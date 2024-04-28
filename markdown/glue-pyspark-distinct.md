# Understanding SQL-like Filtering with PySpark in AWS Glue
This document provides an overview of using PySpark within AWS Glue to apply SQL-like filtering conditions, specifically on a "purchase" dataset stored in Athena. The script initializes the necessary Spark and Glue contexts, loads data, and applies various conditions such as IN, NOT IN, Greater Than, Less Than, and Not Equal To to filter the data accordingly.

## Prerequisites

Ensure the proper setup of the AWS environment, including S3 buckets and IAM roles. Detailed steps can be found here:

* [Prerequisites](/prerequisites.md)
* Setting up [AWS Glue Crawler](/aws-glue-crawler.md)

##  PySpark Script 
The script can be accessed and reviewed here:

[pyspark-distinct](../glue-code/ti-pyspark-distinct.py)

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
* Purpose: Loads the "purchase" table from the Athena database into a DataFrame for subsequent filtering operations.
* Code Example:
  ```ruby
  df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
  ```
### 3. Applying Filters:
* Purpose: Demonstrates the application of various SQL-like conditions to filter the DataFrame based on specific criteria.
* Filters Applied:
  -  IN Condition: Filters rows where product_supplier_id matches any of the specified values.
    ```ruby
    df_in = df.filter(df["product_supplier_id"].isin([150, 259, 21]))
    ```
  - NOT IN Condition: Excludes rows where quantity matches any of the specified values.
    ```ruby
    df_not_in = df.filter(~df["quantity"].isin([295, 743, 67]))
    ```
  - Greater Than Condition: Selects rows where quantity is greater than 200.
    ```ruby
    df_gt = df.filter(df["quantity"] > 200)
    ```
  - Less Than Condition: Selects rows where quantity is less than 200.
    ```ruby
    df_lt = df.filter(df["quantity"] < 200)
    ```
  - Not Equal To Condition: Filters out rows where quantity is not equal to 743.
    ```ruby
    df_ne = df.filter(df["quantity"] != 743)
    ```    
    
### 4. Displaying Results:
* Purpose: Shows the results of the DataFrame after each filtering condition to verify the correctness of the applied filters.
* Code Example:
  ```ruby
  df_in.show()
  df_not_in.show()
  df_gt.show()
  df_lt.show()
  df_ne.show()
  ```
