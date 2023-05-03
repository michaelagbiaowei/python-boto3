import boto3

delete = boto3.resource("dynamodb")

response = delete.delete_table(
    Table="users"
)

print(response["RequestId"])