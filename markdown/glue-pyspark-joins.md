
# Understanding Joins with PySpark in AWS Glue:

This document outlines the use of PySpark in AWS Glue for performing different types of joins between data stored in Athena, specifically between product and category datasets. The script prepares the Spark and Glue contexts, performs data transformations, executes various joins, and displays the results.Below is a detailed breakdown of the script's components and operations:

## Types of Joins

![Joins_Diagram](https://github.com/sarutlaa/tinitiate-aws-glue/assets/141533429/4e134bfc-8804-4f57-80e6-af11137383af)


### 1. Inner Join:
  - What It Does: Merges rows from both datasets where the join column values match.
  - Example: Matches products with their corresponding categories using categoryid.
  - Use Case: Ideal for displaying products that have specific categories defined.
```ruby
inner_df = product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], "inner")
```
    
### 2. Left Join:

  - What It Does: Includes all rows from the left dataset and the matched rows from the right dataset. Unmatched rows from the right dataset will have null values.
  - Example: Shows all products, appending category information where available.
  - Use Case: Useful for displaying all products, highlighting those without specific categories.
```ruby
left_df = product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], "left")
```
    
### 3. Right Join:

  - What It Does: Includes all rows from the right dataset and the matched rows from the left dataset. Unmatched rows from the left dataset will have null values.
  - Example: Lists all categories, appending product information where available.
  - Use Case: Ensures that all categories are displayed, including those without any linked products.
```ruby
right_df = product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], "right")
```

### 4. Full Outer Join:

  - What It Does: Combines results of both left and right joins, including rows from both datasets where there is no match.
  - Example: Shows all products and categories, marking unmatched items with null.
  - Use Case: Provides a comprehensive overview of both products and categories, displaying complete data availability.
```ruby
full_outer_df = product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], "outer")
```
## Prerequisites for the pyspark script execution

Ensure to have the correct IAM roles and S3 bucket configurations set up, which are detailed in these documents:
[Prerequisites]((/prerequisites.md)) and for crawler [crawler](/aws-glue-crawler.md)


## PySpark Script
Below is the PySpark script used in the Glue job. This script initializes Spark and Glue contexts, loads data from Athena, selects specific columns, performs various joins, and logs the output.
[pyspark-joins](../glue-code/ti-pyspark-joins.py)

## Main Operations
1. Initializing Spark and Glue Contexts:
    - What It Does: Sets up the necessary contexts for Spark and Glue operations, configuring log levels to monitor the execution process.
    - Code Example:
      ```ruby
        from pyspark.context import SparkContext
        from awsglue.context import GlueContext
        sc = SparkContext()
        sc.setLogLevel("INFO")
        glueContext = GlueContext(sc)
        ```
2. Data Loading and Preparation:
    - What It Does: Loads tables from the Athena database into data frames and prepares them by selecting and renaming columns to facilitate joining without column name conflicts.
    - Code Example:
      ```ruby
      product_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="product").toDF()
      category_df = glueContext.create_dynamic_frame.from_catalog(database="glue_db", table_name="category").toDF()
      product_selected_df = product_df.select("productid", "productname", "categoryid", "unit_price").withColumnRenamed("categoryid", "product_categoryid")
      category_selected_df = category_df.select("categoryid", "categoryname")
      ```

3. Performing Joins:
    - What It Does: Executes inner, left, right, and full outer joins on the product and category datasets based on the categoryid column.
    - Code Examples:
       ```ruby
      # Inner Join
      inner_df = product_selected_df.join(category_selected_df, "product_categoryid" == "categoryid", "inner")
      # Left Join
      left_df = product_selected_df.join(category_selected_df, "product_categoryid" == "categoryid", "left")
      # Right Join
      right_df = product_selected_df.join(category_selected_df, "product_categoryid" == "categoryid", "right")
      # Full Outer Join
      full_outer_df = product_selected_df.join(category_selected_df, "product_categoryid" == "categoryid", "outer")
      ```
     
4. Logging and Results Display:
     - What It Does: Logs the count of rows in each joined DataFrame and displays the results.
     - Code Examples:
       ```ruby
        glueContext.get_logger().info("Number of rows in the joined DataFrame: {}".format(inner_df.count()))
        inner_df.show()
      ```
     





