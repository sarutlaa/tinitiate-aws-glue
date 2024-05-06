# AWS Glue
> Jay Kumsi & Sravya Arutla

## Glue Topics
* [AWS Glue Overview](Intro.md)
* [AWS Glue Crawler](aws-glue-crawler.md)
   * Source
   * Target
* Glue with PySpark
    * Source S3 (CSV,Parquet,JSON,AWS ION) - Target(S3,RDBMS,DynamoDB)
        * IAM roles needed
        * Code Structure
    * Source RDBMS (Oracle, SQL Server, Postgresql) - Target(S3,RDBMS,DynamoDB) 
    * Source Dynamo - Target(S3,RDBMS,DynamoDB)

## Glue with PySpark
* [IAM Prerequisites](IAM-prerequisites.md)
* [S3 Data Generation](s3-data-generation.md)
* [Crawler Setup Instructions](set-up-instructions.md)
  
## SQL Like Implementations with PySpark and AWS Glue ETL Scripts
All the below codes are taking csv file from S3 as input and then storing results in csv, json and parquet formats. ---- Check with Venkat garu. 


### Data Retrieval and Manipulation

* [Select & Alias](glue-pyspark-select-alias.md)
* [Order By](glue-pyspark-orderby.md)
* [Group By](glue-pyspark-groupby.md)
* [Distinct](glue-pyspark-distinct.md)
* [Filtering](glue-pyspark-condition.md)
* [Having](glue-pyspark-having.md)
* [Joins](glue-pyspark-joins.md)
* [Set Operations](glue-pyspark-set-operations.md)

### Advanced Data Manipulation
* [Analytical Functions](glue-pyspark-analytical.md)
* [Pivot, UnPivot](glue-pyspark-pivot-unpivot.md)
* [Common Table Expressions](glue-pyspark-cte.md)
* [Create Table As Select](glue-pyspark-ctas.md)

### Date and Null Handling
* [Date Formats](glue-pyspark-date-formats.md)
* [Null Checks](glue-pyspark-null-checks.md)

### Advanced Query Techniques
* [Built in Psuedo Columns](glue-pyspark-built-in-pseudo-columns.md)
* [Hierarchial Queries](glue-hierarchial-queries.md)
  
### Advanced I/O Concepts:
* [Data Repartition](glue-repartition.md)
* [Data Partitioning](glue-s3-data-partitioning.md)
* [Bucketing](glue-bucketing.md)

### Pending Ones
* Glue Generate PySpark DataFrame from Single JSON, Multiple JSONs without Athena / Crawler - Todo 
* Glue Generate PySpark DataFrame from Single CSV, Multiple CSVs without Athena / Crawler - Todo
* Glue Generate PySpark DataFrame from Single Parquet, Multiple Parquets without Athena / Crawler - Todo
* Glue Generate PySpark DataFrame from RDBMS (Oracle, SQL Server, Postgresql, MySQL) - Pending
* Glue Generate PySpark DataFrame from DynamoDB - Pending ( nested and non nested table building )
* Glue PySpark DataFrame Built in Psuedo --done ( Current date or time, location - check?? )

### Data Frame Writing into different targets:
* Glue PySpark Targets write DataFrame to S3 (CSV,Parquet,JSON,AWS ION) - AWS ION is pending done
* Glue PySpark Targets write DataFrame to RDBMS (Oracle, SQL Server, Postgresql, MySQL)
* Glue PySpark Targets write DataFrame to NoSQL DynamoDB
* Glue PySpark DataFrame index
* Glue PySpark DataFrame caching
* Glue PySpark DataFrame performance tuning

