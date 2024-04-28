# Understanding Having with PySpark in AWS Glue:

This document provides a guide on using PySpark within AWS Glue to perform group by and count operations, and additionally, to apply filtering similar to the HAVING clause in SQL, specifically on an "electric_vehicles" dataset stored in Athena. The script sets up the necessary Spark and Glue contexts, loads data, groups it by vehicle make and model, counts occurrences, applies a filter on these counts, and displays the results in descending order.

## HAVING Clause:
The HAVING clause is used in SQL to filter the results of a query based on aggregate functions, such as COUNT, SUM, AVG, etc. It filters groups of rows after they have been aggregated, unlike the WHERE clause which filters rows before aggregation. This functionality is crucial for working with grouped data when conditions need to be applied to the results of aggregate functions.

## Prerequisites
Ensure all necessary AWS configurations are in place, including S3 buckets and IAM roles, along with setting up the AWS Glue Catalog and necessary databases. Ad detailed in
* [Prerequisites](/prerequisites.md)
* Setting up [AWS Glue Crawler](/aws-glue-crawler.md)

##  PySpark Script 
The script can be accessed and reviewed here:
[pyspark-having](../glue-code/ti-pyspark-having.py)

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

### 4. Applying Filter (Similar to HAVING):
  * Purpose: Filters the grouped and counted results to only include records where the count exceeds 1000, mimicking the behavior of the HAVING clause.
  * Code Example:
    ```ruby
    result_df_filtered = result_df.filter(result_df["count"] > 1000)
    ```

### 5. Displaying Results:
  * Purpose: Outputs the processed data to show the counts of electric vehicles that meet the filter criteria.
  * Code Example:
    ```ruby
    result_df_filtered.show()
    ```
