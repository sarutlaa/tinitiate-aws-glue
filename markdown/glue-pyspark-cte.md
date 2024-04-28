# Leveraging Temporary Views and SQL Queries
This document outlines using PySpark within AWS Glue to create temporary views and execute SQL queries, focusing on data from the "purchase" table stored in Athena. 
The script sets up the necessary Spark and Glue contexts, loads data, creates a temporary view, and queries it.

## CTE (Common Table Expression)
In this context, creating a temporary view can be seen as analogous to using a CTE in SQL. The temporary view allows for the data to be manipulated and queried as if 
it were a standalone table, aiding in simplifying SQL queries and improving readability.

## Prerequisites

Ensure the proper setup of the AWS environment, including S3 buckets and IAM roles. Detailed steps can be found here:

* [Prerequisites](/prerequisites.md)
* Setting up [AWS Glue Crawler](/aws-glue-crawler.md)

##  PySpark Script 
The script can be accessed and reviewed here:
[pyspark-set-operations](../glue-code/ti-pyspark-cte.py)

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
* Purpose: Loads the "purchase" table from the Athena database into a DataFrame.
* Code Example:
  ```ruby
  df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()

  ```
### 3. Creating a Temporary View:
* Purpose: Creates a temporary view named "temp_table" which can be used in SQL queries, similar to how a CTE would be used.
* Code Example:
  ```ruby
  df.createOrReplaceTempView("temp_table")
  ```

### 4. Executing SQL Queries:
* Purpose: Uses the temporary view to perform SQL queries, simplifying access to and manipulation of the data.
* Code Example:
  ```ruby
  result_df = spark.sql("SELECT * FROM temp_table")
  ```

### 4. Displaying Results:
* Purpose: Shows the results from the SQL query to verify the correctness and effectiveness of the temporary view.
* Code Example:
  ```ruby
  result_df.show()
  ```

