# AWS Glue
> Jay Kumsi & Sravya Arutla

## Glue Topics
* [AWS Glue Overview](Intro.md)
* What IAM Roles are needed OR Glue with PySpark IAM Roles
* [Crawler](aws-glue-crawler.md)
   * Source
   * Target
* Glue with PySpark
    * Source S3 (CSV,Parquet,JSON,AWS ION) - Target(S3,RDBMS,DynamoDB)
        * IAM roles needed
        * Code Structure
    * Source RDBMS (Oracle, SQL Server, Postgresql) - Target(S3,RDBMS,DynamoDB) 
    * Source Dynamo - Target(S3,RDBMS,DynamoDB)

## Glue with PySpark
* [Prerequisites](prerequisites.md)
* [Setting up Instructions](set-up-instructions.md)
  
## SQL Like Implementations with PySpark and AWS Glue ETL Scripts

* [Order By](glue-pyspark-orderby.md)
* [Group By](glue-pyspark-groupby.md)
* [Distinct](glue-pyspark-distinct.md)
* [Filtering](glue-pyspark-condition.md)
* [Having](glue-pyspark-having.md)
* [Joins](glue-pyspark-joins.md)
* [Set Operations](glue-pyspark-set-operations.md)
* [Analytical Functions](glue-pyspark-analytical.md)
* [Pivot, UnPivot](glue-pyspark-pivot-unpivot.md)
* [Common Table Expressions(CTE)](glue-pyspark-cte.md)
* [CTAS](glue-pyspark-ctas.md)
* [Date Formats](glue-pyspark-date-formats.md) Date, DateTime, DateTime TimeZone --error

  
* Glue PySpark DataFrame Joins multiple tables joins(3 or more) - Recheck
* Glue PySpark DataFrame Joins Remove duplicate columns when joined - Check Select script Alias
  AND Glue PySpark DataFrame Select, Rename Columns in Select  
* Glue Generate PySpark DataFrame from Single JSON, Multiple JSONs without Athena / Crawler - Todo 
* Glue Generate PySpark DataFrame from Single CSV, Multiple CSVs without Athena / Crawler - Todo
* Glue Generate PySpark DataFrame from Single Parquet, Multiple Parquets without Athena / Crawler - Todo
* Glue Generate PySpark DataFrame from RDBMS (Oracle, SQL Server, Postgresql, MySQL) - Pending
* Glue Generate PySpark DataFrame from DynamoDB - Pending ( nested and non nested table building )

* Glue PySpark DataFrame Handling: Null, isnull, not null --done
* Glue PySpark DataFrame Psuedo Colums --done ( Custom ones )
* Glue PySpark DataFrame Built in Psuedo --done ( Current date or time, location - check?? )
* Glue PySpark DataFrame Connect by prior(hierarchial queries) -- recurisive
* Glue PySpark DataFrame partitions -- done (Can we partition in pyspark and what is its use case? )

### Data Frame Writing into different targets:

* Glue PySpark Targets write DataFrame to S3 (CSV,Parquet,JSON,AWS ION)
* Glue PySpark Targets write DataFrame to RDBMS (Oracle, SQL Server, Postgresql, MySQL)
* Glue PySpark Targets write DataFrame to NoSQL DynamoDB
* Glue PySpark DataFrame index
* Glue PySpark DataFrame caching
* Glue PySpark DataFrame performance tuning

