import boto3
import os
import decimal

table_name = os.environ['TABLE_NAME']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    response = table.update_item(
        Key={
            'Site': 0
        },
        UpdateExpression="add Visits :val",
        ExpressionAttributeValues={
            ':val': decimal.Decimal(1)
        },
        ReturnValues='UPDATED_NEW'
    )

    visits = int(response['Attributes']['Visits'])

    return {
        'statusCode': 200,
        'body': visits,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
