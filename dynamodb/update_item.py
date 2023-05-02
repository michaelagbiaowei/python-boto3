import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("users")

response = table.update_item(
    Key={
        "first_name": "Michael",
        "last_name": "Agbiaowei"        
        },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 55
    }
)

print("Response ", response)
