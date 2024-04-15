# AWS Glue
> Jay Kumsi

## Glue Topics
* [AWS Glue Overview](markdown/Intro.md)
* What IAM Roles are needed

### Glue with PySpark
#### Spark with various data sources
* S3
* Athena
* EC2 DB, Files
* Dynamo
* RDS
* SNS
* SQS
* AirFlow

#### Glue Spark DynamicFrames and DataFrames
* Glue Dynamic Frames
* Glue PySpark DataFrame Joins (Inner, Left, Right, Full Outer)
 
* How to build Dataframe (S3) , build a data frame from Athena
* Can you build dataframe (S3) from parquet,csv,json
### Glue with Crawler
* [Crawler](markdown/aws-glue-crawler.md)
    * Source
    * Target
    * Source S3 (CSV,Parquet,JSON,AWS ION) - Target(S3,RDBMS,DynamoDB)
        * IAM roles needed
        * Code Structure
    * Source RDBMS (Oracle, SQL Server, Postgresql) - Target(S3,RDBMS,  
                    DynamoDB) 
    * Source Dynamo - Target(S3,RDBMS,DynamoDB)
    * Create Script to crawl the S3 Zip file to Data Catalog
    * Create a log group using the script
    * Add above crawl to the Log group
    * Read errors from latest log in the specified log group
    * Partitioning through crawler 
        1. Unpartitioned table
        2. List partition on dept column
        3. Range partition on Join_date column year value
        4. Composite partition
        5. hash partition
    * partitioning through Athena
    * Inserting through Athena
    * Serde to read parquet/JSon/CSV/Ion


## GITHUB Deployment with Actions
* Working with GitHub
* AWS CLI with Glue-spark
    * Create Job
    * Update Job
    * Run Job
* AWS CLI with Glue-crawler
    * Create Job
    * Update Job
    * Run Job
* Deploy code from github to AWS account
    * Settings
    * actions>yaml file
    * On Push, On Merge
