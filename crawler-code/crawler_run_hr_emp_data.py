import boto3
import botocore.exceptions
import logging
import time
from pprint import pprint

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = boto3.client('glue')
response = client.list_crawlers()
available_crawlers = response["CrawlerNames"]

glue_client = boto3.client(
    'glue', 
    region_name = 'us-east-1'
)

glue_client.start_crawler(
        Name = 'emp_data_crawler'
    )
logger.info(f"Crawler  already exists. Updated successfully.")