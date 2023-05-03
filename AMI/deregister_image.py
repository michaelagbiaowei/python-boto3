import boto3

delete =  boto3.client("ec2")

response = delete.deregister_image(
    ImageId="ami-0f6901fbb8bcb3703"
)

print(response)