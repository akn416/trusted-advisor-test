import sys
import schedule
import time
import boto3
import subprocess
import tempfile
import logging

AWS_ACESS_KEY=AKIAY2QQGWRHTDJ7DW7O
AWS_SECRET=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

logging.basicConfig(
    filename="D:\\s3scanner\\logs\\scanner.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )
y=1
def job():
    # Create SQS client
    sqs = boto3.client('sqs', region_name='us-east-1')

    queue_url = 'https://sqs.us-east-1.amazonaws.com/606698124367/demosite'


    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
        'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
        'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    x = 1
    while x >= 1:
            try:
