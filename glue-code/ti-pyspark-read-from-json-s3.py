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
# gzip_json_path = "s3://ti-author-data/customer-billing/json-gz/"

# Read the regular JSON file using DynamicFrame
dynamic_frame_json = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [json_path]},
    format="json"
)

# # Read the gzip-compressed JSON file using DynamicFrame
# dynamic_frame_gzip_json = glueContext.create_dynamic_frame.from_options(
#     connection_type="s3",
#     connection_options={"paths": [gzip_json_path]},
#     format="json",
#     format_options={"compression": "gzip"}
# )

# Convert DynamicFrames to DataFrames to use Spark SQL functionalities
df_json = dynamic_frame_json.toDF()
# df_gzip_json = dynamic_frame_gzip_json.toDF()

# Example processing (simple count)
print("Count of rows in regular JSON:", df_json.show(5))
# print("Count of rows in gzip JSON:", df_gzip_json.show(5))

# Initialize and commit the job
job.init("manual-job-name", {})
job.commit()
