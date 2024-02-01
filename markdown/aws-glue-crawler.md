# AWS Glue Crawler
> Jay Kumsi

* IAM Roles
* Glue Catalog
* Crawler S3
    * `Source` CSV `Target` CSV
    * `Source` JSON `Target` JSON
    * `Source` Parquet `Target` Parquet
    * `Source` ION `Target` ION
        * New File [Do this with AWS Lambda]
        * Add Rows [Do this with AWS Lambda]
        * Remove Rows [Do this with AWS Lambda]
           
* Crawler DB
    * Crawler On single tables
    * Crawler On PK-FK tables
    * Crawler On View
* Crawler Dynamo
* Crawler Metrics (Stats like DB Tables, last crawled datetime, PCT scanned, Pending time for Crawl)
* Crawler performance tuning
