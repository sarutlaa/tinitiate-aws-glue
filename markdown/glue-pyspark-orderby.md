# Understanding Order By with PySpark in AWS Glue

 This document provides a guide on using PySpark within AWS Glue to perform group by and count operations, specifically analyzing data from an "electric_vehicles" dataset stored in Athena. The script sets up the necessary Spark and Glue contexts, loads data, groups it by vehicle make and model, and counts occurrences. To make the data more insightful, it employs an ORDER BY clause to sort the results in descending order based on the count, making it easier to identify the most common makes and models.

## ORDER BY Clause

The ORDER BY clause is used to sort the results of a query in either ascending or descending order based on one or more columns. This helps organize data meaningfully for easier analysis and presentation.

## Prerequisites
Ensure all necessary AWS configurations are in place, including S3 buckets and IAM roles, along with setting up the AWS Glue Catalog and necessary databases. Ad detailed in
* [Prerequisites](/prerequisites.md)
* Setting up [AWS Glue Crawler](/aws-glue-crawler.md)

##  PySpark Script 
The script can be accessed and reviewed here:
[pyspark-orderby](../glue-code/ti-pyspark-orderby.py)


## Main Operations
### 1. Initializing Spark and Glue Contexts:
* Purpose: Configures the Spark and Glue contexts to ensure proper execution of operations with informative logging.
* Code Example:
  ```ruby
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```
  
### 2. Data Loading:
* Purpose: Loads the "electric_vehicles" table from Athena into a DataFrame, preparing it for analysis.
* Code Example:
  ```ruby
  grouped_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="electric_vehicles").toDF()
  ```

### 3. Grouping and Counting:
* Purpose: Groups the data by vehicle make and model, then counts the occurrences to analyze the distribution of electric vehicles.
* Code Example:
  ```ruby
  from pyspark.sql.functions import count
  result_df = grouped_df.groupBy("make", "model").agg(count("*").alias("count"))
  ```
  
### 4. Sorting the Results:
* Purpose: Orders the grouped results by the count of occurrences in descending order to highlight the most common makes and models.

* Code Example:
  ```ruby
  result_df = result_df.orderBy("count", ascending=False)
  ```
  
### 5. Displaying Results:
* Purpose: Outputs the processed data to show the counts of electric vehicles sorted by popularity.
* Code Example:
  ```ruby
  result_df.show()
  ```
