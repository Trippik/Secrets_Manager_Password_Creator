# Standard Library
import logging
import sys
import os

import boto3
 

class CloudWatchLogsHandler(logging.Handler):
    def __init__(self, log_group:str, stream_name:str, access_key:str, secret_key:str, region:str, **kwargs):
        super(CloudWatchLogsHandler, self).__init__()
        self.log_group = log_group
        self.stream_name = stream_name
        self.session = boto3.session.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
        self.logs_client = self.session.client("logs")
        self.check_group_and_stream()
 
    def check_group_and_stream(self):
        try:
            self.logs_client.create_log_group(logGroupName=self.log_group)
        except self.logs_client.exceptions.ResourceAlreadyExistsException:
            pass  # Log group already exists
        try:
            self.logs_client.create_log_stream(logGroupName=self.log_group, logStreamName=self.stream_name)
        except self.logs_client.exceptions.ResourceAlreadyExistsException:
            pass  # Log stream already exists
 
    def emit(self, record):
        # Create logs client on demand
        if self.logs_client is None:
            self.logs_client = self.session.client("logs")

        # Format log record
        log_entry = self.format(record)

        # Put log events to CloudWatch Logs
        self.logs_client.put_log_events(
            logGroupName=self.log_group,
            logStreamName=self.stream_name,
            logEvents=[{"timestamp": int(record.created * 1000), "message": log_entry}],
        )
 
    def close(self):
        # Close logs client and release resources
        if self.logs_client is not None:
            self.logs_client = None
        super(CloudWatchLogsHandler, self).close()
 
  
logger = logging.getLogger("my_logger")
logging_level = logging.INFO
logger.setLevel(logging_level)
log_format = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
 
stream_name = os.environ['LOG-STREAM']
cloudwatch_handler = CloudWatchLogsHandler(log_group="SecretsManagerPasswordCreator", stream_name=stream_name, access_key=os.environ["ACCESS-KEY"], secret_key=os.environ["SECRET-KEY"], region=os.environ["REGION"])
cloudwatch_handler.setLevel(logging_level)
cloudwatch_handler.setFormatter(log_format)
logger.addHandler(cloudwatch_handler)
 
 
file_handler = logging.FileHandler(filename="SecretsManagerPasswordCreator.log")
file_handler.setLevel(logging_level)
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)
 
console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setLevel(logging_level)
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)