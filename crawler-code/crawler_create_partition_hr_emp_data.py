import os
# Set the AWS profile using an environment variable
os.environ['AWS_PROFILE'] = 'jkumsi'
import boto3
import botocore.exceptions
import logging
import time


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Specify the AWS CLI profile to use
aws_profile = 'jkumsi'

# Create an AWSLogs client
#cloudwatch_logs = boto3.client('aws-glue/crawlers', region_name='us-east-1', profile_name=aws_profile)
cloudwatch_logs = boto3.client('logs', region_name='us-east-1')

# Specify your existing log group and log stream
log_group_name = '/aws-glue/crawlers'
log_stream_name = 'emp_data_crawler'

# Use the specified AWS CLI profile
session = boto3.Session(profile_name=aws_profile)

client = session.client('glue', region_name='us-east-1')
#client = session.client('awsglue.context', region_name='us-east-1')

crawler_name = 'emp_data_crawler'
role_name = 'tini-d-glue-crawler-role-001'
database_name = 'glue_db'
s3_input_path = 's3://tini-d-gluebucket-001/incoming_data/hr-data/'
s3_output_path = 's3://tini-d-gluebucket-001/output_data/'
log_messages = 'Calling Targets'

# Additional parameters for custom partitioning
partition_columns = ['year', 'month', 'day']
table_name = 'hr_data'

# Define Glue Table with StorageDescriptor
table_input = {
    'Name': table_name,
    'DatabaseName': database_name,
    'StorageDescriptor': {
        'Columns': [],
        'Location': s3_output_path,
        'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
        'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
        'SerdeInfo': {
            'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
            'Parameters': {
                'serialization.format': '1'
            }
        },
        'BucketColumns': [],
        'SortColumns': [],
        'Parameters': {
            'classification': 'parquet'
        },
        'SkewedInfo': {
            'SkewedColumnNames': [],
            'SkewedColumnValues': [],
            'SkewedColumnValueLocationMaps': {}
        }
    }
}

crawler_targets = {
    'S3Targets': [
        {
            'Path': s3_input_path
        }
    ],
    'DynamoDBTargets': [],
    'Catalogs': [],
    'JdbcTargets': [],
    'MongoDBTargets': [],
    'KafkaTargets': [],
    'S3Target': [],
    'Table': {
        'DatabaseName': database_name,
        'Name': table_name
    }
}

log_messages ='Hello, I am here'

try:
    # Create Glue Table
    response = client.create_table(**table_input)

    # Attempt to create the Glue Crawler
    response = client.create_crawler(
        Name=crawler_name,
        Role=role_name,
        DatabaseName=database_name,
        Targets=crawler_targets,
        TablePrefix=crawler_name
    )

    response = cloudwatch_logs.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': int(time.time() * 1000),  # Timestamp in milliseconds
                'message': log_messages
            }
        ]
    )
    logger.info(f"Crawler {crawler_name} created successfully.")
except botocore.exceptions.ClientError as e:
    # Handle existing crawler, etc.
    if e.response['Error']['Code'] == 'AlreadyExistsException':
         logger.info(f"Crawler {crawler_name} in Exception.")
    else:
        logger.error(f"Error: {e}")
        raise e
except Exception as e:
    logger.error(f"Error: {e}")
    raise e
