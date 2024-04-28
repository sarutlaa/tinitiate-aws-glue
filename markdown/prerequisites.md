#Prerequisites
Input Data Files in S3
Glue Crawler to crawl the S3 data and then getting the schema of it in Data Catalog
Accessing S3 crawlers data for the tables 'product' and 'category'.
IAM role with permissions for AWS Glue, S3, and Athena

#Setup Instructions
1. S3 Bucket Setup
Upload your CSV files to your S3 bucket.

2. IAM Role Configuration
Create an IAM role for AWS Glue with the necessary permissions to access S3, Glue, and Athena.

3. AWS Glue Setup
Crawler Setup: Create a crawler to populate the AWS Glue Data Catalog with your S3 data schema.
Glue Job: Create a Glue job with the following settings:
IAM role: Select the IAM role created earlier.
Script location: Specify the path to your PySpark script or paste the script directly in the job configuration.
DPUs: Configure the number of DPUs based on your job’s requirement.

5. PySpark Script
Below is the PySpark script used in the Glue job. This script initializes Spark and Glue contexts, loads data from Athena, selects specific columns, performs various joins, and logs the output.
