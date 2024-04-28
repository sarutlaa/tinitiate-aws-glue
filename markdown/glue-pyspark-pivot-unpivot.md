# Understanding Pivot and Unpivot Operations with PySpark in AWS Glue

This document explains how to use PySpark within AWS Glue to perform pivot and unpivot operations, utilizing employee salary data stored in a CSV format in S3. The script sets up the necessary Spark and Glue contexts, loads the data, transforms it using pivot and unpivot techniques to restructure the dataset for different analytical needs, and displays the results.

## Pivot 
Pivot transforms data from a long format (many rows, fewer columns) to a wide format (fewer rows, more columns). This operation turns unique values from a specific column into multiple columns, making the data easier to analyze and visualize side by side.

### Usage Scenarios:

Comparing performance metrics across different categories or time periods displayed as separate columns.
Summarizing data for reports where each category needs its column.

## UnPivot
Unpivot does the opposite by converting data from a wide format back to a long format. This transformation takes values from multiple columns and consolidates them into one column, increasing the number of rows but decreasing the number of columns.

### Usage Scenarios:

Preparing data for analyses that require a standardized format, such as statistical tests or machine learning models.
Simplifying data structure for database storage or applications that require long-format data.

## Prerequisites

Ensure the proper setup of the AWS environment, including S3 buckets and IAM roles. Detailed steps can be found here:

* [Prerequisites](/prerequisites.md)
* Setting up [AWS Glue Crawler](/aws-glue-crawler.md)

##  PySpark Script 
The script can be accessed and reviewed here:
[pyspark-set-operations](../glue-code/ti-pyspark-pivot-unpivot.py)

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
* Purpose: Loads the employee salary data from a CSV file stored in S3 into a DataFrame.
* Code Example:
  ```ruby
  df = spark.read.option("header", "true").csv("s3://ti-p-data/hr-data/employee_dept/")
  ```
### 3. Pivot Operation:
* Purpose: Transforms the dataset to create a new DataFrame where each selected month becomes a separate column with corresponding salary data.
* Code Example:
  ```ruby
  from pyspark.sql.functions import col
  months = ['January', 'February', 'March']
  pivot_df = df.select(
      "employee_id", "employee_name", "department",
      *[col(month + "_salary").alias(month) for month in months]
  )
  ```
### 4. Unpivot Operation:
* Purpose: Transforms the pivoted DataFrame back into a long format where each row represents a month and its corresponding salary for easier comparison across different dimensions.
* Code Example:
  ```ruby
  unpivot_df = pivot_df.selectExpr(
      "employee_id", "employee_name", "department",
      "stack(3, 'January', January, 'February', February, 'March', March) as (month, salary)"
  )
  ```
### 5. Displaying Results:
* Purpose: Shows the results of both the pivoted and unpivoted DataFrames to verify the correctness of the data transformations.
* Code Example:
  ```ruby
  pivot_df.show()
  unpivot_df.show()
  ```
