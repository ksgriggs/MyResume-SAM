import json
import boto3


def handler(event, context):
    """When this function is invoked - retrieve visitor count,
    add one, store in dynamodb, return to client."""
    dynamodb = boto3.client('dynamodb')

    # Get Visits
    response = dynamodb.get_item(
        TableName='counter', Key={'Site': {'N': '0'}})

    # If the item does not exist, create it.
    if 'Item' not in response:
        dynamodb.put_item(TableName='counter', Item={
            'Site': {'N': '0'},
            'Visits': {'N': '0'}
        })
        response = dynamodb.get_item(
            TableName='counter', Key={'Site': {'N': '0'}})

    visits = int(response["Item"]["Visits"]["N"]) + 1

    # Store Visits
    dynamodb.put_item(TableName='counter', Item={
        'Site': {'N': '0'},
        'Visits': {'N': str(visits)}
    })

    return {
        'statusCode': 200,
        'body': json.dumps(visits),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
