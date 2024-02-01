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
