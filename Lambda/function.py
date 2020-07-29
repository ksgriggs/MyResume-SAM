import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('counter')


def lambda_handler(event, context):
    response = table.get_item(
        Key={
            'Site': 0
        }
    )

    if 'Item' not in response:
        # Create Item
        table.put_item(
            Item={
                'Site': 0,
                'Visits': 0
            }
        )
        # Read table again
        response = table.get_item(
            Key={
                'Site': 0
            }
        )

    # Increment Visits and store it
    visits = int(response['Item']['Visits']) + 1

    table.put_item(
        Item={
            'Site': 0,
            'Visits': str(visits)
        }
    )

    return {
        'statusCode': 200,
        'body': visits,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
