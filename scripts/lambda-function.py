import os
import boto3
import json

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime_client = boto3.client('sagemaker-runtime')
content_type = "application/json"

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    data = json.loads(json.dumps(event))
    payload = json.dumps(data)
    
    response = runtime_client.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType=content_type,
        Body=payload)
    
    result = json.loads(response['Body'].read().decode())
    if result[0]['label'] == 'LABEL_1':
        result = {"outcome": "Positive"}
    else:
        result = {"outcome": "Negative"}
    print(result)
    
    
    return result