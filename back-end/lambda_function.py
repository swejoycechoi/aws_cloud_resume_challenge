import boto3
import json
from decimal import Decimal

# Helper function to handle Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)  # Convert Decimal to int
        return super(DecimalEncoder, self).default(obj)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCountTable')  # Ensure this matches your table name

def lambda_handler(event, context):
    try:
        # Increment the visitor counter
        response = table.update_item(
            Key={'visitor_count': 'visitor_count'},  # Partition key
            UpdateExpression='ADD visits :inc',
            ExpressionAttributeValues={':inc': 1},
            ReturnValues='UPDATED_NEW'
        )

        # Return the updated count
        return {
            'statusCode': 200,
            'body': json.dumps(
                {'visitor_count': response['Attributes']['visits']},
                cls=DecimalEncoder
            )
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
