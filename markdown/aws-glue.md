# AWS Glue
> Jay Kumsi & Sravya Arutla

## Glue Topics
* [AWS Glue Overview](Intro.md)
* What IAM Roles are needed
* [Crawler](aws-glue-crawler.md)
   * Source
   * Target
* Glue with PySpark IAM Roles
* [Joins](markdown/glue-pyspark-joins.md)
* Glue PySpark DataFrame Joins two small tables,2 large tables,2 very large tables
* Glue PySpark DataFrame Joins multiple tables joins(3 or more)
* Glue PySpark DataFrame Joins Remove duplicate columns when joined
* Glue Generate PySpark DataFrame from Single JSON, Multiple JSONs without Athena / Crawler
* Glue Generate PySpark DataFrame from Single CSV, Multiple CSVs without Athena / Crawler
* Glue Generate PySpark DataFrame from Single Parquet, Multiple Parquets without Athena / Crawler
* Glue Generate PySpark DataFrame from RDBMS (Oracle, SQL Server, Postgresql, MySQL)
* Glue Generate PySpark DataFrame from DynamoDB
* Glue PySpark DataFrame Select, Rename Columns in Select
* Glue PySpark DataFrame Group By --done
* Glue PySpark DataFrame Analytical Functions --done
* Glue PySpark DataFrame Order By --done
* Glue PySpark DataFrame Having Clause --done
* Glue PySpark DataFrame Filter Conditions IN, NOT IN, >,<,<> --done
* Glue PySpark DataFrame Handling: Null, isnull, not null --done
* Glue PySpark DataFrame Distinct --done
* Glue PySpark DataFrame Psuedo Colums --done
* Glue PySpark DataFrame Built in Psuedo --done
* Glue PySpark DataFrame Date, DateTime, DateTime TimeZone --error
* Glue PySpark DataFrame Union,Union All, Intersect --done
* Glue PySpark DataFrame Pivot, UNPivot --done
* Glue PySpark DataFrame With Clause(CTE) --done
* Glue PySpark DataFrame CTAS --done
* Glue PySpark DataFrame Connect by prior(hierarchial queries) --error
* Glue PySpark DataFrame partitions -- done
* Glue PySpark Targets write DataFrame to S3 (CSV,Parquet,JSON,AWS ION)
* Glue PySpark Targets write DataFrame to RDBMS (Oracle, SQL Server, Postgresql, MySQL)
* Glue PySpark Targets write DataFrame to NoSQL DynamoDB
* Glue PySpark DataFrame index
* Glue PySpark DataFrame caching
* Glue PySpark DataFrame performance tuning

=======
# AWS Glue
> Jay Kumsi

## Glue Topics
*Intro 
* What IAM Roles are needed
* [Crawler](AWS-GLUE-Crawler.md).
   * Source
   * Target
* Glue with PySpark
    * Source S3 (CSV,Parquet,JSON,AWS ION) - Target(S3,RDBMS,DynamoDB)
        * IAM roles needed
        * Code Structure
    * Source RDBMS (Oracle, SQL Server, Postgresql) - Target(S3,RDBMS,DynamoDB) 
    * Source Dynamo - Target(S3,RDBMS,DynamoDB)
* Glue PySpark DataFrame Joins (Inner, Left, Right, Full Outer)
* Glue PySpark DataFrame Group By
* Glue PySpark DataFrame Analytical Functions
* Glue PySpark DataFrame Order By
* Glue PySpark DataFrame Having Clause
* Glue PySpark DataFrame Filter Conditions IN, NOT IN, >,<,<>
* Glue PySpark DataFrame Distinct, Psuedo Colums, Date, DateTime, DateTime TimeZone
* Glue PySpark DataFrame Handling: Null, isnull, not null
