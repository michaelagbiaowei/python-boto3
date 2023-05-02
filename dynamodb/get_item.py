import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("users")

response = table.get_item(
    Key={
        "first_name": "Michael",
        'last_name': 'Agbiaowei'
    }
)

print("Response :", response)

item = response["Item"]
print(item)