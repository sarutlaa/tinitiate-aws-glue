
# AWS Glue Overview

> Jay Kumsi & Sravya Arutla

## Introduction

AWS Glue is a Serverless data integration i.e., fully managed Extract, Transform, and Load (ETL) service that makes it easy to prepare and process data for analytics and machine learning. It automates the discovery, cataloging, cleaning, enriching, and moving of data between various data stores enabling more focus on analyzing the data rather than managing the infrastructure.

![AWS Glue Components](https://github.com/sarutlaa/tinitiate-aws-glue/assets/141533429/49d4152a-1baa-4ff8-ae33-1532e8eeffe3)

***Fig.1 AWS Glue Components***

Below are the listed Key AWS Glue Components.


## AWS Glue Components

AWS Glue utilizes a collaborative framework of multiple components, each contributing to the design and upkeep of ETL processes.

### Glue Console
- Enables the creation, monitoring, and management of ETL jobs by users.

### Glue Data Catalog

- Central Metadata Repository: Stores information on data assets, accessible regardless of their physical location.
- Unified Metadata Store: Serves as a single source for all data sources and targets, enhancing data management and accessibility.
- Seamless Data Discovery: Simplifies the process of discovering data across various datasets.
- Efficient ETL Processes: Enables smooth Extract, Transform, and Load operations, ensuring data is readily prepared for analysis.
- Optimized Query Execution: Facilitates efficient query execution across datasets, improving data retrieval and analysis.


### Database

Databases in the AWS Glue Data Catalog function as collections of related Data Catalog table definitions, systematically organized into logical groups. This structure supports efficient data catalog organization and streamlines the control of access and permissions across a variety of datasets.

### Data Store, Data Source, and Data Target

- Data Store: A repository designated for data storage. Within AWS Glue, data stores encompass Amazon S3 buckets, Amazon RDS databases, Amazon DynamoDB tables, among others.
- Data Source: The origin point from which an ETL job retrieves its data. This encompasses any data store that is accessible by AWS Glue.
- Data Target: The endpoint to which an ETL job delivers the processed data. Similar to the data source, it includes any data store supported by AWS Glue.

### Table

- Provides a metadata definition, capturing the schema of data in its original storage location.
- Includes details like column names, data types, and additional attributes, reflecting the structure of tables in standard relational databases. 

Therefore, AWS Glue tables establish a structured metadata framework, outlining the characteristics of the data without changing its actual form or position.

### Crawler and Classifier

* Crawler: A component of AWS Glue that scans various data stores to automatically discover and infer schemas. It categorizes data formats and suggests schemas and transformations, populating the Glue Data Catalog with table definitions.

* Classifier: Identifies the schema of data. Upon execution, a crawler activates classifiers to deduce the data's format and schema. These classifiers are adept at recognizing a range of file formats and data types, such as JSON, CSV, and Parquet.

### Job

- A business logic that automates the ETL process.
- Involves extracting data from a source, transforming this data according to specified rules, and loading it into a target destination.

### Glue Triggers

- Conditions or schedules that automatically start ETL jobs.
- Configurable to activate on a set schedule, in reaction to specific events, or on-demand, facilitating flexible and automated management of data workflows.

### Development Endpoint

- A development endpoint provides an environment for the interactive development and testing of ETL scripts.
- It offers a serverless Apache Spark environment, enabling exploration and experimentation with data transformation logic prior to deployment as a job.


Each of these components plays a crucial role in the AWS Glue service, working together to provide a comprehensive and scalable solution for data integration and ETL processes across a wide range of data sources and formats.

## AWS Glues Pros and Cons

### Pros

- Serverless maintenance and deployment
- Automatic ETL code generation
- Cost-effective usage billing
- Simplified job scheduling
- Enhanced data visibility
- Broad AWS service integration

### Cons

- AWS-only integration
- SQL-only query support
- No built-in testing environment
- Spark, Scala, and Python expertise required
- No real-time data operations


## Use Cases

- Integration with Amazon Athena
- Integration with Amazon S3
- Integration with Snowflake
- Integration with GitHub
- Creating an event-driven ETL pipeline: with AWS Lambda, you can trigger an ETL job when new data is added to Amazon S3.
