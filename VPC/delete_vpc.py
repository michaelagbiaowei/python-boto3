import boto3

ec2 = boto3.resource('ec2')
DeleteNatGatway = boto3.client("ec2")
DeleteElasticIp = boto3.client("ec2")

# Delete VPC
Delete_vpc = ec2.Vpc('vpc-0ad2289b8e0a7c4b6')
Delete_vpc.delete()

# Detach nat gatway
DetachNat = DeleteNatGatway.detach_internet_gateway(
    InternetGatewayId='your_id',
    VpcId='your_id'
)
# Delete nat
DeleteNat = DeleteNatGatway.delete_nat_gateway(NatGatewayId='your_id')

# Detach Elatic IP
DetachEIP = DeleteElasticIp.disassociate_address(
    AssociationId='your_id',
    PublicIp='your_elastic_ip',
)

# Delete Route tables
DeletRouteTable1 = ec2.delete_route_table(
    RouteTableId='your_id'
)
DeletRouteTable2 = ec2.delete_route_table(
    RouteTableId='your_id'
)

# DeleteSubnets
DeleteSubnet1 = ec2.delete_subnet(
    SubnetId='string',
)
DeleteSubnet2 = ec2.delete_subnet(
    SubnetId='string',
)