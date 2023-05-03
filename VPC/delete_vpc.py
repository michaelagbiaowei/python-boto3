import boto3

ec2 = boto3.resource('ec2')
DeleteNatGatway = boto3.client("ec2")
DeleteElasticIp = boto3.client("ec2")

# Delete nat
DeleteNat = DeleteNatGatway.delete_nat_gateway(NatGatewayId='nat-083132f427b06517d')
print(DeleteNat)

# # Detach Elatic IP
DetachEIP = DeleteElasticIp.disassociate_address(
    AssociationId='your_id',
    PublicIp='your_elastic_ip',
)
print(DetachEIP)

# # Detach and Delete  igw
DetachIgw = ec2.detach_internet_gateway(
    InternetGatewayId='your_id',
    VpcId='vpc-0157aaad35705accc'
)
print(DetachIgw)
DeleteIgw = ec2.delete_internet_gateway(
    InternetGatewayId='your_id',
    VpcId='vpc-0157aaad35705accc'
)
print(DeleteIgw)

# # Delete Route tables
DeletRouteTable1 = ec2.delete_route_table(
    RouteTableId='your_id'
)
print(DeletRouteTable1)
DeletRouteTable2 = ec2.delete_route_table(
    RouteTableId='your_id'
)
print(DeletRouteTable2)

# # Delete Subnets
DeleteSubnet1 = ec2.delete_subnet(
    SubnetId='string',
)
print(DeleteSubnet1)
DeleteSubnet2 = ec2.delete_subnet(
    SubnetId='string',
)
print(DeleteSubnet2)

# Delete VPC
Delete_vpc = ec2.Vpc('vpc-0ad2289b8e0a7c4b6')
Delete_vpc.delete()
print(Delete_vpc)