from moto import mock_dynamodb2
from function import lambda_handler
import boto3
import os


# Using moto to mock AWS resources
@mock_dynamodb2
def test_lambda_handler():
    table_name = os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb', 'us-east-1')

    # Create our mock DynamoDB table
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'Site',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Site',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Put some data into our table
    table.put_item(Item={
        'Site': 0,
        'Visits': 0
        }
    )

    # Call our lambda_handler and let it run against our mock AWS resources
    # It should return this:
    # {'statusCode': 200,
    #  'body': 1,
    #  'headers': {'Content-Type': 'applications/json', 'Access-Control-Allow-Origin': '*'}
    # }
    result = lambda_handler("", "")

    assert result['statusCode'] == 200
    assert 'headers' in result
    assert result['body'] == 1
