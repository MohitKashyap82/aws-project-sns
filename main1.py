import boto3
import json
from time import sleep 


client = boto3.client('sns', region_name = 'us-east-1')
response = client.list_topics()

topics = response.get('Topics', [])
# print("Topics", topics)

for x in range(1, 10):
    response = client.publish( TopicArn='arn:aws:sns:us-east-1:261161414394:name', Message=json.dumps({'name':'mohit kashyap','count': str(1212)}),Subject='test subject',)
    sleep(2)
    print(response)
    break

# hello