import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("users")

response = table.put_item(
    Item = {
        "first_name": "Michael",
        "last_name": "Agbiaowei",
        "age": "99",
        "account_id": "vhg67tv534"
    }
)

print("Response :", response)