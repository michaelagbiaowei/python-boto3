import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("users")

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'account_type': 'standard_user',
            'username': 'miaempire',
            'first_name': 'Michael',
            'last_name': 'Agbiaowei',
            'age': 99,
            'address': {
                'road': '1 road Avenue',
                'city': 'Port Harcourt',
                'state': 'Rivers',
            }
        }
    )
    batch.put_item(
        Item={
            'account_type': 'super_user',
            'username': 'testname',
            'first_name': 'test',
            'last_name': 'ing',
            'age': 59,
            'address': {
                'road': '2 rod Avenue',
                'city': 'Ikeja',
                'state': 'Logos',
            }
        }
    )