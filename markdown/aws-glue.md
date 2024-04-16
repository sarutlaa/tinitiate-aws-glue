# AWS Glue
> Jay Kumsi & Sravya Arutla

## Glue Topics
* [AWS Glue Overview](Intro.md)
* What IAM Roles are needed
* [Crawler](aws-glue-crawler.md)
   * Source
   * Target
* Glue with PySpark IAM Roles
* * Glue with PySpark
    * Source S3 (CSV,Parquet,JSON,AWS ION) - Target(S3,RDBMS,DynamoDB)
        * IAM roles needed
        * Code Structure
    * Source RDBMS (Oracle, SQL Server, Postgresql) - Target(S3,RDBMS,DynamoDB) 
    * Source Dynamo - Target(S3,RDBMS,DynamoDB)
* [Joins](glue-pyspark-joins.md)
* Glue PySpark DataFrame Joins two small tables,2 large tables,2 very large tables
* Glue PySpark DataFrame Joins multiple tables joins(3 or more)
* Glue PySpark DataFrame Joins Remove duplicate columns when joined
* Glue Generate PySpark DataFrame from Single JSON, Multiple JSONs without Athena / Crawler
* Glue Generate PySpark DataFrame from Single CSV, Multiple CSVs without Athena / Crawler
* Glue Generate PySpark DataFrame from Single Parquet, Multiple Parquets without Athena / Crawler
* Glue Generate PySpark DataFrame from RDBMS (Oracle, SQL Server, Postgresql, MySQL)
* Glue Generate PySpark DataFrame from DynamoDB
* Glue PySpark DataFrame Select, Rename Columns in Select
* [Group By](glue-pyspark-groupby.md)
* [Analytical Functions](glue-pyspark-analytical.md)
* [Order By](glue-pyspark-orderby.md)
* [Having](glue-pyspark-having.md)
* [Filtering](glue-pyspark-condition.md) 
* Glue PySpark DataFrame Handling: Null, isnull, not null --done
* [Distinct](glue-pyspark-distinct.md)
* Glue PySpark DataFrame Psuedo Colums --done
* Glue PySpark DataFrame Built in Psuedo --done
* [Date Formats](glue-pyspark-date-formats.md) Date, DateTime, DateTime TimeZone --error
* [Set Operations](glue-pyspark-set-operations.md) Union,Union All, Intersect --done
* [Pivot, UnPivot](glue-pyspark-pivot-unpivot.md)
* [Common Table Expressions(CTE)](glue-pyspark-cte.md)
* [CTAS](glue-pyspark-ctas.md) 
* Glue PySpark DataFrame Connect by prior(hierarchial queries) --error
* Glue PySpark DataFrame partitions -- done
* Glue PySpark Targets write DataFrame to S3 (CSV,Parquet,JSON,AWS ION)
* Glue PySpark Targets write DataFrame to RDBMS (Oracle, SQL Server, Postgresql, MySQL)
* Glue PySpark Targets write DataFrame to NoSQL DynamoDB
* Glue PySpark DataFrame index
* Glue PySpark DataFrame caching
* Glue PySpark DataFrame performance tuning

