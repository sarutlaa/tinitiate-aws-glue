from awsglue.transforms import *
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job

# Initialize Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
job = Job(glueContext)

# Specify the S3 path to the JSON and gzip-compressed JSON files
json_path = "s3://ti-author-data/customer-billing/json/"
gzip_json_path = "s3://ti-author-data/customer-billing/json-gz/"

# Read the regular JSON file using DynamicFrame
dynamic_frame_json = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [json_path]},
    format="json"
)

# Read the gzip-compressed JSON file using Spark DataFrame as DynamicFrame doesn't support reads from compressed json file.
df_gzip_json = spark.read.option("compression", "gzip").json(gzip_json_path)

# Convert DynamicFrames to DataFrames to use Spark SQL functionalities
df_json = dynamic_frame_json.toDF()

# Example processing (simple count)
print("Regular JSON file preview:", df_json.show(5))
print("Compressed JSON file preview:", df_gzip_json.show(5))

# Initialize and commit the job
job.init("manual-job-name", {})
job.commit()
