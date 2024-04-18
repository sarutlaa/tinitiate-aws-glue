
# Understanding Joins with PySpark in AWS Glue:

This document demonstrates the use of PySpark in AWS Glue to process and join data stored in Athena. By utilizing various types of joins, we can combine records from two datasets (product and category) based on their relational keys. Here's a simple breakdown of each type of join used in the script

## Types of Joins
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

## Prerequisites
- Input Data Files in S3
- Glue Crawler to crawl the S3 data and then getting the schema of it in Data Catalog
- Accessing S3 crawlers data for the tables 'product' and 'category'. 
- IAM role with permissions for AWS Glue, S3, and Athena

## Setup Instructions

### 1. S3 Bucket Setup
Upload your CSV files to your S3 bucket.

### 2. IAM Role Configuration
Create an IAM role for AWS Glue with the necessary permissions to access S3, Glue, and Athena.

### 3. AWS Glue Setup
- **Crawler Setup**: Create a crawler to populate the AWS Glue Data Catalog with your S3 data schema.
- **Glue Job**: Create a Glue job with the following settings:
  - IAM role: Select the IAM role created earlier.
  - Script location: Specify the path to your PySpark script or paste the script directly in the job configuration.
  - DPUs: Configure the number of DPUs based on your job’s requirement.

### 4. PySpark Script
Below is the PySpark script used in the Glue job. This script initializes Spark and Glue contexts, loads data from Athena, selects specific columns, performs various joins, and logs the output.

[pyspark-joins](../glue-code/ti-pyspark-joins.py)

### 5. Understanding Joins: 
  - **Inner Join**: Returns records that have matching values in both databases.
  - **Left Join**: Returns all records from the left dataset, and the matched records from the right dataset. If there is no match, the result is `null` on the right side.
  - **Right Join**: Returns all records from the right dataset, and the matched records from the left dataset. If there is no match, the result is `null` on the left side.
  - **Full Outer Join**: Combines the results of both left and right outer joins. The result is `null` on the side that does not have a match.
  - **Cross Join**: Produces the Cartesian product of rows from both datasets. Use with caution as it can result in large datasets.

### 5. Execution
Run the Glue job and monitor the execution in the AWS Glue Console.

## Monitoring and Logs
View execution logs in the AWS Glue Console to monitor the job and troubleshoot any issues.
