import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("users")

response = table.delete_item(
    Key={
        "first_name": "Michael",
        "last_name": "Agbiaowei"
    }
)

print("Response ", response)