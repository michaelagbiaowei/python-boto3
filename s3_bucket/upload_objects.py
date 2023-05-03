import boto3

s3 = boto3.client("s3")

response = s3.upload_file(Bucket="aaabbbccc", Filename="create_bucket.py", Key="create_bucket.py")