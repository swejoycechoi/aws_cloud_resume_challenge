import json
import boto3
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

# Add CORS headers to every response
def add_cors_headers(response):
    response['headers'] = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }
    return response

def lambda_handler(event, context):
    try:
        # Default response for unsupported HTTP methods
        method = event.get('httpMethod', None)
        if method not in ['GET', 'POST']:
            return add_cors_headers({
                'statusCode': 400,
                'body': json.dumps({'error': 'Unsupported HTTP method'})
            })

        # GET request
        if method == 'GET':
            response = table.get_item(Key={'visitor_count': 'visitor_count'})
            count = response.get('Item', {}).get('visits', 0)
            return add_cors_headers({
                'statusCode': 200,
                'body': json.dumps({'visitor_count': count}, cls=DecimalEncoder)
            })

        # POST request
        if method == 'POST':
            try:
                body = json.loads(event.get('body', '{}'))
            except json.JSONDecodeError:
                return add_cors_headers({
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Malformed JSON'})
                })

            if not isinstance(body, dict) or 'expected_key' not in body:
                return add_cors_headers({
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Invalid payload'})
                })
        
        # Increment the visitor counter
        response = table.update_item(
            Key={'visitor_count': 'visitor_count'},  # Partition key
            UpdateExpression='ADD visits :inc',
            ExpressionAttributeValues={':inc': 1},
            ReturnValues='UPDATED_NEW'
        )

        # Return the updated count
        return add_cors_headers({
            'statusCode': 200,
            'body': json.dumps(
                {'visitor_count': response['Attributes']['visits']},
                cls=DecimalEncoder
            )
        })
    except Exception as e:
        return add_cors_headers({
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        })