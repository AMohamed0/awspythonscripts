import boto3

AWS_KEY="<enter>"
AWS_SECRET="<enter>"
REGION="us-east-1"

print("Connecting to EC2")
ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY,
                            aws_secret_access_key=AWS_SECRET,
                            region_name=REGION)

response = ec2.describe_instances()
for instance in response['Reservations'][0]['Instances']:
    print("Instance Type: " + str(instance['InstanceType']))
    print("Instance State: " + str(instance['State']['Name']))
    print("Instance Launch Time: " + str(instance['LaunchTime']))
    print("Instance Public DNS: " + str(instance['PublicDnsName']))
    print("Instance Private DNS: " + str(instance['PrivateDnsName']))
    print("Instance IP: " + str(instance['PublicIpAddress']))
    print("Instance Private IP: " + str(instance['PrivateIpAddress']))
