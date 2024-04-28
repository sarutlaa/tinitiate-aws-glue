# Understanding Distinct Operation with PySpark in AWS Glue
This document provides a detailed guide on using PySpark within AWS Glue to remove duplicate records from a dataset, specifically focusing on a "purchase" table stored in Athena. The script sets up the necessary Spark and Glue contexts, loads the data, performs a distinct operation to ensure uniqueness, and displays the results.

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
### 3. Obtaining Distinct Records:
* Purpose: Removes duplicate entries from the DataFrame to ensure that each row is unique, which is crucial for accurate data analysis and reporting.
* Code Example:
  ```ruby
  distinct_df = df.distinct()
  ```
 
### 4. Displaying Results:
* Purpose: Shows the distinct records from the DataFrame, triggering an action that collects and prints the unique rows to the console.
* Code Example:
  ```ruby
  distinct_df.show()
  ```
