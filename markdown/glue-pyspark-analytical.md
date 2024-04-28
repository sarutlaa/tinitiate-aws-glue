# Understanding Analytical Functions (RANK, DENSE RANK, LEAD, LAG) with PySpark in AWS Glue:

This document outlines the use of PySpark in AWS Glue to apply window functions for data analysis, specifically on sales data stored in Athena. The script sets up the necessary Spark and Glue contexts, executes window functions such as LAG, LEAD, and RANK, and displays the results. 

Window functions in PySpark allow for advanced data analysis and manipulation within a defined "window" of data. These functions enable calculations across a range of data rows that are related to the current row, providing powerful tools for aggregation and comparison without collapsing rows, unlike group-by functions which aggregate data to a single row. Commonly used window functions include lag, lead, rank, and row_number, each of which serves a specific purpose in data analysis:

- *LAG*: Retrieves a value from a previous row in the window, often used to compare current values with those of previous entries.
- *LEAD*: Retrieves a value from a subsequent row in the window, useful for comparing current values to future values.
- *RANK*: Assigns a rank to each row within a partition of a result set, with ties receiving the same rank.
- *ROW_NUMBER*: Assigns a unique sequential integer to rows within a partition of a result set, starting at 1 for the first row in each partition.

Below is a breakdown of the script's components and operations:

## Prerequisites

Refer Prerequisties for setting up the S3 bucket, required IAM roles and
[Prerequisites]((/prerequisites.md)) and for crawler [crawler](/aws-glue-crawler.md)


##  PySpark Script 
[pyspark-analytical-functions](../glue-code/ti-pyspark-analytical.py)


## Main Operations

### 1. Initializing Spark and Glue Contexts:
* What It Does: Configures the Spark and Glue contexts necessary for data operations, with logging set to provide informative messages.
* Code Example:
  ```ruby
  from pyspark.context import SparkContext
  from awsglue.context import GlueContext
  sc = SparkContext()
  sc.setLogLevel("INFO")
  glueContext = GlueContext(sc)
  ```

### 2. Data Loading:
* What It Does: Loads the purchase table from the Athena database into a DataFrame to prepare for analysis.
* Code Example:
  ```ruby
  analyzed_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="purchase").toDF()
  ```


### 3. Applying Window Functions:
* What It Does: Uses window functions to calculate the previous and next invoice prices, as well as the rank of invoice prices within each product supplier group.
* Use Cases: These calculations allow for detailed analysis of sales trends, pricing strategies, and ranking of sales transactions.
* Code Example:
  ```ruby
  from pyspark.sql.window import Window
  from pyspark.sql.functions import col, lag, lead, rank
  
  # Previous invoice price
  analyzed_df = analyzed_df.withColumn("previous_invoice_price", lag("invoice_price").over(Window.partitionBy("product_supplier_id").orderBy("purchase_tnxdate")))
  # Next invoice price
  analyzed_df = analyzed_df.withColumn("next_invoice_price", lead("invoice_price").over(Window.partitionBy("product_supplier_id").orderBy("purchase_tnxdate")))
  # Invoice price rank
  analyzed_df = analyzed_df.withColumn("invoice_price_rank", rank().over(Window.partitionBy("product_supplier_id").orderBy(col("invoice_price").desc())))

  ```

### 4. Displaying Results:
* What It Does: Outputs the transformed DataFrame with newly calculated columns for previous invoice price, next invoice price, and invoice price rank.
* Code Example:
  ```ruby
  analyzed_df.show()
  ```
