
# Understanding Joins with PySpark in AWS Glue:

This document demonstrates the use of PySpark in AWS Glue to process and join data stored in Athena. By utilizing various types of joins, we can combine records from two datasets (product and category) based on their relational keys. Here's a simple breakdown of each type of join used in the script

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
